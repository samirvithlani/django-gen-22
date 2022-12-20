from django.contrib import admin
from django.urls import  include, path
from . import views

urlpatterns = [

    path('addstudent/',views.student_create_view),
    path('studentlist/',views.student_list_view),
    path('deletestudent/<int:id>',views.student_delete_view)
    
]
