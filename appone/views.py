from unittest import result
from venv import create

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
 
def home(request):
    return HttpResponse("Hello, World! This is the home page of appone.")

# Create a JSON endpoint that returns a simple JSON response
from django.http import JsonResponse  

def json_items(request):
    items_list = [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"},
]
    return JsonResponse(items_list, safe=False)


def math_fact(request):
    n = 5
    result = 1
    
    # The logic must be indented under the while statement
    while n > 0:
        result *= n
        n -= 1
    
    # We return the result so the user can see it in the browser
    return HttpResponse(f"The factorial of 5 is: {result}")


def odd_numbers(request):
    n = 100
    result = []
    
    # The logic must be indented under the while statement
    while n > 0:
        if n % 2 != 0:  # Check if the number is odd
            result.append(n)
        n -= 1
    
    # We return the result so the user can see it in the browser
    return HttpResponse(f"The odd numbers from 100 down to 1 are: {result}")