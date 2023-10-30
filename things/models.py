from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Thing(models.Model):
    name = models.TextField(max_length=30, blank=False, unique=True)
    description = models.TextField(max_length=120, blank=True, unique=False)
    quantity = models.PositiveIntegerField(unique=False, validators=[MaxValueValidator(100)])

