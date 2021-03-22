#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:11:09 2021

@author: himanshu
"""
from mysql import connector
mydb=connector.connect(host="localhost",user="himashu",passwd="Himashu@1234",database="COMPANY")
mycursor=mydb.cursor()
print("connection suceesful")

def registration():
    print("Welcome to registration of covid vaacine managament")
    print("Enter your first name")
    f_name=input()
    print("enter your last name")
    l_name=input()
    print("enter your addhar _id")
    addharid=input()
    print("Enter your gender")
    sex=input()
    print("Enter your addresss")
    address=input()
    print("Enter the patient Moble Number")
    MobileNumber=int(input())
    sql="INSERT INTO EMPLOYEE VALUES ({0},{1},{2},{3},{4},{5})".format(f_name,l_name,addharid,sex,address,MobileNumber)
    
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
    print("enter your Addhar id")
    addharid=input()
    print("Enter the date of requested vaccination")
    date=input()
    print("enter the time slot you want to come")
    time=input()
    sql="INSERT INTO APPOINTMENT({0},{1},{2})".format(addharid,date,time)
    try:
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
        return;
    except:
        print("ther is syntax error")
        return;  
        

def dose():
    print("Enter the vaccine number which is given to patient")
    vno=input()
    print("enter the vaccine name which is given to patient")
    vname=input()
    print("enter the appointment_id of the patient")
    aid= input()
    sql="INSERT INTO  Vaccinedose({0},{1},{2})".format(vno,vname,aid)
    try:
        mycursor.execute(sql)
        for i in mycursor:
            print(i)
        return;
    except:
        print("ther is syntax error")
        return;

def inventory():
    print("Enter the vaccine name")
    vno=input()
    print("enter the area")
    vname=input()
    print("enter the city")
    city=input()
    print("Enter the quantity departed")
    q_departed=int(input())
    print("enter the quantity remaning")
    q_remaning=int(input())
    sql="INSERT INTO  inventory({0},{1},{2},{3},{4})".format(vno,vname,city,q_departed,q_remaning)
    try:
        mycursor.execute(sql)
        for i in mycursor:
            print(i)
        return;
    except:
        print("ther is syntax error")
        return;
    
while(True):
    print("Welcome to Covid Vaccine Managment")
    print("Enter your choice")
    print(''' 1.Registration
              2.Appointment
              3. Vaccine Dose
              4. Inventory
          ''')
    choice=int(input("Enter your choice"))
    operations=[registration,appoint,dose,inventory]
    operations[choice-1]()   
    
    
    
    
    
    
    
    

