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

def add():
    print("Enter your query")
    query=input()
    try:
        mycursor.execute(query)
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
    
def update():
    print("Enter your query")
    query=input()
    try:
        mycursor.execute(query)
        result = mycursor.fetchall()
        for i in result:
            print(i)
        return;
    except:
        print("ther is syntax error")
        return;  
        

def delete():
    print("Enter your query")
    query=input()
    try:
        mycursor.execute(query)
        for i in mycursor:
            print(i)
        return;
    except:
        print("ther is syntax error")
        return;
while(True):
    print("Enter which operation you want to prform")
    print(''' 1.ADD
              2.UPDATE
              3.DELETE
          ''')
    choice=int(input("Enter your choice"))
    operations=[add,update,delete]
    operations[choice-1]()     
    
    
    
    
    
    
    