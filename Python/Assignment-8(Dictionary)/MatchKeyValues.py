# 11. Write a Python program to match key values in two dictionaries.

dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}

# Iterate through dict1 and check if the value exists in dict2
for key, value in dict1.items():
    if key in dict2 and dict2[key] == value:
        print(f"{key}: {value} is present in both x and y")