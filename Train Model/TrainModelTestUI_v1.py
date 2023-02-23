import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QSize
import TrackParser


trainArray = []
track = TrackParser.parseTrack('Track Layout.csv')

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("TrainModelTestUI_v1.ui", self)
        self.setWindowTitle('Train Model Test UI')
        self.trainBox.addItem("Train 0")  
        self.currentBlockLabel.setStyleSheet('background-color: black')      

        
        #Setting the current line
        self.greenClickedButton.clicked.connect(self.greenclickedButton)
        self.redClickedButton.clicked.connect(self.redclickedButton)

       
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

        
        #Fault/AC icon init
        sigIcon = QtGui.QIcon("sigOFF.png")
        powIcon = QtGui.QIcon("powOFF.png")
        brakeIcon = QtGui.QIcon("brakesOFF.png")
        ACIm =  QtGui.QIcon("ACOFF.png")
      
        self.sigFaultLabel.setIcon(sigIcon)
        self.sigFaultLabel.setIconSize(QSize(50, 50))
        self.powFaultLabel.setIcon(powIcon)
        self.powFaultLabel.setIconSize(QSize(50, 50))
        self.brakeFaultLabel.setIcon(brakeIcon)
        self.brakeFaultLabel.setIconSize(QSize(50, 50))
        self.ACIcon.setIcon(ACIm)
        self.ACIcon.setIconSize(QSize(50, 50))

        self.sigFault.stateChanged.connect(self.clickBox)
        self.powFault.stateChanged.connect(self.clickBox)
        self.brakeFault.stateChanged.connect(self.clickBox)
        self.AC.stateChanged.connect(self.clickBox)

        #Setting speed icon (static)
        SpeedIm =  QtGui.QIcon("speed.png")
        self.speedIcon.setIcon(SpeedIm)
        self.speedIcon.setIconSize(QSize(75, 75))

        #Adding train to map 
        self.addTrain.clicked.connect(self.addingTrainFunc)


    #FUNCTIONS FOR CLICKING BUTTONS
    def greenclickedButton(self):
            if (self.greenClickedButton.clicked):
                self.greenLabel.setStyleSheet("background-color: rgb(0, 255, 0)")
                self.redLabel.setStyleSheet("background-color: gray")
            self.currentBlockLabel.setStyleSheet('background-color: light gray')

            for x in range(1,151):
                self.currentBlock.addItem("{0}".format(x))
        
    def redclickedButton(self):    
        if (self.redClickedButton.clicked):
            self.redLabel.setStyleSheet("background-color: red")
            self.greenLabel.setStyleSheet("background-color: gray")
        self.currentBlockLabel.setStyleSheet('background-color: light gray')

        for x in range(1,77):
                self.currentBlock.addItem("{0}".format(x))


    #temp set function
    def tempInputfunc(self):
        inputTemp = self.inputTemp.text()
        self.tempLabel.setText("Current Temp: {0} degrees F".format(inputTemp))
    
    #power set function
    def powInputfunc(self):
        inputPow = self.inputPow.text()
        self.powLabel.setText("Current Power: {0} Watts".format(inputPow))

    #commanded speed function
    def commSpeedInputfunc(self):
        inputCommSpeed = self.commSpeed.text()
        self.commSpeedLabel.setText("Comm Speed: {0} mph".format(inputCommSpeed))

    #changing box 
    def clickBox(self):

        #internal lights
        if self.intLights.isChecked():
                self.intLightLabel.setStyleSheet("background-color: green")
                self.intLightLabel.setText("ON")
        else:
            self.intLightLabel.setStyleSheet("background-color: red")
            self.intLightLabel.setText("OFF")

        #external lights
        if self.extLights.isChecked():
                self.extLightLabel.setStyleSheet("background-color: green")
                self.extLightLabel.setText("ON")
        else:
            self.extLightLabel.setStyleSheet("background-color: red")
            self.extLightLabel.setText("OFF")

        #headlights
        if self.headlights.isChecked():
                self.headlightLabel.setStyleSheet("background-color: green")
                self.headlightLabel.setText("ON")
        else:
            self.headlightLabel.setStyleSheet("background-color: red")
            self.headlightLabel.setText("OFF")

        #Left doors
        if self.leftDoor.isChecked():
                self.lDoorLabel.setStyleSheet("background-color: green")
                self.lDoorLabel.setText("ON")
        else:
            self.lDoorLabel.setStyleSheet("background-color: red")
            self.lDoorLabel.setText("OFF")

        #Right doors
        if self.rightDoor.isChecked():
                self.rDoorLabel.setStyleSheet("background-color: green")
                self.rDoorLabel.setText("ON")
        else:
            self.rDoorLabel.setStyleSheet("background-color: red")
            self.rDoorLabel.setText("OFF")

        #Signal Fault
        if self.sigFault.isChecked():
                sigIcon = QtGui.QIcon("sigON.png")
                self.sigFaultLabel.setIcon(sigIcon)
                self.sigFaultLabel.setIconSize(QSize(50, 50))
        else:
            sigIcon = QtGui.QIcon("sigOFF.png")
            self.sigFaultLabel.setIcon(sigIcon)
            self.sigFaultLabel.setIconSize(QSize(50, 50))
        #power Fault
        if self.powFault.isChecked():
                powIcon = QtGui.QIcon("powON.png")
                self.powFaultLabel.setIcon(powIcon)
                self.powFaultLabel.setIconSize(QSize(50, 50))
        else:
            powIcon = QtGui.QIcon("powOFF.png")
            self.powFaultLabel.setIcon(powIcon)
            self.powFaultLabel.setIconSize(QSize(50, 50))
        #brake Fault
        if self.brakeFault.isChecked():
                brakeIcon = QtGui.QIcon("brakesON.png")
                self.brakeFaultLabel.setIcon(brakeIcon)
                self.brakeFaultLabel.setIconSize(QSize(50, 50))
        else:
            brakeIcon = QtGui.QIcon("brakesOFF.png")
            self.brakeFaultLabel.setIcon(brakeIcon)
            self.brakeFaultLabel.setIconSize(QSize(50, 50))

        #AC Fault
        if self.AC.isChecked():
                ACIm = QtGui.QIcon("ACON.png")
                self.ACIcon.setIcon(ACIm)
                self.ACIcon.setIconSize(QSize(50, 50))
        else:
            ACIm = QtGui.QIcon("ACOFF.png")
            self.ACIcon.setIcon(ACIm)
            self.ACIcon.setIconSize(QSize(50, 50))
    
    def addingTrainFunc(self):
        numTrains = self.trainBox.count()
        self.trainBox.addItem("Train {0}".format(numTrains))
        newTrain = Train
        trainArray.append(newTrain)  


#end mainWindow definition

class Train(MainWindow):
    pass    

#end Train class window


#defining the app and the window
app = QtWidgets.QApplication(sys.argv)

firstTrain = Train()
trainArray.append(firstTrain)

window = trainArray[0]
window.show()
app.exec()