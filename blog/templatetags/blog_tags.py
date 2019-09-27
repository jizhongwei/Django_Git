from django import template
from django.db.models import Q

from ..models import *
import markdown

register = template.Library()

@register.simple_tag
def get_the_most_category():
    return Category.objects.filter(Q(name__icontains= 'Django') | Q(name__icontains= 'Linux') | Q(name__icontains= 'Python'))

@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.simple_tag
def get_recent_posts(num = 5):
    return Blog.objects.all()[:num]

@register.simple_tag
def archives():
    return Blog.objects.dates('created_time', 'month', order= 'DESC')

@register.simple_tag
def get_tags():
    return Tag.objects.all()

@register.filter(name= 'markdown')
def make_markdown(blog):
    return markdown.markdown(blog.body, extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
    ])