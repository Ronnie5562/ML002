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

"""_summary_
The line of code ani = FuncAnimation(plt.gcf(), animate, interval=1000) creates a FuncAnimation object and assigns it to the variable ani. The FuncAnimation object is responsible for animating the plot by repeatedly calling the animate function.

Once you create the ani object, you don't need to call it explicitly. The FuncAnimation object runs automatically in the background, updating the plot every interval milliseconds.

To stop the animation, you can call the ani.event_source.stop() method. This method stops the animation by stopping the event source that is responsible for calling the animate function. You can also start the animation again by calling ani.event_source.start().

Alternatively, you can use the plt.show() function to display the plot window and start the animation. This function runs the event loop that is responsible for calling the animate function, and keeps the plot window open until you close it manually.

So in summary, you don't need to call ani explicitly after initializing it. The FuncAnimation object runs automatically in the background and updates the plot every interval milliseconds. You can stop the animation by calling ani.event_source.stop() or start it by calling ani.event_source.start(). Alternatively, you can use plt.show() to display the plot window and start the animation.
"""