import csv
from bs4 import BeautifulSoup
import requests

f = open('Predicting-House-Prices-In-Bengaluru-Train-Data.csv')
reader = csv.reader(f)
w = open('Predicting-House-Prices-In-Bengaluru-Train-Data-pincodes-2.csv','a')
writer = csv.writer(w)

all_rows = []
row0 = next(reader)
row0.append('Pincode')
all_rows.append(row0)

for row in reader:
	locality = row[2]
	modify = [x.lower() for x in locality.split()]
	modify = [x for x in modify if x != '-' and x != ',']
	modify = '-'.join(modify)
	print(modify)
	try:
		r = requests.get("https://www.getpincode.info/" + modify)
		data = r.text
		soup = BeautifulSoup(data)
		pincode = soup.find('div',{'class': 'eight columns'}).find('h1').contents[0]
		print(pincode)
		row.append(pincode)
	except:
		print('Error for ' + locality)
		row.append('ERROR')
	all_rows.append(row)

writer.writerows(all_rows)