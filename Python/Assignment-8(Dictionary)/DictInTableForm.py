# 10. Write a Python program to print a dictionary in table format.
my_dict = {'Name': 'John', 'Age': 30, 'Country': 'USA'}

# Print the dictionary in table format
print(f"{'Key':<10} {'Value':<10}")
print("-" * 20)
for key, value in my_dict.items():
    print(f"{key:<10} {value:<10}")