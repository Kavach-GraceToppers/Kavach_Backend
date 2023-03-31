from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.kavach
reports_collection = db.reports_collection