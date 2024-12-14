# Q7. Write  a  program  to  check  whether  a  triangle  is  valid  or  not,  when  the  three  angles  of  the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles 
# is equal to 180 degrees.

angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))

if angle1 + angle2 + angle3 == 180:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")