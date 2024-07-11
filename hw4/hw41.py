import requests

# Define the URL for the GitHub API request
url = "https://api.github.com/users/avielb/repos"

# Send a GET request to the API
response = requests.get(url)

# Raise an exception if the request was unsuccessful
response.raise_for_status()

# Parse the JSON response
repos = response.json()

# Initialize a counter for the html_url occurrences
html_url_count = 0

# Iterate over the repositories
for repo in repos:
    if "html_url" in repo:
        html_url_count += 1
    # Stop counting once we reach 5
    if html_url_count >= 5:
        break

# Assert that there are at least 5 repositories
assert html_url_count >= 5, f"Expected at least 5 repositories, found {html_url_count}"

print("Test passed! There are at least 5 repositories.")
