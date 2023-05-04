"""_summary_
In this module, I learnt 
       _ _        __  
m(slope) = __(X.Y)__-__(XY)__   <== The formular
       (X)^2 - X^2
                 _    _
b(y-intercept) = y - mx
"""
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean
import numpy as np
style.use("fivethirtyeight")

X_axis = np.array([1, 2, 3, 4, 5, 6, 7], dtype=np.float64)
Y_axis = np.array([5, 4, 6, 5, 6, 7, 8], dtype=np.float64)

def best_fit_slope(X, Y):
    m = (
        ((mean(X) * mean(Y)) - (mean(X * Y)))/
        ((mean(X)**2) - (mean(X**2)))
    )
    return m

def y_intercept(X, Y, M):
    b = (mean(Y) - (M * mean(X)))
    return b


Slope = best_fit_slope(X_axis, Y_axis)
Y_intercept = y_intercept(X_axis, Y_axis, Slope)

regression_line = [((Slope * X) + Y_intercept) for X in X_axis]
print(regression_line)

plt.scatter(X_axis, Y_axis, marker='X', color='#003F72', label='data')
plt.plot(X_axis, regression_line, label='regression line')
plt.legend(title='LEGEND')
plt.tight_layout()
plt.show()