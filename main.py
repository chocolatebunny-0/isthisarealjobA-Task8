import os
from flask import Flask
from flask import jsonify
from emailverify import scrape
from flask import request
from datetime import datetime
from werkzeug import secure_filename
from OCR import convert_image_to_test
from grammatical_error_counter import error_counter
from addresschecker import address_checker
from coynamechecker import match_address_name


app = Flask(__name__)


@app.route('/')
def index():
    email = request.args.get('email', None)
    if email:
        return jsonify(Email=scrape(email))
    return jsonify({'status': 'No email supplied'})

@app.route('/error_count')
def error_count():
    msg_body = request.args.get('msg_body', None)
    if msg_body:
        return jsonify(Error_Counter=error_counter(msg_body))
    return jsonify({'status': 'No message body supplied'})

@app.route('/check_address')
def check_address():
    address = request.args.get('address', None)
    if address:
        return jsonify(Check_Address=address_checker(address))
    return jsonify({'status': 'No address supplied'})


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    filename = os.path.join('files', secure_filename(str(datetime.now()) + '.jpg'))
    f.save(filename)
    return convert_image_to_test(filename)
 
@app.route('/match_name_and_address')
def match_name_and_address():
    thename = request.args.get('name', None)
    theaddress = request.args.get('address', None)
    if theaddress:
        return jsonify(Match_Name_Address=match_address_name(thename, theaddress))
    return jsonify({'status': 'Name or address not supplied'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)