import requests

# Define the URL for the Universities API request
url = "http://universities.hipolabs.com/search?country=Israel"

# Send a GET request to the API
response = requests.get(url)

# Raise an exception if the request was unsuccessful
response.raise_for_status()

# Parse the JSON response
universities = response.json()

# Assert that there are at least 5 universities
assert len(universities) >= 5, f"Expected at least 5 universities, found {len(universities)}"

print(f"Test passed! There are {len(universities)} universities in Israel.")
