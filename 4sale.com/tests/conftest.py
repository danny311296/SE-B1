import sys
import pytest
from flask import Flask


@pytest.fixture
def client():
	app = Flask(__name__)
	return app
