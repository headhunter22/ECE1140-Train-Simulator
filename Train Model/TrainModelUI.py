import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QSize

trainArray = []

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
            self.greenLineButton.setStyleSheet("background-color: green")
            self.redLineButton.setStyleSheet("background-color: gray")
    
    def redclickedButton(self):    
        if (self.redLineButton.clicked):
            redTrack = QtGui.QIcon("REDtrain_layout")
            self.trainMapLabel.setIcon(redTrack)
            self.trainMapLabel.setIconSize(QSize(225,425))
            self.redLineButton.setStyleSheet("background-color: red")
            self.greenLineButton.setStyleSheet("background-color: gray")

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

firstTrain = Train()
trainArray.append(firstTrain)

window = trainArray[0]

window.show()
app.exec()