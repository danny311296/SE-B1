import pytest
import sys 
import numpy as np
sys.path.append('..')
from filter import *

def create():
	try:
		test_filter = Filter()
		return True
	except:
		return False

def test_create():
	assert create()==True


