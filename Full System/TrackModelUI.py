import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QSize
from BlockInfo import BlockInfo
from FaultDisplay import FaultDisplay
from Fault import Fault
from Section import Section
import TrackParser 
from signals import signals

# Main Window Class
class TrackModelUI(QtWidgets.QMainWindow):
    def __init__(self, track, *args, **kwargs):
        # instantiate the original track
        self.track = track

        super().__init__(*args, **kwargs)
        uic.loadUi("MainTrackModel.ui", self)
        self.setWindowTitle('Track Model UI')
        self.GreenLineGenInfo.setStyleSheet('font-size: 16')
        self.RedLineGenInfo.setStyleSheet('font-size: 16')

        # create section dictionary to hold sections
        self.sectionDict = {}

        # create items in scroll area based on track that was instantiated 
        self.createLineItem(self.sectionDict)

        # create the file brower object
        self.fileBrowser = QtWidgets.QFileDialog()

        # connect all buttons to block pages
        for section in self.sectionDict:
            self.sectionDict[section].button.clicked.connect(lambda ch, i=self.sectionDict[section].section: self.generateBlockInfoPage(i))

        # populate broken line and block dropdowns
        self.populateLineSelect()
        self.brokenRailLineSelect.currentTextChanged.connect(self.populateBlockSelect)

        # connect upload track button to open that page
        self.UploadTrack.clicked.connect(self.openTrackUpload)

        # connect a button to show the fault window
        self.FaultWindowButton.clicked.connect(self.showFaultWindow)

        self.RedFaultLayout = QtWidgets.QVBoxLayout()
        self.GreenFaultLayout = QtWidgets.QVBoxLayout()

        self.RedFaultWidget = QtWidgets.QWidget()
        self.RedFaultWidget.setLayout(self.RedFaultLayout)
        self.GreenFaultWidget = QtWidgets.QWidget()
        self.GreenFaultWidget.setLayout(self.GreenFaultLayout)

        self.faultWindow = FaultDisplay(self.track)

        # connect temperature button
        self.tempGo.clicked.connect(self.tempChanged)

        # connect murphy buttons
        self.brokenRailButton.clicked.connect(self.breakRail)
        self.powerFailure.clicked.connect(self.powerFailed)
        self.circuitFailure.clicked.connect(self.circuitFailed)
        self.fixButton.clicked.connect(self.fixFaults)

        # connect signals
        signals.trackModelUpdateGUIOccupancy.connect(self.updateOccupancy)
        signals.trackModelUpdateGUIVacancy.connect(self.updateVacancy)
        signals.timerTicked.connect(self.updateTime)
        # signals.trackModelBrokenRail.connect(self.updateFaults)
        
        # connect test ui signals
        signals.trackModelTestUIUpdateGUIOccupancy.connect(self.updateOccupancy)
        signals.trackModelTestUIUpdateGUIVacancy.connect(self.updateVacancy)
        signals.trackModelTestUIUpdateGUICrossings.connect(self.changeCrossings)
        signals.trackModelTestUIUpdateGUISwitches.connect(self.changeSwitch)
        signals.trackModelTestUIUpdateFault.connect(self.updateFaults)
        signals.trackModelTempUpdated.connect(self.tempUpdate)

    def updateTime(self, hrs, mins, secs):
        self.time.setText(f'{int(hrs):02d}' + ':' + f'{int(mins):02d}' + ':' + f'{int(secs):02d}')

    # update occupancy
    def updateOccupancy(self, inLine, inBlock):

        line = self.track.getLine(inLine)
        block = line.getBlock(inBlock)
        section = block.section
    
        # if block is already occupied, do nothing
        if block.occupied:
            return    

        block.occupied = True

        # update total train counts
        if line.lineName == 'Red':
            self.RedTrainCt.setText(str(int(self.RedTrainCt.text()) + 1))
        else:
            self.GreenTrainCt.setText(str(int(self.GreenTrainCt.text()) + 1))

        # create index string to access dict 
        index = line.lineName + section

        # increment train count on main UI
        self.sectionDict[index].trainCount.setText(str(int(self.sectionDict[index].trainCount.text()) + 1))

        # edit blocks occupied list
        currentText = self.sectionDict[index].occupied.text()

        # if text is currently blank, replace with block
        # if not, append to list
        if currentText == '-':
            self.sectionDict[index].occupied.setText(block.blockName)
        else:
            currentText += ' ' + block.blockName
            self.sectionDict[index].occupied.setText(currentText)

    # update vacancy
    def updateVacancy(self, inLine, inBlock):
        line = self.track.getLine(inLine)
        block = line.getBlock(inBlock)
        section = block.section

        # if block is not occupied, don't do anything
        if not block.occupied:
            return    

        block.occupied = False

        # update total line truck count
        if line.lineName == 'Red':
            self.RedTrainCt.setText(str(int(self.RedTrainCt.text()) - 1))
        else:
            self.GreenTrainCt.setText(str(int(self.GreenTrainCt.text()) - 1))

        # create index string to access dict 
        index = line.lineName + section

        # decrement train count on main UI
        self.sectionDict[index].trainCount.setText(str(int(self.sectionDict[index].trainCount.text()) - 1))

        # edit blocks occupied list
        currentText = self.sectionDict[index].occupied.text()

        # if text is currently only 1 block, replace with blank
        # if not, append to list
        if len(currentText.split()) == 1:
            self.sectionDict[index].occupied.setText('-')
        elif currentText.split()[0] == block.blockName: 
            currentText = currentText.replace(block.blockName + ' ', '')
            self.sectionDict[index].occupied.setText(currentText)
        else:
            currentText = currentText.replace(' ' + block.blockName, '')
            self.sectionDict[index].occupied.setText(currentText)

    # update switch states
    def changeSwitch(self, inLine, inBlock, switchSelect):
        self.track.getLine(inLine).getBlock(inBlock).switchConnection = switchSelect

    # update faults from test UI
    def updateFaults(self, inLine, inBlock, faultType):
        if faultType == 'Broken Rail':
            # highlight Broken Rail orange
            self.BrokenRailLabel.setStyleSheet("color: orange")
        elif faultType == 'Power':
            # highlight Power orange
            self.PowerFaultLabel.setStyleSheet("color: orange")
        else: 
            # highlight Broken Circuit orange
            self.BrokenCircuitLabel.setStyleSheet("color: orange")

        # create a fault in the fault class
        fault = Fault(faultType, inBlock, inLine)

        # if the same line/block already is broken, don't create another
        if faultType == 'Broken Rail' and not self.track.faultExists(fault):
            self.track.addFault(fault)
            signals.trackModelUpdateGUIFaults.emit(fault)

        # if there is already a power fault on the track, don't create another
        if faultType == 'Power' and len(self.track.faults['Power']) == 0:
            # add the fault to the track
            self.track.addFault(fault)
            signals.trackModelUpdateGUIFaults.emit(fault)

        # if there is already a track circuit fault on the track, don't create another
        if faultType == 'Broken Circuit' and len(self.track.faults['Broken Circuit']) == 0:
            # add the fault to the track
            self.track.addFault(fault)
            signals.trackModelUpdateGUIFaults.emit(fault)

    # update rail to break
    def breakRail(self):
        line = self.brokenRailLineSelect.currentText()
        block = self.brokenRailBlockSelect.currentText()

        if line != '' and block != '':
            signals.trackModelBrokenRail.emit(line, block, 'Broken Rail')
        
        self.updateFaults(line, block, 'Broken Rail')

    def powerFailed(self):
        line = self.brokenRailLineSelect.currentText()
        signals.trackModelPowerFailure.emit()
        self.updateFaults(line, '0', 'Power')

    def circuitFailed(self):
        line = self.brokenRailLineSelect.currentText()
        signals.trackModelCircuitFailure.emit()
        self.updateFaults(line, '0', 'Broken Circuit')

    def fixFaults(self):
        # clear the track faults dictionary
        for key in self.track.faults:
            self.track.faults[key].clear()

        # set the color of the labels back to black
        self.BrokenRailLabel.setStyleSheet("color: black")
        self.PowerFaultLabel.setStyleSheet("color: black")
        self.BrokenCircuitLabel.setStyleSheet("color: black")

    # change RR X-ings
    def changeCrossings(self, crossing):
        if crossing == 1:
            self.I47Status.setText("Active")
            self.I47Status.setStyleSheet("border: 2px solid rgb(0, 221, 109); color: rgb(15, 125, 0); background-color: rgb(159, 255, 157)")
            self.E19Status.setText("Active")
            self.E19Status.setStyleSheet("border: 2px solid rgb(0, 221, 109); color: rgb(15, 125, 0); background-color: rgb(159, 255, 157)")
        elif crossing == 2:
            self.I47Status.setText("Active")
            self.I47Status.setStyleSheet("border: 2px solid rgb(0, 221, 109); color: rgb(15, 125, 0); background-color: rgb(159, 255, 157)")
            self.E19Status.setText("Inactive")
            self.E19Status.setStyleSheet("border: 2px solid rgb(188, 6, 0); color: rgb(148, 0, 17); background-color: rgb(255, 135, 119)")
        elif crossing == 3:
            self.I47Status.setText("Inactive")
            self.I47Status.setStyleSheet("border: 2px solid rgb(188, 6, 0); color: rgb(148, 0, 17); background-color: rgb(255, 135, 119)")
            self.E19Status.setText("Active")
            self.E19Status.setStyleSheet("border: 2px solid rgb(0, 221, 109); color: rgb(15, 125, 0); background-color: rgb(159, 255, 157)")
        else:
            self.I47Status.setText("Inactive")
            self.I47Status.setStyleSheet("border: 2px solid rgb(188, 6, 0); color: rgb(148, 0, 17); background-color: rgb(255, 135, 119)")
            self.E19Status.setText("Inactive")
            self.E19Status.setStyleSheet("border: 2px solid rgb(188, 6, 0); color: rgb(148, 0, 17); background-color: rgb(255, 135, 119)")

    # update the heaters based on temp -- add monthly temp
    def tempUpdate(self, temp):
        # turn heaters on if temp is lower than monthly temp
        if temp >= 39:
            self.HeaterStatus.setText("Off")
            self.HeaterStatus.setStyleSheet("border: 2px solid rgb(188, 6, 0); color: rgb(148, 0, 17); background-color: rgb(255, 135, 119)")
        else:
            self.HeaterStatus.setText("On")
            self.HeaterStatus.setStyleSheet("border: 2px solid rgb(0, 221, 109); color: rgb(15, 125, 0); background-color: rgb(159, 255, 157)")

        # display current temp on mainUI
        self.CurrentTempLabel.setText("Current Temp: " + str(temp))

    def tempChanged(self):
        # if entry is nonsense, do nothing
        if not self.tempEntry.text().isnumeric(): 
            return

        signals.trackModelTempUpdated.emit(int(self.tempEntry.text()))

    def createLineItem(self, sectionDict):
        scrollArea = [self.RedLineScrollArea, self.GreenLineScrollArea]

        i = 0
        for line in self.track.lines:
            self.widget = QtWidgets.QWidget()
            self.vbox = QtWidgets.QVBoxLayout()

            for section in line.sections:
                self.hbox = QtWidgets.QHBoxLayout()

                # create labels and add to the hbox
                blockLabel = QtWidgets.QLabel(section.sectionName, self)
                blockLabel.setFixedHeight(50)
                blockLabel.setFixedWidth(75)
                blockLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.hbox.addWidget(blockLabel)

                # create label for # of trains
                trainCount = QtWidgets.QLabel(str(section.numTrains), self)
                trainCount.setFixedHeight(50)
                trainCount.setFixedWidth(75)
                trainCount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.hbox.addWidget(trainCount)

                # create label for occupancy
                occupiedLabel = QtWidgets.QLabel('-', self)
                occupiedLabel.setFixedHeight(50)
                occupiedLabel.setFixedWidth(50)
                occupiedLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.hbox.addWidget(occupiedLabel)

                # create info button and add to hbox
                button = QtWidgets.QPushButton(text='INFO')
                button.setFixedWidth(50)
                self.hbox.addWidget(button)

                row = RowWidget(section, blockLabel, trainCount, occupiedLabel, button)

                sectionDict[line.lineName + section.sectionName] = row

                # add row to vbox
                self.vbox.addLayout(self.hbox)

            # add widget to the scroll area
            self.widget.setLayout(self.vbox)
            scrollArea[i].setWidget(self.widget)

            # increment the scroll area used
            i+=1

    def generateBlockInfoPage(self, section):
        self.blockInfo = BlockInfo(section)

        self.openBlockInfo()

    def openBlockInfo(self):
        self.blockInfo.show()

    def openTrackUpload(self):
        # open the file explorer 
        response = self.fileBrowser.getOpenFileNames(
            caption='Select File',
            directory=os.getcwd(),
            initialFilter='Data File (*.csv)'
        )

        # test to make sure filename isn't blank (upload canceled)
        try:
            filename = str(response[0][0])
            self.reparseTrack(filename)
        except: 
            print('no file selected')

    def reparseTrack(self, filename):
        # put the track into a new track class with the parser
        self.track = TrackParser.parseTrack(filename)

        # recreate the ui with new track
        # clear the widgets from the scroll area
        self.RedLineScrollArea.removeWidget

    def showFaultWindow(self):
        self.faultWindow.show()

    def populateLineSelect(self):
        for line in self.track.lines:
            self.brokenRailLineSelect.addItem(line.lineName)
        
        line = self.brokenRailLineSelect.currentText()
        for block in self.track.getLine(line).blocks:
            self.brokenRailBlockSelect.addItem(block.blockName)
        
    def populateBlockSelect(self):
        self.brokenRailBlockSelect.clear()
        line = self.brokenRailLineSelect.currentText()

        for block in self.track.getLine(line).blocks:
            self.brokenRailBlockSelect.addItem(block.blockName)
# end main UI class

# class for row objects that go in the scroll window
class RowWidget():
    def __init__(self, section, blockLabel, trainCount, occupied, button):
        self.section = section
        self.blockLabel = blockLabel
        self.trainCount = trainCount
        self.occupied = occupied
        self.button = button