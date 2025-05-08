import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
import sklearn.linear_model as lm
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score, max_error

data = pd.read_csv('data_C02_emission.csv')

values = [
    'Engine Size (L)','Cylinders','Fuel Type','Fuel Consumption City (L/100km)','Fuel Consumption Hwy (L/100km)','Fuel Consumption Comb (L/100km)','Fuel Consumption Comb (mpg)','CO2 Emissions (g/km)'
]

X = data[values]
y = data['CO2 Emissions (g/km)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

ohe = OneHotEncoder()
X_encoded_train = ohe.fit_transform(X_train[['Fuel Type']]).toarray()
x_encoded_test = ohe.fit_transform(X_test[['Fuel Type']]).toarray()

linearModel = lm.LinearRegression()
linearModel.fit(X_encoded_train, y_train)

y_test_p = linearModel.predict(x_encoded_test)

ME = max_error(y_test, y_test_p)
print(f"Max Error: {ME}")

error = np.abs(y_test_p, y_test)
print(np.max(error))
max_error_id = np.argmax(error)

max_error_model = data.iloc[max_error_id, 1]
print(max_error_model)