'''Write a program to fill the entire screen with a smiling face. The smiling face has an ASCII value
1'''
import os
os.system('cls' if os.name == 'nt' else 'clear')
print(chr(1) * 1000)