from django.shortcuts import render
from django.http import HttpResponse

#Create Your Views Here

def index(request):
    return HttpResponse("Hello World")
