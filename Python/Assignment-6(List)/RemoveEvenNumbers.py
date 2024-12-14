# 18. Print list after removing EVEN numbers.
my_list = [1, 2, 3, 4, 5, 6]
my_list = [x for x in my_list if x % 2 != 0]  # Remove even numbers
print("List after removing even numbers:", my_list)