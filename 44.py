from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Create an instance of ChromeOptions
options = webdriver.ChromeOptions()

# Get the path to the ChromeDriver executable using WebDriver Manager
service = Service(ChromeDriverManager().install())

# Initialize the WebDriver with the service and options
dr = webdriver.Chrome(service=service, options=options)

# Open the HTML file
dr.get("file:///C:/Users/libby/PycharmProjects/tip_calc/index.html")

# Interact with the web page
billamt = dr.find_element(by="id", value="billamt")
billamt.send_keys("100")
dr.find_element(by="xpath", value="//*[@id='serviceQual']/option[2]").click()
dr.find_element(by="xpath", value="//*[@id='musicQual']/option[2]").click()
dr.find_element(by="id", value="peopleamt").send_keys("5")
dr.find_element(by="id", value="calculate").click()

# Check the result
actual = dr.find_element(by="id", value="tip").text
expected = "8.00"
assert expected == actual

# Keep the browser open for a while
sleep(1000)

# Close the browser
dr.quit()
