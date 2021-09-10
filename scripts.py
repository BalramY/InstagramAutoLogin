from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import random
import unittest
import time



#Set your username and password in below variables.
username = ""
password = ""
# driver = webdriver.Chrome("C://python37/driver/chromedriver.exe")
driver = webdriver.Chrome("C:/Users/huney/Downloads/chromedriver_win32/chromedriver.exe")


driver.get("http://www.instagram.com")
time.sleep(4)

# Find the username box
usern = driver.find_element_by_name("username")
# sends the entered username
usern.send_keys(username)

# Find the password box
passw = driver.find_element_by_name("password")
# sends the entered password
passw.send_keys(password)
time.sleep(2)

# finds the login button
log_c1 = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
log_c1.click()    #clicks the login button
time.sleep(4)

btn_c2 = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
btn_c2.click()
time.sleep(2)

btn_c3 = driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]")
btn_c3.click()

# Generating random value
n1 = random.randint(1, 10) * random.randint(11, 20)
driver.get_screenshot_as_file("Myphoto"+ str(n1) +".png")

driver.quit()

# driver.close()


