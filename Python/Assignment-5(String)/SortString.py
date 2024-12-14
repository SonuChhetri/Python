# Write a program to sort String list by K character frequency 
def sort_by_k_char_freq(strings, k):
    from collections import Counter
    return sorted(strings, key=lambda x: Counter(x)[k], reverse=True)

strings = input("Enter strings separated by space: ").split()
k = input("Enter character to sort by: ")
print(f"Sorted list: {sort_by_k_char_freq(strings, k)}\n")
