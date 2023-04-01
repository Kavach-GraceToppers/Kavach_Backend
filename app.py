from flask import Flask
from pymongo import MongoClient

import routes.user as user
import routes.reports as reports

app = Flask(__name__)

app.add_url_rule('/register_user', methods=["POST"], view_func=user.register_user)
app.add_url_rule('/add_report', method=["POST"], view_func=reports.add_report)

client = MongoClient('localhost', 27017)

db = client.kavach
reports_collection = db.reports_collection
users_collection = db.users_collection
