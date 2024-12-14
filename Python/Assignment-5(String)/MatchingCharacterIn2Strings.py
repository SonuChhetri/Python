'''Write a program to count the Number of matching characters in a pair of string '''
def count_matching_chars(s1, s2):
    return len(set(s1) & set(s2))

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(f"Matching characters: {count_matching_chars(s1, s2)}\n")