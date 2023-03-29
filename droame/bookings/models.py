from django.db import models

# Create your models here.
from customers.models import Customer
from location.models import Location
from droneShot.models import DroneShot

class Booking(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    drone_shot_name = models.ForeignKey(DroneShot, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    event_date=models.DateField()
    event_time=models.TimeField()
    event_address=models.ForeignKey(Location, on_delete=models.CASCADE)
