from django.shortcuts import render,redirect
from location.models import Location
from django.contrib import messages

# Create your views here.
def Create(request):
    return render(request,"CreateLocation.html")

def CreateLocation(request):
    if request.method=="POST":
        door=request.POST.get("door")
        addr=request.POST.get("addr")
        city=request.POST.get("city")
        state=request.POST.get("state")
        query=Location(door_no=door,address=addr,city=city,state=state)
        try:
            query.save()
            messages.success(request,"Location Created Successfully")
            print("Saved")
            return redirect('/')
        except Exception as e:
          messages.error(request,"Error While Creating Location")
          print(e)
          return redirect('/')