# Example of a Python dictionary

import pandas as pd

# Creating a dictionary of a    person
person = {
    "name": ["Alice",None,None],
    "age": [30,None,None],
    "city": ["New York",None,None],
    "is_employed": [True,None,None],
    "skills": ["Python", "Data Analysis", "Machine Learning"]
}

person = pd.DataFrame(person)
print(person)

# Accessing values
print(person["name"])         # Output: Alice
print(person["skills"][0])    # Output: Data Analysis

# Adding a new key-value pair
person["email"] = "alice@example.com"

# Updating a value
person["age"] = 31

# Deleting a key-value pair
del person["city"]

# Looping through the dictionary
print("This is the output:")
for key, value in person.items():
    print(f"{key}, {value}")
