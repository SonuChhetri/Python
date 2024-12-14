# Q12. Given a point (x, y), write a program to find out if it lies on the x-axis, y-axis or at the origin, viz. (0, 0).
x, y = map(int, input("Enter the coordinates of the point (x, y): ").split())

if x == 0 and y == 0:
    print("The point is at the origin.")
elif x == 0:
    print("The point lies on the y-axis.")
elif y == 0:
    print("The point lies on the x-axis.")
else:
    print("The point does not lie on either axis or the origin.")
