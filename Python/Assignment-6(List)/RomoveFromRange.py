#Program to remove all elements in a range from the List
my_list = [10, 20, 30, 40, 50]
my_list = [item for item in my_list if item < 30 or item > 40]  # Remove elements between 30 and 40
print("After removing elements between 30 and 40:", my_list)