# Q4. According to the Gregorian calendar, it was Monday on the date 01/01/1900. If any year is 
# input through the keyboard write a program to find out what is the day on 1 st January of this 
# year.

def find_day_on_jan1(year):
    base_year = 1900
    days_in_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Calculate the number of days between the base year and the input year
    days_passed = 0
    for y in range(base_year, year):
        # Leap year check: divisible by 4 but not 100, or divisible by 400
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            days_passed += 366
        else:
            days_passed += 365
    
    # Calculate the day index by modulo operation
    day_index = days_passed % 7
    return days_in_week[day_index]

year = int(input("Enter a year: "))
print(f"The day on 1st January {year} is: {find_day_on_jan1(year)}")