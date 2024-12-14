'''Write a program to accept the strings which contain all vowels '''
def contains_all_vowels(s):
    vowels = set('aeiou')
    return vowels <= set(s.lower())

s = input("Enter a string: ")
print(f"Contains all vowels: {contains_all_vowels(s)}\n")
