# 21. Create two lists with the first half and second half elements of a list.
my_list = [1, 2, 3, 4, 5, 6]
half = len(my_list) // 2
first_half = my_list[:half]
second_half = my_list[half:]
print("First half:", first_half)
print("Second half:", second_half)