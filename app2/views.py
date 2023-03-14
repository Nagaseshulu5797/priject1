from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def seshu(request):
    return HttpResponse('<h1> lord is with me<h1/>')
