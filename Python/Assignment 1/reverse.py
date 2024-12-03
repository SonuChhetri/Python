# If a five digit number is input through the keyboard, write a program to reverse the number.

def reverse_number(num):

  reversed_num = 0
  while num > 0:
    # Extracting the last digit
    digit = num % 10
    # Appending the digit to the reversed number
    reversed_num = reversed_num * 10 + digit
    # Removing the last digit from the original number
    num //= 10

  return reversed_num

number = int(input("Enter a five-digit number: "))

reversed_number = reverse_number(number)

print("The reversed number is:", reversed_number)