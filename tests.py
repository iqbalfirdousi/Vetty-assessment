from flask_testing import TestCase
from app import app  # Import your Flask app
from flask import Flask
import requests

class APITestCase(TestCase):
    def create_app(self):
        """
        Set up the app for testing purposes
        """
        app.config['TESTING'] = True
        app.config['BASIC_AUTH_USERNAME'] = 'iqbalfird'
        app.config['BASIC_AUTH_PASSWORD'] = 'iqbal123'
        return app

    def test_categories(self):
        """
        Test the /categories endpoint.
        """
        response = self.client.get('/categories', auth=('iqbalfird', 'iqbal123'))
        data = response.json
        self.assertIn('category_id', data[0]) 

    def test_single_coin(self):
        """
        Test the /coins/<coin_id> endpoint.
        """
        response = self.client.get('/coins/bitcoin', auth=('iqbalfird', 'iqbal123'))
        data = response.json
        self.assertIn('id', data) 

    def test_coins(self):
        """
        Test the /coins endpoint.
        """
        response = self.client.get('/coins', auth=('iqbalfird', 'iqbal123'))
        data = response.json
        self.assertGreater(len(data), 0) 

if __name__ == '__main__':
    import unittest
    unittest.main()
