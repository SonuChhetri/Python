'''Write a program in Python to calculate Power(a,b) using function'''
def power(a, b):
    return a ** b

a = int(input("Enter base: "))
b = int(input("Enter exponent: "))
print(f"{a} raised to the power of {b} is {power(a, b)}\n")