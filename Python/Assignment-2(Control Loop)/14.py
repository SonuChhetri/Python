# Q14. A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, for 
# 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after 30 
# days your membership will be cancelled. Write a program to accept the number of days the 
# member is late to return the book and display the fine or the appropriate message.

days_late = int(input("Enter the number of days the book is late: "))

if days_late <= 5:
    fine = days_late * 0.5
elif days_late <= 10:
    fine = 5 * 0.5 + (days_late - 5) * 1
elif days_late <= 30:
    fine = 5 * 0.5 + 5 * 1 + (days_late - 10) * 5
else:
    print("Membership will be cancelled.")
    fine = None

if fine is not None:
    print(f"The fine is: {fine} rupees")