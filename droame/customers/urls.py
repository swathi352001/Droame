from django.contrib import admin
from django.urls import path,include
from customers.views import *

urlpatterns = [
    path('Create',Create,name="Create"),
    path('CreateCustomer',CreateCustomer,name="CreateCustomer"),
    path('List',ListCustomer,name="List"),
    path('edit/<id>',Edit,name="Edit"),
    path('delete/<id>',Delete,name="Delete"),
]
