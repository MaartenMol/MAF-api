#Import needed modules
import pymongo
from pymongo import MongoClient

#Setup MongoDB Conn
client = MongoClient()
db = client.test
customers = db.customers
coupons = db.coupons

posts = db.posts