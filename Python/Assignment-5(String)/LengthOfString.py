'''WAP to calculate the length of a string, avoid space. '''
def length_no_spaces(s):
    return len(s.replace(' ', ''))

s = input("Enter a string: ")
print(f"Length excluding spaces: {length_no_spaces(s)}\n")
