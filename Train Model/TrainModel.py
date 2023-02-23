import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QSize
import TrackParser

trainArray = []
track = TrackParser.parseTrack('Track Layout.csv')

class MainWindowTestUI(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("TrainModelTestUI_v2.ui", self)
        self.setWindowTitle('Train Model Test UI')
        #window.trainBox.addItem("Train 0")  
        
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

    #temp set function
    def tempInputfunc(self):
        inputTemp = self.inputTemp.text()
        window.tempLabel.setText("Current Temp: {0} degrees F".format(inputTemp))
    
    #power set function
    def powInputfunc(self):
        inputPow = self.inputPow.text()
        window.powLabel.setText("Current Power: {0} Watts".format(inputPow))

    #commanded speed function
    def commSpeedInputfunc(self):
        inputCommSpeed = self.commSpeed.text()
        window.commSpeedLabel.setText("Comm Speed: {0} mph".format(inputCommSpeed))

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
                window.lDoorLabel.setText("ON")
        else:
            window.lDoorLabel.setStyleSheet("background-color: red")
            window.lDoorLabel.setText("OFF")

        #Right doors
        if self.rightDoor.isChecked():
                window.rDoorLabel.setStyleSheet("background-color: green")
                window.rDoorLabel.setText("ON")
        else:
            window.rDoorLabel.setStyleSheet("background-color: red")
            window.rDoorLabel.setText("OFF")

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


#end test UI definition

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        uic.loadUi("TrainModelUI.ui", self)
        self.setWindowTitle('Train Model UI')

        #Icon declaration for off states
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

        #Setting speed icon (static)
        SpeedIm =  QtGui.QIcon("speed.png")
        self.speedIcon.setIcon(SpeedIm)
        self.speedIcon.setIconSize(QSize(75, 75))

        self.greenLineButton.clicked.connect(self.greenclickedButton)
        self.redLineButton.clicked.connect(self.redclickedButton)
        self.EmerButton.setStyleSheet("background-color: red")
        self.EmerButton.clicked.connect(self.emerBrakeButton)
       
    def greenclickedButton(self):
        if (self.greenLineButton.clicked):
            greenTrack = QtGui.QIcon("GREENtrain_layout")
            self.trainMapLabel.setIcon(greenTrack)
            self.trainMapLabel.setIconSize(QSize(225,425))
            self.greenLineButton.setStyleSheet("background-color: rgb(0, 255, 0)")
            self.redLineButton.setStyleSheet("background-color: gray")

            testUI.currentBlock.clear()

            for x in range(1,151):
                testUI.currentBlock.addItem("{0}".format(x))
    
    def redclickedButton(self):    
        if (self.redLineButton.clicked):
            redTrack = QtGui.QIcon("REDtrain_layout")
            self.trainMapLabel.setIcon(redTrack)
            self.trainMapLabel.setIconSize(QSize(225,425))
            self.redLineButton.setStyleSheet("background-color: red")
            self.greenLineButton.setStyleSheet("background-color: gray")
            
            testUI.currentBlock.clear()

            for x in range(1,77):
                testUI.currentBlock.addItem("{0}".format(x))

    def emerBrakeButton(self):

        if (self.EmerButton.styleSheet() == 'background-color: red'):
            self.actSpeed.setText("Actual Speed:           0 MPH")
            self.actSpeed.setStyleSheet("background-color: red; border: 2px solid black; border-radius: 4px;padding: 2px;")
            self.EmerButton.setText("Reset")
            self.EmerButton.setStyleSheet("background-color: gray; border: 2px solid black; border-radius: 4px;padding: 2px;")

        else:
            self.actSpeed.setText("Actual Speed:")
            self.actSpeed.setStyleSheet("background-color:  light gray; border: 2px solid black; border-radius: 4px;padding: 2px;")
            self.EmerButton.setText("EMERGENCY BRAKE")
            self.EmerButton.setStyleSheet("background-color: red")


#end mainWindow definition

class Train(MainWindow):
    pass    

#end Train class window



#defining the app and the window
app = QtWidgets.QApplication(sys.argv)

firstTrain = MainWindow()
testUI = MainWindowTestUI()
trainArray.append(firstTrain)

window = firstTrain

window.show()
testUI.show()
app.exec()