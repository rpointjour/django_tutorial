# Views are python functions that take http requests and returns an http response like in HTML docs
# Add http response for views
# Add templates for response
from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())