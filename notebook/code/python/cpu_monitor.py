import psutil
from time import sleep, strftime
import matplotlib.pyplot as plt

pltLength = 100
x = [i for i in range(pltLength)]
y = [None for i in range(pltLength)]
i = 0

plt.ion()

def write_cpu(cpu):
    with open("cpu.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(cpu)))

def graph(cpu):
    global i
    if i < pltLength:
        y[i] = cpu
        i += 1
    else:
        # Once enough data is captured, append the newest data point and delete the oldest
        y.append(cpu)
        del y[0]

    plt.clf()
    plt.xlim(0, pltLength)
    plt.plot(x, y, "b-o")
    plt.draw()
    plt.pause(0.1)


while True:
    cpu = psutil.cpu_percent()
    write_cpu(cpu)
    graph(cpu)
    sleep(1)
