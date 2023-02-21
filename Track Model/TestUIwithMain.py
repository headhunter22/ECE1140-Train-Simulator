import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QSize
import TrackParser

sectionDict = {}

# Test UI class
class TestUI(QtWidgets.QMainWindow):

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
        track.getLine(self.SwitchLineSelect.currentText()).getBlock(self.SwitchBlockSelect.currentText()).switchConnection = True

    def changeSwitchOpt2(self):
        track.getLine(self.SwitchLineSelect.currentText()).getBlock(self.SwitchBlockSelect.currentText()).switchConnection = False
#end TestUI class 

# Main Window Class
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("MainTrackModel.ui", self)
        self.setWindowTitle('Track Model UI')

        # create items in scroll area based on track that was instantiated 
        self.createLineItem(sectionDict)

        # connect all buttons to block pages
        for section in sectionDict:
            self.blockInfo = BlockInfo()
            sectionDict[section].button.clicked.connect(self.openBlockInfo)

    def createLineItem(self, sectionDict):
        scrollArea = [self.RedLineScrollArea, self.GreenLineScrollArea]

        i = 0
        for line in track.lines:
            self.widget = QtWidgets.QWidget()
            self.vbox = QtWidgets.QVBoxLayout()

            for section in line.sections:
                self.hbox = QtWidgets.QHBoxLayout()

                # create labels and add to the hbox
                sectionLabel = QtWidgets.QLabel(section.sectionName, self)
                sectionLabel.setFixedHeight(50)
                sectionLabel.setFixedWidth(75)
                sectionLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.hbox.addWidget(sectionLabel)

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

                row = RowWidget(sectionLabel, trainCount, occupiedLabel, button)

                sectionDict[line.lineName + section.sectionName] = row

                # add row to vbox
                self.vbox.addLayout(self.hbox)

            # add widget to the scroll area
            self.widget.setLayout(self.vbox)
            scrollArea[i].setWidget(self.widget)

            # increment the scroll area used
            i+=1


    #def generateBlockInfoPage():


    def openBlockInfo(self):
        self.generateBlockInfoPage()
        self.blockInfo.show()

# end main UI class

# class for row objects that go in the scroll window
class RowWidget():
    def __init__(self, section, trainCount, occupied, button):
        self.section = section
        self.trainCount = trainCount
        self.occupied = occupied
        self.button = button

# Main Window Class
class BlockInfo(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("BlockInfo.ui", self)
        self.setWindowTitle('Block Info')

# defining the app and the window
# parse the track file
track = TrackParser.parseTrack('Track Layout.csv')
app = QtWidgets.QApplication(sys.argv)

# create window objects
testWindow = TestUI()
window = MainWindow()

# show windows
testWindow.show()
window.show()

app.exec()