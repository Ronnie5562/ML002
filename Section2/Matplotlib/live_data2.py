import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")


def animate(i):
    data = pd.read_csv("live_data.csv")
    x_data = list(data["x_data"])
    Team_1 = list(data["Team_1"])
    Team_2 = list(data["Team_2"])

    plt.cla()
    plt.plot(x_data, Team_1, linewidth=1, label="Team 1")
    plt.plot(x_data, Team_2, linewidth=1, label="Team 2")
    plt.legend(loc="upper left")


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
