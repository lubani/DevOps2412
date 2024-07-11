import requests
import random

# List of sample names to choose from
names_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]

# Generate 3 random names
random_names = random.sample(names_list, 3)


# Function to check age using Agify API
def check_age(name):
    url = f"https://api.agify.io/?name={name}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    age = data.get("age", None)
    assert age is not None, f"Age for {name} is None"
    assert 0 <= age <= 120, f"Age for {name} is out of range: {age}"
    print(f"Name: {name}, Age: {age} - Valid age")


# Check the age for each random name
for name in random_names:
    check_age(name)

print("All tests passed!")
