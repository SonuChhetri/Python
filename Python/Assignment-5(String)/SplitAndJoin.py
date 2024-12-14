'''Write a program to split and join a string '''
def split_and_join(s):
    return '-'.join(s.split())

s = input("Enter a sentence: ")
print(f"Split and joined string: {split_and_join(s)}\n")
