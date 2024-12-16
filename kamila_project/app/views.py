from django.shortcuts import render
from .models import Post


def base(request):
    return render(request, 'app/base.html')


def index(request):
    return render(request, 'app/index.html')


def blog(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'app/blog.html', {'posts': posts})


def post(request):
    return render(request, 'app/post.html')
