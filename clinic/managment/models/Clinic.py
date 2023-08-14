from django.db import models
from .User import User


class Clinic(models.Model):
    name = models.CharField(max_length=30,blank=False,unique=True,null=False)
    address = models.CharField(max_length=100,blank=True,null=True)
    manager = models.ForeignKey(User,to_field='username',on_delete=models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return self.name