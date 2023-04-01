import app
import time
from flask import request
from werkzeug.utils import secure_filename


def insert_report(nature: str, location: str, alert_level: str, email: str = ""):
    report = app.reports_collection.insert_one({
        "nature": nature,
        "location": location,
        "time": int(time.time()),
        "alert_level": alert_level,
        "email": email,
        "clip_location": ""
    })
    report_id = str(report.inserted_id)
    print("Inserted: " + str(report_id))
    return report_id


def get_alert_level_from_nature(nature: str):
    low = ["vandalism", "shop_lifting", "fighting", "arrest"]
    mid = ["assault", "abuse", "burglary", "stealing"]
    high = ["explosion", "shooting", "arson", "road_accident", "robbery"]
    if nature in low:
        return "low"
    elif nature in mid:
        return "mid"
    elif nature in high:
        return "high"
    else:
        return "normal"


def run_inference():
    try:
        f = request.files['file']

        if crime_found:
            report_id = insert_report(nature, "Manipal", get_alert_level_from_nature(nature), request.form['email'])
            app.reports_collection.update_one({"_id": report_id},
                                              {"$set": {"clip_location": "./video_data/" + secure_filename(report_id) + ".mp4"}})
            f.save("./video_data/" + secure_filename(report_id) + ".mp4")
            return {"status": "crime_found", "report_id": report_id}
        else:
            return {"status": "normal"}
    except Exception as error:
        return {"status": "error", "error": str(error)}

