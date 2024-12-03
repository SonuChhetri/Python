#If the total selling price of 15 items and the total profit earned on them is input through the 
# keyboard, write a program to find the cost price of one item

# Input total selling price and total profit
selling_price = float(input("Enter the selling price of 15 items: "))
profit = float(input("Enter total profit: "))

# Calculate the total cost price of 15 items
cost_price =selling_price - profit

# Calculate the cost price of one item
per_item = cost_price / 15

print(f"The cost price of each item is: {per_item:.2f}")