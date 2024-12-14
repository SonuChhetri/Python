# Function to create and print squares of numbers from 1 to 30
def print_squares():
    squares = [x**2 for x in range(1, 31)]
    print("Squares from 1 to 30:", squares)


print_squares()