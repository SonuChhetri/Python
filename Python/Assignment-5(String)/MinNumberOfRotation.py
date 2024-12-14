# Write a program to find minimum number of rotations to obtain actual string
def min_rotations_to_original(s):
    n = len(s)
    concatenated = s + s
    for i in range(1, n + 1):
        if concatenated[i:i + n] == s:
            return i
    return -1

'Example Usage'
string = input("Enter a string: ")
rotations = min_rotations_to_original(string)
if rotations != -1:
    print(f"Minimum number of rotations to obtain the original string: {rotations}")
else:
    print("Rotation not possible.")
