import app
import time
from flask import request
from werkzeug.utils import secure_filename


def insert_report(nature: str, location: str, alert_level: str, clip_location: str = ""):
    report = app.reports_collection.insert_one({
        "nature": nature,
        "location": location,
        "time": int(time.time()),
        "alert_level": alert_level,
        "clip_location": clip_location
    })
    report_id = str(report.inserted_id)
    print("Inserted: " + str(report_id))
    return report_id


def add_report():
    try:
        report_id = insert_report(request.form['nature'], request.form['location'], request.form['alert_level'],
                                  request.form['clip_location'])
        f = request.files['file']
        f.save("./video_data/" + secure_filename(request.form['report_id']) + ".mp4")
        return {"status": "success", "report_id": report_id}
    except Exception as error:
        return {"status": "error", "error": str(error)}
