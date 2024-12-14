# 5. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = 5
squares_dict = {x: x**2 for x in range(1, n + 1)}
print("Dictionary of squares:", squares_dict)
