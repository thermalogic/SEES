from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import sys
import psutil
import time 

class Widget(QtWidgets.QWidget):

    def __init__(self, interval=2.0, timewindow=50):
        """ interval,timewindow:seconds"""
        super(Widget, self).__init__()
        self._interval =interval
        self._timewindow = timewindow
   
        self.setWindowTitle('CPU Utilization as a Percentage')
        self.button = QtWidgets.QPushButton(
            text="Monitoring Off, Press the Button to Start",
            checkable=True)
        self.button.clicked.connect(self.monitoring)

        lay = QtWidgets.QVBoxLayout(self)
        hlay = QtWidgets.QHBoxLayout()
        lay.addLayout(hlay)
        lay.addWidget(self.button)

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

        lay.addWidget(self.graphWidget)

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

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        return self.graphWidget.plot(x, y, name=plotname, pen=pen,
                                     symbol='o', symbolSize=5, symbolBrush=(color))

    def update_plot_data(self):
        cpu_percent = psutil.cpu_percent()
        if (self.i==0.0):
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
            self.button.setText("Monitoring Off, Press the Button Start")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Widget(interval=0.5, timewindow=25.0)
    w.show()
    sys.exit(app.exec_())
