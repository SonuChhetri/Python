'''Write a program to find the range of a set of numbers. Range is the difference between the
smallest and biggest number in the list.'''
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
range_of_numbers = max(numbers) - min(numbers)
print(f"Range: {range_of_numbers}\n")