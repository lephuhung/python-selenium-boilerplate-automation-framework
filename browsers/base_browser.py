""""""
from selenium.webdriver.remote.webdriver import WebDriver


class BaseBrowser:
    """"""

    def __init__(self, driver: WebDriver):
        self.driver = driver
