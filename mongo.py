import pymongo
from pymongo import MongoClient
import requests 
import time


cluster = MongoClient("mongodb+srv://Jason:1234@cluster0.majyd.mongodb.net/test?retryWrites=true&w=majority") ## database link
# db = cluster["test"] ##database
# collection = db["test"] ##collection

db = cluster["test"] ##database
collection = db["example"] ##collection

##

key = '3711ff28a46fd9f7cbc915ca70a67b30'
#get cypto prices 
def get_cypto_price():
        try:
            r = requests.get('https://financialmodelingprep.com/api/v3/quote/BTCUSD?apikey=' + key)
            return r.json()
        except Exception as exc:
            print('error: ',exc)


max_time = 200000
for i in range(max_time):
    time.sleep(60)
    post = get_cypto_price()[0]
    collection.insert_one(post)
