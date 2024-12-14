''' Write a program to specific Characters Frequency in String List'''
def specific_char_frequency(strings, chars):
    from collections import Counter
    freq = Counter(''.join(strings))
    return {char: freq[char] for char in chars}

strings = input("Enter strings separated by spaces: ").split()
chars = input("Enter specific characters: ")
print(f"Frequencies: {specific_char_frequency(strings, chars)}\n")
