#The distance between two cities (in km.) is input through the keyboard. Write a program to 
# convert and print this distance in meters, feet, inches and centimeters.

distance_between_two_cities = float(input("Enter the distance between two cities(in km): "));

# 1 kilometer = 1000 metres
m = distance_between_two_cities * 1000;
print(f"Distance between two cities in metres: {m} m");

# 1 kilometer = 3280.84 feet
feet = distance_between_two_cities * 3280.84;
print(f"Distance between two cities in feet: {feet} feet");

# 1 kilometer = 39,370.1 inches
inches = distance_between_two_cities * 39370.1;
print(f"Distance between the two cities in inches: {inches} inches")

# 1 kilometer = 100,000 centimeters
cm = distance_between_two_cities * 100000;
print(f"Distance between two cities in centimetre: {cm} cm");