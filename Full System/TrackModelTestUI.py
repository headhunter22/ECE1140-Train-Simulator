import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
import TrackParser
from Fault import Fault
from signals import signals

# Test UI class
class TestUI(QtWidgets.QMainWindow):

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
                if block.switchStem:
                    self.SwitchBlockSelect.addItem(block.blockName)
                self.OccBlockSel.addItem(block.blockName)
                self.FaultBlockSelect.addItem(block.blockName)

            self.SwitchOption1.setText('0')
            self.SwitchOption2.setText('10')

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

        signals.trackModelTempUpdated.emit(int(self.tempEntry.text()))

    # function to get crossing statuses when they change
    def changeCrossingStatuses(self):
        if self.RedXing.isChecked() and self.GreenXing.isChecked():
            signals.trackModelTestUIUpdateGUICrossings.emit(1) 
        elif self.RedXing.isChecked() and not self.GreenXing.isChecked():
            signals.trackModelTestUIUpdateGUICrossings.emit(2)
        elif not self.RedXing.isChecked() and self.GreenXing.isChecked():
            signals.trackModelTestUIUpdateGUICrossings.emit(3)
        else:
            signals.trackModelTestUIUpdateGUICrossings.emit(4)

    # function to change dropdowns for switch selection
    def switchLineChanged(self, line):
        # clear current options in the dropdowns 
        self.SwitchBlockSelect.clear()

        # add the appropriate blocks
        for section in self.track.getLine(line).sections:
            for block in section.blocks:
                if block.switchStem:
                    self.SwitchBlockSelect.addItem(block.blockName)

        # display options for first switch
        if line == 'Green':
            self.SwitchOption1.setText('1')
            self.SwitchOption2.setText('12')
        else:
            self.SwitchOption1.setText('0')
            self.SwitchOption2.setText('10')

    def switchBlockChanged(self):
        line = self.SwitchLineSelect.currentText()

        try:    
            self.SwitchOption1.setText(self.track.getLine(line).getBlock(self.SwitchBlockSelect.currentText()).swOpt1)
            self.SwitchOption2.setText(self.track.getLine(line).getBlock(self.SwitchBlockSelect.currentText()).swOpt2)
        except:
            pass

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
        signals.trackModelTestUIUpdateGUIOccupancy.emit(self.OccLineSel.currentText(), self.OccBlockSel.currentText())
        
    def setVac(self):
        signals.trackModelTestUIUpdateGUIVacancy.emit(self.OccLineSel.currentText(), self.OccBlockSel.currentText())

    def changeSwitchOpt1(self):
        signals.trackModelUpdateGUISwitches.emit(int(self.SwitchBlockSelect.currentText()), int(self.SwitchOption1.text()))

    def changeSwitchOpt2(self):
        signals.trackModelUpdateGUISwitches.emit(int(self.SwitchBlockSelect.currentText()), int(self.SwitchOption2.text()))

    def induceFault(self, faultType):
        signals.trackModelTestUIUpdateFault.emit(self.FaultLineSelect.currentText(), self.FaultBlockSelect.currentText(), faultType)

#end TestUI class