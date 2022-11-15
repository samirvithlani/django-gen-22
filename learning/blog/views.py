
from django.http import HttpResponse
from django.shortcuts import render
from . models import Employee

# Create your views here.
def index(request):
    print(request)
    return HttpResponse("Hello World")

def aboutUs(request):
    return render(request,'aboutus.html')
    
def contactUs(request):
    data ={
        "firstName":"John",
        "lastName":"Doe",
        "address":"1234 Main Street",
    }
    return render(request,'blog/contactus.html',data)

def getEmployeesData(request):
    #fetch data from EMployee table
    employees = Employee.objects.all().values()
    print(employees)
    return render(request,'blog/employees.html',{'employees':employees})