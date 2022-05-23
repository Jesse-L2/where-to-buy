"""Docstring here

Before use, you must first install and configure the appropriate Selenium driver. See
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
"""
import os
import scraping.constants as constants
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# TODO: rotate proxies to avoid getting IP banned

# webdriver.Chrome methods + user defined methods
class Price_Bot():
    def __init__(self, close=False):
        # Using webdriver manager
        self.driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.close = close
        super(Price_Bot, self).__init__()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def nav_to_home_page(self, website_url):
        print(f'Getting {website_url}')
        return self.driver.get(website_url)

    # Works for most websites assuming they named the type of the button to be submit for a search
    def click_search(self):
        search_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_button.click()

    def search_input(self, item_to_search):
        search_bar = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        self.driver.implicitly_wait(5)
        search_bar.click()
        search_bar.send_keys(item_to_search)
        click_to_search = self.driver.find_element(By.ID, 'nav-search-submit-button')
        click_to_search.click()

    def get_price(self):
        self.driver.implicitly_wait(5)
        item_names = self.driver.find_elements(By.CLASS_NAME, 'a-size-medium a-color-base a-text-normal')
        for item in item_names:
            print(item.text)
        print(f"Found the following items: {item_names}")
        price = self.driver.find_element(By.CLASS_NAME, 'a-price-whole')
        print(price)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close Chrome browser when done
        if self.close:
            print('Exiting')
            self.quit()


def main():
    # TODO: implement as context manager like:
    # with Price_Bot() as bot:
    #     bot.nav_to_home_page('https://www.amazon.com')
    price_checker = Price_Bot()
    price_checker.nav_to_home_page('https://www.amazon.com')
    price_checker.search_input("55 inch tv")


if __name__ == "__main__":
    main()
