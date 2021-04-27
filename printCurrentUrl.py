from selenium import webdriver
chrome_driver_path = "D:\KTPM\ChromeDriver Set-up\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
driver.set_window_position(0,0)
driver.set_window_size(1300,800)

get_url = driver.current_url
print(get_url)

driver.close()