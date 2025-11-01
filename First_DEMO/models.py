from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description = models.CharField(max_length=255,unique=True)
    price = models.FloatField(unique=True)

    def __str__(self):
        return self.name