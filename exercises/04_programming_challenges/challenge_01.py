# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:28:38 2023

@author: wooihaw
"""

# c - No. of chickens
# r - No. of rabbits
# c + r = 35
# 2*c + 4*r = 94

for c in range(36):  # Try from 0 chicken to 35 chickens
    r = 35 - c
    if 2*c + 4*r == 94:
        print(f"There are {c} chickens and {r} rabbits.")