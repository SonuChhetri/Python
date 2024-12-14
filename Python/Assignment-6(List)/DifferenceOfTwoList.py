#Program to find the differences of two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
diff = list(set(list1) - set(list2))  # Difference of lists
print("Difference between lists:", diff)