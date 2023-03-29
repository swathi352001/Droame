from django.shortcuts import render,redirect
from .models import Customer
from location.models import Location
from django.contrib import messages
from django.db.utils import IntegrityError

# Create your views here.
def Create(request):
    data=Location.objects.all()
    return render(request,"CreateCustomer.html",context={"data":data})

def CreateCustomer(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone_number=request.POST.get("phone_number")
        location=request.POST.get("addr")
        print(name,email,phone_number,location)
        try:
            query=Customer(name=name,email=email,phone_number=phone_number,address=Location.objects.get(id=location))
            query.save()
            messages.success(request,"Customer Created Successfully")
            print("Saved")
            return redirect('/customers/List')
        except Location.DoesNotExist:
            messages.error(request,"Please create location before creating customer")
            return redirect('/customers/Create')
    
        except IntegrityError:
          messages.error(request,"Customer with email-id already exists")
          return redirect('/customers/Create')

def ListCustomer(request):
   data=Customer.objects.all()
   return render(request=request,template_name='ListCustomer.html',context={"data":data})

def Edit(request,id):
   if request.method=="POST":
       try:
            data=Customer.objects.get(id=id)
            data.email=request.POST.get("email")
            data.name=request.POST.get("name")
            data.phone_number=request.POST.get("phone_number")
            location=request.POST.get("addr")
            print(request.POST.get("addr"))
            data.address=Location.objects.get(id=location)
            data.save()
            messages.success(request,"Updated customer details successfully")
            return redirect('/customers/List')
       except IntegrityError:
           messages.error(request,"Customer with email-id already exists")
       except Customer.DoesNotExist:
           messages.error(request,"No Customer exist")
       except Location.DoesNotExist:
           messages.error(request,"Please create location before updating customer")
      
   try:
      customer=Customer.objects.get(id=id)
      location=Location.objects.all()
      data={
          "customer":customer,
          "location":location,
      }

      return render(request,"EditCustomer.html",context={"data":data})
   except:
       return redirect("/customers/List")

def Delete(request,id):
    try:
        data=Customer.objects.get(id=id)
        data.delete()
        messages.success(request,"Deleted customer successfully")
        return redirect("/customers/List")
    except:
        messages.error(request,"Error while deleting customer. Please try again")
        return redirect("/customers/List")
