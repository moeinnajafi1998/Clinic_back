from django.db import models
from .Clinic import Clinic

class WhareHouse(models.Model):
    name = models.CharField(max_length=30,blank=False,unique=True,null=False)
    clinic = models.ForeignKey(Clinic,to_field='name',blank=False,null=False,on_delete=models.CASCADE)

    def __str__(self):
        return self.name