from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    TYPE_CHOICES = (
        ('Clinic_Admin', 'CA'),
        ('Typical_User', 'TU'),
        ('Nurse', 'N'),
        ('Sick', 'S'),
    )

    user_type = models.CharField(
        max_length=12,
        choices=TYPE_CHOICES,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.username