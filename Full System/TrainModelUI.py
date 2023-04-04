import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Block import Block
from Track import Track
from Train import Train
from TrainController import TrainController
from signals import signals
from trainModel_fullsys import MainWindow

class TrainModelUI(QObject, MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setUp(self)

        signals.SIGNALNAME.connect(self.displayPower)
        signals.actSpeedtoTrainModelUI.connect(self.displaySpeed)
        
    def displayPower(self):
        self.powLabel.setText("Power Input: {0} Watts".format(SIGNALNAME))

    def displaySpeed(self):
        self.actSpeed.setText("Power Input: {0} Watts".format(signals.actSpeedtoTrainModelUI)) #actSpeed is the qt creator object
        
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()