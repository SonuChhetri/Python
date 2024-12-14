''' Write a program to least Frequent Character in String '''
def least_frequent_char(s):
    from collections import Counter
    count = Counter(s)
    return min(count, key=count.get)

s = input("Enter a string: ")
print(f"Least frequent character: {least_frequent_char(s)}\n")
