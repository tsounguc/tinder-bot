import os
import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Login information
email = os.environ.get("email", "Couldn't find email address")
user_name = os.environ.get("username", "Couldn't find username")
password = os.environ.get("password", "couldn't find password")

# Instantiate options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Instantiate driver
driver = webdriver.Chrome(options=options)

# Open tinder
driver.get("https://tinder.com/")
driver.maximize_window()

# log in
time.sleep(6)
login_button = driver.find_element(By.XPATH,
                                   '//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()

time.sleep(4)
facebook_button = driver.find_element(By.XPATH,
                                      '//*[@id="s2018968691"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div')
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

time.sleep(6)
driver.switch_to.window(base_window)

# Cookies and permissions
time.sleep(5)
allow_location = driver.find_element(By.XPATH,
                                     '//*[@id="s2018968691"]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]')
allow_location.click()

time.sleep(5)
disable_notification = driver.find_element(By.XPATH,
                                           '//*[@id="s2018968691"]/main/div[1]/div/div/div[3]/button[2]/div[2]/div[2]')
disable_notification.click()

time.sleep(5)
accept_cookies = driver.find_element(By.XPATH, '//*[@id="s-547617529"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_cookies.click()

# swipe
time.sleep(4)
swipe_left = driver.find_element(By.XPATH,
                                 '//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div[1]/div['
                                 '1]/div/div[3]/div/div[2]/button')
swipe_right = driver.find_element(By.XPATH,
                                  '//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div[1]/div['
                                  '1]/div/div[3]/div/div[4]/button')
for _ in range(100):
    try:
        time.sleep(5)
        swipe_left = driver.find_element(By.XPATH,
                                         '//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div[1]/div['
                                         '1]/div/div[3]/div/div[2]/button')
        swipe_right = driver.find_element(By.XPATH,
                                          '//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div[1]/div['
                                          '1]/div/div[3]/div/div[4]/button')
        swipe_right.click()
    except selenium.common.exceptions.NoSuchElementException:
        time.sleep(5)
        swipe_right = driver.find_element(By.XPATH,
                                          '//*[@id="s-547617529"]/div/div[1]/div/main/div[1]/div/div/div[1]/div['
                                          '1]/div/div[3]/div/div[4]/button')

        swipe_right.click()
