# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:19:57 2020
Multiple Linear Regression 
@author: alex-dev
"""

#import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
#from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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
yPrediction = regressor.predict()
