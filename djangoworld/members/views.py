# Add http response for views
# Views are python functions that take http requests and returns an http response like in HTML docs
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")