# Write a Python script to ask for the length and width of a rectangle, 
# calculate and print the perimeter and area of the rectangle.
# E.g.
# Enter length: 5
# Enter width: 3
# perimeter = 16, area = 15.

l = float(input("Enter length: "))
w = float(input("Enter width: "))

area = l * w
perimeter = 2*l + 2*w

print(f"{perimeter = }, {area = }")