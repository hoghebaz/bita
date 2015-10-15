from django.db import models

# Create your models here.

class Kindergarten(models.Model): 

    name = models.CharField(max_length=300) 
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=400)
    city_code = models. IntegerField(default=21)
    email = models.EmailField()
    capacity = models.IntegerField(default=0) 
    
    
