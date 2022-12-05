# Django Tutorial

From W3 Schools: https://www.w3schools.com/django/index.php

## Django Development Process
1. Create Virtual Environment

    `python -m venv myproject`

2. Activate Virtual Environment

    `myproject\Scripts\activate.bat`
    
3. Install Django into Virtual Environment

    `python -m pip install Django`
    
4. Create Django Project

    `django-admin startproject djangoworld`
    
5. Run Django Project

    `python manage.py runserver`
    
6. Create Django App

    `python manage.py startapp members`
    
7. Create index View

    `members/views.py`
    
    `def index(request):`
        
8. Add Template(s)

    `members/templates`
    
    `/templates/index.html`
    
9. Include Template(s) in View

    `members/views.py`
    
    `from django.template import loader`
    
    `template = loader.get_template('index.html')`
    
10. Modify Project Settings

    `djangoworld/settings.py`
    
    `members.apps.MembersConfig`
    
11. Migrate App(s)

    `python manage.py makemigrations members`
    
## Back-End Development using Python
- Virtual Environment
  - **myproject**
- Django Project
  - **djangoworld**
  ![image](https://user-images.githubusercontent.com/54840122/205466114-32079b8c-ec40-4c0c-8b19-01fa36e2a79b.png)
  
 - Views
    - **index**
    
    - **add**
    
    - **addrecord**
    
 - Templates
    - **myfirst.html**
      
      ![image](https://user-images.githubusercontent.com/54840122/205467560-d550e9e8-f53c-4e1e-8706-84d30451f6a2.png)
    - **index.html**
      
      
      ![image](https://user-images.githubusercontent.com/54840122/205524003-264865c9-c9fd-4580-a0de-04c2134c962f.png)

      
    - **add.html**
      
      ![image](https://user-images.githubusercontent.com/54840122/205516606-f9c3c63f-2888-4820-88be-e3192d7659ab.png)


  - Model
      
      ![image](https://user-images.githubusercontent.com/54840122/205512795-36ccbca5-02b9-4ab2-b145-cd8f61d0dde6.png)

 
## Django Framework: MVT Model

- Model
  - `models.py`
  - **Tables for databases**
- View
  - `views.py`
  - **Python functions that take http requests and return an http response**
- Template
  - `/templates`
  - **Response from View (usually in HTML)**

- Structure

![django](https://user-images.githubusercontent.com/54840122/205463140-55d19147-3d97-43ab-ae70-6c5f8b7fb988.JPG)
