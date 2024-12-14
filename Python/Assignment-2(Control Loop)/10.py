# Q10.  Given three points (x1,  y1), (x2, y2) and (x3, y3), write a program to check if all the three 
# points fall on one straight line.
x1, y1 = map(int, input("Enter x1, y1: ").split())
x2, y2 = map(int, input("Enter x2, y2: ").split())
x3, y3 = map(int, input("Enter x3, y3: ").split())

if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("The points are collinear.")
else:
    print("The points are not collinear.")