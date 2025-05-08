import numpy as np
import csv
import matplotlib.pyplot as plt

# a)
# f = np.loadtxt('data.csv', delimiter=',', skiprows=1)
# row_count = sum(1 for row in f)
# print(row_count)

# b)
# f = np.loadtxt('data.csv', delimiter=',', skiprows=1)

# mass = []
# for item in f:
#     mass.append(item[2])

# height = []
# for item in f:
#     height.append(item[1])

# plt.scatter(mass,height)
# plt.show()

# c)
# f = np.loadtxt('data.csv', delimiter=',', skiprows=1)

# mass = f[1::50,2]
# height = f[1::50,1]

# plt.scatter(mass,height)
# plt.show()

# d)
# f = np.loadtxt('data.csv', delimiter=',', skiprows=1)

# min = f[0,1]
# max= f[0,1]
# mean = 0
# for item in f:
#     if item[1] < min:
#         min = item[1]
#     if item[1] > max:
#         max = item[1]
#     mean += item[1]

# row_count = sum(1 for item in f)
# mean /= row_count

# print(f"Min: {min}\nMax: {max}\nMean: {mean}")

# e)
# f = np.loadtxt('data.csv', delimiter=',', skiprows=1)
# minM = f[0,1]
# maxM = f[0,1]
# meanM = 0
# minF = f[0,1]
# maxF = f[0,1]
# meanF = 0
# for item in f:
#     if item[0] == 1:
#         if item[1] < minM:
#             minM = item[1]
#         if item[1] > maxM:
#             maxM = item[1]
#         meanM += item[1]
#     else:
#         if item[1] < minF:
#             minF = item[1]
#         if item[1] > maxF:
#             maxF = item[1]
#         meanF += item[1]

# row_count = sum(1 for item in f)

# row_countM = sum(1 for item in f if item[0] == 1)
# meanM /= row_countM

# row_countF = row_count - row_countM
# meanF /= row_countF

# print(f"Male: Min: {minM}\nMax: {maxM}\nMean: {meanM}")
# print(f"Femmale: Min: {minF}\nMax: {maxF}\nMean: {meanF}")