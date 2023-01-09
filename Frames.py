# frames are not accessible by web elements , so we need ot use switch_to.frame()
# But we cannot switch form one frame to another ,
# so we need to go to main page go to frame , go back to main page and then go to next frame
# by using _switch_to.default_content()
# Frames can be identified by name , id , webelement
# if there are nested iframes , you need to switch to locate outter frane -> switch to outter frame -> locate inner frame -> switch to inner frame
#switch_to.parentframe -> to swith to parent frame


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests as requests    # installed Requests pacakge form settings


driver = webdriver.Chrome(r"C:\Users\rutuja.patil05\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.switch_to.frame("singleframe")
driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("dog")
time.sleep(3)
driver.switch_to.default_content()
driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()
driver.switch_to.frame("singleframe")
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("cat")