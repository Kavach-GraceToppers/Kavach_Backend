from flask import Flask
from pymongo import MongoClient

import routes.user as user
import routes.inference as inference
import routes.reports as reports

app = Flask(__name__)

app.add_url_rule('/register_user', methods=["POST"], view_func=user.register_user)
app.add_url_rule('/login', methods=["POST"], view_func=user.login)

app.add_url_rule('/run_inference', methods=["POST"], view_func=inference.run_inference)
app.add_url_rule('/get_reports', methods=['POST'], view_func=reports.get_reports())
client = MongoClient('localhost', 27017)

db = client.kavach
reports_collection = db.reports_collection
users_collection = db.users_collection
