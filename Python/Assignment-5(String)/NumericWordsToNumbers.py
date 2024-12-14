'''Write a program to  convert numeric words to numbers'''
def words_to_numbers(s):
    num_words = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, 
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    return [num_words[word.lower()] for word in s.split() if word.lower() in num_words]

s = input("Enter numeric words: ")
print(f"Converted numbers: {words_to_numbers(s)}\n")
