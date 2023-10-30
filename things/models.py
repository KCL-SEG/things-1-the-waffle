from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Thing(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField(unique=False)
    quantity = models.PositiveIntegerField(unique=False)
