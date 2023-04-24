import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')


x_data = []
y_data = []
x_index = count()

def animate(i):
    x_data.append(next(x_index))
    y_data.append(random.randint(0, 6))

    plt.cla() # Clears the graph
    plt.plot(x_data, y_data, linewidth=1, marker='^') # Plots the graph with the newly updated data.

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()