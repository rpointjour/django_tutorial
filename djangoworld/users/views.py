from django.http import HttpResponse
from django.template import loader

# Index View: Users Template
def index(request):
    template = loader.get_template('users.html')
    return HttpResponse(template.render())

# Variables View: Variables Template
def variables(request):
    template = loader.get_template('variables.html')
    context = {     # Create variable(s) using context object to render to template
        'user': 'new user',
        'car' : 'Ford Mustang GT',
        'cost' : '37000',
        'yes' : 'true',
        'temperature' : '25.4'
    }
    return HttpResponse(template.render(context, request))