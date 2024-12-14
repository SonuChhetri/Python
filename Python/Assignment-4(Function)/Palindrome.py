'''Write a program in Python to check whether an inputted number is palindrome.'''
num = input("Enter a number: ")
if num == num[::-1]:
    print(f"{num} is a palindrome\n")
else:
    print(f"{num} is not a palindrome\n")