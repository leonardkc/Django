from django.http import HttpRequest, HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def mike(request):
    return HttpResponse("Hello, Mike!")

def marvhiee(request):
    return HttpResponse("Hello, Marvhiee!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")
