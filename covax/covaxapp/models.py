from django.db import models

class Register(models.Model):
    aadhar_id = models.CharField(max_length = 12, primary_key=True)
    First_name = models.CharField(max_length = 30)
    Last_name = models.CharField(max_length = 20)
    Age = models.IntegerField()
    Sex = models.CharField(max_length = 4)
    address = models.CharField(max_length = 50)
    Mobile = models.CharField(max_length = 20)
    email = models.CharField(max_length=45,default="NULL")
    class Meta:
        db_table="Register"


class Appointment(models.Model):
    appointment_id = models.IntegerField(max_length=10, primary_key=True)
    ADate = models.DateField()
    ATime = models.CharField(max_length = 20)
    Cid = models.CharField(max_length=12)
    Vname = models.CharField(max_length=45,default='NULL')
    class Meta:
        db_table = "Appointment"

class supplier(models.Model):
    Supplier_regNO =models.IntegerField(primary_key=True)
    Sname = models.CharField(max_length = 30)
    SAddress = models.CharField(max_length = 30)
    Telephone_number = models.CharField(max_length = 10)
    class Meta:
        db_table = "SUPPLIERS"

class stock(models.Model):
    Locality = models.CharField(max_length = 30, primary_key=True)
    Vaccine_name = models.CharField(max_length=30)
    Quantity_departed = models.IntegerField()
    Quantity_Remaning =models.IntegerField()
    Supplier_regNo = models.IntegerField()
    class Meta:
        db_table = "stock"

