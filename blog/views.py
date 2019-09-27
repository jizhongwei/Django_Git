from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def index(request):
    post_list = Blog.objects.filter(status='p')
    return render(request, 'blog/index.html', locals())

def detail(request, pk):
    pass

def category(request, pk):
    pass

def tag(request,pk):
    pass

def search(request):
    pass

def archives(request, year, month):
    pass