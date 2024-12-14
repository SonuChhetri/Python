''' Write a program to frequency of numbers in String '''
def number_frequency(s):
    from collections import Counter
    return {char: s.count(char) for char in s if char.isdigit()}

s = input("Enter a string: ")
print(f"Number frequencies: {number_frequency(s)}\n")
