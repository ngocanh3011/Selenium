from selenium import webdriver
import time
chrome_driver_path = "D:\KTPM\ChromeDriver Set-up\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()
time.sleep(5)

driver.get("http://practice.automationtesting.in/")


driver.close()