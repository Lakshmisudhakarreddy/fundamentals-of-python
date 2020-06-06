# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 06:37:15 2020

@author: sudha
"""    



def power(x,y):
 
    if(y==1):
        return(x)
    if(y!=1):
        return(x*power(x,y-1))
x=int(input("enter x:"))
y=int(input("enter y: "))
print("result:",power(x,y))    


input('').split()
