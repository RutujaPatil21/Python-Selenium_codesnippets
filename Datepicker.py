import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\rutuja.patil05\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://jqueryui.com/datepicker/")

# Logic :
# 1]we first compare the input year and month  with the month and year displayed in the calender
# 2] We then get the anchor tags of the dates in the tbody-> tr-> td
# 3] compare that with teh dat ewe want to enter

driver.switch_to.frame(0)

mon="May"
dt="21"
yr="2023"

driver.find_element(By.ID,"datepicker").click()





while True:
    year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    #dt = driver.find_element(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a").text
    if mon==month and yr==year:
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
   if ele.text==dt:
        ele.click()
        time.sleep(3)
        break










driver.close()
