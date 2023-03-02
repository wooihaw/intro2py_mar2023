# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:48:44 2023

@author: wooihaw
"""

s1 = set(range(5, 101, 5))  # set of numbers divisible by 5
s2 = set(range(7, 101, 7))  # set of numbers divisible by 
s3 = set(range(1, 101))  # set of numbers from 1 to 100

s4 = s3 - (s1 | s2)  # set of numbers not divisiable by 5 or 7
print(s4)