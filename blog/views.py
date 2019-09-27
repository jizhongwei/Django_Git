from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

from .models import *
import markdown


def index(request):
    post_list = Blog.objects.filter(status='p')
    return render(request, 'blog/index.html', locals())

def detail(request, pk):
    post = get_object_or_404(Blog, pk = pk)
    post.increase_views()
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
    tag = get_object_or_404(Tag, pk = pk)
    post_list = Blog.objects.filter(tags= tag)
    return render(request, 'blog/index.html', locals())

def search(request):
    q = request.GET.get('q')
    post_list = Blog.objects.filter(Q(title__icontains= q) | Q(body__icontains= q))
    return render(request, 'blog/index.html', locals())

def archives(request, year, month):
    post_list = Blog.objects.filter(created_time__year= year,
                                    created_time__month= month)
    return render(request, 'blog/index.html', locals())