# The  length  &  breadth  of  a  rectangle  and  radius  of  a  circle  are  input  through  the  keyboard. Write  a  program  to  calculate  the  area  &  perimeter  of  the  rectangle,and  the  area  & circumference of the circle.

import math  # Importing the math module to access the value of pi

length = float(input("Enter the length of a rectangle: "))
breadth = float(input("Enter the breadth of a rectangle: "))

# Calculating area and perimeter of the rectangle
area_rectangle = length * breadth
perimeter_rectangle = 2 * (length + breadth)

print(f"Area of Rectangle: {area_rectangle}")
print(f"Perimeter of Rectangle: {perimeter_rectangle}")

radius = float(input("Enter radius of a circle: "))

# Calculating area and circumference of the circle
area_circle = math.pi * (radius ** 2)
circumference_circle = 2 * math.pi * radius

print(f"Area of circle is: {area_circle:.2f}")
print(f"Circumference of circle:: {circumference_circle:.2f}")
