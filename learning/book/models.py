from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    ratings = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'books'
        
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'country'
    
    def __str__(self):
        return self.name
    


class City(models.Model):
    name = models.CharField(max_length=100)
    country =models.ForeignKey(Country,on_delete=models.CASCADE)
    population = models.PositiveIntegerField()
    
    class Meta:
        db_table= 'city'
                
    def __str__(self):
        return self.name            
    
    