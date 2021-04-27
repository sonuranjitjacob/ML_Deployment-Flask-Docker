#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 09:54:29 2021

@author: tester
"""


import config
import pandas as pd
import numpy as np 
import pickle
from sklearn import model_selection


import statsmodels.api as sm
import statsmodels.formula.api as smf


def run():
    dfx = pd.read_csv(config.TRAINING_FILE).dropna()
    
    df_train, df_test = model_selection.train_test_split(
            dfx, test_size=0.2, random_state=42, stratify=dfx.Direction)
    
    model = smf.glm(formula = 'Direction~Lag1+Lag2+Lag3+Lag4+Lag5+Volume', data=df_train, family=sm.families.Binomial())
    print('Training begun')
    result = model.fit()
    pickle.dump(result, open(config.MODEL_PATH, 'wb'))
    print('Training completed and model saved')
    
# This makes sure the run function is invoked when called if imported by another program  
if __name__ == "__main__":
    run()