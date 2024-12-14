# 4. Write a program to print all the ASCII values and their equivalent characters using a while loop. 

value = 0
while value <= 255:
    print(f"ASCII value {value}: {chr(value)}")
    value += 1
print()