'''Write a program in Python to calculate combinatoric C(n,r) using function.'''
from math import factorial

def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("Enter n: "))
r = int(input("Enter r: "))
print(f"C({n}, {r}) = {combination(n, r)}\n")
