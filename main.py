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
from cac_leke import name_verification
from linkedin2 import linkedin_job_search

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

@app.route('/match_name_and_address')
def match_name_and_address():
    thename = request.args.get('name', None)
    theaddress = request.args.get('address', None)
    if theaddress:
        return jsonify(Match_Name_Address=match_address_name(thename, theaddress))
    return jsonify({'status': 'Name or address not supplied'})

@app.route('/check_name')
def check_name():
    check = request.args.get('company_name', None)
    if check:
        return jsonify(Verify_Name=name_verification(check))
    return jsonify({'status': 'Name not correctly supplied'})

@app.route('/linkedin_presence')
def linkedin_presence():
    presence = request.args.get('ln_company_name', None)
    if presence:
        return jsonify(Verify_on_Linkedin=linkedin_job_search(presence))
    return jsonify({'status': 'Name not correctly supplied'})

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    filename = os.path.join('files', secure_filename(str(datetime.now()) + '.jpg'))
    f.save(filename)
    return convert_image_to_test(filename)
 



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
