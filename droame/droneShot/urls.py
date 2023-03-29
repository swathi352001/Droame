from django.urls import path,include
from droneShot.views import *

urlpatterns = [
    path('Create',Create,name="Create"),
    path('CreateShot',CreateShot,name="CreateShot")
]