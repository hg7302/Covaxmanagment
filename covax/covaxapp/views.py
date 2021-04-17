from django.shortcuts import render
from .models import Register
from .models import Appointment
from .models import supplier
from .models import stock
from django. contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate

def main(request):
    return render(request, "main.html")

def user(request):
    return render(request,"home.html")

def myadmin(request):
    return render(request,"aduser.html")

def home(request):
    storage = messages.get_messages(request)
    storage.used = True
    return render(request, "register.html")

def regUser(request):
    if request.method == 'POST':
        aadhar_id = request.POST.get('aadhar_id')
        First_name= request.POST.get('First_name')
        Last_name= request.POST.get('Last_name')
        Age= request.POST.get('Age')
        Sex= request.POST.get('Sex')
        address= request.POST.get('address')
        Mobile = request.POST.get('Mobile')
        email = request.POST.get('email')
        checkAadhar = Register.objects.filter(aadhar_id = aadhar_id)
        if checkAadhar:
            return render(request,"register.html", {"msg":"Already Registered!!"})
        else:
            if len(aadhar_id)>12:
                return render(request,"register.html", {"msg":"Aadhar id of more than 12 characters not allowed"})
            else:
                ins = Register(aadhar_id=aadhar_id, First_name=First_name, Last_name=Last_name, Age=Age, Sex=Sex, address=address, Mobile=Mobile)
                ins.save()
                return render(request,"register.html", {"msg":"Registered successfully"})
    else:
        return render(request, "register.html")
def app(request):
    storage = messages.get_messages(request)
    storage.used = True
    return render(request, "appointment.html")

def bookappointment(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        ADate = request.POST.get('ADate')
        ATime = request.POST.get('ATime')
        Cid = request.POST.get('Cid')
        Vname = request.POST.get('Vname')
        checkAdh = Register.objects.filter(aadhar_id = Cid)
        if checkAdh:
            checkApp = Appointment.objects.filter(Cid=Cid)
            if checkApp:
                return render(request, "appointment.html", {"msg": "Already took an appointment!!"})
            insa = Appointment(appointment_id=appointment_id, ADate=ADate, ATime=ATime, Cid=Cid)
            insa.save()
            return render(request, "appointment.html", {"msg": "Your appointment is successful"})
        else:

            return render(request, "appointment.html", {"msg":"Aadhar id not found. Please register first."})
    else:
        return render(request, "appointment.html")
def supp(request):
    storage = messages.get_messages(request)
    storage.used = True
    return render(request, "supplier.html")

def supplierinfo(request):
    if request.method == 'POST':
        Supplier_regNO = request.POST.get('Supplier_regNO')
        Sname = request.POST.get('Sname')
        SAddress = request.POST.get('SAddress')
        Telephone_number= request.POST.get('Telephone_number')
        print(Telephone_number)
        inssup = supplier(Supplier_regNO=Supplier_regNO, Sname=Sname, SAddress=SAddress, Telephone_number=Telephone_number)
        inssup.save()
        return render(request, "supplier.html",{"msg":"Inserted successfully"})
    else:
        return render(request, "supplier.html")

def stock(request):
    storage = messages.get_messages(request)
    storage.used = True
    return render(request, "stock.html")

def stockinfo(request):
    if request.method == 'POST':
        Locality = request.POST.get('Locality')
        Vaccine_name = request.POST.get('Vaccine_name')
        Quantity_departed = request.POST.get('Quantity_departed')
        Quantity_Remaning = request.POST.get ('Quantity_Remaning')
        Supplier_regNo = request.POST.get ('Supplier_regNo')
        #inssup = stock(Vaccine_name=Vaccine_name,Locality=Locality,Quantity_departed=Quantity_departed,Quantity_Remaning=Quantity_Remaning,Supplier_regNo=Supplier_regNo)
        #inssup.save()
        obj = stock( Locality=Locality,Vaccine_name=Vaccine_name,  Quantity_departed=Quantity_departed, Quantity_Remaning=Quantity_Remaning, Supplier_regNo=Supplier_regNo)
        obj.save()
        print("Saved")
        return render(request, "stock.html",{"msg":"Inserted successfully"})
    else:
        return render(request, "stock.html")

def delapp(request):
    return render(request, "delapp.html")

def deleteapp(request):
    Cid = request.POST.get('Cid')
    Appointment.objects.filter(Cid=Cid).delete()
    checkApp = Appointment.objects.filter(Cid=Cid)
    if checkApp:
        return render(request, "appointment.html",{"msg":"Appointment cancelled successfully"})
    else:
        return render(request, "appointment.html", {"msg": "No appointment found for this Aadhar Id"})

def updapp(request):
    return render(request, "updateapp.html")

def updateapp(request):
    Cid = request.POST.get('Cid')
    Appointment.objects.filter(Cid=Cid)
    checkApp = Appointment.objects.filter(Cid=Cid)
    if checkApp:
        return render(request, "appointment.html", {"msg": "your appointment updated successfully"})
    else:
        return render(request, "appointment.html", {"msg": "No appointment found for this Aadhar Id"})







