from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *
import markdown


def index(request):
    post_list = Blog.objects.filter(status='p')
    return render(request, 'blog/index.html', locals())

def detail(request, pk):
    post = get_object_or_404(Blog, pk = pk)
    # post.body = markdown.markdown(post.body,
    #                               extensions = [
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                               ])
    return render(request, 'blog/detail.html', locals())

def category(request, pk):
    cate = get_object_or_404(Category, pk = pk)
    post_list = Blog.objects.filter(category= cate)
    return render(request, 'blog/index.html' ,locals())

def tag(request,pk):
    pass

def search(request):
    pass

def archives(request, year, month):
    post_list = Blog.objects.filter(created_time__year= year,
                                    created_time__month= month)
    return render(request, 'blog/index.html', locals())