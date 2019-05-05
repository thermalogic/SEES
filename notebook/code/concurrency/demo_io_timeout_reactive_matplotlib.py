from rx import Observable
import numpy as np
import matplotlib.pyplot as plt
import time
import sys  
sys.path.append('./code/concurrency/')  
from io_timeout import get_data_with_timeout

intervalTime=100
delay=1
tag="CPU_PERCENT"
cpu_data = (Observable
            .interval(intervalTime) 
            .map(lambda rc,value: get_data_with_timeout(delay,tag))
            .publish())

cpu_data.connect()

def monitor_cpu(npoints):
    plt.figure()
    plt.title("The Simple CPU Percent Monitor")
    lines, = plt.plot([], [],"b-o")
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

    cpu_data_window = cpu_data.buffer_with_count(npoints, 1)
    
    def update_plot(cpu_readings):
        lines.set_xdata(np.arange(len(cpu_readings)))
        lines.set_ydata(np.array(cpu_readings)[:,1])
        str_curtime=time.strftime("%F %H:%M:%S", time.localtime(time.time()))  
        
        #if np.array(cpu_readings)[-1,1] is None: 
         #   str_cursecond=str_cursecond+" (Timeout)"
        
        time_text.set_text("Time:"+str_curtime)
        
        table_vals = [[tag,"%",str(np.array(cpu_readings)[:,1][-1])]]
        tbl = plt.table(cellText=table_vals,
               colLabels=col_labels,
               colWidths=[0.2] * 3,
               cellLoc='center',
               loc='best')
         
        plt.draw()
    
    cpu_data_window.subscribe(update_plot)
    plt.show()

if __name__ == '__main__':
    monitor_cpu(10)
