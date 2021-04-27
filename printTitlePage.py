from selenium import webdriver
chrome_driver_path = "D:\KTPM\ChromeDriver Set-up\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
get_title = driver.title
print(get_title)

driver.close()