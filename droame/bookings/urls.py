from django.contrib import admin
from django.urls import path,include
from bookings.views import *

urlpatterns = [
    path('Create',Create,name="Create"),
    path('CreateBooking',CreateBooking,name="CreateBooking"),
    path('List',ListBooking,name="List"),
    path('edit/<id>',Edit,name="Edit"),
    path('delete/<id>',Delete,name="Delete"),
]
