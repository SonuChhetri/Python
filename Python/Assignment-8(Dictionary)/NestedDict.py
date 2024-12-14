''' 14. Write a Python program to convert more than one list to a nested dictionary.
strings1 = ['S001', 'S002', 'S003', 'S004']
strings2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
marks = [85, 98, 89, 92]'''

# Convert the lists to a nested dictionary
nested_dict = [{strings1[i]: {strings2[i]: marks[i]}} for i in range(len(strings1))]

print("Nested dictionary:", nested_dict)