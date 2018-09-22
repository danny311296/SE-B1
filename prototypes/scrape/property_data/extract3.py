from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import csv

browser = webdriver.Chrome(executable_path='/Users/danielisaac/Downloads/chromedriver')
#browser.get("https://www.99acres.com/search/property/buy/residential-all/bangalore-all?search_type=QS&search_location=CP20&lstAcn=CP_R&lstAcnId=20&src=CLUSTER&preference=S&selected_tab=1&city=20&res_com=R&property_type=R&isvoicesearch=N&keyword_suggest=bangalore%20(all)%3B&fullSelectedSuggestions=bangalore%20(all)&strEntityMap=W3sidHlwZSI6ImNpdHkifSx7IjEiOlsiYmFuZ2Fsb3JlIChhbGwpIiwiQ0lUWV8yMCwgUFJFRkVSRU5DRV9TLCBSRVNDT01fUiJdfV0%3D&texttypedtillsuggestion=Bangalore&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&suggestion=CITY_20%2C%20PREFERENCE_S%2C%20RESCOM_R&searchform=1&price_min=null&price_max=null")
browser.get("https://www.99acres.com/search/property/buy/independent-house/bangalore-all?search_type=QS&search_location=SH&lstAcn=SEARCH&lstAcnId=9532695904381129&src=CLUSTER&preference=S&city=20&res_com=R&property_type=2&selected_tab=1&isvoicesearch=N&keyword_suggest=bangalore%20(all)%3B&fullSelectedSuggestions=bangalore%20(all)&strEntityMap=W3sidHlwZSI6ImNpdHkifSx7IjEiOlsiYmFuZ2Fsb3JlIChhbGwpIiwiQ0lUWV8yMCwgUFJFRkVSRU5DRV9TLCBSRVNDT01fUiJdfV0%3D&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&searchform=1&price_min=null&price_max=null")
l = [['locality','area','cost','costPerSquareFeet','bedrooms']]

for i in range(10):
	elems = browser.find_elements_by_class_name('srpWrap')
	for elem in elems:
		title = elem.find_element_by_tag_name('span').text.split('in')[1].strip()
		print(title)
		price = elem.find_element_by_class_name('srpNw_price').text
		print(price)
		area = elem.find_element_by_class_name('_auto_areaValue').find_element_by_tag_name('b').text
		print(area)
		bedrooms = elem.find_element_by_class_name('_auto_bedroom').find_element_by_tag_name('b').text
		print(bedrooms)
		perSquareFeet = elem.find_element_by_class_name('_auto_ppu_area').text
		print(perSquareFeet)
		l.append([title,area,price,perSquareFeet,bedrooms])
	#browser.get('https://www.99acres.com/independent-house-in-bangalore-ffid-page-' + str(i + 2))

with open('property2.csv','w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(l)