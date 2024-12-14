#Convert a string to integers list
string = "1, 2, 3, 4, 5"
int_list = [int(x) for x in string.split(", ")]  # Convert string to integers list
print("Converted list:", int_list)