# Basis-Bibliotheken einfügen
from flask import Flask, Response, request
from flask_cors import CORS
import pandas as pd
import os
import pickle

app = Flask(__name__)

CORS(app)

# Load training data
training_data = pd.read_csv(os.path.join('data', 'auto-data-mpg.csv'))

# Load trained model
trained_model = pickle.load(open(os.path.join('data', 'models', 'baummethoden_lr.pickle'), 'rb'))

@app.route("/", methods=["GET"])
def index():
    return {"Hallo": "World"}

@app.route("/hello_world", methods=["GET"])
def hello_world():
    return "<h1>Hello World!</h1>"

@app.route("/training_data", methods=["GET"])
def get_training_data():
    return Response(training_data.to_json(), mimetype="application/json")

@app.route("/predict", methods=["GET"])
def predict():
    zylinder = request.args.get("zylinder")
    ps = request.args.get("ps")
    gewicht = request.args.get("gewicht")
    beschleunigung = request.args.get("beschleunigung")
    baujahr = request.args.get("baujahr")

    # creating a prediction from Features
    prediction = trained_model.predict([zylinder, ps, gewicht, beschleunigung, baujahr])

    app.logger.info("Prediction: {}".format(prediction))

    # Return JSON response
    return {"result": prediction.tolist()}

#if __name__ == "__main__":
    #app.run(debug=True)
