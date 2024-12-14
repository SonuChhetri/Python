'''Write a program to capitalize the first and last character of each word in a string '''
def capitalize_first_last(s):
    words = s.split()
    return ' '.join([w[0].upper() + w[1:-1] + w[-1].upper() if len(w) > 1 else w.upper() for w in words])

s = input("Enter a string: ")
print(f"Transformed string: {capitalize_first_last(s)}\n")