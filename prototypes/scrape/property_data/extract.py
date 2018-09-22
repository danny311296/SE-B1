from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import csv
import pandas as pd

r  = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa,Residential-Plot&cityName=Bangalore")
data = r.text

soup = BeautifulSoup(data)

l = []

for div in soup.find_all('div', {'class': 'm-srp-card__container'}):
	l.append([])
	a = div.find_all('div', {'class': 'm-srp-card__summary__title'})
	b = div.find_all('div', {'class': 'm-srp-card__summary__info'})
	price = div.find('span', {'class': 'm-srp-card__price'}).contents[0]
	road = str(div.find('a',{'class': 'm-srp-card__title'}).contents)
	l[len(l)-1].append(('price', price))
	road = ''.join(''.join(road.split()).split('forSalein\\n')[1])
	l[len(l)-1].append(('road', road.replace('\\n\']','')))
	for i in range(len(a)):
		l[len(l)-1].append((a[i].contents[0],b[i].contents[0]))

for elem in l: 
	print(elem,end='\n\n\n')