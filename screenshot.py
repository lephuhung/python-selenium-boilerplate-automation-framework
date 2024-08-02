from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import argparse
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os
def main(html_file_path):
    chromedriver_path = './chromedriver.exe'
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Verify that the file exists
    if not os.path.isfile(html_file_path):
        print(f"The file {html_file_path} does not exist.")
        driver.quit()
        exit(1)

    file_url = "file:///" + os.path.abspath(html_file_path).replace('\\', '/')
    print(f"File URL: {file_url}")
    driver.get(file_url)
    time.sleep(5)

    try:
        element = driver.find_element(By.XPATH, "//div[@class='main-page']")
        # Use JavaScript to get the full width and height of the webpage
        width = driver.execute_script("return Math.max( document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth );")
        height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")

        # Set the window size to match the entire webpage
        driver.set_window_size(width, height)
        
        # Define the output image path
        output_image_path = os.path.join(os.path.dirname(html_file_path), 'invoice.png')
        element.screenshot(output_image_path)
        print(f"Screenshot saved to {output_image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Take a screenshot of an HTML element.")
    parser.add_argument("html_file_path", type=str, help="Path to the HTML file.")
    args = parser.parse_args()
    main(args.html_file_path)