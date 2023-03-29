from django.shortcuts import render,redirect
from .models import Booking
from .models import Customer
from .models import Location
from .models import DroneShot
from django.contrib import messages


# Create your views here.

#renders CreateBookings page
def Create(request):
    location=Location.objects.all()
    droneShot=DroneShot.objects.all()
    data={
         "location":location,
         "droneShot":droneShot,
    }
    return render(request,"CreateBookings.html",context={"data":data})


#saves the booking
def CreateBooking(request):
    email=request.POST.get("email")
    shot=request.POST.get("shot")
    event_date=request.POST.get("event_date")
    event_time=request.POST.get("event_time")
    event_address=request.POST.get("addr")
    try:
        customer=Customer.objects.get(email=email)
        droneShot=DroneShot.objects.get(id=shot)
        address=Location.objects.get(id=event_address)
        print(customer.id)
        query=Booking(drone_shot_name=droneShot,customer=customer,event_time=event_time,event_date=event_date,event_address=address)
        query.save()
        print("saved")
        messages.success(request,"Booking Created Successfuly")
        return redirect("/bookings/List")
    except Customer.DoesNotExist:
           messages.error(request,"No customer found with the given email-id. Please create customer before creating bookings")
           return redirect("/bookings/Create")
    except DroneShot.DoesNotExist:
        messages.error(request,"No drone shots found. Please create drone shots before creating bookings")
        return redirect("/bookings/Create")
    except Location.DoesNotExist:
        messages.error(request,"No locations found. Please create locations shots before creating bookings")
        return redirect("/bookings/Create")
    

#returns the list of bookings
def ListBooking(request):
   data=Booking.objects.all()
   return render(request=request,template_name='ListBookings.html',context={"data":data})

def Edit(request,id):
    if request.method=="POST":
        try:
            data=Booking.objects.get(id=id)
            location=request.POST.get("addr")
            email=request.POST.get("email")
            shot=request.POST.get("shot")

            data.event_time=request.POST.get("event_time")
            data.event_date=request.POST.get("event_date")
            data.customer=Customer.objects.get(email=email)
            data.drone_shot_name=DroneShot.objects.get(id=shot)
            data.event_address=Location.objects.get(id=location)
            data.save()
            messages.success(request,"Updated booking details successfully")
            return redirect('/bookings/List')
        except Customer.DoesNotExist:
           messages.error(request,"No customer found with the given email-id. Please create customer before updating bookings")
        except Exception:
            messages.error(request,"Error while updating booking")    
    try:
        booking=Booking.objects.get(id=id)
        location=Location.objects.all()
        shot=DroneShot.objects.all()
        data={
            "booking":booking,
            "location":location,
            "shot":shot,
        }
        return render(request,"EditBookings.html",context={"data":data})
    except Booking.DoesNotExist:
        messages.error(request,"No Booking exsits.")
    except Location.DoesNotExist:
        messages.error(request,"No Location exsits.")
    except DroneShot.DoesNotExist:
        messages.error(request,"No DroneShot exsits.")
    except Exception as e:
        print(e)
        return redirect('/bookings/List')

def Delete(request,id):
    try:
        data=Booking.objects.get(id=id)
        data.delete()
        messages.success(request,"Deleted booking successfully")
        return redirect("/bookings/List")
    except:
        messages.error(request,"Error while deleting booking. Please try again")
        return redirect("/bookings/List")


            