from PyQt6 import QtWidgets, QtCore
import pyqtgraph as pg
import sys
import time
from echo_client_cpu_class import *


class Widget(QtWidgets.QWidget):

    def __init__(self, interval=2.0, timewindow=50):
        """ interval,timewindow:seconds"""
        super(Widget, self).__init__()
        self._interval = interval
        self._timewindow = timewindow

        self.button = QtWidgets.QPushButton(
            text="Monitoring Off, Press the Button to Start",
            checkable=True)
        self.button.clicked.connect(self.monitoring)

        vlay = QtWidgets.QVBoxLayout(self)  # vertically arranged widgets
        vlay.addWidget(self.button)

        self.graphWidget = pg.PlotWidget()

        # Add Background colour to white
        self.graphWidget.setBackground('w')
        # Add Title
        self.graphWidget.setTitle(
            "The Live Data of CPU Utilization as a Percentage ", color="b", size="15pt")
        # Add Axis Labels
        styles = {"color": "black", "font-size": "15px"}
        self.graphWidget.setLabel("left", "CPU(%)", **styles)

        axis = pg.DateAxisItem(orientation='bottom')
        self.graphWidget.setAxisItems({"bottom": axis})
        self.graphWidget.setLabel(
            "bottom", f"Time (interval:{self._interval}s timewindow:{self._timewindow}s)", **styles)

        # Add legend
        self.graphWidget.addLegend()
        # Add grid
        self.graphWidget.showGrid(x=True, y=True)

        vlay.addWidget(self.graphWidget)

        self.i = 0
        curtime = time.time()
        self.graphWidget.setXRange(
            curtime, curtime+self._timewindow, padding=0)

        self.x = []
        self.cpu = []
        self.data_line = self.plot([], [], "CPU(%)", 'b')

        self.timer = QtCore.QTimer()
        self.timer.setInterval(int(self._interval*1000))
        self.timer.timeout.connect(self.update_plot_data)
        self.monitoring_on = False
        # client
        self.client = clientcpu(host="localhost", port=5000)
        self.client.connect()
        self.setWindowTitle(f'CPU Utilization as a Percentage (Server Host: {self.client.host} Port: {self.client.port})')


    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        return self.graphWidget.plot(x, y, name=plotname, pen=pen,
                                     symbol='o', symbolSize=5, symbolBrush=(color))

    def update_plot_data(self):
        cpu_percent = self.client.receive_data()
        if (self.i == 0.0):
            curtime = time.time()
            self.graphWidget.setXRange(
                    curtime, curtime+self._timewindow, padding=0)

        if self.i < self._timewindow:
            self.x.append(time.time())  # Add a new value
            self.cpu.append(cpu_percent)  # Add a new value.
            self.i += self._interval
        else:
            # Once enough data is captured, append the newest data point and delete the oldest
            curtime = time.time()
            self.x.append(curtime)  # Add a new value
            self.cpu.append(cpu_percent)
            del self.x[0]
            del self.cpu[0]
            self.graphWidget.setXRange(
                    curtime-self._timewindow, curtime, padding=0)

        self.data_line.setData(self.x, self.cpu)  # Update the data.

    def monitoring(self):
        if self.monitoring_on == False:
            self.timer.start()
            self.monitoring_on = True
            self.button.setText("Monitoring On, Press the Button to Stop")
        else:
            self.timer.stop()
            self.monitoring_on = False
            self.button.setText("Monitoring Off, Press the Button to Start")

    def closeEvent(self, event):
        self.client.disconnect()
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Widget(interval=0.5, timewindow=25.0)
    w.show()
    sys.exit(app.exec())
