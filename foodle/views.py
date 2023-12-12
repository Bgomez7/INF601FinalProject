from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the foodle index.")

