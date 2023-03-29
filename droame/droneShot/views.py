from django.shortcuts import render,redirect
from droneShot.models import DroneShot
from django.contrib import messages

# Create your views here.
def Create(request):
    return render(request,"CreateShot.html")

def CreateShot(request):
    if request.method=="POST":
        name=request.POST.get("name")
        type=request.POST.get("type")
        query=DroneShot(shot_name=name,drone_type=type)
        try:
            query.save()
            messages.success(request,"Drone Shot Created Successfully")
            print("Saved")
            return redirect('/')
        except Exception as e:
          messages.error(request,"Error While Creating Drone Shot")
          print(e)
          return redirect('/')
