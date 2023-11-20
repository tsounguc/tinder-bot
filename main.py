import os
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Login information
email = os.environ.get("email","Couldn't find email address")
user_name = os.environ.get("username", "Couldn't find username")
password = os.environ.get("password", "couldn't find password")


#Instantiate options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Instantiate driver
driver = webdriver.Chrome(options=options)

# Open tinder
driver.get("https://tinder.com/")
driver.maximize_window()

# log in
time.sleep(10)
login_button = driver.find_element(By.XPATH, '//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()

time.sleep(4)
facebook_button = driver.find_element(By.XPATH, '//*[@id="s2018968691"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div')
facebook_button.click()

time.sleep(6)
base_window = driver.window_handles[0]
facebook_login_window = driver.window_handles[1]
driver.switch_to.window(facebook_login_window)

email_input = driver.find_element(By.ID, 'email')
email_input.send_keys(email)

password_input = driver.find_element(By.ID, 'pass')
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)





