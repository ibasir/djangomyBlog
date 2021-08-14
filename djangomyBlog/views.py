from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    # return HttpResponse('Its about page')
    return render (request,'about.html')

def home(request):
    # return HttpResponse('Its Home page')
        return render (request,'home.html')
