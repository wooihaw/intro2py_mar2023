# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:49:01 2023

@author: wooihaw
"""

from collections import Counter

with open("data/alice.txt", "r") as f:
    s = f.read()
    t = [c.lower() if c.isalpha() else ' ' for c in s]
    u = ''.join(t)
    w = u.split()  # split into words in a list
    
    count = Counter(w)
    print(f"10 most frequent words: {count.most_common(10)}")
    print(f"The word 'alice' appears {count['alice']} times.")
    