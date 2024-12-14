''' Write a program to string slicing in Python to check if a string can become empty by 
recursive deletion '''
def can_become_empty(s, sub):
    while sub in s:
        s = s.replace(sub, '')
    return not s

s = input("Enter a string: ")
sub = input("Enter substring: ")
print(f"Can become empty: {can_become_empty(s, sub)}\n")
