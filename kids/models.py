from django.db import models

# Create your models here.

class Kindergarten(models.Model): 

    name = models.CharField(max_length=300) 
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=400)
    city_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=12, default=" ")
    capacity = models.IntegerField(default=0) 
        
    def __unicode__(self):       
        output = "\n\t%s \n\t%s =\n\t%s \n\t%s \n" % (self.name_string(), 
                                                    self.phone_number_string(),
                                                    self.complete_address(),
                                                    self.capacity_string())
        return output
        
    def name_string(self): 
        return '{:10s}'.format('name') + " = " + self.name     
        
    def complete_address(self): 
        output = '{:10s}'.format('address') + " = " + self.city + " " + self.address
        return output 
        
    
    def phone_number_string(self): 
        return '{:10s}'.format('phone') + " = " + self.city_code + " " + self.phone_number 
        
        
    def capacity_string(self): 
        output = '{:10}'.format('capacity') + " = " + ( "%d" % self.capacity )
        return output
        
    
    
