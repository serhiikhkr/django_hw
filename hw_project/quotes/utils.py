from pymongo import MongoClient


def get_mongodb():
    client = MongoClient("mongodb+srv://helloworld:goitserhii@serhii.n5tsqhh.mongodb.net/?retryWrites=true&w=majority")

    db = client.test
    return db
