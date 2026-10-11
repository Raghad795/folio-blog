from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Category, Post, Comment

# Create your views here.

def main(request):
    return render(request, 'main.html')


def users(request):
    all_users = User.objects.all()

    context = {
        'users': all_users
    }
    return render(request, 'users.html', context)

def blogs(request):
    all_posts = Post.objects.all()

    context = {
        'posts': all_posts
    }
    return render(request, 'blogs.html', context)

def blogdetails(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {
        'post': post
    }
    return render(request, 'blogdetails.html', context)

def comments(request):
    all_comments = Comment.objects.all()

    context = {
        "comments" : all_comments
    }

    return render(request, 'comments.html', context)

def categories(request):
    all_categories = Category.objects.all()

    context = {
        'categories' : all_categories
    }
    return render(request, 'categories.html', context)

