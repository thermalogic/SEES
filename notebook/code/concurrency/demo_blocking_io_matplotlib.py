import time
from collections import deque
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import psutil

def virtual_interface_data(tag):
    # time.sleep(0.1)
    tagfuncs={"CPU_PERCENT": psutil.cpu_percent(),
               "MEM_PERCENT": psutil.virtual_memory().percent,
               "BAT_PERCENT": psutil.sensors_battery().percent} 
    try:              
        value= tagfuncs[tag]
        rc=1    
    except:
        rc,value=0,None  
    return (rc,value)        
            
tag="CPU_PERCENT"
y = deque()

columns = ()
col_labels = ['Tag', 'Unit', 'Value']
table_vals = [[tag,"%",""]]


fig, ax = plt.subplots()
ax.set_title("The Simple Monitor:"+tag)
ln, = plt.plot([], [], 'b-o')
str_cursecond=str(time.localtime(time.time()).tm_sec)   
time_text = ax.text(0.5, 80, "")

tbl = ax.table(cellText=table_vals,
               colLabels=col_labels,
               colWidths=[0.2] * 3,
               cellLoc='center',
               loc='best')

def init():
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 100)
    return ln,

def update(frames):
    rc,value = virtual_interface_data(tag)
    if len(y) < 10:
        y.append(value)
    else:
        y.popleft()
        y.append(value)

    str_curtime=time.strftime("%F %H:%M:%S", time.localtime(time.time()))
    time_text.set_text("Time:"+str_curtime)
    
    table_vals = [[tag,"%",str(value)]]
    tbl = ax.table(cellText=table_vals,
               colLabels=col_labels,
               colWidths=[0.2] *3,
               cellLoc='center',
               loc='best')

    ln.set_xdata(np.arange(len(y)))
    ln.set_ydata(np.array(y))
    return ln,time_text, tbl

ani = FuncAnimation(fig, update,init_func=init, blit=True,interval=1000)
plt.show()
