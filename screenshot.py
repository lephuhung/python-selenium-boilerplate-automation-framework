from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os
# Set the path to the ChromeDriver executable
chromedriver_path = './chromedriver'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chromedriver_path)

parser = argparse.ArgumentParser(description='Load a local HTML file and take a screenshot of an element with class "main".')
parser.add_argument('html_file', help='The path to the local HTML file')
args = parser.parse_args()

# Verify that the file exists
if not os.path.isfile(args.html_file):
    print(f"The file {args.html_file} does not exist.")
    exit(1)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome, without opening a browser window

# Set up the WebDriver (adjust the path if necessary)
webdriver_service = Service('path/to/chromedriver')  # Replace with your path to ChromeDriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Load the local HTML file
driver.get(f"file:///{os.path.abspath(args.html_file)}")

# Allow some time for the page to load
time.sleep(2)

# Find the element with class 'main'
try:
    element = driver.find_element(By.CLASS_NAME, 'main')
    # Take a screenshot of the element
    element.screenshot('element_screenshot.png')
    print("Screenshot saved as element_screenshot.png")
except:
    print("Element with class 'main' not found.")

# Close the browser
driver.quit()