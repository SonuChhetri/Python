# 1 .If  cost  price  and  selling price  of  an  item  is input through  the  keyboard,  write  a  program  to determine whether the seller has made profit or incurred loss. Also determine how much profit 
# he made or loss he incurred.

cost_price = float(input("Enter Cost price of an item: "))
selling_price = float(input("Enter selling price of the item: "))
loss = cost_price - selling_price
profit = selling_price - cost_price

if cost_price > selling_price:
    print("Loss:", loss)
elif cost_price < selling_price:
    print("Profit:", profit)