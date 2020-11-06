from django.db import models

# Create your models here.
class Organisation(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    requirement=models.CharField(max_length=2000)
    contact=models.IntegerField()

class Expert(models.Model):
    name=models.CharField(max_length=100)
    skill=models.CharField(max_length=500)
    experience=models.FloatField()
    contact=models.IntegerField()
