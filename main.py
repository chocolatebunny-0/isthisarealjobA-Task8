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
    app.run(host='127.0.0.1', port=8080, debug=True)
