# Q15. If  the  three  sides  of  a  triangle  are  entered  through  the  keyboard,  write  a  program  to check whether the triangle is valid or not. The triangle is valid if the sum of two sides is greater than 
# the largest of the three sides.
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if a + b > c and b + c > a and c + a > b:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")