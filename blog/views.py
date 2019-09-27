from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *


def index(request):
    post_list = Blog.objects.filter(status='p')
    return render(request, 'blog/index.html', locals())

def detail(request, pk):
    post = get_object_or_404(Blog, pk = pk)
    return render(request, 'blog/detail.html', locals())

def category(request, pk):
    pass

def tag(request,pk):
    pass

def search(request):
    pass

def archives(request, year, month):
    pass