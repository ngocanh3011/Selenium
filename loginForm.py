from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "D:\KTPM\ChromeDriver Set-up\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

fomrAuth = driver.find_element_by_link_text("Form Authentication")
fomrAuth.click()
time.sleep(1)

enterName = driver.find_element_by_id("username")
enterName.send_keys("tomsmith")
time.sleep(1)

enterPass = driver.find_element_by_id("password")
enterPass.send_keys("SuperSecretPassword!")
time.sleep(1)

loginBtn = driver.find_element_by_css_selector(".radius i")
loginBtn.click()
time.sleep(2)

get_title = driver.title
print(get_title)

driver.close()