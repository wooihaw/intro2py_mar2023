# -*- coding: utf-8 -*-
"""
Created on Tue Feb  28 12:14:38 2023

@author: wooihaw
"""

#%% Check size of variable
a = 1234567890
print(a.__sizeof__())

#%% Binary and hexadecimal numbers
a = 0b10110001
b = 0x123def
c = a + b

print(a, b, c, sep=',')
print(hex(a))
print(bin(b))

#%% Do not begin a variable name with a digit
# 1star = 12345  # This will cause a syntax error
_1star = 12345  # instead we can start with an underscore

#%% Converting from one data type to another
a, b, c = 1, 2.3, 'abc'

d = float(a)
e = int(b)
f = int(c, base=16)  # Treating c as a hexadecimal number

print(a, b, c, d, e, f, sep=',')

x = '12345'
y = int(x)
print(x, y, sep=',')

g = str(a)
# h = g + 1  # string cannot be added with an integer

#%% Arithmetic operators have different priorities
a = 2**2
b = -2**2
print(a, b, sep='\n')

c = (-2)**2
print(c)

#%% Comparison operators will return either True or False
a = 10
b = 25
print(a < b)
print(a > b)
print(a == b)
print(a != b)

print(0 <= a < 20)
print(0 <= b < 20)

#%% Mixing single quotes and double quotes in strings
s1 = "It's a python."
s2 = 'John said "Yes, I am the one.".'
print(s1, s2, sep='\n')

s3 = 'It\'s a python.'
print(s3)

#%% Multiline string
s4 = '''This is a multiline
string that spans multiple
lines.'''
s5 = """This is another multiline
string that spans multiple
lines."""
print(s4, s5, sep='\n')

#%% String slicing examples
s = 'apple pie'
print(s[2:-2])
print(s[-2:2])  # Not working since the default step is 1
print(s[-2:2:-1])  # Works by change the step to -1

#%% String concatenation and repetition
s = 'hello'
t = 'c' + s[1:]
print(s, t, sep='\n')

print('=' * 40)
print('This is a new section.')
print(5 * 'Ha ')

#%% More string methods
m = 'Hello, World!'
print(m.swapcase())
print(m.split())
print(m.replace('l', ''))  # remove all 'l'
print(m.replace('l', '', 1))  # only remove the first 'l'
print(m)

n = 'abc123'
print(n.isalpha())
print(n.isdigit())
print(n.isalnum())

p = '    This is a string.   \n'
print(p)
print(p.lstrip())
print(p.rstrip())
print(p.strip())

q = '    This is a string.   \n   abc'
r = q.split('\n')
print(r)
print(r[0].strip())
print(r[1].strip())

s = r[0].strip() + r[1].strip()
print(s)

print('The character "l" appears ' + str(m.count('l')) + ' times')
print(f'The character "l" appears {m.count("l")} times')

#%% f-string formating
a = 123
b = 45.678
print(f'{a=}, {a=:04x}, {a=:016b}, {b=:.2f}, {b=:.4f}')

print("Python is a \N{snake}")
print("I am \N{grinning face}")

#%% List join, append and extend
alist = [1, 2, 3]
print(f'{alist=}')

alist = alist + [4]  # can only join with another list
alist += [5]  # same as above (alist = alist + [5])
print(f'{alist=}')

alist.append(6)  # Only can append one item
print(f'{alist=}')

alist.extend([7, 8])  # Similar to join
print(f'{alist=}')

alist.append([9, 0])
print(f'{alist=}')

# Use len() function to check the number of items in a list
print(f'Number of items in alist: {len(alist)}')

print(f'{alist[-1][0]=}')  # select the last item and its first element

#%% Sorting a list
blist = [3, 1, 4, 2, 6, 5, 0]
clist = sorted(blist, reverse=True)  # return a sorted list, descending order
print(f'{blist=}, {clist=}')

dlist = blist.sort()  # inplace sorting (blist is sorted)
print(f'{blist=}, {dlist=}')

#%% String to list and vice-versa
astring = 'Testing 123!'
alist = list(astring)  # convert string to list
print(f'{astring=}')
print(f'{alist=}')

bstring = ''.join(alist)
cstring = '-'.join(alist)
print(f'{bstring=}')
print(f'{cstring=}')

#%% List methods
alist = [1, 2.5, 'abc', [3, 7.2], 'xyz', 101, 1]

print(f'{alist.count(1)=}')

print(f'{alist.index("xyz")=}')
print(f'{alist.index(1)=}')  # only return the index of the first match

alist.remove(1)  # only remove the first match
print(f'{alist=}')  

alist.insert(2, 'Hello')  # Insert at index 2
print(f'{alist=}')

a = alist.pop(4)  # remove and return the item at index 4
print(f'{a=}')
print(f'{alist=}')

alist.clear()  # clear the list to become empty list
print(f'{alist=}')

#%% Using get() method for dictionary
adict = dict(a=1, b=2)
# print(adict['c'])  # KeyError as the key 'c' cannot be found
print(adict.get('c', 'Not found'))

print(adict.setdefault('d', 4))
print(f'{adict=}')

#%% Different between del and pop() method
adict = dict(a=1, b=2, c=3)
print(f'{adict=}')

del adict['b']
print(f'{adict=}')

d = adict.pop('c')
print(f'{adict=}')
print(f'{d=}')

#%% Joining 2 dictionaries
d1 = dict(a=1, b=2)
d2 = dict(x=3, y=4, z=5)

d3 = d1 | d2  # merge dictionaries using a union operator
print(f'{d3=}')

d1.update(d2)  # join d2 into d1
print(f'{d1=}')

d1['a'] = -1  # update the value for 'a'
print(f'{d1=}')

d4 = dict(b=0)
d1.update(d4)  # update the value for 'b' from d4
print(f'{d1=}')

