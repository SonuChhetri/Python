''' Write a program to odd Frequency Characters'''
def odd_frequency_chars(s):
    from collections import Counter
    count = Counter(s)
    return [char for char, freq in count.items() if freq % 2 != 0]

s = input("Enter a string: ")
print(f"Characters with odd frequencies: {odd_frequency_chars(s)}\n")
