from flask_restx import Resource
import requests
from flask import request
from resources.auth import basic_auth 

class CoinList(Resource):
    @basic_auth.required
    def get(self):
        """
        List all coins with their market data.
        Returns a paginated list of coins with market data in CAD.
        """
        page_num = int(request.args.get('page_num', 1))
        per_page = int(request.args.get('per_page', 10))
        url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=cad&page={page_num}&per_page={per_page}'
        response = requests.get(url)
        return response.json()

class Coin(Resource):
    @basic_auth.required
    def get(self, coin_id):
        """
        Get a specific coin's market data by ID.
        """
        url = f'https://api.coingecko.com/api/v3/coins/{coin_id}'
        response = requests.get(url)
        return response.json()
