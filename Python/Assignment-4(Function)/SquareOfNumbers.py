''' Write a program in Python to find the square of any number using the function. '''
def square(num):
    return num ** 2

num = int(input("Enter a number: "))
print(f"Square of {num} is {square(num)}\n")