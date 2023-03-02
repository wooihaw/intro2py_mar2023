# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:27:14 2023

@author: wooihaw
"""

# Using map() and filter()
ans1 = list(map(lambda y: y*y, filter(lambda x: x%2==0, range(1, 101))))
print(f"{ans1=}")

# Using list comprehension
ans2 = [x*x for x in range(1, 101) if x%2==0]
print(f"{ans2=}")

# Using for loop
ans3 = []
for x in range(1, 101):
    if x%2==0:
        ans3.append(x*x)
print(f"{ans3=}")