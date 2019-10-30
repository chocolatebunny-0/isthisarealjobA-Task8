from flask import Flask
from flask import jsonify
from emailverify import scrape

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(Email=scrape())

@app.route('/ha')
def indexa():
    return "loooo"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
