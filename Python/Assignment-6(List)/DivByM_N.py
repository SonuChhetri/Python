#Program to print all numbers which are divisible by M and N in the List.
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
M, N = 2, 3
result = [x for x in my_list if x % M == 0 and x % N == 0]
print("Numbers divisible by both M and N:", result)
