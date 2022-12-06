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

# Tags View: Tags Template
def tags(request):
    template = loader.get_template('tags.html')
    return HttpResponse(template.render())

# If Else View: If Else Template
def ifelse(request):
    template = loader.get_template('ifElse.html')
    context = {
        'greeting' : 1,
        'apple' : 'red',
        'paper' : 'green',
        'jeans' : 'blue',
        'mobile': ['phones', 'watches', 'tablets'],
        'devices' : ['phones', 'watches', 'tablets'],
    }
    return HttpResponse(template.render(context, request))

# For Loop View: For Loop Template
def forloop(request):
    template = loader.get_template('forloop.html')
    context = {         # Define Python Lists and Dictionary for the loop
        'heroes' : ['Spider-Man', 'Hulk', 'Thor', 'Wolverine', 'Blade'],
        'villains' : ['Venom', 'Green Goblin', 'Magneto', 'Doctor Doom', 'Thanos'],
        'phones' : [
            {
                'brand': 'Apple',
                'model' : 'iPhone 13 Pro',
                'size' : '256GB'
            },
            {
                'brand': 'Samsung',
                'model' : 'Galaxy',
                'size' : '128GB'
            }
        ]
    }
    return HttpResponse(template.render(context, request))