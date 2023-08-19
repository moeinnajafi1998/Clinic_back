from django.db import models
from django_jalali.db import models as jmodels
from managment.models import Item
from managment.models import Service

class VisitAppointment(models.Model):
    nurse = models.CharField(max_length=30,blank=False,unique=False,null=False)
    sick = models.CharField(max_length=30,blank=False,unique=False,null=False)
    clinic = models.CharField(max_length=30,blank=False,unique=False,null=False)
    typical_user = models.CharField(max_length=30,blank=False,unique=False,null=False)
    used_items = models.ManyToManyField(Item,blank=True)
    services = models.ManyToManyField(Service,blank=True)
    description = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.nurse + " : " + str(self.sick)