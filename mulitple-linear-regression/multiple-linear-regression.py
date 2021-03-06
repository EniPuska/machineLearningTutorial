# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:19:57 2020
Multiple Linear Regression 
@author: alex-dev
"""

import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
#from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

#import the dataset
#windows                                                                         
dataset = pd.read_csv("C:\\Users\\alex-dev\\Desktop\\projects\\machine-learning\\mulitple-linear-regression\\50_Startups.csv")
#Linux
#dataset = pd.read_csv("./Data.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

#encode categorial data
labelEncoderX = LabelEncoder()
x[:, 3] = labelEncoderX.fit_transform(x[:, 3])
transform = ColumnTransformer([("State", OneHotEncoder(), [3])], remainder="passthrough")
x = transform.fit_transform(x)

#Avoiding the Dummy variable Trap
x = x[:, 1:]
#Splitting the dataset into the Training set and Test set
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.2, random_state = 42)

#feature scaling
'''scaleX = StandardScaler()
xTrain = scaleX.fit_transform(xTrain)
xTest = scaleX.transform(xTest)
print(xTrain)'''

#Fitting Multiple Linear Regression to the Training Set
regressor = LinearRegression()
regressor.fit(xTrain, yTrain)

#Predict the Test set results
yPrediction = regressor.predict(xTest)

#Building the optimal model

x = np.append(arr = np.ones((50, 1)).astype(int), values = x, axis = 1)
xOpt = np.array(x[:, [0, 1, 2, 3, 4, 5]], dtype=float)
regressorOLS = sm.OLS(endog = y, exog=xOpt).fit();
regressorOLS.summary();
#remove the second column
xOpt = np.array(x[:, [0, 1, 3, 4, 5]], dtype=int)
regressorOLS = sm.OLS(endog = y, exog=xOpt).fit();
regressorOLS.summary();
#remove the first column
xOpt = np.array(x[:, [0, 3, 4, 5]], dtype=int)
regressorOLS = sm.OLS(endog = y, exog=xOpt).fit();
regressorOLS.summary();
#remove the forth column
xOpt = np.array(x[:, [0, 3, 5]], dtype=int)
regressorOLS = sm.OLS(endog = y, exog=xOpt).fit();
regressorOLS.summary();
#remove the fifth column
xOpt = np.array(x[:, [0, 3]], dtype=int)
regressorOLS = sm.OLS(endog = y, exog=xOpt).fit();
regressorOLS.summary();