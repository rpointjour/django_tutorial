from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('variables/', views.variables, name='variables'),
    path('tags/', views.tags, name='tags' ),
]