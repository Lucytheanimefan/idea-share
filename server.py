from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://amanocha:idea@ds147789.mlab.com:47789/heroku_ds7lr288')
    db = client.heroku_ds7lr288
    return db