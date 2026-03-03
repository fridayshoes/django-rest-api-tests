from django.shortcuts import render
from django.http import HttpResponse  # <--- Add this import

# Create your views here.

def home(request):
    return HttpResponse("This is the home page for appthree!")
def app_three_view1(request):
    return HttpResponse("This is the first view for appthree!")
def app_three_view2(request):
    return HttpResponse("This is the second view for appthree!")
def app_three_view3(request):
    return HttpResponse("This is the third view for appthree!")