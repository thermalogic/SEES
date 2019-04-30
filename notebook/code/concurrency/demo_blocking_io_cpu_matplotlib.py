import time
from collections import deque
import matplotlib.pyplot as plt
import numpy as np
import psutil
from matplotlib.animation import FuncAnimation

def get_data():
    #time.sleep(2)
    time.sleep(0.1)
    return psutil.cpu_percent()

def cpu_monitor_sync():
    """ blocking I/O call"""
    return get_data()

fig, ax = plt.subplots()
ln, = plt.plot([], [], 'b-o')
str_cursecond=str(time.localtime(time.time()).tm_sec)   
time_text = ax.text(1, 40, "")

y = deque()

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(1, 100)
    return ln,

def update(frames):
    value = cpu_monitor_sync()
    if len(y) < 10:
        y.append(value)
    else:
        y.popleft()
        y.append(value)

    str_cursecond=str(time.localtime(time.time()).tm_sec)   
    time_text.set_text("cursecond:"+str_cursecond)

    ln.set_xdata(np.arange(len(y)))
    ln.set_ydata(np.array(y))
    return ln,time_text

ani = FuncAnimation(fig, update,init_func=init, blit=True,interval=1000)
plt.show()
