from django.db import models

# Create your models here.
class DroneShot(models.Model):
    shot_name=models.CharField(max_length=100)
    drone_type=models.CharField(max_length=100)