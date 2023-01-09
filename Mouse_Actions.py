import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\rutuja.patil05\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://www.ebay.com/")
time.sleep(3)

menu =driver.find_element(By.XPATH,"//li[@class='hl-cat-nav__js-tab']//a[contains(text(),'Electronics')]")
apple=driver.find_element(By.XPATH,"//a[normalize-space()='Apple']")
act=ActionChains(driver)  # ActionsChains() is a class for mouse actions , act is the obj we will use , need to pass driver obj


# move_to_element () is used to perform mouse hover action
act.move_to_element(menu).move_to_element(apple).click().perform()

#right click action
act.context_click(menu).perform()


# double click
act.double_click(menu).perform()


#drag and drop
act.drag_and_drop(source ele , target ele).perform()

# to do mouse drag actions on sliders
# get location of that element and then add the values to x and y axis

print(menu.location)  # you will get x and y cordinates form this e.g. x=100 y=100

act.drag_and_drop_by_offset(source , 150 , 150)  # 100+50 i,e drag the source by 50


