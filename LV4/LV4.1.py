import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
import sklearn.linear_model as lm
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score

# a)
data = pd.read_csv('data_C02_emission.csv')

numerical_features = [
    'Engine Size (L)','Cylinders','Fuel Consumption City (L/100km)','Fuel Consumption Hwy (L/100km)','Fuel Consumption Comb (L/100km)','Fuel Consumption Comb (mpg)','CO2 Emissions (g/km)'
]
output = 'CO2 Emissions (g/km)'

X = data[numerical_features]
y = data[output]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

# b)
plt.scatter(X_train['Engine Size (L)'], y_train, c='blue')
plt.scatter(X_test['Engine Size (L)'], y_test, c='red')
plt.show()

# c)
plt.hist(X_train['Engine Size (L)'])
plt.show()

sc = MinMaxScaler()
X_train_n = sc.fit_transform(X_train)
plt.hist
plt.hist(X_train_n[:, 0])
plt.show()

X_test_n = sc.transform(X_test)

# d)
linearModel = lm.LinearRegression()
linearModel.fit(X_train_n, y_train)

y_test_p = linearModel.predict(X_test_n)
MAE = mean_absolute_error(y_test, y_test_p)

print(y_test_p)
print(MAE)

# e)
plt.scatter(y_test, y_test_p)
plt.show()

# f)
MAE = mean_absolute_error(y_test , y_test_p)
MSE = mean_squared_error(y_test , y_test_p)
MAPE = mean_absolute_percentage_error(y_test, y_test_p)
R_TWO_SCORE = r2_score(y_test, y_test_p)

print(f"MAE: {MAE}, MSE: {MSE}, MAPE: {MAPE}, R2 SCORE: {R_TWO_SCORE}")