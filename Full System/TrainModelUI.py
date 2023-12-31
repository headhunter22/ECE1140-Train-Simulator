import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Block import Block
from Track import Track
from Train import Train
from TrainController import TrainController
from signals import signals

class popUpWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("trainModPopUp.ui", self)

class TrainModelUI(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("trainModel_fullsys.ui", self)

        self.popUp = popUpWindow()
        #self.block = Block()
        self.tempSlider.setMinimum(60)
        self.tempSlider.setMaximum(80)
        self.tempSlider.setValue(70)
        self.ACprogressBar.setMinimum(60)
        self.ACprogressBar.setMaximum(80)
        self.ACprogressBar.setValue(70)
        self.tempSlider.valueChanged.connect(self.sliderChanged)

        self.sigFaulVar = False
        self.powFaulVar = False
        self.brakeFaulVar = False
        self.sigFaultLabel.clicked.connect(self.sigFaultFunc)
        self.powFaultLabel.clicked.connect(self.powFaultFunc)
        self.brakeFaultLabel.clicked.connect(self.brakeFaultFunc)
 


        #Connecting the received signals to their display functions
        signals.trainModelUpdateGUISpeed.connect(self.displaySpeed)
        signals.trainModelGUIBlock.connect(self.displayBlock)
        signals.trainModelGUIcommandedSpeed.connect(self.displayCommSpeed)
        signals.trainModelGUIpower.connect(self.displayPower)
        signals.timerTicked.connect(self.clockUpdate)
        signals.trainControllerExteriorLights.connect(self.externalLights)
        signals.trainControllerInteriorLights.connect(self.internalLights)
        signals.trainControllerLeftDoors.connect(self.LeftDoors)
        signals.trainControllerRightDoors.connect(self.RightDoors)
        signals.trainModelGUIacc.connect(self.displayAcc)
        signals.trainModelPassengers.connect(self.passengerUpdate)
        signals.trainModelDestinationSignal.connect(self.trainDest)
        signals.trainModelLineSignal.connect(self.lineConfig)
        signals.trainControllerDispatchedSignal.connect(self.addTrain)
        signals.trainModelGUISpeedLim.connect(self.speedLim)
        signals.trainControllerEmerBrake.connect(self.brakeUI)
        signals.trackModelBeaconSending.connect(self.beaconFunc)
        signals.trainModelAuthorityToTrainController.connect(self.updateAuthority)
        #displaying the stats of the train popup

        self.popUpUI.clicked.connect(self.displayPopUp)
        self.EmerButton.clicked.connect(self.emergencyBrake)
        self.EmerButton.styleSheet() == 'background-color: red'

        self.trainBox.currentIndexChanged.connect(self.trainViewSwitched)
        
        #icon set up
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

        self.intLightLabel.setStyleSheet("background-color: red")
        self.intLightLabel.setText("OFF")
        self.rDoorLabel.setStyleSheet("background-color: red")
        self.rDoorLabel.setText("CLOSED")
        self.lDoorLabel.setStyleSheet("background-color: red")
        self.lDoorLabel.setText("CLOSED")
        self.headlightLabel.setStyleSheet("background-color: red")
        self.headlightLabel.setText("OFF")
        
    def displaySpeed(self, train):
        speedMpH = float(train)*2.237
        txt = f"{speedMpH:.2f}"
        floatTxt = float(txt)
        self.actSpeed.setText("Speed: {0} mi/h".format(floatTxt)) #actSpeed is the qt creator object

    def displayAcc(self,train):
        if self.brakeFaulVar == True:
            self.trainAcc.setStyleSheet("background-color: red;border: 2px solid black; border-radius: 4px;padding: 2px;")
        else:
            self.trainAcc.setStyleSheet("background-color: light gray;border: 2px solid black; border-radius: 4px;padding: 2px;")

        acc = float(train)*2.237
        txt = f"{acc:.2f}"
        floatTxt = float(txt)
        self.trainAcc.setText("Acc.: {0} mi/h/s".format(floatTxt)) #actSpeed is the qt creator object
    
    def displayBlock(self, block):
        self.currBlockLabel.setText("Current Block = {0}".format(block)) #commSpeedLabel is the qt creator object
        
    
    def displayCommSpeed(self, train):
        commSpeedMpH = float(train)*.621
        self.commSpeedLabel.setText("Commanded Speed = {0} mi/h".format(commSpeedMpH)) #currBlockLabel is the qt creator object
        
    def speedLim(self,lim):
        commSpeedMpH = float(lim)*.621
        self.speedLimitLabel.setText("Speed Limit = {0} mi/h".format(commSpeedMpH)) #speedLimitLabel is the qt creator object
    
    
    def displayPower(self,train):
        if self.powFaulVar == True: 
            self.powLabel.setStyleSheet("background-color: red;border: 2px solid black; border-radius: 4px;padding: 2px;")
        else:
            self.powLabel.setStyleSheet("background-color: light gray;border: 2px solid black; border-radius: 4px;padding: 2px;")

        self.powLabel.setText("Power Input: {0} Watts".format(train))
        self.powProgressBar.setMinimum(0)
        self.powProgressBar.setMaximum(120001)
        self.powProgressBar.setTextVisible(0)
        roundTrain = round(float(train))
        self.powProgressBar.setValue(int(roundTrain))
    
    def displayPopUp(self):
        self.popUp.show()
    
    def clockUpdate(self, hrs, mins, secs):
        self.dateLabel.setText(f'{int(hrs):02d}' + ':' + f'{int(mins):02d}' + ':' + f'{int(secs):02d}' + '      April 27, 2023')
    
    def externalLights(self,train):
        if train:
                self.headlightLabel.setStyleSheet("background-color: green")
                self.headlightLabel.setText("ON")
        else:
            self.headlightLabel.setStyleSheet("background-color: red")
            self.headlightLabel.setText("OFF")

    def LeftDoors(self,train):
        if train:
                self.lDoorLabel.setStyleSheet("background-color: green")
                self.lDoorLabel.setText("OPEN")
        else:
            self.lDoorLabel.setStyleSheet("background-color: red")
            self.lDoorLabel.setText("CLOSED")

    def RightDoors(self,train):
        if train:
                self.rDoorLabel.setStyleSheet("background-color: green")
                self.rDoorLabel.setText("OPEN")
        else:
            self.rDoorLabel.setStyleSheet("background-color: red")
            self.rDoorLabel.setText("CLOSED")
    
    def internalLights(self,train):
        if train:
                self.intLightLabel.setStyleSheet("background-color: green")
                self.intLightLabel.setText("ON")
        else:
            self.intLightLabel.setStyleSheet("background-color: red")
            self.intLightLabel.setText("OFF")
    
    def emergencyBrake(self):      
        if (self.EmerButton.styleSheet() == 'background-color: red'):
            self.actSpeed.setStyleSheet("background-color: red; border: 2px solid black; border-radius: 4px;padding: 2px;")
            self.EmerButton.setText("Reset")
            self.EmerButton.setStyleSheet("background-color: gray; border: 2px solid black; border-radius: 4px;padding: 2px; font: 16pt Segoe UI")
            signals.trainModelEmerBrake.emit(True)
        else:
            self.actSpeed.setStyleSheet("background-color:  light gray; border: 2px solid black; border-radius: 4px;padding: 2px;")
            self.EmerButton.setText("EMERGENCY BRAKE")
            self.EmerButton.setStyleSheet("background-color: red")
            signals.trainModelEmerBrake.emit(False)
    
    def passengerUpdate(self,numPass):
        self.popUp.numPass.setText(str(numPass))
        totalWeight = numPass*150 + (90169.065) #total weight of train
        print('update!')
        self.popUp.currMass.setText(str(totalWeight))
    
    def sliderChanged(self):
        sliderSize = self.tempSlider.value()
        self.ACprogressBar.setMinimum(60)
        self.ACprogressBar.setMaximum(80)
        self.ACprogressBar.setTextVisible(0)
        self.tempText.setText('Current Temp: ' + str(sliderSize) + ' F')
        self.ACprogressBar.setValue(sliderSize)

    def trainDest(self, trainDest):
        text = 'Destination: '
        for x in trainDest:
            if x == 2:
                station = 'Pioneer'
            elif x == 9:
                station = 'Edgebrook'
            elif x == 16:
                station = 'Profeta'
            elif x == 22:
                station = 'Whited'
            elif x == 31:
                station = 'South Bank'
            elif x == 39:
                station = 'Central'
            elif x == 48:
                station = 'Inglewood'
            elif x == 57:
                station = 'Overbrook'
            elif x == 65:
                station = 'Glenbury'
           
            elif x == 73:
                station = 'Dormont'
            elif x == 77:
                station = 'Mt Lebanon'
            elif x == 88:
                station = 'Poplar'
            elif x == 96:
                station = 'Castle Shannon'
            elif x == 105:
                station = 'Dormont'
            elif x == 114:
                station = 'Glenbury'
            elif x == 123:
                station = 'Overbrook'
            elif x == 132:
                station = 'Inglewood'
            else:
                station = 'Central'

            text = text + station + '\n   '
            signals.trainModelStationtoTrainController.emit(text)
        self.destLabel.setText(text)


    def lineConfig(self, line):
        print(str(line.lineName))
        if (line.lineName == 'Red'):
            self.redLineButton.setStyleSheet("background-color: red")
            self.greenLineButton.setStyleSheet("background-color: light gray")
        else:
            self.redLineButton.setStyleSheet("background-color: light gray")
            self.greenLineButton.setStyleSheet("background-color: green")
        
    def trainViewSwitched(self):
        print('train view switched')
    
    def addTrain(self,train):
        self.trainBox.addItem("Train {0}".format(train.ID))
    
    def brakeUI(self, brake):
        if brake == False:
            self.actSpeed.setStyleSheet("background-color:  light gray; border: 2px solid black; border-radius: 4px;padding: 2px;")
            self.EmerButton.setText("EMERGENCY BRAKE")
            self.EmerButton.setStyleSheet("background-color: red")
        else:
            self.actSpeed.setStyleSheet("background-color: red; border: 2px solid black; border-radius: 4px;padding: 2px;")
            self.EmerButton.setText("Reset")
            self.EmerButton.setStyleSheet("background-color: gray; border: 2px solid black; border-radius: 4px;padding: 2px; font: 16pt Segoe UI")

    def beaconFunc(self, block):
        print("sig fault = " + str(self.sigFaulVar))
        if self.sigFaulVar == True:
            self.beaconLabel.setText('SIGNAL FAULT: NO BEACON INFO')
            self.beaconLabel.setStyleSheet("background-color: red")
        elif (block.beaconBool == True):
            self.beaconLabel.setStyleSheet("background-color: light gray; border: 2px solid black; border-radius: 4px;padding: 2px")
            if str(block.beacon.stationName) == 'None':
                self.beaconLabel.setText('Beacon Information: \nPassing a Switch')
            else:
                self.beaconLabel.setText('Beacon Information: \n' + str(block.beacon.stationName)
                                     +'\nExit Side: '+ str(block.beacon.stationSide))    
        else:
            self.beaconLabel.setStyleSheet("background-color: light gray; border: 2px solid black; border-radius: 4px;padding: 2px")
            self.beaconLabel.setText("No Beacon Information")
    
    def sigFaultFunc(self):
        if self.sigFaulVar == False:
            sigIcon = QtGui.QIcon("sigON.png")
            self.sigFaultLabel.setIcon(sigIcon)
            self.sigFaultLabel.setIconSize(QSize(50, 50))
            self.sigFaulVar = True
        else:
            sigIcon = QtGui.QIcon("sigOFF.png")
            self.sigFaultLabel.setIcon(sigIcon)
            self.sigFaultLabel.setIconSize(QSize(50, 50))
            self.sigFaulVar = False

    def powFaultFunc(self):
        if self.powFaulVar == False:
            powIcon = QtGui.QIcon("powON.png")
            self.powFaultLabel.setIcon(powIcon)
            self.powFaultLabel.setIconSize(QSize(50, 50))
            self.powFaulVar = True
        else:
            powIcon = QtGui.QIcon("powOFF.png")
            self.powFaultLabel.setIcon(powIcon)
            self.powFaultLabel.setIconSize(QSize(50, 50))
            self.powFaulVar = False
        signals.powFaultsig.emit(self.powFaulVar)

    
    def brakeFaultFunc(self):
        if self.brakeFaulVar == False:
            brakeIcon = QtGui.QIcon("brakesON.png")
            self.brakeFaultLabel.setIcon(brakeIcon)
            self.brakeFaultLabel.setIconSize(QSize(50, 50))
            self.brakeFaulVar = True
        else:
            brakeIcon = QtGui.QIcon("brakesOFF.png")
            self.brakeFaultLabel.setIcon(brakeIcon)
            self.brakeFaultLabel.setIconSize(QSize(50, 50))
            self.brakeFaulVar = False
        signals.brakeFaultsig.emit(self.brakeFaulVar)

    def updateAuthority(self, auth):
         x = auth
         txt = f"{x:.2f}"
         self.y = float(txt)
         self.authority.setText("Authority: {0} meters".format(self.y))
