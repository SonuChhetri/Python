'''Write a program to enter the numbers till the user wants and at the end it should display the count
of positive, negative and zeros entered.'''
positive = negative = zeros = 0
while True:
    num = int(input("Enter a number (or -999 to stop): "))
    if num == -999:
        break
    elif num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zeros += 1