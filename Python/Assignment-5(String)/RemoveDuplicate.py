''' Write a program to remove all duplicates from a given string in Python, keeping the 
first character only '''
def remove_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

s = input("Enter a string: ")
print(f"String after removing duplicates: {remove_duplicates(s)}\n")