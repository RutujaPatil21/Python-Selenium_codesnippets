# to use key actions like ctrl A , ctrl v etc using ActionChains class

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(r"C:\Users\rutuja.patil05\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://text-compare.com/")
driver.maximize_window()

input=driver.find_element(By.XPATH,"//textarea[@id='inputText1']").send_keys("welcome")
output=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")


act=ActionChains(driver)       # create action class obj

# for pressing Ctrl+a

act.key_down(Keys.CONTROL)     #press ctrl
act.send_keys("a")             # press a
act.key_up(Keys.CONTROL)       # release ctrl
act.perform()

# this can be written in to single line as
# act.key_down(Keys.CONTROL)send_keys("a").key_up(Keys.CONTROL).perform()

act=ActionChains(driver)       # create action class obj
act.key_down(Keys.CONTROL)     #press ctrl
act.send_keys("c")             # press c
act.key_up(Keys.CONTROL)
act.perform()

act.send_keys(Keys.TAB).perform()      # press tab to move to next input box

act=ActionChains(driver)       # create action class obj
act.key_down(Keys.CONTROL)     #press ctrl
act.send_keys("v")             # press v
act.key_up(Keys.CONTROL)
act.perform()