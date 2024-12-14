''' Write a program to find words that are greater than the given length k'''
def words_greater_than_k(s, k):
    return [word for word in s.split() if len(word) > k]

s = input("Enter a sentence: ")
k = int(input("Enter length k: "))
print(f"Words greater than length {k}: {words_greater_than_k(s, k)}\n")
