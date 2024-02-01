# Basis-Bibliotheken einfügen
from flask import Flask, Response
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)

CORS(app)

training_data = pd.read_csv(os.path.join('data', 'auto-data-mpg.csv'))

@app.route("/", methods = ["GET"])
def index():
    return {"Hallo": "World"}

@app.route("/hello_world", methods=("GET"))
def hello_world():
    return "<h1>Hello World!</h1>"

@app.route("/training_data", methods=("GET"))
def get_training_data():
    return Response(training_data.to_json(), mimetype="application/json")
    return "<h1>Hello World!</h1>"
