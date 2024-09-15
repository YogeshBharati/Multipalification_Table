from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape

# Create your views here.

def home(request):
    return HttpResponse(" <h1>Welcome to My Website</h1>")

def multiply(request, number):
    try:
        
        # Build the HTML response
        data = f"<h1>Multiplication Table of {number}</h1>"
        data += "<ul style='list-style-type:none;'>"
        
        for i in range(1, 11):
            data += f"<li>{number} * {i} = {(number * i)}</li>"
        
        data += "</ul>"
        
        return HttpResponse(data, content_type="text/html")
    
    except:
        # Log the exception for debugging
        return HttpResponse("Something went wrong. Please try again later.")



