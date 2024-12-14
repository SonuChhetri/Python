# 12. Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.


dict_range = {
    'x': list(range(11, 20)),
    'y': list(range(21, 30)),
    'z': list(range(31, 40))
}

# Accessing the fifth value of each list
for key, values in dict_range.items():
    print(f"The fifth value in list for {key} is {values[4]}")