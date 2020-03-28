from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    context = {
        'posts': Post.objects.all(),
        'title': 'Loc dep zai'
    }
    return render(request, 'blog/home.html', context)


def infor(request):
    return HttpResponse('<h1>Index page</h1>')


def about(request):
    # return HttpResponse('<h1>About page</h1>')
    context = {
    }
    return render(request, 'blog/about.html', context)
