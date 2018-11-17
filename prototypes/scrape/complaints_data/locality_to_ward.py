from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import csv
import pandas as pd

l = [["locality","ward"]]

for i in range(1,199):
	r  = requests.get("http://www.vigeyegpms.in/bbmp/?module=public&action=wardinfo&wardid="+str(i))
	data = r.text
	soup = BeautifulSoup(data,'lxml')
	ward = soup.find('font', {'size': '3%'}).contents[0].replace('Ward', '')
	localities = soup.find_all('td', {'width': '50%'})[13].contents[0].split(',')
	for item in localities:
		l.append([item.strip(),ward.strip()])

print(l)

with open('locality_to_ward.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(l)