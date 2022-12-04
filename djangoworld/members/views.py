# Views are python functions that take http requests and returns an http response like in HTML docs
# Add http response for views
# Add templates for response
# template = loader.get_template('myfirst.html')
from django.http import HttpResponse
from django.template import loader
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  output = ""
  for x in mymembers:
    output += x["firstname"]
  return HttpResponse(output)