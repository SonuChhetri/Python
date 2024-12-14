'''Write a program to find all close matches of input string from a list'''
from difflib import get_close_matches
def find_close_matches(word, words):
    return get_close_matches(word, words)

words = input("Enter words separated by space: ").split()
word = input("Enter word to match: ")
print(f"Close matches: {find_close_matches(word, words)}\n")
