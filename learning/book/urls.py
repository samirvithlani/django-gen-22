from django.contrib import admin
from django.urls import  include, path
from . import views

urlpatterns = [

 path('booklist/',views.getAllBooks),
 path('country/',views.getCountryData),
 
]