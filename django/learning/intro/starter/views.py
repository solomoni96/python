# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello, welcome home')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('About page')
    return render(request, 'about.html')
