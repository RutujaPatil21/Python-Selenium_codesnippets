from selenium import webdriver
from selenium.webdriver.common.by import By
import requests as requests    # installed Requests pacakge form settings




#---------Broken links-------------

driver = webdriver.Chrome(r"C:\Users\rutuja.patil05\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

alllinks=driver.find_elements(By.TAG_NAME,'a')
# printing all the links
print(len(links))
for links in alllinks:
    print(links)


# hitting all the links to server using request object . the links that have status
# more than 400 will be considered as broken links
for link in alllinks:
        url=link.get_attribute('href')
        try:
            res=requests.head(url)  #hitting all the links to server
        except:
            None
        if res.status_code > 400:
            print("broken link")
        else:
            print("Not broken")
