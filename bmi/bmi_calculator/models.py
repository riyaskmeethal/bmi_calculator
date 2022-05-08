from django.db import models

# Create your models here.



class BmiModel(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()