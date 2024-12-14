# Q11. Given the coordinates (x, y) of a center of a circle and it’s radius, write a program which will 
# determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use 
# sqrt( ) and pow( ) functions)
import math

x_center, y_center = map(int, input("Enter the center of the circle (x, y): ").split())
radius = float(input("Enter the radius of the circle: "))
x_point, y_point = map(int, input("Enter the point coordinates (x, y): ").split())

distance = math.sqrt((x_point - x_center) ** 2 + (y_point - y_center) ** 2)

if distance < radius:
    print("The point lies inside the circle.")
elif distance == radius:
    print("The point lies on the circle.")
else:
    print("The point lies outside the circle.")