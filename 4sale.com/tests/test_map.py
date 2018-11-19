import sys 
import numpy as np
sys.path.append('..')

from map import *

def create():
	try:
		mapservices = MapServices()
		return True
	except:
		return False

def test_create():
	assert create()==True

def test_test_cases():
	mapservices = MapServices()
	mapservices.geocode_address('Bangalore')
	assert mapservices.lat >= 12.9 and mapservices.lat <= 12.98
	assert mapservices.long >= 77.58 and mapservices.long <= 77.6
	dist = mapservices.get_distance_metrics('PR Layout Bangalore 560017','Pes University Banashankari')
	assert dist[2]/1000 >=15 and dist[2]/1000 <=22
	