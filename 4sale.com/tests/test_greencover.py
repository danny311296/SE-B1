import sys 
import numpy as np
sys.path.append('..')

from greencover import *

def create():
	try:
		imgprocessor = Image_Processor(12.9716,77.5946)
		return True
	except:
		return False

def test_create():
	assert create()==True

def test_values():
	imgprocessor = Image_Processor(12.9716,77.5946)
	assert type(imgprocessor.img)==np.ndarray 
	assert imgprocessor.green_percent >= 0 and imgprocessor.green_percent <= 100

def test_test_cases():
	d = {'Antartica': {'lat':-82.8628,'lng':135.00},'Amazon':{'lat':-3.4653,'lng':-62.2159}}
	maximum_expected_green_cover = {'Antartica':1,'Amazon':99}
	minimum_expected_green_cover = {'Antartica':0,'Amazon':50}
	for key,value in d.items():
		imgprocessor = Image_Processor(value['lat'],value['lng'])
		print(imgprocessor.green_percent)
		assert imgprocessor.green_percent <= maximum_expected_green_cover[key] and imgprocessor.green_percent >= minimum_expected_green_cover[key]
