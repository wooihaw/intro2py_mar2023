# Write a Python script to concatenate following dictionaries to create a new one.
# Expected Result: 
# d4 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

d1 = {'a': 10, 'b': 20}
d2 = {'c': 30, 'd': 40}
d3 = {'e': 50}

# Use update() method
d4_1 = {}
for d in (d1, d2, d3):
    d4_1.update(d)
print(f"{d4_1=}")

# Use union operator
d4_2 = d1 | d2 | d3
print(f"{d4_2=}")

# Use for loop
d4_3 = {}
for d in (d1, d2, d3):
    for k in d:
        d4_3[k] = d[k]
print(f"{d4_3=}")

# Use dictionary comprehension
d4_4 = {k: d[k] for d in (d1, d2, d3) for k in d}
print(f"{d4_4=}")

# Use ** to unpack the dictionary
d4_5 = {**d1, **d2, **d3}
print(f"{d4_5=}")