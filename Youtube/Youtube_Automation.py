from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *
import time

root = Tk()

channel = Entry(root)
PATH = 'C:\\Program Files (x86)\\chromedriver.exe'	
driver = webdriver.Chrome(PATH)

channel.get()
driver.get("https://www.youtube.com/c/" + channel + "/videos")

video = driver.find_element_by_xpath('//*[@id="video-title"]')
video.click()


driver.implicitly_wait(2)
skip_ad = driver.find_element_by_xpath('//*[@id="ad-text:a"]')
skip_ad.click()
