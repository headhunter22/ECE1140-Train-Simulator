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

        #Connecting the received signals to their display functions
        signals.trainModelUpdateGUISpeed.connect(self.displaySpeed)
        signals.trainModelGUIBlock.connect(self.displayBlock)
        signals.trainModelGUIcommandedSpeed.connect(self.displayCommSpeed)
        signals.trainModelGUIpower.connect(self.displayPower)

    def displaySpeed(self, train):
        speedMpH = float(train)*2.237
        self.actSpeed.setText("Speed: {0} mi/h".format(speedMpH)) #actSpeed is the qt creator object
    
    def displayBlock(self, train):
        self.commSpeedLabel.setText("Current Block = {0}".format(train)) #commSpeedLabel is the qt creator object
        
    def displayCommSpeed(self, train):
        commSpeedMpH = float(train)*.621
        self.currBlockLabel.setText("Commanded Speed = {0} mi/h".format(commSpeedMpH)) #currBlockLabel is the qt creator object
        self.speedLimitLabel.setText("Speed Limit = {0} mi/h".format(commSpeedMpH)) #speedLimitLabel is the qt creator object
    
    def displayPower(self,train):
        self.powLabel.setText("Power Input: {0} Watts".format(train))
        self.powProgressBar.setMinimum(0)
        self.powProgressBar.setMaximum(120001)
        self.powProgressBar.setTextVisible(0)
        roundTrain = round(float(train))
        self.powProgressBar.setValue(int(roundTrain))
