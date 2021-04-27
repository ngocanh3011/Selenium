from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "D:\KTPM\ChromeDriver Set-up\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
myAccBtn = driver.find_element_by_id("menu-item-50")
myAccBtn.click()

enterEmail = driver.find_element_by_id("reg_email")
enterEmail.send_keys("tranngocanh45@gmail.com")

enterEmail = driver.find_element_by_id("reg_password")
enterEmail.send_keys("ngocanhtran123@")

registerBtn = driver.find_element_by_name("register")
print(registerBtn.text)
registerBtn.click()

# driver.close()