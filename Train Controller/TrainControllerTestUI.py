from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class TestUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Train Controller Test UI")
        self.resize(980, 620)

            # Commanded Speed slider init #
        self.CommSpeedSlider = QtWidgets.QSlider(self)
        self.CommandedSpeed = QtWidgets.QLabel("Commanded Speed", self)
        self.CommSpeedSlider.setGeometry(800, 25, 50, 250)
        self.CommandedSpeed.setGeometry(750, 250, 200, 100)
        self.CommSpeedSlider.setMinimum(-100)
        self.CommSpeedSlider.setMaximum(100)
        self.CommSpeedSlider.setSingleStep(1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CommandedSpeed.setFont(font)
        self.CommSpeedSlider.valueChanged.connect(self.CommandedSpeedChange)

            # Authority Request init # 
        self.AuthoritySlider = QtWidgets.QSlider(self)
        self.AuthLabel = QtWidgets.QLabel("Authority", self)
        self.AuthoritySlider.setGeometry(800, 325, 50, 250)
        self.AuthLabel.setGeometry(795, 575, 100, 25)
        self.AuthoritySlider.setMinimum(0)
        self.AuthoritySlider.setMaximum(10)
        self.AuthoritySlider.setSingleStep(1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AuthLabel.setFont(font)
        self.AuthoritySlider.valueChanged.connect(self.AuthorityChange)

        # Headlight signal Display #
        self.TestHeadlights = QtWidgets.QPushButton(" ", self)
        self.TestHeadlights.setGeometry(50, 50, 50, 50)
        self.TestHeadlights.setCheckable(False)
        self.TestHeadlights.setStyleSheet("QPushButton { background-color : rgb(255,0,0)}")
        self.TestHeadlightsLabel = QtWidgets.QLabel("Headlights", self)
        self.TestHeadlightsLabel.setGeometry(105, 50, 200, 50)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TestHeadlightsLabel.setFont(font)

        # Internal Lights signal Display #
        self.TestInternalLights = QtWidgets.QPushButton(" ", self)
        self.TestInternalLights.setGeometry(50, 105, 50, 50)
        self.TestInternalLights.setCheckable(False)
        self.TestInternalLights.setStyleSheet("QPushButton { background-color : rgb(255,0,0)}")
        self.TestInternalLightsLabel = QtWidgets.QLabel("Internal Lights", self)
        self.TestInternalLightsLabel.setGeometry(105, 105, 200, 50)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TestInternalLightsLabel.setFont(font)

        # Left Doors signal Display #
        self.TestLeftDoors = QtWidgets.QPushButton(" ", self)
        self.TestLeftDoors.setGeometry(50, 160, 50, 50)
        self.TestLeftDoors.setCheckable(False)
        self.TestLeftDoors.setStyleSheet("QPushButton { background-color : rgb(255,0,0)}")
        self.TestLeftDoorsLabel = QtWidgets.QLabel("Left Doors", self)
        self.TestLeftDoorsLabel.setGeometry(105, 160, 200, 50)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TestLeftDoorsLabel.setFont(font)

        # Right Doors signal Display #
        self.TestRightDoors = QtWidgets.QPushButton(" ", self)
        self.TestRightDoors.setGeometry(50, 215, 50, 50)
        self.TestRightDoors.setCheckable(False)
        self.TestRightDoors.setStyleSheet("QPushButton { background-color : rgb(255,0,0)}")
        self.TestRightDoorsLabel = QtWidgets.QLabel("Right Doors", self)
        self.TestRightDoorsLabel.setGeometry(105, 215, 200, 50)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TestRightDoorsLabel.setFont(font)

        # Emergency Brake signal Display #
        self.TestEmerBrake = QtWidgets.QPushButton(" ", self)
        self.TestEmerBrake.setGeometry(50, 270, 50, 50)
        self.TestEmerBrake.setCheckable(False)
        self.TestEmerBrake.setStyleSheet("QPushButton { background-color : rgb(255,0,0)}")
        self.TestEmerBrakeLabel = QtWidgets.QLabel("Emergency Brake", self)
        self.TestEmerBrakeLabel.setGeometry(105, 270, 200, 50)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TestEmerBrakeLabel.setFont(font)

        # Showing Test Power Output #
        self.TestPowerShown = QtWidgets.QPushButton("0 Watts", self)
        self.TestPowerShown.setGeometry(425, 50, 200, 100)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.TestPowerShown.setFont(font)
        self.TestPowerShown.setCheckable(False)
        self.TestPowerShown.setStyleSheet("QPushButton { background-color : rgb(255,255,255) }")

        # Manual Mode signal Display #
        self.TestManualMode = QtWidgets.QPushButton(" ", self)
        self.TestManualMode.setGeometry(50, 325, 50, 50)
        self.TestManualMode.setCheckable(False)
        self.TestManualMode.setStyleSheet("QPushButton { background-color : rgb(255,0,0)}")
        self.TestManualModeLabel = QtWidgets.QLabel("Manual Mode", self)
        self.TestManualModeLabel.setGeometry(105, 325, 200, 50)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TestManualModeLabel.setFont(font)

        # Auto Mode signal Display #
        self.TestAutoMode = QtWidgets.QPushButton(" ", self)
        self.TestAutoMode.setGeometry(50, 380, 50, 50)
        self.TestAutoMode.setCheckable(False)
        self.TestAutoMode.setStyleSheet("QPushButton { background-color : rgb(255,0,0)}")
        self.TestAutoModeLabel = QtWidgets.QLabel("Auto Mode", self)
        self.TestAutoModeLabel.setGeometry(105, 380, 200, 50)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TestAutoModeLabel.setFont(font)

    def CommandedSpeedChange(self, j):
         window.CommandedSpeed.setText("Commanded Speed: {0}mph".format(j))

    def AuthorityChange(self, k):
         window.Authority.setText("Authority: {0}mi".format(k))

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QtWidgets.QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = TestUI()
# Show window
window.show()

# Start the event loop.
#app.exec()