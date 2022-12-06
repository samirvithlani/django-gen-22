from django.contrib import admin
from django.urls import  include, path
from . import views

urlpatterns = [

    path('addstudent/',views.student_create_view)
]
