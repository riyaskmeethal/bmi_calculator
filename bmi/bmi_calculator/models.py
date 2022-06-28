from django.db import models

# Create your models here.


scales = (("meter","Meter"),("foot",'Foot'))

class BmiModel(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    meters = models.FloatField()
    centi_meters = models.FloatField()
    foots = models.FloatField()
    inches = models.FloatField()