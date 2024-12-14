'''Write a program to find the octal equivalent of the entered number'''
number = int(input("Enter a number: "))
octal = oct(number)[2:]
print(f"Octal equivalent of {number} is {octal}\n")

