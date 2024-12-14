''' Write a program to generating random strings until a given string is generated '''
def generate_random_until_match(target):
    import random
    import string
    attempts = 0
    while True:
        attempts += 1
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=len(target)))
        print(f"Attempt {attempts}: {random_string}")
        if random_string == target:
            break
    print(f"Matched string: {random_string} in {attempts} attempts\n")

target = input("Enter target string: ")
generate_random_until_match(target)