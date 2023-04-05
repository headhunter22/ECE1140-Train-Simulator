import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Block import Block
from Track import Track
from Train import Train
from TrainController import TrainController
from signals import signals


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("trainModel_fullsys.ui", self)

        signals.trainModelUpdateGUISpeed.connect(self.displaySpeed)


    def displaySpeed(self, train):
        self.actSpeed.setText("Speed: {0} mi/h".format(train)) #actSpeed is the qt creator object
        
#app = QtWidgets.QApplication(sys.argv)
#window = MainWindow()
#window.show()
#app.exec()