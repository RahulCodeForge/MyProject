from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Home(request):

    return HttpResponse("Welcome to blog page ")

def About(request):


    return HttpResponse("Welcome to blog About page")    
