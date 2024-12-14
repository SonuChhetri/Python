'''Write a program to add first seven terms of the following series using a for loop: 1
1!+2/2!+3/3!+⋯ +n/n!'''
from math import factorial
series_sum = sum(i / factorial(i) for i in range(1, 8))
print(f"Sum of the series: {series_sum}\n")
