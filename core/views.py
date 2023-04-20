from django.shortcuts import render

from crowdfunding.models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'core/index.html', {'posts': posts})

def about(request):
    return render(request, 'core/about.html')