#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 10:56:02 2021

@author: tester
"""


import config
import pandas as pd
import numpy as np 
import pickle
from sklearn import model_selection
from sklearn.metrics import classification_report

def run():
    dfx = pd.read_csv(config.TRAINING_FILE).dropna()
    
    df_train, df_test = model_selection.train_test_split(
            dfx, test_size=0.2, random_state=42, stratify=dfx.Direction)
    
    loaded_model = pickle.load(open(config.MODEL_PATH, 'rb'))
    predictions = loaded_model.predict(df_test.iloc[0:1])
    print(predictions)
#    predictions = ["Down" if x > 0.5 else "Up" for x in predictions]
# 
#    print(classification_report(df_test['Direction'], predictions))


# This makes sure the run function is invoked when called if imported by another program  
if __name__ == "__main__":
    run()