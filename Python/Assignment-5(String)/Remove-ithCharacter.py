'''WAP to remove i^th character of a string. '''
def remove_ith_char(s, i):
    return s[:i] + s[i+1:]

s = input("Enter a string: ")
i = int(input("Enter the index to remove: "))
print(f"String after removal: {remove_ith_char(s, i)}\n")
