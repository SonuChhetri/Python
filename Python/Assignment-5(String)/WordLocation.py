#Write a program to word location in String 
def word_location(s, word):
    return s.find(word)

s = input("Enter a string: ")
word = input("Enter word to find: ")
print(f"Word location: {word_location(s, word)}\n")

