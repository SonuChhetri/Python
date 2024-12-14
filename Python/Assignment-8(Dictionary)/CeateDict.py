'''locales\ 9. Write a Python program to create a dictionary from a string.
sample_string = 'MCA1stsem''''

# Create dictionary with letter count
char_count = {}
for index, char in enumerate(sample_string):
    char_count[char] = index + 1  # Use index + 1 as the count (for the position of character in string)
print("Character count dictionary:", char_count)