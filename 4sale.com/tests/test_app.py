import pytest
import pytest_flask
from flask import url_for


class TestApp:

	
	
	def test_form_about(self, client):
		res = client.get(url_for('about'))
		assert res.status_code == 200
	
	def test_form_contact(self, client):
		res = client.get(url_for('contact'))
		assert res.status_code == 200
	
	def test_listings_single(self, client):
		res = client.get(url_for('listings_single'))
		assert res.status_code == 302
	
	def test_listings(self, client):
		res = client.get(url_for('listings'))
		assert res.status_code == 200
	
	def test_login(self, client):
		res = client.get(url_for('login'))
		assert res.status_code == 200
		
	def test_post_ad(self, client):
		res = client.get(url_for('post-ad'))
		assert res.status_code == 200
		
	def test_register(self, client):
		res = client.get(url_for('register'))
		assert res.status_code == 200
		
	def test_news(self, client):
		res = client.get(url_for('news'))
		assert res.status_code == 200
		
	def test_ques_ans(self, client):
		res = client.get(url_for('ques_ans'))
		assert res.status_code == 200
		
	def test_reply(self, client):
		res = client.get(url_for('reply'))
		assert res.status_code == 200
		
	
