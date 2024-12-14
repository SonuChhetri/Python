'''Write a program in Python to print sum of all +ve numbers and all -ve numbers'''
positive_sum = negative_sum = 0
while True:
    num = int(input("Enter a number (-999 to stop): "))
    if num == -999:
        break
    if num > 0:
        positive_sum += num
    elif num < 0:
        negative_sum += num
print(f"Sum of positive numbers: {positive_sum}, Sum of negative numbers: {negative_sum}\n")
