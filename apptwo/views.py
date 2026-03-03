from django.shortcuts import render
from django.http import HttpResponse  # <--- Add this import

# Create your views here.

def home(request):
    return HttpResponse("Hello, World! This is the home page of apptwo.")

def app_two_view1(request):
    return HttpResponse("This is the first view for apptwo!")

def app_two_view2(request):
    return HttpResponse("This is the second view for apptwo!")

def app_two_view3(request):
    return HttpResponse("This is the third view for apptwo!")