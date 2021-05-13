from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "D:\KTPM\ChromeDriver Set-up\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
myAccBtn = driver.find_element_by_id("menu-item-50")
myAccBtn.click()

enterEmail = driver.find_element_by_id("reg_email")
enterEmail.send_keys("nanh@gmail.com")
time.sleep(2)

enterPass = driver.find_element_by_id("reg_password")
enterPass.send_keys("ngocanhtran123@")
time.sleep(2)

registerBtn = driver.find_element_by_name("register")
registerBtn.click()
time.sleep(2)

driver.close()