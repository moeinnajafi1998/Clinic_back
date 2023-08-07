from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30,blank=False,unique=True,null=False)
    TYPE_CHOICES = (
        ('Professional', 'P'),
        ('General', 'G'),
    )

    type = models.CharField(
        max_length=12,
        choices=TYPE_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name