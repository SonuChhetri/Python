#Remove all occurrences a given element from the list
my_list = [1, 2, 3, 4, 3, 5]
my_list = [item for item in my_list if item != 3]  # Remove all occurrences of 3
print("After removing all occurrences of 3:", my_list)