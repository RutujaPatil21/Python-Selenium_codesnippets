from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#-----------checkbox----------------
driver = webdriver.Chrome(r"C:\Users\rutuja.patil05\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
checkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")

# select a particular value
mon=driver.find_element(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
mon.click()

# select all values
for i in range(len(checkbox)):
        checkbox[i].click()




time.sleep(1)
driver.close()

