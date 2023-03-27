from PyQt6 import QtCore, QtWidgets, uic
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("ClockTest.ui", self)
        self.setWindowTitle('Track Model UI')

        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.stop)

        self.clock = QtCore.QTimer()
        self.time = 0
        self.started = False

    def start(self):
        print('Start Timer')

        self.clock.start(1000)
        self.clock.setInterval(1000)

        self.clock.timeout.connect(self.changeLabel)

    def stop(self):
        print('Stop Timer')
        self.clock.stop()
    
    def changeLabel(self):
        self.time += 1

        hrs = self.time / 3600
        mins = (hrs - int(hrs)) * 60
        secs = (mins - int(mins)) * 60

        self.label.setText(f'{int(hrs):02d}' + ':' + f'{int(mins):02d}' + ':' + f'{int(secs):02d}')

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()