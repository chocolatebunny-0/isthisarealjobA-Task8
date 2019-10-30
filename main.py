from flask import Flask
from flask import jsonify
from emailverify import scrape
from flask import request


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
