from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the website
driver.get("https://hub.docker.com")

# Wait for the title to be present and fetch it
try:
    WebDriverWait(driver, 10).until(EC.title_is("Docker Hub Container Image Library | App Containerization"))
    title = driver.title
except Exception as e:
    title = ""

# Assert that the title is “Docker Hub Container Image Library | App Containerization”
expected_title = "Docker Hub Container Image Library | App Containerization"
assert title == expected_title, f"Expected title to be '{expected_title}' but got '{title}'"

print(f"Test passed! The title is '{title}'.")

# Close the WebDriver
driver.quit()
