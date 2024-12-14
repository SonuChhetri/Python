'''Write a program in Python to calculate sum of Fibonacci series.'''
def fibonacci_sum(n):
    a, b, total = 0, 1, 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total
n = int(input("Enter the number of terms: "))
print(f"Sum of first {n} Fibonacci numbers is {fibonacci_sum(n)}\n")