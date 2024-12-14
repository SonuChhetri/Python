# 1. Write a program to calculate overtime pay of 10 employees. Overtime is paid at the rate of Rs. 
# 12.00 per hour for every hour worked above 40 hours. Assume that employees do not work for 
# fractional part of an hour.
hours_worked = int(input("Enter number of hours worked by an employee: "))
for employee in range(1, 11):
    
    if hours_worked > 40:
        extra_hours_worked = hours_worked - 40
        overtime_pay = extra_hours_worked * 12
        print(f"Employee {employee} earns Rs.{overtime_pay} as overtime pay")
else:
        print(f"Employee has no overtime pay")