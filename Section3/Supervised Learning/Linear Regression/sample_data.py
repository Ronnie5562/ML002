"""_summary_
In this module, I wrote a program to generate a random but confined dataset in order for me to visualize how linear regression works. Sounds cool right 😵‍💫😵‍💫??
from staryboys⭐⭐ import Ronald⭐⭐
"""

import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean
import numpy as np
import random

style.use("ggplot")

def create_dataset(how_many_dset, variance, step=2, correlation=False):
    """_summary_

    Args:
        how_many_dset (_type_): _description_: How many datapoints should we have?.
        variance (_type_): _description_: How wide should be the range of the dataset.
        step (int, optional): _description_. Defaults to 2.
        correlation (bool, string, optional): _description_: Determines the kind of regression graph we get depending on the input: 'Positive' or 'Negative' respectively. Defaults to False (if left as false, the graph will have no correlation at all)
    """
    y_init_value = 1
    Y_axis = []
    for x in range(how_many_dset):
        y_value = y_init_value + random.randrange(-variance, variance)
        Y_axis.append(y_value)

        # To control the kind of regression we get:
        if correlation and correlation == 'Positive':
            y_init_value += step
        elif correlation and correlation == 'Negative':
            y_init_value -= step
    
    X_axis = [x for x in range(len(Y_axis))]
    return [np.array(X_axis, dtype=np.float64), np.array(Y_axis, dtype=np.float64)]

def best_fit_slope(x_axis, y_axis):
    slope = (
        ((mean(x_axis) * mean(y_axis)) - (mean(x_axis * y_axis)))/
        ((mean(x_axis)**2) - (mean(x_axis**2)))
    )
    return slope


plt.plot()


def y_intercept(x_axis, y_axis, slope):
    """_summary_
    This function implements the straight line graph equation ==> b = y - mx from y = mx + b

    where m = slope
          x = value of x
          b = y_intercept

    """
    b = (mean(y_axis) - (slope * mean(x_axis)))
    return b


def regression_line(y_intercept, x_axis, slope):
    """_summary_
    The regression line is basically a list of all the ys we get each time we input an x in this formular ==>  y = mx + b

    where m = slope
          x = value of x
          b = y_intercept

    """
    ys = [((slope * x) + y_intercept) for x in x_axis]
    return ys



X_axis, Y_axis = create_dataset(20, 5, correlation='Positive')
Slope = best_fit_slope(X_axis, Y_axis)
Y_intercept = y_intercept(X_axis, Y_axis, Slope)
Regression_line = regression_line(Y_intercept, X_axis, Slope)


plt.scatter(X_axis, Y_axis, label="Data points")
plt.plot(X_axis, Regression_line, label="Reg line", linewidth=1, color="#5555FF")
plt.legend(title="LEGEND", loc="upper left")
plt.show()
# print(X_axis)
# print(Y_axis)