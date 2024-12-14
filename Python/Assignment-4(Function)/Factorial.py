'''. Write a program in Python to calculate factorial of a natural number.'''
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

num = int(input("Enter a natural number: "))
print(f"Factorial of {num} is {factorial(num)}\n")