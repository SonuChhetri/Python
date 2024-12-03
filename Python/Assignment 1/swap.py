# Two numbers are input through the keyboard into two locations C and D. Write a program to 
# interchange the contents of C and D.
C = float(input("Enter first number: "))
D = float(input("Enter second number: "))

C, D = D, C

print(f"Interchanged numbers are C = {C}, D = {D}")