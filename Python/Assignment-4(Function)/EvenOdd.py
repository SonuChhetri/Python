'''Write a program in Python to find the square of any number using the function'''
def is_even(num):
    return num % 2 == 0

num = int(input("Enter a number: "))
print(f"{num} is {'even' if is_even(num) else 'odd'}\n")
