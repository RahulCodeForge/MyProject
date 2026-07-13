from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Home(request):

    return HttpResponse("welcome to shop Home Page ")

def Product(request):

    return HttpResponse("Welcome to Shop Product page ")    
