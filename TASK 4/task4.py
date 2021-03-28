#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:11:09 2021

@author: himanshu
"""
from mysql import connector
import random
mydb=connector.connect(host="localhost",user="himashu",passwd="Himashu@1234",database="COVAX")
mycursor=mydb.cursor()
print("connection suceesful")

def registration():
    print("Welcome to registration of covid vaacine managament")
    print("Enter your first name")
    f_name=input()
    print("enter your last name")
    l_name=input()
    print("enter your addhar _id")
    addharid=int(input())
    print(addharid)
    print("Enter your gender in M or F  format")
    sex=input()
    print("Enter your age")
    age=int(input())
    print("Enter your addresss")
    address=input()
    print("Enter the patient Moble Number")
    MobileNumber=int(input())
    sql="INSERT INTO Patient VALUES ({0},'{1}','{2}',{3},'{4}','{5}',{6});".format(addharid,f_name,l_name,age,sex,address,MobileNumber)
    
    try:
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
        return;
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex)._name_, ex.args)
        print (message)
    finally:
        mydb.commit()
    
def appoint():
    print("enter your Addhar id you have entered in the registration Process")
    addharid=int(input())
    print("Enter the date of requested vaccination in mm-dd")
    date=input()
    print("enter the time slot you want to come in hr:mi format")
    time=input()
    r1=random.randint(1000,10000000000)
    sql="INSERT INTO Appointment VALUES ({0},'2021-{1}','{2}',{3});".format(r1,date,time,addharid)
    try:
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
        return;
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex)._name_, ex.args)
        print (message)
    finally:
        mydb.commit()

def dose():
    print("Enter the vaccine number which is given to patient")
    vno=int(input())
    print("enter the vaccine name of whoch you want to get vaccinated")
    vname=input()
    print("enter the appointment_id of the patient")
    aid= int(input())
    print("enter your aadhar_id")
    pid=int(input())
    sql="INSERT INTO  VaccineDose VALUES ({0},{1},{2},'{3}');".format(vno,aid,pid,vname)
    try:
        mycursor.execute(sql)
        for i in mycursor:
            print(i)
        return;
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex)._name_, ex.args)
        print (message)
    finally:
        mydb.commit()

def inventory():
    print("Enter the barcode of the box")
    bcode=int(input())
    print("Enter the vaccine name")
    vname=input()
    print("enter the Locality")
    Local=input()
    print("enter the area")
    area=input()
    print("Enter the quantity departed")
    q_departed=int(input())
    print("enter the quantity remaning")
    q_remaning=int(input())
    print("Enter the Supplier registration Number")
    Srno=int(input())
    if q_departed<q_remaning :
        print("Can't exist departed less than remaning")
    sql="INSERT INTO  STOCK VALUES ({0},'{1}','{2}','{3}',{4},{5},{6});".format(bcode,vname,Local,area,q_departed,q_remaning,Srno)
    try:
        mycursor.execute(sql)
        for i in mycursor:
            print(i)
        return;
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex)._name_, ex.args)
        print (message)
    finally:
        mydb.commit()

def supplier():
    print("Enter the Supplier registration Number")
    srno=int(input())
    print("Enter the supplier name")
    sname=input()
    print("enter the Supplier Address")
    saddress=input()
    print("enter the TelephoneNumber")
    Tno=int(input())
    sql="INSERT INTO  SUPPLIERS VALUES ({0},'{1}','{2}',{3});".format(srno,sname,saddress,Tno)
    try:
        mycursor.execute(sql)
        for i in mycursor:
            print(i)
        return;
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex)._name_, ex.args)
        print (message)
    finally:
        mydb.commit()

    
def sign():
    print("Welcome to Covid Vaccine Managment")
    print("Enter your choice")
    print(''' 1.Registration
              2.Appointment
              3. Vaccine Dose
          ''')
    
    choice=int(input("Enter your choice"))
    operations=[registration,appoint,dose]
    operations[choice-1]()   
def admin():
    print("welcome to admin screen")
    print("Enter your choice")
    print(''' 1.  STOCK MANAGAMENT
              2.  SUPPLIERS MANAGMENT
        ''')
    choice=int(input("Enter your choice"))
    operations=[inventory,supplier]
    operations[choice-1]() 


if __name__ == '__main__':
    while(True):
         print("Welcome to the first advance covid managment Database")
         print("Eter your role")
         print('''   1. Admin
                2. User
                ''')
         choice=int(input("Enter your choice"))
         operations=[admin,sign]
         operations[choice-1]() 
    
    
    
    
    
    
    
    

