# Q9. If a four-digit number is input through the keyboard, write a program to obtain the sum of the first and last digit of this number.
def sum_first_last_digits(num):

  # Extracting the last digit
  last_digit = num % 10
  # Extracting the first digit
  first_digit = num // 1000

  return first_digit + last_digit

number = int(input("Enter a four-digit number: "))

sum_digits = sum_first_last_digits(number)

print("The sum of the first and last digits is:", sum_digits)