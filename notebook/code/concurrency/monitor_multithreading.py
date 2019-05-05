from threading import Thread, Timer
from queue import Queue
import time
from collections import deque
import matplotlib.pyplot as plt
import numpy as np
import psutil

def GetTagData(tag):
    time.sleep(2)
    tagfuncs={"CPU_PERCENT": psutil.cpu_percent(),
               "MEM_PERCENT": psutil.virtual_memory().percent,
               "BAT_PERCENT": psutil.sensors_battery().percent} 
    try:              
        value= tagfuncs[tag]
        rc=1    
    except Exception as msg:
        rc,value=0,None  
    return (rc,value)  

def PeriodDataProducer(delay,tag,out_q):
    rc, value =  GetTagData(tag)
    if rc == 1:
        out_q.put((rc, value))
    else:
        out_q.put((rc, value))
    t = Timer(delay, PeriodDataProducer, (delay, tag,out_q))
    t.start()


def DataConsumerPlot(in_q,npoints):
    y = deque()
    plt.figure()
    plt.title("The Simple CPU Percent Monitor")
    lines, = plt.plot([], [], "b-o")
    time_text = plt.text(0.5, 80, "")
    plt.xlim(0, npoints-1)
    plt.ylim(0, 100)
    
    columns = ()
    col_labels = ['Tag', 'Unit', 'Value']
    table_vals = [[tag,"%",""]]
    tbl = plt.table(cellText=table_vals,
               colLabels=col_labels,
               colWidths=[0.2] * 3,
               cellLoc='center',
               loc='best')

    def DataConsumer(in_q,npoints):
        while True:
            rcvalue = in_q.get()
            if len(y) < npoints:
                y.append(rcvalue[1])
            else:
                y.popleft()
                y.append(rcvalue[1])

            lines.set_xdata(np.arange(len(y)))
            lines.set_ydata(np.array(y))
            str_curtime=time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))   
            time_text.set_text("Time:"+str_curtime)
            
            table_vals = [[tag,"%",str(np.array(y)[-1])]]
            tbl = plt.table(cellText=table_vals,
                  colLabels=col_labels,
                  colWidths=[0.2] * 3,
                  cellLoc='center',
                  loc='best')
        
            plt.draw()

    c = Thread(target=DataConsumer, args=(in_q,npoints))
    c.start()
    plt.show()


if __name__ == '__main__':
    q = Queue()
    delay = 3
    tag="CPU_PERCENT"
    p = PeriodDataProducer(delay,tag, q)
    npoints = 10
    DataConsumerPlot(q,npoints)
    q.join()
