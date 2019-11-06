import os
from flask import Flask
from flask_cors import CORS
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
from nairaland_senti import*




app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])

def index():
    email = request.form['email']
    if email:
        return jsonify(Email=scrape(email))
    return jsonify({'status': 'No email supplied'})

@app.route('/error_count', methods=['POST'])

def error_count():
    msg_body = request.form['msg_body']
    if msg_body:
        return jsonify(Error_Counter=error_counter(msg_body))
    return jsonify({'status': 'No message body supplied'})

@app.route('/check_address', methods=['POST'])

def check_address():
    address = request.form['address']
    if address:
        return jsonify(Check_Address=address_checker(address))
    return jsonify({'status': 'No address supplied'})

@app.route('/match_name_and_address', methods=['POST'])

def match_name_and_address():
    thename = request.form['name']
    theaddress = request.form['address']
    if theaddress:
        return jsonify(Match_Name_Address=match_address_name(thename, theaddress))
    return jsonify({'status': 'Name or address not supplied'})

@app.route('/check_name', methods=['POST'])

def check_name():
    check = request.form['company_name']
    if check:
        return jsonify(Verify_Name=name_verification(check))
    return jsonify({'status': 'Name not correctly supplied'})

@app.route('/linkedin_presence', methods=['POST'])

def linkedin_presence():
    presence = request.form['ln_company_name']
    if presence:
        return jsonify(Verify_on_Linkedin=linkedin_job_search(presence))
    return jsonify({'status': 'Name not correctly supplied'})

@app.route('/nairaland_sentimental_analysis', methods=['POST'])

def nairaland_sentimental_analysis():
    n_analysis = request.form['searchTerm']
    if n_analysis:
        return jsonify(Verify_on_Nairaland=NScraper(n_analysis))
    return jsonify({'status': 'Name not correctly supplied'})

@app.route('/upload', methods=['POST'])

def upload():
    f = request.files['file']
    filename = os.path.join('files', secure_filename(str(datetime.now()) + '.jpg'))
    f.save(filename)
    return convert_image_to_test(filename)

@app.route('/full', methods=['POST'])

def check_job():
    
    coy_name = request.form['coy_name']
    address = request.form['address']
    msg_body = request.form['body']
    #email = request.form['email']
    
    global confidence
    confidence = 0
    
    #if "is OK" in scrape(email):
        #confidence += 10
    #else:
        #confidence = confidence
    
    print(confidence, " done")
    
    if "real" in error_counter(msg_body):  
        confidence += 25
    else:
        confidence = confidence
        
    print(confidence, " done") 
    
    if address_checker(address) == "available":
        confidence += 10
    else:
        confidence = confidence

    print(confidence, " done")

    #if linkedin_job_search(coy_name) == "The company is on Linkedin and analysis shows it is a big company":
        #confidence += 20
    #else:
        #confidence = confidence

    #print(confidence, " done")

    if "be real" in NScraper(coy_name):
        confidence += 15
    elif "conclude on" in NScraper(coy_name):
        confidence += 7
    else:
        confidence = confidence

    print(confidence, " done")

    if name_verification(coy_name) == "company records are found on CAC page":
        confidence += 50
    else:
        confidence = 0

    print(confidence, " done")

    return jsonify(Confidence=str(confidence)+"%")



#backup

@app.route('/el')
def index1():
    email = request.args.get('email', None)
    if email:
        return jsonify(Email=scrape(email))
    return jsonify({'status': 'No email supplied'})

@app.route('/error_count1')
def error_count1():
    msg_body = request.args.get('msg_body', None)
    if msg_body:
        return jsonify(Error_Counter=error_counter(msg_body))
    return jsonify({'status': 'No message body supplied'})

@app.route('/check_address1')
def check_address1():
    address = request.args.get('address', None)
    if address:
        return jsonify(Check_Address=address_checker(address))
    return jsonify({'status': 'No address supplied'})

@app.route('/match_name_and_address1')
def match_name_and_address1():
    thename = request.args.get('name', None)
    theaddress = request.args.get('address', None)
    if theaddress:
        return jsonify(Match_Name_Address=match_address_name(thename, theaddress))
    return jsonify({'status': 'Name or address not supplied'})

@app.route('/check_name1')
def check_name1():
    check = request.args.get('company_name', None)
    if check:
        return jsonify(Verify_Name=name_verification(check))
    return jsonify({'status': 'Name not correctly supplied'})

@app.route('/linkedin_presence1')
def linkedin_presence1():
    presence = request.args.get('ln_company_name', None)
    if presence:
        return jsonify(Verify_on_Linkedin=linkedin_job_search(presence))
    return jsonify({'status': 'Name not correctly supplied'})

@app.route('/nairaland_sentimental_analysis1')
def nairaland_sentimental_analysis1():
    n_analysis = request.args.get('searchTerm', None)
    if n_analysis:
        return jsonify(Verify_on_Nairaland=NScraper(n_analysis))
    return jsonify({'status': 'Name not correctly supplied'})

@app.route('/upload1', methods=['POST'])
def upload1():
    f = request.files['file']
    filename = os.path.join('files', secure_filename(str(datetime.now()) + '.jpg'))
    f.save(filename)
    return convert_image_to_test(filename)

@app.route('/full1')
def check_job1():
    
    coy_name = request.args.get('coy_name', None)
    address = request.args.get('address', None)
    msg_body = request.args.get('body', None)
    email = request.args.get('email', None)
    
    #global confidence
    confidence = 0
    
    if "is OK" in scrape(email):
        confidence += 10
    else:
        confidence = confidence
    
    print(confidence, " done")
    
    if "real" in error_counter(msg_body):  
        confidence += 15
    else:
        confidence = confidence
        
    print(confidence, " done") 
    
    if address_checker(address) == "available":
        confidence += 10
    else:
        confidence = confidence

    print(confidence, " done")

    if linkedin_job_search(coy_name) == "The company is on Linkedin and analysis shows it is a big company":
        confidence += 20
    else:
        confidence = confidence

    print(confidence, " done")

    if "be real" in NScraper(coy_name):
        confidence += 15
    elif "conclude on" in NScraper(coy_name):
        confidence += 7
    else:
        confidence = confidence

    print(confidence, " done")

    if name_verification(coy_name) == "company records are found on CAC page":
        confidence += 30
    else:
        confidence = 0

    print(confidence, " done")

    return jsonify(Confidence=str(confidence)+"%")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
