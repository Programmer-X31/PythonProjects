from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time
import sys

PATH = "C:\\Program Files (x86)\\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://github.com/login")

# Signing In


def signIn():
    # signIn_button = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
    # signIn_button.click()

    signIn_username = driver.find_element_by_xpath('//*[@id="login_field"]')
    signIn_username.click()
    signIn_username.send_keys("Programmer-X31")

    signIn_password = driver.find_element_by_xpath('//*[@id="password"]')
    signIn_password.click()
    signIn_password.send_keys("Baahubali#31")

    signIn_loginButton = driver.find_element_by_xpath(
        '//*[@id="login"]/form/div[4]/input[12]'
    )
    signIn_loginButton.click()

# To click for creating a new repo
def createRepository():
    driver.get("https://github.com/new")


    # To create a Repository without details
    repository_name = driver.find_element_by_xpath('//*[@id="repository_name"]')
    repository_name.send_keys(sys.argv[1])

    driver.implicitly_wait(2)
    
    driver.find_element_by_class_name('btn btn-primary first-in-line').click() # CREATE The Repository

# Signing Out
def signOut():
    signOut_dropdown = driver.find_element_by_xpath(
        "/html/body/div[1]/header/div[7]/details/summary/span[2]"
    )
    signOut_dropdown.click()

    signOut_button = driver.find_element_by_xpath(
        "/html/body/div[1]/header/div[7]/details/details-menu/form/button"
    )
    signOut_button.click()
    sys.exit()


signIn()
createRepository()
signOut()
