from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib


    
def init_browser():
    QUANTITY = 6
    URL = f'https://www.stubhub.com/yoasobi-new-york-city-tickets-8-6-2024/event/153463870/?quantity={QUANTITY}'

    # Path to the ChromeDriver executable
    DRIVER_PATH = '/opt/homebrew/bin/chromedriver'

    # Create Chrome options
    options = webdriver.ChromeOptions()

    # Set ChromeDriver path as service
    service = webdriver.ChromeService(executable_path=DRIVER_PATH)

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to a website
    driver.get(URL)

    # Print the title of the website
    print("Title of the page is:", driver.title)

    time.sleep(5)

    # Wait for the container element to be present
    container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'listings-container'))
    )
    return container.text

def get_prices(data):
    sections = data.split('\n')
    sections.sort()
    # print(sections)
    prices = []
    for data in sections:
        try: 
            price = int(data.replace('$', ''))
            # print(price)
            prices.append(price)
            
        except:
            continue
    # print(prices)
    return prices





