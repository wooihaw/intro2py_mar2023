# Write a Python script to find the second largest value in a list.
alist = [12, 43, 57, 98, 83, -103, 256, -55, 185]
print(f'{alist=}')

alist.sort()
print(f"Second largest value: {alist[-2]}")