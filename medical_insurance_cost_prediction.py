# -*- coding: utf-8 -*-
"""Medical Insurance Cost Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UgK_lGb-EXCctwTj4R68Nr4I4gqgaql0

*Importing Dependencies*
"""

# Load required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics



"""*Data Collection & Analysis*"""

# Loading the data from CSV file to a Pandas DataFrame
insurance = pd.read_csv('/content/insurance.csv')



# Print first five rows of the dataframe
print(insurance.head(5))

# Number of rows and columns in the dataframe
print(insurance.shape)

# Getting more information about the dataset
print(insurance.info())

"""Categorical Features in the dataset
1.   Sex
2.   Smoke
3.   Region




"""

# Check for missing data
insurance.isnull().sum()

"""Data Analysis"""

# Statistical Measures of the Dataset
print(insurance.describe())

# Distribution of Age
sns.set()
plt.figure(figsize=(6,6))
sns.distplot(insurance['age'])
plt.title('Age Distribution')
plt.show()



# Distribution of Gender
sns.set()
plt.figure(figsize=(6,6))
sns.countplot(x = 'sex', data = insurance)
plt.title('Gender Distribution')
plt.show()

insurance['sex'].value_counts()

# Distribution of Children
sns.set()
plt.figure(figsize=(6,6))
sns.distplot(insurance['bmi'])
plt.title('BMI Distribution')
plt.show()

# Distribution of Children
sns.set()
plt.figure(figsize=(6,6))
sns.countplot(x = 'children', data = insurance)
plt.title('Children Distribution')
plt.show()

insurance['children'].value_counts()

# Distribution of Smokers
sns.set()
plt.figure(figsize=(6,6))
sns.countplot(x = 'smoker', data = insurance)
plt.title('Smoker Distribution')
plt.show()

insurance['smoker'].value_counts()

# Distribution of Region
sns.set()
plt.figure(figsize=(6,6))
sns.countplot(x = 'region', data = insurance)
plt.title('Region Distribution')
plt.show()

insurance['region'].value_counts()

# Distribution of Charges
sns.set()
plt.figure(figsize=(6,6))
sns.distplot(insurance['charges'])
plt.title('Charges Distribution')
plt.show()

"""Data Pre-Processing
Encoding the categorical features
"""

# Encoding the sex column
insurance.replace({'sex':{'male':0,'female':1}}, inplace=True)

# Encoding the smoker column
insurance.replace({'smoker':{'yes':0,'no':1}}, inplace=True)

# Encoding the region column
insurance.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}}, inplace=True)

print(insurance)

"""Splitting the dataset into Features and Target"""

X = insurance.drop(columns='charges', axis=1)
Y = insurance['charges']

print(X)

print(Y)

"""Splitting the data into Train and Test"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training - Linear Regression"""

# Loading the Linear Regression Model
regressor = LinearRegression()

regressor.fit(X_train, Y_train)

# Prediction on Training data
training_data_prediction = regressor.predict(X_train)

# R Squared Value
r2_train = metrics.r2_score(Y_train, training_data_prediction)
print('R Squared Value: ', r2_train)

# Prediction on Test data
test_data_prediction = regressor.predict(X_test)

# R Squared Value
r2_test = metrics.r2_score(Y_test, test_data_prediction)
print('R Squared Value: ', r2_test)

"""Building a Predictive System"""

input_data = (31,1,25.74,0,1,0)

# Changing input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = regressor.predict(input_data_reshaped)
print(prediction)

print('The insurance cost is USD ', prediction[0])
