# Q5. A five-digit number is entered through the keyboard. Write a program to obtain the reversed 
# number and to determine whether the original and reversed numbers are equal or not.

number = int(input("Enter a five-digit number: "))

# Reverse the number
reversed_number = int(str(number)[::-1])   #str(number)[::-1] converts the number to a string, then uses Python’s slice notation with [::-1] to reverse the string. int(...) converts the reversed string back to an integer, giving us the reversed number

if number == reversed_number:
    print("The original and reversed numbers are equal.")
else:
    print("The original and reversed numbers are not equal.")
print(f"Reversed number is: {reversed_number}")
