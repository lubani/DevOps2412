from datetime import datetime
import requests
print(datetime.now())
urls = {"Github": "https://github.com",
        "Google": "https://www.google.com",
        "Youtube": "https://www.youtube.com"}
for name, url in urls.items():
    response = requests.get("https://github.com")
    if response.status_code == 200:
        print(f"{name} is up")
