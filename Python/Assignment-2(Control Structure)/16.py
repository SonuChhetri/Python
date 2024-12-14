# Q16.If  the  three  sides  of  a  triangle  are  entered  through  the  keyboard,  write  a  program  to  check whether the triangle is isosceles, equilateral, scalene or right angled triangle. 
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if a == b == c:
    print("The triangle is equilateral.")
elif a == b or b == c or c == a:
    print("The triangle is isosceles.")
elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("The triangle is right-angled.")
else:
    print("The triangle is scalene.")