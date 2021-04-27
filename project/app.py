#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 11:07:32 2021

@author: tester
"""


import config
import flask
from flask import Flask, request
import time
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

def stock_prediction(data):
    loaded_model = pickle.load(open(config.MODEL_PATH, 'rb'))
    predictions = loaded_model.predict(data)
    print("PREDICTION", predictions)

    return predictions
    
@app.route("/predict")
def predict():
    Lag1 = request.args.get("Lag1")
    Lag2 = request.args.get("Lag2")
    Lag3 = request.args.get("Lag3")
    Lag4 = request.args.get("Lag4")
    Lag5 = request.args.get("Lag5")
    Volume = request.args.get("Volume")
    
    feature_list = [Lag1, Lag2, Lag3, Lag4, Lag5, Volume]
    
    int_features = [[float(x) for x in feature_list]]
    data = pd.DataFrame(int_features, columns=['Lag1','Lag2','Lag3','Lag4','Lag5', 'Volume'])
    print(data)
    start_time = time.time()
    down_prediction = stock_prediction(data)
    up_prediction = 1 - down_prediction

    output = {}
    
    output["output"] = {
            "Down probability": str(down_prediction[0]),
            "Up probability": str(up_prediction[0]),
            "time taken": str(time.time() - start_time),
            }
    
    return flask.jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="9999")