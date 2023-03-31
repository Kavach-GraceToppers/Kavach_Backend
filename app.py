import uuid

from flask import Flask
from pymongo import MongoClient
import time

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.kavach
reports_collection = db.reports_collection


def insert_report(nature: str, location: str, alert_level: str, clip_location: str = ""):
    report_id = str(uuid.uuid4())
    reports_collection.insert_one({
        "id": report_id,
        "nature": nature,
        "location": location,
        "time": int(time.time()),
        "alert_level": alert_level,
        "clip_location": clip_location
    })
    print("Inserted: " + report_id)

