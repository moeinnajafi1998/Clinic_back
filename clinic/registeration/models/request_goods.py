from django.db import models
from django_jalali.db import models as jmodels


class RequestGoods(models.Model):
    item = models.CharField(max_length=30,blank=False,unique=False,null=False)
    number = models.IntegerField(default=1,blank=False,unique=False,null=False)
    clinic = models.CharField(max_length=30,blank=False,unique=False,null=False)
    typical_user = models.CharField(max_length=30,blank=False,unique=False,null=False)
    description = models.TextField(blank=True,null=True)
    is_done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item + " : " + self.number