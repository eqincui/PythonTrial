from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://eqincui:1234abcd@cluster0-nyuzr.mongodb.net/test")

db=client.test

for event in db.mitti.find():
    pprint(event)
    print('\n')

	
	