# 2. Write a Python script to check whether a given key already exists in a dictionary.
my_dict = {1: 10, 2: 20, 3: 30}
key = 2
if key in my_dict:
    print(f"Key {key} exists in the dictionary.")
else:
    print(f"Key {key} does not exist in the dictionary.")