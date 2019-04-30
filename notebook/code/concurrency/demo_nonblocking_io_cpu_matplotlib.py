import time
from collections import deque
import matplotlib.pyplot as plt
import numpy as np
import psutil
from matplotlib.animation import FuncAnimation

import sys  
sys.path.append('./code/concurrency/')  
from nonblocking_io_cpu import get_data_with_timeout

fig, ax = plt.subplots()
ln, = plt.plot([], [], 'b-o')
str_cursecond=str(time.localtime(time.time()).tm_sec)   
time_text = ax.text(0.5, 80, "")

y = deque()

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(1, 100)
    return ln,

def update(frames):
    rc,value = get_data_with_timeout(3)
    if len(y) < 10:
        y.append(value)
    else:
        y.popleft()
        y.append(value)
    str_curtime=time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))  
    if value is None:
        str_cursecond=str_cursecond+" (Timeout)"
    time_text.set_text("Time:"+str_curtime)

    ln.set_xdata(np.arange(len(y)))
    ln.set_ydata(np.array(y))
    return ln,time_text

ani = FuncAnimation(fig, update,init_func=init, blit=True,interval=1000)
plt.show()
