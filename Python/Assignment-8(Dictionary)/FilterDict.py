# 13. Write a Python program to filter a dictionary based on values.
original_dict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

# Filter out people with marks greater than 170
filtered_dict = {key: value for key, value in original_dict.items() if value > 170}

print("Marks greater than 170:", filtered_dict)
