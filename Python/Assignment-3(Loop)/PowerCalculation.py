# 3. Two numbers are entered through the keyboard. Write a program to find the value of one number 
# raised to the power of another.

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = 1
for i  in range(exponent):
    result*=base

print(f"{base} raised to the power {exponent} is {result}.")