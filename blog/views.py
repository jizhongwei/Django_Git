from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Welcome To Dick's Blog Index Page!</h2>")