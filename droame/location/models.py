from django.db import models

# Create your models here.
class Location(models.Model):
    door_no=models.CharField(max_length=10)
    address=models.CharField(max_length=250)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)