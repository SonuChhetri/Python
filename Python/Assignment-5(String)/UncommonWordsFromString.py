'''Write a program to find uncommon words from two Strings '''
def find_uncommon_words(s1, s2):
    from collections import Counter
    count = Counter(s1.split()) + Counter(s2.split())
    return [word for word, freq in count.items() if freq == 1]

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(f"Uncommon words: {find_uncommon_words(s1, s2)}\n")
