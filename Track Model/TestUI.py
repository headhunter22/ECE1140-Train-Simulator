import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
import TrackParser
from MainWindow import MainWindow
from Fault import Fault

# Test UI class
class TestUI(QtWidgets.QMainWindow):
    occupancyPressed = pyqtSignal(str, str)
    vacancyPressed = pyqtSignal(str, str)
    crossingChanged = pyqtSignal(int)

    def __init__(self, track, *args, **kwargs):
        self.track = track

        super().__init__(*args, **kwargs)
        uic.loadUi("TestUI.ui", self)
        self.setWindowTitle('Track Model Test UI')

        # add line & block options based on the track object
        for line in self.track.lines:
            self.SwitchLineSelect.addItem(line.lineName)
            self.OccLineSel.addItem(line.lineName)
            self.FaultLineSelect.addItem(line.lineName)

        for section in self.track.lines[0].sections:
            for block in section.blocks:
                self.SwitchBlockSelect.addItem(block.blockName)
                self.OccBlockSel.addItem(block.blockName)
                self.FaultBlockSelect.addItem(block.blockName)

        # set up options for switch buttons
        self.SwitchOption1.clicked.connect(self.changeSwitchOpt1)
        self.SwitchOption2.clicked.connect(self.changeSwitchOpt2)

        # connect crossing checkboxes
        self.RedXing.toggled.connect(self.changeCrossingStatuses)
        self.GreenXing.toggled.connect(self.changeCrossingStatuses)

        # connect dropdowns to switching functions
        self.SwitchBlockSelect.currentTextChanged.connect(self.switchBlockChanged)
        self.SwitchLineSelect.currentTextChanged.connect(self.switchLineChanged)
        self.OccLineSel.currentTextChanged.connect(self.occLineChanged)
        self.FaultLineSelect.currentTextChanged.connect(self.faultLineChanged)

        # connect occupied/vacant buttons
        self.setOccupied.clicked.connect(self.setOcc)
        self.setVacant.clicked.connect(self.setVac)

        # connect enter temperature button
        self.EnterTemp.clicked.connect(self.tempChanged)

        # link fault go button
        self.FaultGoButton.clicked.connect(lambda: self.induceFault(self.FaultTypeSelect.currentText()))

    # FUNCTIONS
    # function to change the track heater status based on temp input
    def tempChanged(self):
        # if entry is nonsense, do nothing
        if not self.tempEntry.text().isnumeric(): 
            return

        # turn heaters on if temp is lower than 39deg
        if int(self.tempEntry.text()) >= 39:
            self.HeaterStatus.setText("Heater Status: OFF")
            MainWindow.HeaterStatus.setText("Off")
            MainWindow.HeaterStatus.setStyleSheet("border: 2px solid rgb(188, 6, 0); color: rgb(148, 0, 17); background-color: rgb(255, 135, 119)")
        else:
            self.HeaterStatus.setText("Heater Status: ON")
            MainWindow.HeaterStatus.setText("On")
            MainWindow.HeaterStatus.setStyleSheet("border: 2px solid rgb(0, 221, 109); color: rgb(15, 125, 0); background-color: rgb(159, 255, 157)")

        # display current temp on mainUI
        MainWindow.CurrentTempLabel.setText("Current Temp: " + self.tempEntry.text())

    # function to get crossing statuses when they change
    def changeCrossingStatuses(self):
        if self.RedXing.isChecked() and self.GreenXing.isChecked():
            self.crossingChanged.emit(1) 
        elif self.RedXing.isChecked() and not self.GreenXing.isChecked():
            self.crossingChanged.emit(2)
        elif not self.RedXing.isChecked() and self.GreenXing.isChecked():
            self.crossingChanged.emit(3)
        else:
            self.crossingChanged.emit(4)

    # function to change dropdowns for switch selection
    def switchLineChanged(self, line):
        # clear current options in the dropdowns 
        self.SwitchBlockSelect.clear()

        # add the appropriate blocks
        for section in self.track.getLine(line).sections:
            for block in section.blocks:
                self.SwitchBlockSelect.addItem(block.blockName)

        # add connection if there is one
        self.switchBlockChanged()

    def switchBlockChanged(self):
        # update the label for the connection
        infrastructureText = self.track.getLine(self.SwitchLineSelect.currentText()).getBlock(self.SwitchBlockSelect.currentText()).infrastructure

        # if its not a switch, don't display
        if 'SWITCH' not in infrastructureText or 'YARD' in infrastructureText:
            self.SwitchOption1.setText("")
            self.SwitchOption2.setText("")
            return

        # parse out the options
        start = infrastructureText.find('(')
        middle = infrastructureText.find(';') 
        end = infrastructureText.find(')')

        opt1 = infrastructureText[start+1:middle] 
        opt2 = infrastructureText[middle+1:end]

        self.SwitchOption1.setText(opt1)
        self.SwitchOption2.setText(opt2)

    def occLineChanged(self, line):
        # clear current options in the dropdowns 
        self.OccBlockSel.clear()

        # add the appropriate blocks
        for section in self.track.getLine(line).sections:
            for block in section.blocks:
                self.OccBlockSel.addItem(block.blockName)

    def faultLineChanged(self, line):
        # clear current options in the dropdowns 
        self.FaultBlockSelect.clear()

        # add the appropriate blocks
        for section in self.track.getLine(line).sections:
            for block in section.blocks:
                self.FaultBlockSelect.addItem(block.blockName)

    def setOcc(self):
        self.occupancyPressed.emit(self.OccLineSel.currentText(), self.OccBlockSel.currentText())
        
    def setVac(self):
        self.vacancyPressed.emit(self.OccLineSel.currentText(), self.OccBlockSel.currentText())

    def changeSwitchOpt1(self):
        self.track.getLine(self.SwitchLineSelect.currentText()).getBlock(self.SwitchBlockSelect.currentText()).switchConnection = self.SwitchOption1.text()

    def changeSwitchOpt2(self):
        self.track.getLine(self.SwitchLineSelect.currentText()).getBlock(self.SwitchBlockSelect.currentText()).switchConnection = self.SwitchOption2.text()

    # needs to send signal
    def induceFault(self, faultType):
        # create label for rail breakages scroll and add to section
        faultLabel = QtWidgets.QLabel(self.FaultLineSelect.currentText() + ' ' + self.FaultBlockSelect.currentText(), self)
        faultLabel.setFixedHeight(30)

        if faultType == 'Broken Rail':
            # highlight Broken Rail orange
            MainWindow.BrokenRailLabel.setStyleSheet("color: orange")

            # add to broken rails section
            if self.FaultLineSelect.currentText() == 'Red':
                MainWindow.RedFaultLayout.addWidget(faultLabel)
            else:
                MainWindow.GreenFaultLayout.addWidget(faultLabel)
        elif faultType == 'Power':
            # highlight Power orange
            MainWindow.PowerFaultLabel.setStyleSheet("color: orange")
        else: 
            # highlight Broken Circuit orange
            MainWindow.BrokenCircuitLabel.setStyleSheet("color: orange")

        ''' THIS NEEDS TO BE ADDED TO A SIGNAL SENT
        # create fault object
        fault = Fault(faultType, faultLabel.text())

        # add to faultDict
        if faultType not in faultDict:
            faultDict[faultType] = [fault.location]
        else:
            faultDict[faultType].append(fault.location)
        '''

#end TestUI class