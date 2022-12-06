from django.db import models

# Create your models here.
class Student1(models.Model):
    name = models.CharField(max_length=50)
    email =models.EmailField(max_length=50)
    rollno= models.PositiveIntegerField()
    
    class Meta:
        db_table = 'student1'
        
    def __str__(self):
        return self.name