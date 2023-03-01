# Write a Python script to multiply all the items in a list.
alist = [12, 43, 57, 98, 83, -103, 256, -1]
print(f'{alist=}')

# Sum of all items in a list
sum_list = 0
for i in alist:
    sum_list = sum_list + i  # sum_list += i
print(f"{sum_list=}, {sum(alist)=}")

# Product of all items in a list
prod_list = 1
for i in alist:
    prod_list *= i
print(f"{prod_list=}")