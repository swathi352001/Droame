from django.urls import path,include
from location.views import *

urlpatterns = [
    path('Create',Create,name="Create"),
    path('CreateLocation',CreateLocation,name="CreateLocation")
]