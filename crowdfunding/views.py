from django.shortcuts import get_object_or_404, render, redirect
import razorpay
from .models import Post, Transaction
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from django.core.mail import send_mail
from allauth.socialaccount.models import SocialAccount

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def user(request, slug):
    posts = Post.objects.filter(author=slug)
    return render(request, 'core/index.html', {'posts':posts, 'author':slug})

def detail(request, author, url):
    post = get_object_or_404(Post, author=author, url=url)

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=post.contribution_amount,
                                                       currency= 'INR',
                                                       payment_capture='0'))
    
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/' + url

    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = post.contribution_amount
    context['amount'] = int(post.contribution_amount)//100
    context['currency'] = 'INR'
    context['callback_url'] = callback_url
    context['title'] = post.title
    context['intro'] = post.intro
    context['body'] = post.body
    context['created_at'] = post.created_at
    context['post'] = post

    return render(request, 'crowdfunding/detail.html', context=context)




@csrf_exempt
def paymenthandler(request, author, url):
    post = get_object_or_404(Post, author=author, url=url)
    referer = request.META.get('HTTP_REFERER')
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = post.contribution_amount 
                try:
                    # capture the payment
                    razorpay_client.payment.capture(payment_id, amount)

                    # create a Transaction instance and save it to the database
                    transaction = Transaction(
                        payment_id=payment_id,
                        razorpay_order_id=razorpay_order_id,
                        razorpay_signature=signature,
                        amount=amount,
                        post_id=post.url,
                        donor=request.user.username,
                    )
                    transaction.save()
                    donated_amount = int(post.contribution_amount)//100
                    subject = 'Successful donation to '+ post.title
                    message = 'Hello '+request.user.first_name+". Thank you for making a contribution of Rs." + str(donated_amount) + " for " + post.title + "." + "Your payment id is: " + payment_id
                    from_email = settings.DEFAULT_FROM_EMAIL
                    recipient_list = [request.user.email]  # List of recipient email addresses

                    send_mail(subject, message, from_email, recipient_list)
 
                    # render success page on successful caputre of payment
                    return redirect(referer)
                except:
                    # if there is an error while capturing payment.
                    return redirect(referer)
            else:
                # if signature verification fails.
                return redirect(referer)
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()
