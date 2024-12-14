'''Write a program to take input a string of digits and convert it to an integer without 
using int() function. '''
def str_to_int(s):
    number = 0
    for char in s:
        number = number * 10 + (ord(char) - ord('0'))
    return number

s = input("Enter a string of digits: ")
print(f"Converted integer: {str_to_int(s)}\n")