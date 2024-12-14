#Write a program to find consecutive characters frequency 
def consecutive_char_freq(s):
    from itertools import groupby
    return {char: len(list(group)) for char, group in groupby(s)}

s = input("Enter a string: ")
print(f"Consecutive character frequencies: {consecutive_char_freq(s)}\n")
