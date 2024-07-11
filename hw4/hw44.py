from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the website
driver.get("https://www.ycombinator.com/")

# Get the title of the page
title = driver.title

# Assert that the title is "Y Combinator"
assert title == "Y Combinator", f"Expected title to be 'Y Combinator' but got '{title}'"

print("Test passed! The title is 'Y Combinator'.")

# Close the WebDriver
driver.quit()
