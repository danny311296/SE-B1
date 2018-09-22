from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import csv

browser = webdriver.Chrome(executable_path='/Users/danielisaac/Downloads/chromedriver')
browser.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa,Residential-Plot&cityName=Bangalore")

l = []

j = 0
elems = browser.find_elements_by_class_name('m-srp-card__container')
for elem in elems:
	price = elem.find_element_by_class_name('m-srp-card__price').text
	a = elem.find_elements_by_class_name('m-srp-card__summary__title')
	b = elem.find_elements_by_class_name('m-srp-card__summary__info')
	road = elem.find_element_by_class_name('m-srp-card__title').text
	print(price + ' ' + road)
	for i in range(len(a)):
		print(a[i].text , ' ' , b[i].text)

print(len(elems))