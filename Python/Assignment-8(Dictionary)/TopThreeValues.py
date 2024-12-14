#10. Write a Python program to get the top three items in terms of cost in a shop.

d1 = {'dress': 23, 'pant': 45, 'shoe': 12, 'bungle': 55, 'book': 8}

# Sort the dictionary by value in descending order and get the top 3 items
top_three_items = sorted(d1.items(), key=lambda item: item[1], reverse=True)[:3]

# Print the top 3 items
for item, cost in top_three_items:
    print(f"{item} {cost}")