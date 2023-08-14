from django.db import models
from .Category import Category
from .WhareHouse import WhareHouse


class Item(models.Model):
    name = models.CharField(max_length=30,blank=False,unique=True,null=False)
    category = models.ForeignKey(Category,to_field='name',blank=True,null=True,on_delete=models.SET_NULL)
    wharehouse =  models.ForeignKey(WhareHouse,to_field='name',blank=True,null=True,on_delete=models.SET_NULL)