from app import reports_collection
import time
from flask import request


def insert_report(nature: str, location: str, alert_level: str, clip_location: str = ""):
    report = reports_collection.insert_one({
        "nature": nature,
        "location": location,
        "time": int(time.time()),
        "alert_level": alert_level,
        "clip_location": clip_location
    })
    report_id = report.inserted_id
    print("Inserted: " + report_id)
    return report_id


def add_report():
    try:
        report_id = insert_report(request.form['nature'], request.form['location'], request.form['alert_level'],
                                  request.form['clip_location'])
        return {"status": "success", "report_id": report_id}
    except Exception as error:
        return {"status": str(error)}
