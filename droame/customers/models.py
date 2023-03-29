from django.db import models
from location.models import Location
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField(unique=True,blank=False,null=False)
    phone_number = models.BigIntegerField(max_length=10,blank=False,null=False)
    address=models.ForeignKey(Location,on_delete=models.CASCADE)

