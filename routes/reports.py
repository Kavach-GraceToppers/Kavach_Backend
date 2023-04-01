import app
from flask import request
from werkzeug.utils import secure_filename


def get_reports():
    email = request.form['email']
    ps = request.form['password']
    try:
        user = app.users_collection.find_one({"email": email, "password": ps})
        if user is not None:
            if user["role"] == "public":
                return app.reports_collection.findMany({})
            else:
                return app.reports_collection.findMany({"email": email})
        else:
            return "User cannot be found."
    except Exception as error:
        return {"status": "error", "error": str(error)}