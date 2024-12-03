# A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is  input  through  the  keyboard  in  hundreds, find the  total number  of  currency  notes  of  each denomination the cashier will have to give to the withdrawer. 

 
amount = float(input("Enter the amount to withdraw in hundreds: "))# Get the amount in hundreds from the user
 # Calculate the number of 100 denomination notes
hundred_notes=amount // 100
     # Calculate the number of 50 denomination notes from the remaining amount
remaining_amount =amount % 100
fifty_notes= remaining_amount // 50
remaining_amount = remaining_amount % 50
    # Calculate the number of 10 denomination notes from the remaining amount
ten_notes= remaining_amount // 10
remaining_amount = remaining_amount % 10
 # Print the result (note that the remaining amount should be zero)
print(f"100 denomination notes: {int(hundred_notes)}")
print(f"50 denomination notes: {int(fifty_notes)}")
print(f"10 denomination notes: {int(ten_notes)}")