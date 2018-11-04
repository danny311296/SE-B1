from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

class Scraper:
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path='bin/chromedriver')
        
    def scrape_complaints(self,numberOfPages=200):
        self.browser.get("http://www.vigeyegpms.in/bbmp/index.php?module=helpdeskpublic&action=view-complaints")
        l = []
        for i in range(numberOfPages):
            elems = self.browser.find_elements_by_class_name('alt')
            for elem in elems[1:]:
                locality = elem.find_elements_by_tag_name('td')[2].text
                complaints = elem.find_elements_by_tag_name('td')[4].text
                l.append([locality,complaints])
            buttons = self.browser.find_elements_by_class_name('texts')[5]
            buttons.click()
        with open('db/input_csv_files/complaints3.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(l)
            
    