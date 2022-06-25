from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import sys
import psutil


class Widget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setWindowTitle('CPU Percent Monitor')
        self.button = QtWidgets.QPushButton(
            text="Press the Button to Start",
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
        self.graphWidget.setTitle("CPU Percent Live Data", color="b", size="15pt")
        # Add Axis Labels
        styles = {"color": "black", "font-size": "15px"}
        self.graphWidget.setLabel("left", "CPU(%)", **styles)
        self.graphWidget.setLabel("bottom", "Index", **styles)
        # Add legend
        self.graphWidget.addLegend()
        # Add grid
        self.graphWidget.showGrid(x=True, y=True)

        lay.addWidget(self.graphWidget)

        self.i = 0
        self.plt_length = 50

        self.graphWidget.setXRange(0, self.plt_length-1, padding=0)
        # self.graphWidget.setYRange(0, 100, padding=0)

        self.x = []
        self.cpu = []
        self.data_line = self.plot([], [], "CPU(%)", 'b')

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot_data)
        self.monitoring_on = False

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        return self.graphWidget.plot(x, y, name=plotname, pen=pen,
                                     symbol='+', symbolSize=5, symbolBrush=(color))

    def update_plot_data(self):
        cpu_percent = psutil.cpu_percent()
        if self.i < self.plt_length:
            self.x.append(self.i)  # Add a new value
            self.cpu.append(cpu_percent)  # Add a new value.
            self.i += 1
        else:
            # Once enough data is captured, append the newest data point and delete the oldest
            self.cpu.append(cpu_percent)
            del self.cpu[0]
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
    w = Widget()
    w.show()
    sys.exit(app.exec_())
