# Test


# Imports
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

FILEPATH =  os.path.dirname(os.path.abspath(__file__))
DRIVER_PATH = 'C:/Users/NickC/Documents/Programming/screen-scraping/chomedriver.exe'
CHROME_DRIVER = f'{FILEPATH}\chromedriver.exe'
FIREFOX_DRIVER = f'{FILEPATH}\geckodriver.exe'

print(DRIVER_PATH)


def chrome_test():
    print('Hello World')
    
    
    print(os.path.exists(CHROME_DRIVER))
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
    driver.get('https://google.com')
    print(driver.title)
    driver.quit()


def firefox_test():
    driver = webdriver.Firefox()
    driver.get('https://google.com')
    print(driver.title)
    driver.quit()
    


if __name__ == '__main__':
    # chrome_test()
    firefox_test()
