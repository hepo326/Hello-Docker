from flask import Flask, request, jsonify,render_template
from flask.logging import create_logger
import logging


app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=80, debug=True) 
