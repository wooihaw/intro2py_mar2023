# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 09:10:52 2023

@author: wooihaw
"""

#%% Example on for loop with enumerate

alist = list('abcde')
for i, j in enumerate(alist, start=1):
    print(f"{i}. {j}")
    
#%% Repeat tasks with for loop without assigning variable

for _ in range(5):
    print("Hello world!")

#%% Using zip() function to loop through 3 lists

alist = [1, 3, 5, 7, 9]
blist = [2, 4, 6, 8]
clist = list('aeiou')

for p, (q, r, s) in enumerate(zip(alist, blist, clist), start=1):
    print(f"{p}. {q}, {r}, {s}")
    
#%% Example on list comprehension
# Find out how many even numbers are there in a list
alist = [12, 43, 76, 99, 11, 123, 234, 72]

# Use for loop
n_even = 0
for i in alist:
    if i%2 == 0:  # remainder should be 0 for even number
        n_even += 1
print(f"There are {n_even} numbers in the list")

# Use list comprehension
n_even2 = len([i for i in alist if i%2==0])
print(f"There are {n_even2} numbers in the list")

#%% Can we have tuple comprehension?

atuple = (i for i in range(100) if i%2)
print(atuple)  # This is not a tuple, but a generator object
print(atuple.__sizeof__())
print(tuple(atuple))  # convert to tuple

btuple = tuple(range(1, 100, 2))
print(btuple)  # This is a tuple
print(btuple.__sizeof__())

#%% Function examples
def add_one(x):
    print(x+1)

add_one(4)
x = add_one(5)
print(f"{x=}")

y = print("hello world!")  
print(y)  # print() does not return any value

alist = [3, 1, 2]
blist = alist.sort()
print(f"{blist=}")  # sort() method returns None

clist = sorted(alist)
print(f"{clist=}")  # sorted() function will return a sorted copy of the list

#%% Anonymous function example 1
alist = ['ID21', 'ID7', 'ID57', 'ID101', 'ID3', 'ID85']
blist = sorted(alist)
print(f"{blist=}")

clist = sorted(alist, key=lambda x: int(x[2:]))
print(f"{clist=}")

#%% Anonymous function example 2
paper_size = ('A1', 'A4', 'A3', 'A5', 'A2')

print(f"{max(paper_size)=}")

print(f"{max(paper_size, key=lambda x: -int(x[1]))=}")

print(f"{min(paper_size, key=lambda x: -int(x[1]))=}")

#%% map() example

alist = list(range(1, 11))

# Use map()
sqr1 = list(map(lambda x: x*x, alist))
print(f"{sqr1=}")

# Use list comprehension
sqr2 = [x*x for x in alist]
print(f"{sqr2=}")

#%% filter() example
alist = ['bell', 'apple', 'pear', 'orange']

# Use filter()
blist = list(filter(lambda s:s[0] in 'aeiou', alist))
print(f"{blist=}")

# Use list comprehension
clist = [s for s in alist if s[0] in 'aeiou']
print(f"{clist=}")