# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import upload

# create webdriver object
driver = webdriver.Chrome()

def screenshot(leaving,destination,date):
    """
    :param leaving: IATA code of departure airport
    :param destination: IATA code of arrival airport
    :param date: format: year-month-day (XXXX-XX-XX)
    :return: generates image of flight ticket
    """
    url = f"https://www.kayak.com/flights/{leaving}-{destination}/{date}?sort=bestflight_a&fs=airlines=~AA"
    print(url)

    driver.get(url)
    driver.fullscreen_window()

    # get element
    element = driver.find_element(By.CSS_SELECTOR, ".best-flights-list")

    # Specify the path
    path = r'images'

    dir_list = os.listdir(path)
    num = len(dir_list)
    element.screenshot(rf'images\image{num}.png')
    return upload.upload(rf'images\image{num}.png')

# Example:


#screenshot('JFK','IAH','2023-03-24')