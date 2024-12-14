# Q18. An Insurance company follows following rules to calculate premium. 
# • If a person’s health is excellent and the person is between 25 and 35 years of age and lives in 
# a  city  and  is  a  male  then  the  premium  is  Rs.  4  per  thousand  and  his  policy  amount  cannot exceed Rs. 2 lakhs. 
# • If a person satisfies all the above conditions except that the sex is female then the premium is 
# Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakh. 
# • If a person’s health is poor and the person is between 25 and 35 years of age and lives in a 
# village and is a male then the premium is Rs. 6 per thousand and his policy cannot exceed Rs. 
# 10,000. 
# • In all other cases the person is not insured. 
# Write  a  program  to  output  whether  the  person  should  be  insured  or  not,  his/her  premium  rate  and maximum amount for which he/she can be insured.

# Input details
health = input("Enter health (excellent/poor): ").strip().lower()
age = int(input("Enter age: "))
residence = input("Enter residence (city/village): ").strip().lower()
sex = input("Enter sex (male/female): ").strip().lower()

# Initialize default values
premium_rate = None
max_amount = None

# Check conditions for insurance
if health == "excellent" and 25 <= age <= 35 and residence == "city":
    if sex == "male":
        premium_rate = 4  # Rs. 4 per thousand
        max_amount = 200000  # Max 2 lakhs
    elif sex == "female":
        premium_rate = 3  # Rs. 3 per thousand
        max_amount = 100000  # Max 1 lakh
elif health == "poor" and 25 <= age <= 35 and residence == "village" and sex == "male":
    premium_rate = 6  # Rs. 6 per thousand
    max_amount = 10000  # Max 10,000
else:
    print("The person is not insured.")
    
# Display the result
if premium_rate and max_amount:
    print(f"The person can be insured.")
    print(f"Premium rate: Rs. {premium_rate} per thousand")
    print(f"Maximum policy amount: Rs. {max_amount}")
