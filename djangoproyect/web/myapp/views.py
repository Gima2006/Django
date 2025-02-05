from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hola(request,username):
    print(username)
    return HttpResponse("Hola mundo, {{username}}")

def index(request):
    return HttpResponse("inde page")

def about(request):
    return HttpResponse("<h1>About </h1>")