from django.shortcuts import render
from django.http import HttpResponse
from .models import registration

def home(request):
    if request.method == "GET":
        firstname= request.GET.get('firstname')
        lastname=request.GET.get('lastname')
        gender=request.GET.get('gender')
        phone=request.GET.get('phone')
        email=request.GET.get('email')
        birthday=request.GET.get('birthday')
        address=request.GET.get('address')
        file=request.GET.get('file')
        state=request.GET.get('state')
        service=request.GET.get('service')
       
    
        newregistration=registration(first_name=firstname,last_name=lastname,gender=gender,phone=phone,email=email,birthday=birthday,address=address,file=file,state=state,service=service)
        newregistration.save()
    return render(request,'home.html')

