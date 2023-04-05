import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Block import Block
from Track import Track
from Train import Train
from TrainController import TrainController
from signals import signals


class TrainModelUI(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("trainModel_fullsys.ui", self)

        signals.trainModelUpdateGUISpeed.connect(self.displaySpeed)
        signals.trainModelGUIBlock.connect(self.displayBlock)
        signals.trainModelGUIcommandedSpeed.connect(self.displayCommSpeed)
        signals.trainModelGUIpower.connect(self.displayPower)

    def displaySpeed(self, train):
        self.actSpeed.setText("Speed: {0} mi/h".format(train)) #actSpeed is the qt creator object
    
    def displayBlock(self, train):
        self.commSpeedLabel.setText("Current Block = {0}".format(train)) #actSpeed is the qt creator object
        
    def displayCommSpeed(self, train):
        self.currBlockLabel.setText("Commanded Speed = {0}".format(train)) #actSpeed is the qt creator object
    
    def displayPower(self,train):
        self.powLabel.setText("Power Input: {0} Watts".format(train))
        self.powProgressBar.setMinimum(0)
        self.powProgressBar.setMaximum(120001)
        self.powProgressBar.setTextVisible(0)
        
#app = QtWidgets.QApplication(sys.argv)
#window = MainWindow()
#window.show()
#app.exec()