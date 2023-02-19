from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Train Controller")
        self.resize(980, 620)


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
        self.RateText.setGeometry(750, 275, 200, 100)
        self.RateReq.setGeometry(800, 50, 50, 250)
        self.CommandedSpeed.setGeometry(750, 325, 200, 100)
        self.RateReq.setMinimum(-100)
        self.RateReq.setMaximum(100)
        self.RateReq.setSingleStep(1)
        self.RateReq.setTickInterval(5)

        # Slider increment labels # 
        self.HundredLabel = QtWidgets.QLabel("100 Mph", self)
        self.FiftyLabel = QtWidgets.QLabel("50 Mph", self)
        self.ZeroLabel = QtWidgets.QLabel("0 Mph", self)
        self.NegFiftyLabel = QtWidgets.QLabel("-50 Mph", self)
        self.NegHundredLabel = QtWidgets.QLabel("-100 Mph", self)

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

        self.RightDoors = QtWidgets.QPushButton("Interior Lights", self)
        self.RightDoors.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
        self.RightDoors.setGeometry(150, 400, 100, 50)
        self.RightDoors.setCheckable(True)

        # Connections #
        self.Headlights.clicked.connect(self.HeadlightsClick)
        self.InteriorLights.clicked.connect(self.InteriorLightsClick)
        self.LeftDoors.clicked.connect(self.LeftDoorsClick)
        self.RightDoors.clicked.connect(self.RightDoorsClick)

        # Showing Power Output #
        self.PowerShown = QtWidgets.QPushButton("0 Watts", self)
        self.PowerShown.setGeometry(425, 50, 200, 100)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.PowerShown.setFont(font)
        self.PowerShown.setCheckable(False)
        self.PowerShown.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")


        # Calling the clicked-on EmerBrake functions #
    def EBClick(self):
            if self.EmerBrake.isChecked() == False:
                 self.EmerBrake.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
                 print("Emergency Brake Disengaged")

            if self.EmerBrake.isChecked() == True:
                 self.EmerBrake.setStyleSheet("QPushButton { background-color : rgb(255,0,0) }")
                 print("Emergency Brake Engaged")
    
    def EBText(self):
            if self.EmerBrake.isChecked() == True:
               self.txt.setVisible(True)

            if self.EmerBrake.isChecked() == False:
               self.txt.setVisible(False)


        # Calling Slider changes functions #
    def SliderMoved(self, i):
        self.RateText.setText("Requested Speed: {0}mph".format(i))
        self.RateText.update()

        # Commanded Speed Changes #
    def CommandedSpeedChange(self, j):
         self.CommandedSpeed.setText("Commanded Speed: {0}".format(j))

        
        # Calling headlights clicked function #
    def HeadlightsClick(self):
        if self.Headlights.isChecked() == True:
             self.Headlights.setStyleSheet("QPushButton { background-color : rgb(0,255,0) }")
             print("Headlights On")

        if self.Headlights.isChecked() == False:
             self.Headlights.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
             print("Headlights Off")

        # Calling InteriorLights clicked function #
    def InteriorLightsClick(self):
        if self.InteriorLights.isChecked() == True:
             self.InteriorLights.setStyleSheet("QPushButton { background-color : rgb(0,255,0) }")
             print("Interior Lights On")

        if self.InteriorLights.isChecked() == False:
             self.InteriorLights.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
             print("Interior Lights Off")

        # Calling LeftDoors clicked function #
    def LeftDoorsClick(self):
        if self.LeftDoors.isChecked() == True:
             self.LeftDoors.setStyleSheet("QPushButton { background-color : rgb(0,255,0) }")
             print("Left Doors Opened")

        if self.LeftDoors.isChecked() == False:
             self.LeftDoors.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
             print("Left Doors Closed")

        # Calling RightDoors clicked function #
    def RightDoorsClick(self):
        if self.RightDoors.isChecked() == True:
             self.RightDoors.setStyleSheet("QPushButton { background-color : rgb(0,255,0) }")
             print("Right Doors Opened")

        if self.RightDoors.isChecked() == False:
             self.RightDoors.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")
             print("Left Doors Closed")


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QtWidgets.QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
# Show window
window.show()

# Start the event loop.
app.exec()