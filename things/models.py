from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Thing(models.Model):
    name = models.TextField()
    description = models.TextField()
    quantity = models.PositiveIntegerField()
