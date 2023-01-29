# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import upload

# create webdriver object
driver = webdriver.Chrome()

def screenshot(event):

    url = 'https://www.ticketmaster.com/search?q=' + event.replace(' ', '%20')
    print(url)

    driver.get(url)
    driver.fullscreen_window()

    # get element
    element = driver.find_element(By.CSS_SELECTOR, ".ddKzwG")

    src = element.get_attribute("src")
    driver.quit()

    return(src)




