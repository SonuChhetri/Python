''' Write a program to swap commas and dots in a String '''
def swap_commas_dots(s):
    return s.replace(',', 'temp').replace('.', ',').replace('temp', '.')

s = input("Enter a string: ")
print(f"String after swap: {swap_commas_dots(s)}\n")
