from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def work(request):
    return render(request, 'myapp/index.html')

def place(request):
    return HttpResponse("Working in perungudi for his IT Works")

def salary(request):
    return HttpResponse("monthly 5k, there are providing for the interns")

def task(request):
    return HttpResponse("Doing a web oriented task based projects")

def frds(request):
    return HttpResponse("Overall city my frds only")

def college(request):
    return HttpResponse("AVS College of arts & Science, salem")