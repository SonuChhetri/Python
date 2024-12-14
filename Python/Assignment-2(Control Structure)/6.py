# Q6. If  the  ages  of  Ram,  Shyam  and  Ajay  are  input  through  the  keyboard,  write  a  program  to determine the youngest of the three.

age_ram = int(input("Enter Ram's age: "))
age_shyam = int(input("Enter Shyam's age: "))
age_ajay = int(input("Enter Ajay's age: "))

if age_ram < age_shyam and age_ram < age_ajay:
    youngest = age_ram
    print("Ram is the youngest.")
elif age_shyam < age_ram and age_shyam < age_ajay:
    youngest = age_shyam
    print("Shyam is the youngest.")
else:
    youngest = age_ajay
    print("Ajay is the youngest.")

print(f"The youngest age is: {youngest}")