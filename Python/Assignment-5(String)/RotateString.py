# Write a program to perform string slicing in Python to rotate a string
def rotate_string(s, n):
    return s[n:] + s[:n]

s = input("Enter a string: ")
n = int(input("Enter number of rotations: "))
print(f"Rotated string: {rotate_string(s, n)}\n")
