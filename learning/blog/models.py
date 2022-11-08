from django.db import models

#create table employee(name varchar(100),email varchar())
# Create your models here.
class Employee(models.Model):
    # do not speecify id field, it will be created automatically
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100) 
    age = models.IntegerField()
    isActive =models.BooleanField(default=True)
    password = models.CharField(max_length=100,null=False)
    address = models.TextField()
    salary = models.FloatField(null=True)
    mobile = models.BigIntegerField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True,null=True)
    updateedAt = models.DateTimeField(auto_now=True,null=True)
    birthdate = models.DateField(null=True)
    birthtime = models.TimeField(null=True)
    
    #optional
    #if table name not give application name.class name blog_employee
    class Meta:
        db_table = "employee"
     
    def __str__(self):
        return self.name 
