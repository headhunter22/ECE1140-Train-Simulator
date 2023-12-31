from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from signals import signals
from Wayside import Wayside

class TrainControllerUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Train Controller")
        self.resize(980, 620)

        # Connect Signals #
        signals.trainControllerPower.connect(self.updatePower)
        signals.trainControllerSpeed.connect(self.updateSpeed)
        signals.trainModelAuthorityToTrainController.connect(self.updateAuthority)
        signals.trainControllerUpdateCommSpeed.connect(self.updateCommandedSpeed)
        signals.trainModelEmerBrake.connect(self.EBClick)
        signals.timerTicked.connect(self.changeLabel)
        signals.trainControllerKP.connect(self.updateKP)
        signals.trainControllerKI.connect(self.updateKI)
        signals.trainModelStationtoTrainController.connect(self.updateStations)

        # Create Time element # 
        self.dataTime = QtWidgets.QLabel(" ", self)
        self.dataTime.setGeometry(420, 500, 200, 100)
        font1 = QtGui.QFont()
        font1.setPointSize(24)
        self.dataTime.setFont(font1)


        # Emergency Brake button init #
        self.EmerBrake = QtWidgets.QPushButton('EMERGENCY BRAKE', self)
        self.txt = QtWidgets.QPushButton("Emergency Brake Disengaged", self)
        self.EmerBrake.setGeometry(50, 50, 200, 200)
        self.txt.setGeometry(50, 250, 200, 50)
        self.txt.setText("Emergency Brake Engaged")
        self.txt.setStyleSheet("QPushButton { background-color : rgb(255,0,0)}")
        self.EmerBrake.setCheckable(True)
        self.EmerBrake.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
        self.txt.setCheckable(False)
        self.txt.setVisible(False)
        self.EmerBrake.clicked.connect(self.EBClick)
        self.EmerBrake.clicked.connect(self.EBText)


        # Slide Request init #
        self.RateReq = QtWidgets.QSlider(self)
        self.RateText = QtWidgets.QLabel("Requested Speed: 0mph", self)
        self.CommandedSpeed = QtWidgets.QLabel("Commanded Speed: 0mph", self)
        self.Authority = QtWidgets.QLabel("Authority: 0 meters", self)
        self.RateText.setGeometry(750, 275, 200, 100)
        self.RateReq.setGeometry(800, 50, 50, 250)
        self.CommandedSpeed.setGeometry(750, 300, 200, 100)
        self.Authority.setGeometry(750, 325, 200, 100)
        self.RateReq.setMinimum(0)
        self.RateReq.setMaximum(45)
        self.RateReq.setSingleStep(1)
        self.RateReq.setValue(20)

        # Slider increment labels # 
        self.HundredLabel = QtWidgets.QLabel("45 Mph", self)
        self.FiftyLabel = QtWidgets.QLabel("35 Mph", self)
        self.ZeroLabel = QtWidgets.QLabel("25 Mph", self)
        self.NegFiftyLabel = QtWidgets.QLabel("15 Mph", self)
        self.NegHundredLabel = QtWidgets.QLabel("0 Mph", self)

        self.HundredLabel.setGeometry(850, 30, 50, 50)
        self.FiftyLabel.setGeometry(850, 90, 50, 50)
        self.ZeroLabel.setGeometry(850, 150, 50, 50)
        self.NegFiftyLabel.setGeometry(850, 209, 50, 50)
        self.NegHundredLabel.setGeometry(850, 269, 55, 50)
       
        # Connection #
        self.RateReq.valueChanged.connect(self.SliderMoved)


        # Train Model Command Signals #
        self.Headlights = QtWidgets.QPushButton("Headlights", self)
        self.Headlights.setGeometry(50, 350, 100, 50)
        self.Headlights.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
        self.Headlights.setCheckable(True)

        self.InteriorLights = QtWidgets.QPushButton("Interior Lights", self)
        self.InteriorLights.setGeometry(150, 350, 100, 50)
        self.InteriorLights.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
        self.InteriorLights.setCheckable(True)

        self.LeftDoors = QtWidgets.QPushButton("Left Doors", self)
        self.LeftDoors.setGeometry(50, 400, 100, 50)
        self.LeftDoors.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
        self.LeftDoors.setCheckable(True)

        self.RightDoors = QtWidgets.QPushButton("Right Doors", self)
        self.RightDoors.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
        self.RightDoors.setGeometry(150, 400, 100, 50)
        self.RightDoors.setCheckable(True)

        # Connections #
        self.Headlights.clicked.connect(self.HeadlightsClick)
        self.InteriorLights.clicked.connect(self.InteriorLightsClick)
        self.LeftDoors.clicked.connect(self.LeftDoorsClick)
        self.RightDoors.clicked.connect(self.RightDoorsClick)

        # Showing Power Output #
        self.PowerShown = QtWidgets.QPushButton("0 KWatts", self)
        self.PowerShown.setGeometry(325, 50, 250, 100)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.PowerShown.setFont(font)
        self.PowerShown.setCheckable(False)
        self.PowerShown.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")

        # Showing Actual speed #
        self.SpeedShown = QtWidgets.QPushButton("0 mph", self)
        self.SpeedShown.setGeometry(325, 155, 250, 100)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.SpeedShown.setFont(font)
        self.SpeedShown.setCheckable(False)
        self.SpeedShown.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")

        # Init Service Brake Button #
        self.ServiceBrake = QtWidgets.QPushButton("Service Brake", self)
        self.ServiceBrake.setGeometry(350, 385, 200, 100)
        self.ServiceBrake.setFont(font)
        self.ServiceBrake.setCheckable(True)
        self.ServiceBrake.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
        self.ServiceBrake.clicked.connect(self.ServiceBrakeClick)

        # Init A/C button
        self.AC = QtWidgets.QPushButton("Train A/C", self)
        self.AC.setGeometry(350, 280, 200, 100)
        self.AC.setFont(font)
        self.AC.setCheckable(True)
        self.AC.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
        self.AC.clicked.connect(self.ACClick)

        # Init Manual/Automatic Buttons #
        self.ManualMode = QtWidgets.QPushButton("Manual Mode", self)
        self.ManualMode.setGeometry(775, 400, 100, 100)
        self.ManualMode.setStyleSheet("QPushButton { background-color : rgb(255,0,0) }")
        self.ManualMode.setCheckable(True)
        self.AutoMode = QtWidgets.QPushButton("Automatic Mode", self)
        self.AutoMode.setStyleSheet("QPushButton { background-color : rgb(0,255,0) }")
        self.AutoMode.setGeometry(775, 505, 100, 100)
        self.AutoMode.setCheckable(True)
        self.AutoMode.setChecked(True)
        self.AutoModeClick()

        #Connections #
        self.ManualMode.clicked.connect(self.ManualModeClick)
        self.AutoMode.clicked.connect(self.AutoModeClick)

        # Init gain change windows #
        self.GainChange = QtWidgets.QPushButton("Edit Gain Values", self)
        self.GainChange.setGeometry(25, 550, 100, 50)
        self.GainChange.clicked.connect(self.OpenGainWindow)

        # Init KP/KI Labels
        self.KPLabel = QtWidgets.QLabel("KP: 100.0", self)
        self.KILabel = QtWidgets.QLabel("KI: 100.0", self)
        self.KPLabel.setGeometry(130, 550, 75, 25)
        self.KILabel.setGeometry(130, 575, 75, 25)

        # Init station label #
        self.stationLabel = QtWidgets.QLabel(" ", self)
        self.stationLabel.setGeometry(625, 25, 400, 100)
        font3 = QtGui.QFont()
        font3.setPointSize(14)
        self.stationLabel.setFont(font3)

    def updateKP(self, kp):
         self.KPLabel.setText("KP: " + str(kp))

    def updateKI(self, ki):
         self.KILabel.setText("KI: " + str(ki))

    def updateStations(self, string):
         self.stationLabel.setText(string)
    
    def CloseGainWindow(self):
        self.GW.close()

        # Calling the clicked-on EmerBrake functions #
    def EBClick(self, emerBrake):
            if self.EmerBrake.isChecked() == False or emerBrake == False:
                 self.EmerBrake.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
                 signals.trainControllerEmerBrake.emit(False)

            if self.EmerBrake.isChecked() == True or emerBrake == True:
                 self.EmerBrake.setStyleSheet("QPushButton { background-color : rgb(255,0,0) }")
                 signals.trainControllerEmerBrake.emit(True)
                 
    
    def EBText(self):
            if self.EmerBrake.isChecked() == True:
               self.txt.setVisible(True)

            if self.EmerBrake.isChecked() == False:
               self.txt.setVisible(False)


        # Calling Slider changes functions #
    def SliderMoved(self, i):
        self.RateText.setText("Requested Speed: {0}mph".format(i))
        signals.trainControllerManualModeToTrainModel.emit(True,i)

        # Calling headlights clicked function #
    def HeadlightsClick(self):
        if self.Headlights.isChecked() == True:
             self.Headlights.setStyleSheet("QPushButton { background-color : rgb(0,255,0) }")
             signals.trainControllerExteriorLights.emit(True)


        if self.Headlights.isChecked() == False:
             self.Headlights.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
             signals.trainControllerExteriorLights.emit(False)

        # Calling InteriorLights clicked function #
    def InteriorLightsClick(self):
        if self.InteriorLights.isChecked() == True:
             self.InteriorLights.setStyleSheet("QPushButton { background-color : rgb(0,255,0) }")
             signals.trainControllerInteriorLights.emit(True)

        if self.InteriorLights.isChecked() == False:
             self.InteriorLights.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
             signals.trainControllerInteriorLights.emit(False)

        # Calling LeftDoors clicked function #
    def LeftDoorsClick(self):
        if self.LeftDoors.isChecked() == True:
             self.LeftDoors.setStyleSheet("QPushButton { background-color : rgb(0,255,0) }")
             signals.trainControllerLeftDoors.emit(True)

        if self.LeftDoors.isChecked() == False:
             self.LeftDoors.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
             signals.trainControllerLeftDoors.emit(False)

        # Calling RightDoors clicked function #
    def RightDoorsClick(self):
        if self.RightDoors.isChecked() == True:
             self.RightDoors.setStyleSheet("QPushButton { background-color : rgb(0,255,0) }")
             signals.trainControllerRightDoors.emit(True)


        if self.RightDoors.isChecked() == False:
             self.RightDoors.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
             signals.trainControllerRightDoors.emit(False)

        # Calling Manual button Functions #
    def ManualModeClick(self):
        if self.ManualMode.isChecked() == True:
              self.ManualMode.setStyleSheet("QPushButton { background-color : rgb(0,255,0) }")
              self.AutoMode.setChecked(True)
              self.AutoModeClick()

        if self.ManualMode.isChecked() == False:
              self.ManualMode.setStyleSheet("QPushButton { background-color : rgb(255,0,0) }")
              self.AutoModeClick()

       # Calling Auto button function #
    def AutoModeClick(self):
         if self.AutoMode.isChecked() == True:
              self.AutoMode.setStyleSheet("QPushButton { background-color : rgb(0,255,0) }")
              self.ManualMode.setCheckable(False)
              self.EmerBrake.setCheckable(True)
              self.RightDoors.setCheckable(False)
              self.LeftDoors.setCheckable(False)
              self.Headlights.setCheckable(False)
              self.InteriorLights.setCheckable(False)
              self.RateReq.setDisabled(True)
              self.ServiceBrake.setCheckable(False)
              self.AC.setCheckable(False)
              self.ManualMode.setStyleSheet("QPushButton { background-color : rgb(255,0,0) }")
              signals.trainControllerManualModeToTrainModel.emit(False, 123)

         if self.AutoMode.isChecked() == False:
              self.AutoMode.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
              self.ManualMode.setCheckable(True)
              self.EmerBrake.setCheckable(True)
              self.RightDoors.setCheckable(True)
              self.LeftDoors.setCheckable(True)
              self.Headlights.setCheckable(True)
              self.InteriorLights.setCheckable(True)
              self.RateReq.setDisabled(False)
              self.ServiceBrake.setCheckable(True)
              self.AC.setCheckable(True)
              self.ManualMode.setStyleSheet("QPushButton { background-color : rgb(0,255,0) }")
              self.AutoMode.setStyleSheet("QPushButton { background-color : rgb(255,0,0) }")
              signals.trainControllerManualModeToTrainModel.emit(True, self.CommandedSpeed)

    def ServiceBrakeClick(self):
         if self.ServiceBrake.isChecked() == True:
              self.ServiceBrake.setStyleSheet("QPushButton { background-color : rgb(0, 255, 0) }")
              signals.trainControllerServiceBrakeMan.emit(True)
              signals.trainControllerPower.emit(0.0)

         if self.ServiceBrake.isChecked() == False:
              self.ServiceBrake.setStyleSheet("QPushButton { background-color : rgb(255, 255, 255) }")
              signals.trainControllerServiceBrakeMan.emit(False)

    def updatePower(self, power):
         x = power
         power = power/1000
         txt = f"{power:.2f}"
         y = float(txt)
         self.power = y
         self.PowerShown.setText("{0} KWatts".format(y))

    def updateSpeed(self, speed):
         self.speed = speed
         self.SpeedShown.setText("{0} Mph".format(speed))

    def OpenGainWindow(self):
         self.GW = GainWindow()
         self.GW.show()

    def updateAuthority(self, auth):
         x = auth
         txt = f"{x:.2f}"
         self.y = float(txt)
         self.Authority.setText("Authority: {0} meters".format(self.y))

    def updateCommandedSpeed(self, commSpeed):
         x = commSpeed / 1.609
         txt = f"{x:.2f}"
         self.y = float(txt)
         self.CommandedSpeed.setText("Commanded Speed: {0}mph".format(self.y))

    def ACClick(self):
         if self.AC.isChecked() == True:
              self.AC.setStyleSheet("QPushButton { background-color : rgb(0, 255, 0) }")
              signals.trainControllerAC.emit(True)

         if self.AC.isChecked() == False:
              self.AC.setStyleSheet("QPushButton { background-color : rgb(255, 255, 255) }")
              signals.trainControllerAC.emit(False)

    def changeLabel(self, hrs, mins, secs): ####### 
        self.dataTime.setText(f'{int(hrs):02d}' + ':' + f'{int(mins):02d}' + ':' + f'{int(secs):02d}')

class GainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(GainWindow, self).__init__()


        self.setWindowTitle("Edit Gain")
        self.resize(490, 310)

        # init labels and text inserts #
        self.KpLabel = QtWidgets.QLabel("KP Gain: ", self)
        self.KpLabel.setGeometry(100, 50, 115, 100)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.KpLabel.setFont(font)

        self.KILabel = QtWidgets.QLabel("KI Gain: ", self)
        self.KILabel.setGeometry(100, 150, 110, 100)
        self.KILabel.setFont(font)

         # init KP/PI Edits, confirm button # 
        self.KIChange = QtWidgets.QLineEdit(" ", self)
        self.KIChange.setGeometry(225, 92, 50, 25)
        self.KPChange = QtWidgets.QLineEdit(" ", self)
        self.KPChange.setGeometry(225, 192, 50, 25)

        # Show updated KP/KI Values #
        self.correctedKPValue = QtWidgets.QLabel("New KP: ", self)
        self.correctedKPValue.setGeometry(285, 50, 115, 100)
        self.correctedKIValue = QtWidgets.QLabel("New KI: ", self)
        self.correctedKIValue.setGeometry(285, 150, 110, 100)

        self.confirm = QtWidgets.QPushButton("Confirm", self)
        self.confirm.setGeometry(370, 250, 100, 50)
        self.confirm.setCheckable(True)
        self.confirm.clicked.connect(self.confirmClick)

        self.confirmLabel = QtWidgets.QLabel(" ", self)
        self.confirmLabel.setGeometry(50, 225, 350, 100)
        font2 = QtGui.QFont()
        font2.setPointSize(14)
        self.confirmLabel.setFont(font2)
        

    def confirmClick(self):
        textkp = self.KIChange.text()
        INPUT2 = float(textkp)
        signals.trainControllerUIKP.emit(INPUT2)
        self.KIChange.setText(textkp)
        self.correctedKPValue.setText("New KP: " + textkp)

        textki = self.KIChange.text()
        INPUT3 = float(textki)
        signals.trainControllerUIKI.emit(INPUT3)
        self.KIChange.setText(textki)
        self.correctedKIValue.setText("New KI: " + textki)

        self.confirmLabel.setText("KP and KI values have been updated")

        signals.trainControllerKP.emit(INPUT2)
        signals.trainControllerKI.emit(INPUT3)