# Q4. Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a program 
# to convert this temperature into Centigrade degrees.

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Converting Fahrenheit to Celsius
celsius = (fahrenheit - 32) * 5 / 9

print(f"The temperature in Celsius is: {celsius}°C")