'''3. Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20, 4: 6}
dic2 = {3: 30, 4: 40, 5: 2}
dic3 = {5: 50, 6: 60}'''

# Concatenate dictionaries with addition for common keys
result = dic1.copy()  # Make a copy of dic1 to avoid modifying it
for d in [dic2, dic3]:
    for key, value in d.items():
        if key in result:
            result[key] += value  # Add values if the key exists in the result
        else:
            result[key] = value
print("Concatenated dictionary with added values for common keys:", result)