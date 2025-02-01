from flask_restx import Resource
import requests
from flask import request
from resources.auth import basic_auth  

class CategoryList(Resource):
    @basic_auth.required
    def get(self):
        """
        List all coin categories.
        """
        url = 'https://api.coingecko.com/api/v3/coins/categories/list'
        response = requests.get(url)
        return response.json()
