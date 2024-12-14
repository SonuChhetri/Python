''' Write a program to program to check if a string contains any special character '''
def contains_special_char(s):
    import re
    return bool(re.search(r'[^a-zA-Z0-9]', s))

s = input("Enter a string: ")
print(f"Contains special characters: {contains_special_char(s)}\n")
