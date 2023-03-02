# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:34:17 2023

@author: wooihaw
"""

class Circle:
    def __init__(self, r):
        self.r = r
    def __str__(self):
        return f"This is a circle with the radius of {self.r}"
    def area(self):
        return 3.142 * self.r ** 2
    def circumference(self):
        return 2 * 3.142 * self.r

circle1 = Circle(4)
print(circle1)
print(f"Area = {circle1.area()}")
print(f"Circumference = {circle1.circumference()}")