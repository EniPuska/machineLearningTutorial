#Linear Regression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#import the dataset
#windows 
dataset = pd.read_csv("C:\\Users\\alex-dev\\Desktop\\projects\\machine-learning\\linear-regression\\Salary_Data.csv")
#Linux
#dataset = pd.read_csv("./Data.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#Splitting the dataset into the Training set and Test set
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 1/3, random_state = 42)

#feature scaling
'''scaleX = StandardScaler()
xTrain = scaleX.fit_transform(xTrain)
xTest = scaleX.transform(xTest)
print(xTrain)'''

regressor = LinearRegression()
regressor.fit(xTrain, yTrain)

print(y)
