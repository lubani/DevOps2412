import requests

# Delete item with ID 1
delete_response = requests.delete('http://127.0.0.1:5000/items/1')

if delete_response.status_code == 200:
    print("Success:", delete_response.json())
else:
    print("Error:", delete_response.status_code, delete_response.json())

# Verify the item has been deleted
get_response = requests.get('http://127.0.0.1:5000/items')
actual = len(get_response.json())
print(f'actual == {actual}')
expected = 2
assert actual == expected
