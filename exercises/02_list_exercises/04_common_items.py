# Write a Python script to find common items between two lists.
alist = [99, 'P', 1, 'xyz', 'a', 2.5]
blist = ['xyz', 2.5, 2.5, 3, 99, 99, 2.5, 'xyz', -1.2, 99]

# Use set
print(f"Common items: {set(alist) & set(blist)}")

# Use for loop
clist = []
for i in alist:
    if i in blist:
        clist.append(i)
print(f"Common items: {clist}")

# Use list comprehension
clist2 = [i for i in alist if i in blist]
print(f"Common items: {clist2}")