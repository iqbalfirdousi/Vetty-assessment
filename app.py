from flask import Flask
from flask_restx import Api
from resources.auth import basic_auth  

app = Flask(__name__)
api = Api(app, version='1.0', title='Cryptocurrency API',
          description='A simple API to fetch cryptocurrency market data')


app.config['BASIC_AUTH_USERNAME'] = 'iqbalfird'
app.config['BASIC_AUTH_PASSWORD'] = 'iqbal123'


basic_auth.init_app(app)


from resources.coin import CoinList, Coin
from resources.category import CategoryList

api.add_resource(CoinList, '/coins')
api.add_resource(Coin, '/coins/<string:coin_id>')
api.add_resource(CategoryList, '/categories')

if __name__ == '__main__':
    app.run(debug=True)
