from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    TYPE_CHOICES = (
        ('Clinic_Admin', 'CA'),
        ('Typical_User', 'TU'), # منشی
        ('Nurse', 'N'),
        ('Sick', 'S'),
        ('Warehouse_Keeper', 'WK'),
        ('Financial_Manager', 'FM'),  
    )

    user_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        blank=True,
        null=True,
    )

    image = models.ImageField(upload_to='users/',null=True,blank=True)

    
    def __str__(self):
        return self.username