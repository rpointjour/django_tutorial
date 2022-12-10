# Django Tutorial

From W3 Schools: https://www.w3schools.com/django/index.php
 
## Django QuerySet Structure

- QuerySet
- Get Data
- Filter
- Order By

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

## Django Project & App Development


## Django Apps

- **Members**

<img src="https://user-images.githubusercontent.com/54840122/206818949-20628654-d6a4-495b-b5f3-ce7d55a5b870.png" alt="Members App" style="width:50%;height:50%;">

- **Users**

<img src="https://user-images.githubusercontent.com/54840122/206008721-95ff6b4b-fb4d-4382-89e7-2b5f5b887fef.png" 
alt="Users App" style="width:70%;height:80%;">

## Static Files

- `members.css`
- `IMG_3046.JPG`
- `myfile.js`

## Django QuerySets

<img src="https://user-images.githubusercontent.com/54840122/206816208-b02829d9-5bd1-4434-970d-6a7b066e8a73.png" alt="QuerySet Users" style="width:70%;height:70%;">

- **Query Data**
  - `Users.objects.all()`
- **Get Data**
  - `Users.objects.all().values()`
- **Return Specific Data**
  - `Users.objects.values_list('username')`
- **Filter Data**
  - `Users.objects.filter(username='starfox').values()`
- **Order Data**
  - `Users.objects.all().order_by('username').values()`
  
## Structure

![django](https://user-images.githubusercontent.com/54840122/205463140-55d19147-3d97-43ab-ae70-6c5f8b7fb988.JPG)
