from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator

# Create your models here.

class Thing(models.Model):
    name = models.TextField(max_length=30, blank=False, unique=True, validators=[MinLengthValidator(0), MaxLengthValidator(30)])
    description = models.TextField(max_length=120, blank=True, validators=[MinLengthValidator(0), MaxLengthValidator(120)])
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

