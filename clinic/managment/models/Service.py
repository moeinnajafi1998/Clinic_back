from django.db import models
from django_jalali.db import models as jmodels

class Service(models.Model):
    name = models.CharField(max_length=30,blank=False,unique=False,null=False)
    description = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name 