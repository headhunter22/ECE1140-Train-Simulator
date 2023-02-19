import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QSize
import TrackParser


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("TestUI.ui", self)
        self.setWindowTitle('Track Model Test UI')

        # add line & block options based on the track object
        for line in track.lines:
            self.SwitchLineSelect.addItem(line.lineName)
            self.OccLineSel.addItem(line.lineName)
            self.FaultLineSelect.addItem(line.lineName)

        for section in track.lines[0].sections:
            for block in section.blocks:
                self.SwitchBlockSelect.addItem(block.blockName)
                self.OccBlockSel.addItem(block.blockName)
                self.FaultBlockSelect.addItem(block.blockName)

        self.Connection.setText(track.lines[0].sections[0].blocks[0].infrastructure)

        # connect crossing checkboxes
        self.RedXing.toggled.connect(self.getCrossingStatuses)
        self.GreenXing.toggled.connect(self.getCrossingStatuses)

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

    # FUNCTIONS
    # function to change the track heater status based on temp input
    def tempChanged(self):
        if not self.tempEntry.text().isnumeric(): 
            return
        if int(self.tempEntry.text()) >= 39:
            self.HeaterStatus.setText("Heater Status: OFF")
        else:
            self.HeaterStatus.setText("Heater Status: ON")

    # function to get crossing statuses when they change
    def getCrossingStatuses(self):
        print([self.RedXing.isChecked(), self.GreenXing.isChecked()])

    # function to change dropdowns for switch selection
    def switchLineChanged(self, line):
        # clear current options in the dropdowns 
        self.SwitchBlockSelect.clear()

        # add the appropriate blocks
        for section in track.getLine(line).sections:
            for block in section.blocks:
                self.SwitchBlockSelect.addItem(block.blockName)

        # add connection if there is one
        self.switchBlockChanged()

    def switchBlockChanged(self):
        # update the label for the connection
        self.Connection.setText(track.getLine(self.SwitchLineSelect.currentText()).getBlock(self.SwitchBlockSelect.currentText()).infrastructure)    

    def occLineChanged(self, line):
        # clear current options in the dropdowns 
        self.OccBlockSel.clear()

        # add the appropriate blocks
        for section in track.getLine(line).sections:
            for block in section.blocks:
                self.OccBlockSel.addItem(block.blockName)

    def faultLineChanged(self, line):
        # clear current options in the dropdowns 
        self.FaultBlockSelect.clear()

        # add the appropriate blocks
        for section in track.getLine(line).sections:
            for block in section.blocks:
                self.FaultBlockSelect.addItem(block.blockName)

    def setOcc(self):
        track.getLine(self.OccLineSel.currentText()).getBlock(self.OccBlockSel.currentText()).occupied = True        

    def setVac(self):
        track.getLine(self.OccLineSel.currentText()).getBlock(self.OccBlockSel.currentText()).occupied = False

#end class definition

#defining the app and the window
# parse the track file
track = TrackParser.parseTrack('Track Layout.csv')
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()