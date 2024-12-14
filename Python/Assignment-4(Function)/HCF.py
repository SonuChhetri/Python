'''Write a program in Python to calculate H.C.F using while loop.'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
while num2:
    num1, num2 = num2, num1 % num2
print(f"H.C.F is {num1}\n")
