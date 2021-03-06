from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "D:\KTPM\ChromeDriver Set-up\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://itmscoaching.herokuapp.com/form")
enterFstName = driver.find_element_by_id("first-name")
enterFstName.send_keys("Binh") 
 
enterLastName = driver.find_element_by_id("last-name")
enterLastName.send_keys("Nguyen")

enterJobTitle = driver.find_element_by_id("job-title")
enterJobTitle.send_keys("Tester")

clickRradSchool = driver.find_element_by_id("radio-button-3")
clickRradSchool.click()

clickFemale = driver.find_element_by_id("checkbox-2")
clickFemale.click()

experience = driver.find_element_by_xpath('//*[@id="select-menu"]/option[4]')
experience.click()

date = driver.find_element_by_id("datepicker")
date.send_keys("07/20/2011") 
# đề ở lab là 20/07/2011 nhưng ở web date ở trạng thái mm/dd/yy nên em thay bằng 07/20/2011

submitBtn = driver.find_element_by_link_text("Submit")
submitBtn.click()
time.sleep(1)

driver.close()