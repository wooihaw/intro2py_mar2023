# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:01:59 2023

@author: wooihaw
"""

def mean(d: list) -> float:
    '''Return the mean value of a list of numbers'''
    return sum(d)/len(d)

def median(d: list) -> float:
    '''Return the median value of a list of numbers'''
    n = len(d)
    b = sorted(d)
    if n%2==1:
        return b[n//2]
    else:
        return (b[n//2 - 1] + b[n//2]) / 2

with open("data/Heathrow.txt", "r") as f:
    raw_data = f.readlines()
    data = [float(t.strip()) for t in raw_data]
    
    print(f"Minimum: {min(data)}, maximum: {max(data)}")
    print(f"Mean: {mean(data)}, median: {median(data)}")