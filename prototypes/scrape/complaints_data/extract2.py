from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import csv

browser = webdriver.Chrome(executable_path='/Users/danielisaac/Downloads/chromedriver')
browser.get("http://www.vigeyegpms.in/bbmp/index.php?module=helpdeskpublic&action=view-complaints")

l = [['Ward','Complaint']]

for i in range(200):
	elems = browser.find_elements_by_class_name('alt')
	for elem in elems[1:]:
		locality = elem.find_elements_by_tag_name('td')[2].text
		complaints = elem.find_elements_by_tag_name('td')[4].text
		l.append([locality,complaints])
	buttons = browser.find_elements_by_class_name('texts')[5]
	buttons.click()
	print(l)


with open('complaints3.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(l)