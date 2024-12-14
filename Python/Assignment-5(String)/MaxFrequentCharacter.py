'''Write a program to maximum frequency character in String '''
def max_frequency_char(s):
    from collections import Counter
    count = Counter(s)
    return max(count, key=count.get)

s = input("Enter a string: ")
print(f"Maximum frequency character: {max_frequency_char(s)}\n")
