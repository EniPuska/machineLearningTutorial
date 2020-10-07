import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
#import the dataset
#windows 
#dataset = pd.read_csv("C:\\Users\\alex-dev\\Desktop\\projects\\machine-learning\\data-processing\\data.csv")
#Linux
dataset = pd.read_csv("./Data.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#taking missing data
'''imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])'''

#encode categorial data
'''labelEncoderX = LabelEncoder()
x[:, 0] = labelEncoderX.fit_transform(x[:, 0])
transform = ColumnTransformer([("countries", OneHotEncoder(), [0])], remainder="passthrough")
x = transform.fit_transform(x)
labelEncoderY = LabelEncoder()
y = labelEncoderY.fit_transform(y)''' 

#Splitting the dataset into the Training set and Test set
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.2, random_state = 42)

#feature scaling
'''scaleX = StandardScaler()
xTrain = scaleX.fit_transform(xTrain)
xTest = scaleX.transform(xTest)
print(xTrain)'''