# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 21:16:04 2019

@author: ahirr
"""
Number = int(input("Please Enter any Number: "))    
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
     
print("\n Reverse of entered number is = %d" %Reverse)

            
    
