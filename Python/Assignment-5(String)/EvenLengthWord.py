'''WAP to print even length words in a string. '''
def even_length_words(s):
    words = s.split()
    return [word for word in words if len(word) % 2 == 0]

s = input("Enter a string: ")
print(f"Even length words: {even_length_words(s)}\n")