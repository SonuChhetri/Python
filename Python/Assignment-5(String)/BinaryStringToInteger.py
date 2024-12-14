'''Write a program to take binary input numbers and convert it to an integer without 
using int() function.'''
def binary_to_int(b):
    number = 0
    for char in b:
        number = number * 2 + (ord(char) - ord('0'))
    return number

b = input("Enter a binary string: ")
print(f"Converted integer: {binary_to_int(b)}\n")