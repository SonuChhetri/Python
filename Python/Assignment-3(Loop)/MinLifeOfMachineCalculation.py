# 14. A  machine  is  purchased  which  will  produce  earning  of  Rs.  1000  per  year  while  it  lasts. The machine costs Rs. 6000 and will have a salvage of Rs. 2000 when it is condemned. If 12 percent 
# per  annum  can  be  earned  on  alternate  investments  what  would  be  the  minimum  life  of  the 
# machine to make it a more attractive investment compared to alternative investment?

def calculate_npv(life, cash_inflow, discount_rate, salvage_value, initial_cost):
    # Calculate the NPV
    npv = 0
    for t in range(1, life + 1):
        npv += cash_inflow / (1 + discount_rate) ** t
    # Add salvage value contribution
    npv += salvage_value / (1 + discount_rate) ** life
    # Subtract the initial cost
    npv -= initial_cost
    return npv

# Machine parameters
cash_inflow = 1000  # Rs. per year
discount_rate = 0.12  # 12% per annum
salvage_value = 2000  # Rs.
initial_cost = 6000  # Rs.

# Using a for loop to find the minimum life
for life in range(1, 100):  # Assume a maximum limit for life
    npv = calculate_npv(life, cash_inflow, discount_rate, salvage_value, initial_cost)
    if npv > 0:
        print(f"The minimum life of the machine to make it a more attractive investment is {life} years.")
        break
