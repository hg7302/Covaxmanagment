from django.shortcuts import render
from .models import Register
from .models import Appointment
from .models import supplier
from .models import stock
from django. contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
import smtplib, ssl

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
        Vname = request.POST.get('vaccine_name')
        checkAdh = Register.objects.filter(aadhar_id = Cid)
        if checkAdh:
            checkApp = Appointment.objects.filter(Cid=Cid)
            if checkApp:
                return render(request, "appointment.html", {"msg": "Already took an appointment!!"})
            insa = Appointment(appointment_id=appointment_id, ADate=ADate, ATime=ATime, Cid=Cid,Vname=Vname)
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

def stockrdt(request):
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
    storage = messages.get_messages(request)
    storage.used = True
    return render(request, "delapp.html")

def deleteapp(request):
    Cid = request.POST.get('Cid')

    checkApp = Appointment.objects.filter(Cid=Cid)
    if checkApp:
        Appointment.objects.filter(Cid=Cid).delete()
        return render(request, "appointment.html",{"msg":"Appointment cancelled successfully"})
    else:
        print("in else")
        return render(request, "appointment.html", {"msg": "No appointment found for this Aadhar Id"})

def updapp(request):
    return render(request, "updateapp.html")

def updateapp(request):
    Cid = request.POST.get('Cid')
    ADate = request.POST.get('ADate')
    ATime = request.POST.get('ATime')
    Appointment.objects.filter(Cid=Cid)
    checkApp = Appointment.objects.filter(Cid=Cid)
    if checkApp:
        Appointment.objects.filter(Cid=Cid).update(ADate=ADate)
        Appointment.objects.filter(Cid=Cid).update(ATime=ATime)
        return render(request, "appointment.html", {"msg": "your appointment updated successfully"})
    else:
        return render(request, "appointment.html", {"msg": "No appointment found for this Aadhar Id"})




list_of_admins = {
    "admin": "guptahimanshu2021@gmail.com",
    "ayushi": "ayushisharma210698@gmail.com",
    "himanshu": "guptahimanshu0302@gmail.com"
}
list_of_passwords = {
    "admin": "admin",
    "ayushi": "sharma",
    "himanshu": "gupta"
}


def send(username, email):
    email_id = "guptahimanshu2021@gmail.com"
    password = "fubasbyhuvqswkfk"  # enter your application password
    print(username)
    print(email)

    try:
        x = list_of_admins[username]
        print(x)
        if x == email:
            subject = """\
            Password reset
            """
            text = """\
            Your password for the {0} is {1}""".format(username, list_of_passwords[username])
            print("starting to send")
            conn = smtplib.SMTP('imap.gmail.com', 587)
            conn.ehlo()
            conn.starttls()
            print("in ttls")
            conn.login(email_id, password)
            message = 'Subject: {}\n\n{}'.format(subject, text)
            conn.sendmail(email_id, email, message)
            print("sent email")
            return 1
        else:
            return 0
    except KeyError:
        return 0

def adminuser(request):
    return render(request, 'aduser.html')
def forgot(request):
    return render(request, 'forgotpassword.html')
def forgotres(request):
    if request.method == 'POST':
        username=request.POST.get('userid')
        email=request.POST.get('email')
        result=send(username,email)
        if result==1:
            return render(request,'forgotresponse.html',{'msg':"The password has been sent to your email id!! "})
        else:
            return render(request, 'forgotresponse.html', {'msg': "You have entered wrong email id!! "})

def back(request):
    if request.method == 'POST':
        username = request.POST.get('userid')
        email = request.POST.get('email')
        result = send(username, email)
        if result == 1:
            return render(request, 'forgot_response.html', {"msg": "the password has sent to your emailid"})
        else:
            return render(request, 'forgot_response.html', {"msg": "Sorry wrong Email"})


def adminhome(request):
    if request.method == 'POST':
        name = request.POST.get('userid')
        password = request.POST.get('password')
        print(name)
        print(password)
        if name == 'himanshu' and password == 'gupta':
            return render(request, "admin.html", {"msg": "you are good"})
        elif name != 'admin' or password != 'admin':
            return render(request, "aduser.html", {"msg": "Incorrect Username or password"})
        else:
            return render(request, "forgotpassword.html", {"msg": "you are not good"})

def viewstock(request):
    stockFetch = stock.objects.raw('select Vaccine_name,Locality,Quantity_departed,Quantity_Remaning,Sname from stock  a, suppliers b where a.Supplier_regNo = b.Supplier_regNo')
    return render(request, "viewstock.html", {"stockValue": stockFetch})

def viewappointments(request):
    AppointmentFetch = Appointment.objects.raw('select First_name,Last_name,appointment_id,Cid,ATime,Adate,Vname from appointment,register where Cid=aadhar_id')
    return render(request, "viewappointments.html", {"appValue": AppointmentFetch})
