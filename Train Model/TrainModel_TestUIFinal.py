import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from PyQt6 import uic
from PyQt6.QtCore import QSize
import TrackParser
from pathlib import Path
import os
import time
from TrainModel import MainWindow


trainArray = []
track = TrackParser.parseTrack('Track Layout.csv')

class MainWindowTestUI(QtWidgets.QMainWindow):

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("TrainModelTestUI_v2.ui", self)
        self.setWindowTitle('Train Model Test UI')
        #window.trainBox.addItem("Train 0") 
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

        #adding a train schedule function
        self.loadTrainSchedule.clicked.connect(self.trainScheduleFunc)

        #Adding train to map 
        self.addTrain.clicked.connect(self.addingTrainFunc)

        #when the current block is changed
        self.currentBlock.currentIndexChanged.connect(self.changedCurrentBlock)

        #when the time is changed
        self.dateBox.dateTimeChanged.connect(self.dateTimeFunc)

    def trainScheduleFunc(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self,'Open file', home_dir)
        file_name = os.path.basename(fname[0])
        window.currentFile.setText("Current Schedule: {0}.csv".format(os.path.splitext(file_name)[0]))
        if fname[0]:
             f = open(fname[0], 'r')
             with f:
                  data = f.read()

        track = TrackParser.parseTrack(file_name)
        return track

    #temp set function
    def tempInputfunc(self):
        inputTemp = self.inputTemp.text()
        if int(inputTemp) > 90 or int(inputTemp)<60:
            return
        window.tempLabel.setText("Internal Temp: {0} degrees F".format(inputTemp))
        window.ACprogressBar.setMinimum(60)
        window.ACprogressBar.setMaximum(90)
        window.ACprogressBar.setTextVisible(0)
        window.ACprogressBar.setValue(int(inputTemp))
    
    #power set function
    def powInputfunc(self):
        inputPow = self.inputPow.text()
        window.powLabel.setText("Power Input: {0} Watts".format(inputPow))
        window.powProgressBar.setMinimum(0)
        window.powProgressBar.setMaximum(10000)
        window.powProgressBar.setTextVisible(0)
        window.powProgressBar.setValue(int(inputPow))

    #commanded speed function
    def commSpeedInputfunc(self):
        inputCommSpeed = self.commSpeed.text()
        window.commSpeedLabel.setText("Commanded Speed: {0} mph".format(inputCommSpeed))

    #changing box 
    def clickBox(self):

        #internal lights
        if self.intLights.isChecked():
                window.intLightLabel.setStyleSheet("background-color: green")
                window.intLightLabel.setText("ON")
        else:
            window.intLightLabel.setStyleSheet("background-color: red")
            window.intLightLabel.setText("OFF")

        #external lights
        if self.extLights.isChecked():
                window.extLightLabel.setStyleSheet("background-color: green")
                window.extLightLabel.setText("ON")
        else:
            window.extLightLabel.setStyleSheet("background-color: red")
            window.extLightLabel.setText("OFF")

        #headlights
        if self.headlights.isChecked():
                window.headlightLabel.setStyleSheet("background-color: green")
                window.headlightLabel.setText("ON")
        else:
            window.headlightLabel.setStyleSheet("background-color: red")
            window.headlightLabel.setText("OFF")

        #Left doors
        if self.leftDoor.isChecked():
                window.lDoorLabel.setStyleSheet("background-color: green")
                window.lDoorLabel.setText("OPEN")
        else:
            window.lDoorLabel.setStyleSheet("background-color: red")
            window.lDoorLabel.setText("CLOSED")

        #Right doors
        if self.rightDoor.isChecked():
                window.rDoorLabel.setStyleSheet("background-color: green")
                window.rDoorLabel.setText("OPEN")
        else:
            window.rDoorLabel.setStyleSheet("background-color: red")
            window.rDoorLabel.setText("CLOSED")

        #Signal Fault
        if self.sigFault.isChecked():
                sigIcon = QtGui.QIcon("sigON.png")
                window.sigFaultLabel.setIcon(sigIcon)
                window.sigFaultLabel.setIconSize(QSize(50, 50))
        else:
            sigIcon = QtGui.QIcon("sigOFF.png")
            window.sigFaultLabel.setIcon(sigIcon)
            window.sigFaultLabel.setIconSize(QSize(50, 50))
        #power Fault
        if self.powFault.isChecked():
                powIcon = QtGui.QIcon("powON.png")
                window.powFaultLabel.setIcon(powIcon)
                window.powFaultLabel.setIconSize(QSize(50, 50))
        else:
            powIcon = QtGui.QIcon("powOFF.png")
            window.powFaultLabel.setIcon(powIcon)
            window.powFaultLabel.setIconSize(QSize(50, 50))
        #brake Fault
        if self.brakeFault.isChecked():
                brakeIcon = QtGui.QIcon("brakesON.png")
                window.brakeFaultLabel.setIcon(brakeIcon)
                window.brakeFaultLabel.setIconSize(QSize(50, 50))
        else:   
            brakeIcon = QtGui.QIcon("brakesOFF.png")
            window.brakeFaultLabel.setIcon(brakeIcon)
            window.brakeFaultLabel.setIconSize(QSize(50, 50))

        #AC Fault
        if self.AC.isChecked():
                ACIm = QtGui.QIcon("ACON.png")
                window.ACIcon.setIcon(ACIm)
                window.ACIcon.setIconSize(QSize(50, 50))
        else:
            ACIm = QtGui.QIcon("ACOFF.png")
            window.ACIcon.setIcon(ACIm)
            window.ACIcon.setIconSize(QSize(50, 50))
    
    def addingTrainFunc(self):
        numTrains = window.trainBox.count()
        window.trainBox.addItem("Train {0}".format(numTrains))
        newTrain = Train
        trainArray.append(newTrain)  
    
    def changedCurrentBlock(self):
         if self.currentBlock.currentText() == "":
            return
         currentBlockVal = self.currentBlock.currentIndex()
         blockVal = int(currentBlockVal) + 1
         window.currBlockLabel.setText("Current Block:  {0}".format(str(blockVal)))
         speedVar = track.getLine('Red').getBlock(str(blockVal)).speedLimit
         window.speedLimitLabel.setText("Speed Limit: {0}".format(speedVar))

    def dateTimeFunc(self):
        dateTime = self.dateBox.dateTime()
        dateTime_str = dateTime.toString(self.dateBox.displayFormat())
        window.dateLabel.setText(dateTime_str) 

class Train(MainWindow):
    pass    

#end Train class window
  
#end test UI definition

#defining the app and the window
app = QtWidgets.QApplication(sys.argv)

firstTrain = MainWindow()
testUI = MainWindowTestUI()
trainArray.append(firstTrain)

window = firstTrain
