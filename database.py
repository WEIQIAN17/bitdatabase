import requests 
import pandas as pd 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time
import datetime

key = '3711ff28a46fd9f7cbc915ca70a67b30'
#get cypto prices 
def get_cypto_price():
        try:
            r = requests.get('https://financialmodelingprep.com/api/v3/quote/BTCUSD?apikey=' + key)
            #return r.json()[0]['price']
            return r.json()[0]
        except Exception as exc:
            print('error: ',exc)

##
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:*password*/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#db = Marshmallow(app)

class BitPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exchange = db.Column(db.String(64))  
    price = db.Column(db.String(64))     
    horah = db.Column(db.DateTime)

    def __init__(self, exchange, price, horah):
        self.exchange = exchange
        self.price = price
        if horah is None:
            horah = datetime.utcnow()
        self.horah = horah

    def __repr__(self):
        return '<Exchange {}>'.format(self.exchange)

if __name__ == '__main__':
    max_time = 3
    for i in range(max_time):
        time.sleep(60)
        ct = datetime.datetime.now()
        ct = ct.replace(second=0, microsecond=0)
        #data = {'exchange':'Other', 'price': get_cypto_price()['price'], 'horah': ct}
        #data = get_cypto_price()
        #data = get_cypto_price()['price']
        #print(data, ct)
        data = BitPrice(exchange = 'Other', price = get_cypto_price()['price'], horah = ct)
        db.session.add(data)
        db.session.commit()
        #print("bitcoin price:-", get_cypto_price(),  " current time:-", ct)
