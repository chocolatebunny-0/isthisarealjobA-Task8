import os
from flask import Flask
from flask import jsonify
from emailverify import scrape
from flask import request
from datetime import datetime
from werkzeug import secure_filename
from OCR import convert_image_to_test


app = Flask(__name__)


@app.route('/')
def index():
    email = request.args.get('email', None)
    if email:
        return jsonify(Email=scrape(email))
    return jsonify({'status': 'No email supplied'})

@app.route('/ha')
def indexa():
    return "loooo"


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    filename = os.path.join('files', secure_filename(str(datetime.now()) + '.jpg'))
    f.save(filename)
    return convert_image_to_test(filename)
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
