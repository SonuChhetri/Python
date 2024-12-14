# 2. Write a program to find the factorial value of any number entered through the keyboard.

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}.")