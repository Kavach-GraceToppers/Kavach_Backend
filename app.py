from flask import Flask
from pymongo import MongoClient

from routes import reports
from routes import user

app = Flask(__name__)

app.add_url_rule('/register_user', view_func=user.register_user)
app.add_url_rule('/add_report', view_func=reports.add_report)


client = MongoClient('localhost', 27017)

db = client.kavach
reports_collection = db.reports_collection
users_collection = db.users_collection




