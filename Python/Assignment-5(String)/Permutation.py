'''. Write a program to print permutation of a given string using inbuilt function'''
from itertools import permutations
def print_permutations(s):
    return [''.join(p) for p in permutations(s)]
s = input("Enter a string: ")
print(f"Permutations: {print_permutations(s)}\n")