from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import csv
import pandas as pd

r  = requests.get("http://www.vigeyegpms.in/bbmp/?module=helpdeskpublic&action=view-complaints")
data = r.text

soup = BeautifulSoup(data)

l = []

for div in soup.find_all('tr', {'class': 'alt'}):
	l.append([])
	l[len(l)-1].append(' '.join(''.join(div.findChildren('td')[2].contents).split()))
	l[len(l)-1].append(' '.join(''.join(div.findChildren('td')[4].contents).split()))

for elem in l: 
	print(elem,end='\n\n\n')