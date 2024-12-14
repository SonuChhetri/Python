# 5. Write a program to print out all Armstrong numbers between 1 and 500. If sum of cubes of each 
# digit of the number is equal to the number itself, then the number is called an Armstrong number. 
# For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )

# Solution
for num in range(1, 501):
    digits = [int(d) for d in str(num)]
    if sum(d ** 3 for d in digits) == num:
        print(num)