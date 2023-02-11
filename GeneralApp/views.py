from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('HOME PAGE <a href="/about">about</a>')

def about(request):
    return HttpResponse('ABOUT PAGE <a href="/">Home</a>')

def htmlpage(request):
    return render(request, 'page.html')