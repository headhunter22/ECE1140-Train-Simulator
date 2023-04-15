import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from PyQt6 import uic
from PyQt6.QtCore import QSize
import TrackParser
from pathlib import Path
import os
import time

class MainWindowTestUI(QtWidgets.QMainWindow):

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("TrainModelTestUI_v2.ui", self)
        self.setWindowTitle('Train Model Test UI')
        self.currentBlock.setCurrentIndex(0)      
        
        #temperature set
        self.tempButton.clicked.connect(self.tempInputfunc)
        #power set 
        self.powButton.clicked.connect(self.powInputfunc)
        #commanded speed 
        self.commSpeedButton.clicked.connect(self.commSpeedInputfunc)

        #light status change
        self.intLights.stateChanged.connect(self.clickBox)
        self.extLights.stateChanged.connect(self.clickBox)
        self.headlights.stateChanged.connect(self.clickBox)
        self.leftDoor.stateChanged.connect(self.clickBox)
        self.rightDoor.stateChanged.connect(self.clickBox)
        
        self.sigFault.stateChanged.connect(self.clickBox)
        self.powFault.stateChanged.connect(self.clickBox)
        self.brakeFault.stateChanged.connect(self.clickBox)
        self.AC.stateChanged.connect(self.clickBox)

        #Adding train to map 
        self.addTrain.clicked.connect(self.addingTrainFunc)

        #when the current block is changed
        self.currentBlock.currentIndexChanged.connect(self.changedCurrentBlock)

        #when the time is changed
        self.dateBox.dateTimeChanged.connect(self.dateTimeFunc)

    #temp set function
    def tempInputfunc(self):
        print("tempInputfunc")

    #power set function
    def powInputfunc(self):
        print("powInputfunc")

    #commanded speed function
    def commSpeedInputfunc(self):
        print("commSpeedInputfunc")

    #changing box 
    def clickBox(self):
        print("clickbox")

    def addingTrainFunc(self):
        print("tempInputfunc")
    
    def changedCurrentBlock(self):
        print("changedCurrentBlock")

    def dateTimeFunc(self):
        print("dateTimeFunc")

  
#end test UI definition
