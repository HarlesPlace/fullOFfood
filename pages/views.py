from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {}
    return render(request, 'pages/index.html', context)

def about(request):
    context = {}
    return render(request, 'pages/about.html', context)