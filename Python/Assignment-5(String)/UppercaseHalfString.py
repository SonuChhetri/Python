'''Write a program uppercase Half String. '''
def uppercase_half(s):
    mid = len(s) // 2
    return s[:mid].upper() + s[mid:]

s = input("Enter a string: ")
print(f"Half uppercase: {uppercase_half(s)}\n")