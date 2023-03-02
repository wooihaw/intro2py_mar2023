# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:36:49 2023

@author: wooihaw
"""

while True:
    try:
        investment = float(input("Enter the initial investment: "))
        annual_rate = float(input("Enter the annual rate (%): "))
        years = int(input("Enter years of investment: "))
    except:
        print("Invalid input! Please re-enter.")
    else:
        break

print(f"Initial investment: ${investment:.2f}, annual rate: {annual_rate}%, years of investment: {years}")

for i in range(years):
    investment = investment + investment * annual_rate/100
    print(f"Year {i+1: >2}: $ {investment:.2f}")