#Program to input, append and print the list elements.
my_list = []
n = int(input("How many elements to add? "))
for _ in range(n):
    element = input("Enter element: ")
    my_list.append(element)
print("Final list:", my_list)