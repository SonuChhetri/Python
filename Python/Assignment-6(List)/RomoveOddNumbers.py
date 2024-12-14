# 22. Print list after removing ODD numbers.
my_list = [1, 2, 3, 4, 5, 6]
my_list = [x for x in my_list if x % 2 == 0]  # Remove odd numbers
print("List after removing odd numbers:", my_list)