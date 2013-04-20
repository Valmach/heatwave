from django.db import models
import datetime

# Create your models here.

class Volunteer(models.Model):
    name = models.CharField(max_length = 100)
    number = models.CharField(max_length = 20)
    geo_lat = models.DecimalField('latitude', max_digits=13, decimal_places=10, blank=True, null=True)
    geo_long = models.DecimalField('longitude', max_digits=13, decimal_places=10, blank=True, null=True)
    
    
    def __unicode__(self):
             return self.name
             
          
class Vulnerable(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    number = models.CharField(max_length = 20)
    geo_lat = models.DecimalField('latitude', max_digits=13, decimal_places=10, blank=True, null=True)
    geo_long = models.DecimalField('longitude', max_digits=13, decimal_places=10, blank=True, null=True)
    
    
    def __unicode__(self):
             return self.name
             
class Alert(models.Model):
    to = models.ForeignKey(Volunteer)
    regarding = models.ForeignKey(Vulnerable)
    sent = models.DateTimeField(auto_now_add= True)
    is_okay = models.BooleanField(default = False)
    
    def __unicode__(self):
            return "To " + self.to.name + " RE: " + self.regrading.name