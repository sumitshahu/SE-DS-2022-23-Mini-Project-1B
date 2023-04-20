from django.shortcuts import render, redirect
import razorpay
from django.conf import settings
from django.core.mail import send_mail
from crowdfunding.models import Post

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def index(request):
    posts = Post.objects.all()
    return render(request, 'core/index.html', {'posts': posts})

def about(request):
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=50000,
                                                       currency='INR',
                                                       payment_capture='0'))

    # Get the Razorpay Order ID
    razorpay_order_id = razorpay_order['id']

    # Define the callback URL for handling the payment response
    callback_url = 'payment/'

    # Render the about.html template with the necessary context variables
    context = {
        'razorpay_merchant_key': settings.RAZOR_KEY_ID,  # Replace with your Razorpay merchant key
        'razorpay_amount': razorpay_order['amount'],
        'currency': razorpay_order['currency'],
        'razorpay_order_id': razorpay_order_id,
        'callback_url': callback_url
    }
    return render(request, 'core/about.html', context)

def payment(request):
    # Retrieve the Razorpay Order ID and Payment ID from the callback response
    razorpay_order_id = request.POST.get('razorpay_order_id')
    razorpay_payment_id = request.POST.get('razorpay_payment_id')

    # Verify the payment using Razorpay API
    razorpay_client.payment.capture(razorpay_payment_id, razorpay_order_id)

    subject = "Django-Crowdfunding donation recieved!"
    message = 'Hello '+request.user.first_name+". Thank you for donating to django-crowdfunding."
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [request.user.email]  # List of recipient email addresses

    send_mail(subject, message, from_email, recipient_list)

    # Return a success response
    return redirect('about')

def user(request, author):
    posts = Post.objects.filter(author=author)
    return render(request, 'core/index.html', {'posts':posts, 'author':author})

def login(request):
    posts = Post.objects.filter(author=request.user.username)
    return render(request, 'core/index.html', {'posts':posts, 'author':request.user.username})
