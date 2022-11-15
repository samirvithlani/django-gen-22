from django.db import models

# Create your models here.
hobbies = (
    ('sports', 'Sports'),
    ('music', 'Music'),
    ('reading', 'Reading'),
    ('movies', 'Movies'),
    ('travel', 'Travel'),
    ('cooking', 'Cooking'),
)
class User(models.Model):
    name = models.CharField(max_length=50)
    hobbies = models.CharField(max_length=50, choices=hobbies)
    age = models.IntegerField(null=False)
    email = models.EmailField(max_length=50, null=False,unique=True)
    
    class Meta:
        db_table = "user1"
        
    def __str__(self):
        return self.name 

class Netflix(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=False)
    
    class Meta:
        db_table = "netflix"
        
    def __str__(self):
        return self.name
    
    
