from werkzeug.utils import secure_filename

import app
import time
from flask import request


def upload_file():
    try:
        f = request.files['file']
        f.save("./video_data/"+secure_filename(request.form['report_id'])+".mp4")
        return 'file uploaded successfully'
    except Exception as error:
        return {"status":str(error)}

