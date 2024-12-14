# 8. Write a Python program to get the maximum and minimum values of a dictionary.

my_dict = {"a": 10, "b": 20, "c": 5}
max_key = max(my_dict, key=my_dict.get)
min_key = min(my_dict, key=my_dict.get)
print(f"Max value is {my_dict[max_key]} for key '{max_key}'")
print(f"Min value is {my_dict[min_key]} for key '{min_key}'")