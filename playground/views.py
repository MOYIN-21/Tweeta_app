from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to django")


def hello(request, name):
    return render(request, 'hello.html', {"name": name})


def number(request, num):
    return render(request, 'number.html', {"num": num})
