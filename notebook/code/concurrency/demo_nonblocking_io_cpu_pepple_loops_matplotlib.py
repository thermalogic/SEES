from queue import Queue
from threading import Thread, Timer
import time
from collections import deque
import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append('./code/concurrency/')

from nonblocking_io_cpu_pepple import get_data_with_timeout


def PeriodDataProducer(delay,out_q):
    rc, value = get_data_with_timeout(delay)
    if rc == 1:
        out_q.put((rc, value))
    else:
        out_q.put((rc, value))

    t = Timer(delay, PeriodDataProducer, (delay, out_q))
    t.start()


def DataConsumerPlot(in_q,npoints):
    y = deque()
    plt.figure()
    plt.title("The Simplest CPU Percent Monitor")
    lines, = plt.plot([], [], "b-o")
    time_text = plt.text(0.5, 80, "")
    plt.xlim(0, npoints-1)
    plt.ylim(0, 100)

    def DataConsumer(in_q):
        while True:
            rcvalue = in_q.get()
            if len(y) < 10:
                y.append(rcvalue[1])
            else:
                y.popleft()
                y.append(rcvalue[1])

            lines.set_xdata(np.arange(len(y)))
            lines.set_ydata(np.array(y))
            str_curtime=time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))   
            if rcvalue[1] is None:
                str_cursecond=str_cursecond+" (Timeout)"
            time_text.set_text("Time:"+str_curtime)
            plt.draw()

    c = Thread(target=DataConsumer, args=(in_q,))
    c.start()
    plt.show()


if __name__ == '__main__':
    q = Queue()
    delay = 1
    p = PeriodDataProducer(delay, q)
    npoints = 10
    DataConsumerPlot(q,npoints)
    q.join()
