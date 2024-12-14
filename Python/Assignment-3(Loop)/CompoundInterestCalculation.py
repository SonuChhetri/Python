# 15. When interest compounds q times per year at an annual rate of r % for n years, the principle p 
# compounds to an amount a as per the following formula. Write a program to read 10 sets of p, r, 
# n & q and calculate the corresponding as. 
# 𝑎=𝑝(1+𝑟𝑞)𝑛𝑝

for i in range(1, 11):
    print(f"Set {i}:")
    p = float(input("Enter the principal amount (P): "))
    r = float(input("Enter the annual interest rate (r) in %: ")) / 100
    n = int(input("Enter the number of years (n): "))
    q = int(input("Enter the number of times interest is compounded per year (q): "))

    a = p * (1 + r / q) ** (q * n)
    print(f"The compounded amount (A) is: Rs. {a:.2f}")
    print()