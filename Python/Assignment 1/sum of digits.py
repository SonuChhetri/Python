#If a five-digit number is input through the keyboard, write a program to calculate the sum of its digits.(Hint: Use the modulus operator ‘%’)
# Input a five-digit number
number = int(input("Enter a five-digit number: "))
original_number = number  # Storing the original number for later display
# Checking if the number is a valid five-digit number
if 10000 <= number <= 99999:
    sum_of_digits = 0
    while number > 0:
        digit = number % 10      # Get the last digit
        sum_of_digits += digit    # Add it to the sum
        number //= 10             # Remove the last digit
    print(f"The sum of the digits of {original_number} is: {sum_of_digits}")
else:
    print("Please enter a valid five-digit number!")
