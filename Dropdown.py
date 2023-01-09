import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\rutuja.patil05\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://cosmocode.io/automation-practice-webtable/")

# find len of rows
# write xpath for main table  (//table[@id='countries']) then add //tr to count tr in the table
rows=driver.find_elements(By.XPATH,"//table[@id='countries']//tr")
print(len(rows))

# find len of headings/cols
col=driver.find_elements(By.XPATH,"//table[@id='countries']//tr/td/h3")
print(len(col))

# to print data of a specific row/col

data=driver.find_element(By.XPATH,"//table[@id='countries']//tr[3]/td[2]").text
data1=driver.find_element(By.TAG_NAME,"td")
print(data)


# to print all the data in table

for r in range(2, len(rows) + 1):
    for c in range(2, len(col) + 1):
        data_xpath = '//table/tbody/tr[{}]/td[{}]'.format(r, c)
        data1 = driver.find_element(By.XPATH,data_xpath).text
        print(data1)

    print(" ")

driver.quit()