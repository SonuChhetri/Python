#Program to Create two lists with EVEN numbers and ODD numbers from a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
even_list = [x for x in my_list if x % 2 == 0]
odd_list = [x for x in my_list if x % 2 != 0]
print("Even list:", even_list)
print("Odd list:", odd_list)
