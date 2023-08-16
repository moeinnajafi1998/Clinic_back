from django.db import models
from django_jalali.db import models as jmodels

class MedicalAppointment(models.Model):
    sick = models.CharField(max_length=50,blank=False,unique=False,null=False)
    clinic = models.CharField(max_length=50,blank=False,unique=False,null=False)
    typical_user = models.CharField(max_length=50,blank=False,unique=False,null=False)
    nurse = models.CharField(max_length=50,blank=False,unique=False,null=False)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    date = jmodels.jDateField(default='1402-01-01')
    time = models.CharField(max_length=5,blank=False,unique=False,null=False,default='08:00')


    def __str__(self):
        return self.sick + " : " + self.clinic