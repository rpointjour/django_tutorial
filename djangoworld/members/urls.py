# Add urls file in the same folder as view

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add' ),
    path('add/addrecord/', views.addrecord, name='addrecord'),
]