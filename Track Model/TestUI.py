import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
import TrackParser
from Fault import Fault

# Test UI class
class TestUI(QtWidgets.QMainWindow):
    occupancyPressed = pyqtSignal(str, str)
    vacancyPressed = pyqtSignal(str, str)
    crossingChanged = pyqtSignal(int)
    switchChanged = pyqtSignal(str, str, str)
    tempSignal = pyqtSignal(int)
    faultSignal = pyqtSignal(str, str, str)

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

        self.tempSignal.emit(int(self.tempEntry.text()))

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
        if self.SwitchBlockSelect.currentText() == '':
            return 

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

    # function to change dropdowns for occupancy selection
    def occLineChanged(self, line):
        # clear current options in the dropdowns 
        self.OccBlockSel.clear()

        # add the appropriate blocks
        for section in self.track.getLine(line).sections:
            for block in section.blocks:
                self.OccBlockSel.addItem(block.blockName)

    # function to change dropdowns for fault selection
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
        self.switchChanged.emit(self.SwitchLineSelect.currentText(), self.SwitchBlockSelect.currentText(), self.SwitchOption1.text())

    def changeSwitchOpt2(self):
        self.switchChanged.emit(self.SwitchLineSelect.currentText(), self.SwitchBlockSelect.currentText(), self.SwitchOption2.text())

    def induceFault(self, faultType):
        # emit signal
        self.faultSignal.emit(self.FaultLineSelect.currentText(), self.FaultBlockSelect.currentText(), faultType)

#end TestUI class