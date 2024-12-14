'''Python program to check if a string has at least one letter and one number '''
def has_letters_and_numbers(s):
    has_letter = any(c.isalpha() for c in s)
    has_number = any(c.isdigit() for c in s)
    return has_letter and has_number

s = input("Enter a string: ")
print(f"Contains letters and numbers: {has_letters_and_numbers(s)}\n")