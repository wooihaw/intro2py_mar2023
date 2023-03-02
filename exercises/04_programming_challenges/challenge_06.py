# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:19:54 2023

@author: wooihaw
"""

def  convert_cel_to_far(C):
    return C * 9/5 + 32
    

def convert_far_to_cel(F):
    return (F - 32) * 5/9


f = float(input("Enter a temperature in degrees Fahrenheit: "))
print(f"The temperature in degree Celsius is {convert_far_to_cel(f):.2f}")

c = float(input("Enter a temperature in degrees Celsius: "))
print(f"The temperature in degree Fahrenheit is {convert_cel_to_far(c):.2f}")