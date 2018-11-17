import sys 
import numpy as np
sys.path.append('..')

from utils import *

def test_normalize():
	assert normalize('It\'s nice today') == 'Its nice today'

def test_generate_tag_list():
	tags = [{'tag':'lawn'},{'tag':'gym'}]
	assert generate_tag_list(tags) == ['lawn','gym']