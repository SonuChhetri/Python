'''Write a program Python to calculate l.c.m using while loop.'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
greater = max(num1, num2)
while True:
    if greater % num1 == 0 and greater % num2 == 0:
        print(f"L.C.M is {greater}\n")
        break
    greater += 1