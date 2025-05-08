import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# a)
# data = pd.read_csv('data_C02_emission.csv')

# emissions = data.loc[:, ['CO2 Emissions (g/km)']]

# plt.hist(emissions)
# plt.show()

# b)
# data = pd.read_csv('data_C02_emission.csv')

# sns.scatterplot(
#     data=data,
#     x='Fuel Consumption City (L/100km)',
#     y='CO2 Emissions (g/km)',
#     hue='Fuel Type'
# )
# plt.show()

# c)
# data = pd.read_csv('data_C02_emission.csv')

# sns.boxplot(
#     data=data,
#     x='Fuel Consumption Hwy (L/100km)',
#     hue='Fuel Type'
# )
# plt.show()

# d)
# data = pd.read_csv('data_C02_emission.csv')

# fuel_counts = data.groupby('Fuel Type').size().reset_index(name='Count')

# sns.barplot(
#     data=fuel_counts,
#     x='Fuel Type',
#     y='Count'
# )
# plt.show()

# e)
# data = pd.read_csv('data_C02_emission.csv')

# avg_emission = data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean().reset_index()

# sns.barplot(
#     data=avg_emission,
#     x='Cylinders',
#     y='CO2 Emissions (g/km)',
#     palette='viridis'
# )
# plt.show()