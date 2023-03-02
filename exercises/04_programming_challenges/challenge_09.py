# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:41:48 2023

@author: wooihaw
"""

from random import choice, shuffle

animals = ['wolf', 'whale', 'cheetah', 'lizard', 'tiger', 'monkey', 'parrot',
'gorilla', 'dolphin', 'snake']

animal = choice(animals)

anagram = list(animal)
shuffle(anagram)

ans = input(f"Do you know what is this animal -> {''.join(anagram)}? ")

if ans == animal:
    print("Bingo! You are right!")
else:
    print(f"Wrong answer! The correct answer is {animal}")
