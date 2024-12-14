'''7. Write a Python program to map two lists into a dictionary.
keys = ["a", "b", "c"]
values = [1, 2, 3]'''

# Map lists to dictionary
mapped_dict = dict(zip(keys, values))
print("Mapped dictionary:", mapped_dict)