import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QSize
import TrackParser
from Fault import Fault

# Test UI class
class TestUI(QtWidgets.QMainWindow):

    def __init__(self, track, *args, **kwargs):
        self.track = track

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
            window.HeaterStatus.setText("Off")
            window.HeaterStatus.setStyleSheet("border: 2px solid rgb(188, 6, 0); color: rgb(148, 0, 17); background-color: rgb(255, 135, 119)")
        else:
            self.HeaterStatus.setText("Heater Status: ON")
            window.HeaterStatus.setText("On")
            window.HeaterStatus.setStyleSheet("border: 2px solid rgb(0, 221, 109); color: rgb(15, 125, 0); background-color: rgb(159, 255, 157)")

        # display current temp on mainUI
        window.CurrentTempLabel.setText("Current Temp: " + self.tempEntry.text())

    # function to get crossing statuses when they change
    def changeCrossingStatuses(self):
        if self.RedXing.isChecked(): 
            window.I47Status.setText("Active")
            window.I47Status.setStyleSheet("border: 2px solid rgb(0, 221, 109); color: rgb(15, 125, 0); background-color: rgb(159, 255, 157)")
        else:
            window.I47Status.setText("Inactive")
            window.I47Status.setStyleSheet("border: 2px solid rgb(188, 6, 0); color: rgb(148, 0, 17); background-color: rgb(255, 135, 119)")
        
        if self.GreenXing.isChecked():
            window.E19Status.setText("Active")
            window.E19Status.setStyleSheet("border: 2px solid rgb(0, 221, 109); color: rgb(15, 125, 0); background-color: rgb(159, 255, 157)")
        else:
            window.E19Status.setText("Inactive")
            window.E19Status.setStyleSheet("border: 2px solid rgb(188, 6, 0); color: rgb(148, 0, 17); background-color: rgb(255, 135, 119)")

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
        infrastructureText = track.getLine(self.SwitchLineSelect.currentText()).getBlock(self.SwitchBlockSelect.currentText()).infrastructure

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
        line = track.getLine(self.OccLineSel.currentText())
        block = line.getBlock(self.OccBlockSel.currentText())
        section = block.section
    
        # if block is already occupied, do nothing
        if block.occupied:
            return    

        block.occupied = True

        # change total train count
        if line.lineName == 'Red':
            window.RedTrainCt.setText(str(int(window.RedTrainCt.text()) + 1))
        else:
            window.GreenTrainCt.setText(str(int(window.GreenTrainCt.text()) + 1))

        # create index string to access dict 
        index = line.lineName + section

        # increment train count on main UI
        sectionDict[index].trainCount.setText(str(int(sectionDict[index].trainCount.text()) + 1))

        # edit blocks occupied list
        currentText = sectionDict[index].occupied.text()

        # if text is currently blank, replace with block
        # if not, append to list
        if currentText == '-':
            sectionDict[index].occupied.setText(block.blockName)
        else:
            currentText += ' ' + block.blockName
            sectionDict[index].occupied.setText(currentText)

    def setVac(self):
        line = track.getLine(self.OccLineSel.currentText())
        block = line.getBlock(self.OccBlockSel.currentText())
        section = block.section

        # if block is not occupied, don't do anything
        if not block.occupied:
            return    

        block.occupied = False

        # update total line truck count
        if line.lineName == 'Red':
            window.RedTrainCt.setText(str(int(window.RedTrainCt.text()) - 1))
        else:
            window.GreenTrainCt.setText(str(int(window.GreenTrainCt.text()) - 1))

        # create index string to access dict 
        index = line.lineName + section

        # decrement train count on main UI
        sectionDict[index].trainCount.setText(str(int(sectionDict[index].trainCount.text()) - 1))

        # edit blocks occupied list
        currentText = sectionDict[index].occupied.text()

        # if text is currently only 1 block, replace with blank
        # if not, append to list
        if len(currentText.split()) == 1:
            sectionDict[index].occupied.setText('-')
        elif currentText.split()[0] == block.blockName: 
            currentText = currentText.replace(block.blockName + ' ', '')
            sectionDict[index].occupied.setText(currentText)
        else:
            currentText = currentText.replace(' ' + block.blockName, '')
            sectionDict[index].occupied.setText(currentText)

    def changeSwitchOpt1(self):
        track.getLine(self.SwitchLineSelect.currentText()).getBlock(self.SwitchBlockSelect.currentText()).switchConnection = self.SwitchOption1.text()

    def changeSwitchOpt2(self):
        track.getLine(self.SwitchLineSelect.currentText()).getBlock(self.SwitchBlockSelect.currentText()).switchConnection = self.SwitchOption2.text()

    def induceFault(self, faultType):
        # create label for rail breakages scroll and add to section
        faultLabel = QtWidgets.QLabel(self.FaultLineSelect.currentText() + ' ' + self.FaultBlockSelect.currentText(), self)
        faultLabel.setFixedHeight(30)

        if faultType == 'Broken Rail':
            # highlight Broken Rail orange
            window.BrokenRailLabel.setStyleSheet("color: orange")

            # add to broken rails section
            if self.FaultLineSelect.currentText() == 'Red':
                window.RedFaultLayout.addWidget(faultLabel)
            else:
                window.GreenFaultLayout.addWidget(faultLabel)
        elif faultType == 'Power':
            # highlight Power orange
            window.PowerFaultLabel.setStyleSheet("color: orange")
        else: 
            # highlight Broken Circuit orange
            window.BrokenCircuitLabel.setStyleSheet("color: orange")

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