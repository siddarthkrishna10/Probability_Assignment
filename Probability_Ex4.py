import math
import pandas as pd
import numpy as np
from numpy import genfromtxt

#Here I've edited your dataset a little; changing the X and Y cells to their respective digits
#to calculate the Expectation of Z in a faster and simpler way. The edited sheet is in the git repo
df = genfromtxt('https://github.com/siddarthkrishna10/Probability_Assignment/blob/master/datasets/dsa_proba_data1.csv',
                delimiter=',')
Ez = 0

for i in range(1,7):
    for j in range(1,10):
        Ez += df[i][0] * df[0][j] * df[i][j]

path = "https://github.com/siddarthkrishna10/Probability_Assignment/blob/master/datasets/dsa_proba_data.xlsx"
df1 = pd.read_excel(path)
df_ar = np.array(df1)
elements = df_ar[0:, 1:]

a = [0, 1, 2, 3, 4, 5, 6, 7, 8]

x = np.array([[0]*9, [1]*9, [2]*9, [3]*9, [4]*9, [5]*9])
y = np.array([a, a, a, a, a, a])

Ex = np.multiply(x, elements)
Ey = np.multiply(y, elements)

x1 = np.sum(Ex)
y1 = np.sum(Ey)

#Excercie 4.1
print("E(X) = ", round(x1, 2),", E(Y) = ", round(y1, 2))
print("Expectation: E(Z) = ", round(Ez, 2))

xs = np.subtract(x, x1)
ys = np.subtract(y, y1)

xs = np.square(xs)
ys = np.square(ys)

Ex1 = np.multiply(xs, elements)
Ey1 = np.multiply(ys, elements)

vx = np.sum(Ex1)
vy = np.sum(Ey1)

#Excercie 4.2
cov = Ez - x1*y1
print("Covariance: Cov(Z) = ", round(vx, 3), ",", round(cov, 3), ",",
      round(cov, 3), ",", round(vy, 3))

#Excercie 4.3
corr = cov/(math.sqrt(vx)*math.sqrt(vy))
print("Correlation: Corr(Z) = ", round(corr, 3))
print("Since the correlation value isn't zero, X and Y aren't independent")

alpha = cov/vx
beta = y1 - (alpha*x1)

#Excercie 4.4
print("Alpha = ", round(alpha, 3), ", Beta = ", round(beta, 3))
