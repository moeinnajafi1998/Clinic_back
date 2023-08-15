from django.db import models


class RequestSession(models.Model):
    sick = models.CharField(max_length=50,blank=False,unique=False,null=False)
    clinic = models.CharField(max_length=50,blank=False,unique=False,null=False)
    description = models.TextField()
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.sick + " : " + self.clinic