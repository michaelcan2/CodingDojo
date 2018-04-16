from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('homepage')
    return render(request,'homepage.html')

def about(request):
    response = "hello second response to you"
    # return HttpResponse(response)
    return render(request, 'about.html')