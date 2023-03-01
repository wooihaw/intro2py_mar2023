# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:19:53 2023

@author: wooihaw
"""

#%% Set examples
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
s2 = {1, 3, 5, 7, 9}
s3 = {2, 4, 6, 8, 10}

print(f"{s1-s3=}")  # print the items in s1 that is not in s3
print(f"{s3-s1=}")  # print the items in s3 that is not in s1
print(f"{s1.symmetric_difference(s3)=}") # print the items not in s1 and s3
print(f"{s3.symmetric_difference(s1)=}") # print the items not in s3 and s1

#%% Use set to get the unique items

# Using for loop
alist = [1, 2, 1, 5, 'a', 'b', 'a', 2]
ulist = []

for i in alist:
    if i not in ulist:
        ulist.append(i)
print(ulist)

# Using set
print(list(set(alist)))

#%% Using zip() to iterate multiple lists
fruits = ['apple', 'orange', 'durian', 'rambutan']
prices = [1.5, 2.5, 15]

for i, j in zip(fruits, prices):
    print(f"{i.capitalize()}: RM{j:.2f}")
    
# Use enumerate to automatically index the iteration
for i, (j, k) in enumerate(zip(fruits, prices), start=1):
    print(f"{i}. {j.capitalize()}: RM{k:.2f}")

#%% List comprehension example 1
names = ['ali', 'bala', 'chen', 'dave']

# Use for loop
cap_names = []
for n in names:
    cap_names.append(n.capitalize())
print(cap_names)

# Use list comprehension
cap_names2 = [n.capitalize() for n in names]
print(cap_names2)

#%% List comprehension example 2
languages = ['Java', 'Rust', 'Python', 'Swift', 'Go', 'Julia']

# Use for loop
filtered_list = []
for i in languages:
    if 'o' in i:
        filtered_list.append(i)
print(filtered_list)

# Use list comprehension
filtered_list2 = [i for i in languages if 'o' in i]
print(filtered_list2)

#%% Dictionary comprehension example
fruit_prices = dict(apple=1.5, orange=2.5, durian=15)

# Create a dictionary with discounted price (10%) using for loop
discounted_prices = {}
for k in fruit_prices:
    discounted_prices[k] = 0.9 * fruit_prices[k]
print(discounted_prices)

# Create a dictionary with discounted price (10%) using dictionary comprehension
discounted_prices2 = {k: 0.9*fruit_prices[k] for k in fruit_prices}
print(discounted_prices2)
