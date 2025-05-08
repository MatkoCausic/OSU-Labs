import pandas as pd
import numpy as np

# a)
# data = pd.read_csv('data_C02_emission.csv')

# print(data.info())
# print(data.describe())
# print(data.isnull().sum())

# print(data)

# b)
# data = pd.read_csv('data_C02_emission.csv')

# max = data.sort_values(by=['Fuel Consumption City (L/100km)'], ascending=[False]).head(3)
# min = data.sort_values(by=['Fuel Consumption City (L/100km)']).head(3)
# print(max.loc[:,['Make','Model','Fuel Consumption City (L/100km)']])
# print(min.loc[:,['Make','Model','Fuel Consumption City (L/100km)']])

# c)
# data = pd.read_csv('data_C02_emission.csv')

# cars = data[(data['Engine Size (L)'] >= 2.5) & (data['Engine Size (L)'] <= 3.5)]
# print(cars.loc[:, ['Engine Size (L)']])

# print(cars.loc[:, ['Fuel Consumption Comb (L/100km)']].mean())

# d)
# data = pd.read_csv('data_C02_emission.csv')

# audi = data[data['Make'] == 'Audi']
# print(audi.info())
# print(audi[audi['Cylinders'] == 4].loc[:, ['Fuel Consumption Comb (L/100km)']].mean())

# e)
# data = pd.read_csv('data_C02_emission.csv')

# max = data.loc[:, ['Cylinders']].max().item()
# cil = 4
# while cil <= max:
#     info = data[data['Cylinders'] == cil].count()
#     print(f"{cil} cylinders: {info}")
#     emission = data[data['Cylinders'] == cil].loc[:, ['CO2 Emissions (g/km)']].mean()
#     print(f"{cil} emission: {emission}")
#     cil += 2

# i)
data = pd.read_csv('data_C02_emission.csv')

print(data.corr(numeric_only=True))