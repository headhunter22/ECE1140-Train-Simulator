import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QSize
from BlockInfo import BlockInfo
from FaultDisplay import FaultDisplay
import TrackParser 

# Main Window Class
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, track, *args, **kwargs):
        # instantiate the original track
        self.track = track

        super().__init__(*args, **kwargs)
        uic.loadUi("MainTrackModel.ui", self)
        self.setWindowTitle('Track Model UI')

        # create section dictionary to hold sections
        self.sectionDict = {}

        # create items in scroll area based on track that was instantiated 
        self.createLineItem(self.sectionDict)

        # connect all buttons to block pages
        for section in self.sectionDict:
            self.sectionDict[section].button.clicked.connect(lambda ch, i=self.sectionDict[section].section: self.generateBlockInfoPage(i))

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

        self.RedBreakagesScroll.setWidget(self.RedFaultWidget)
        self.GreenBreakagesScroll.setWidget(self.GreenFaultWidget)

    # update occupancy
    def updateOccupancy(self, inLine, inBlock):
        # have to send current line and block through signal !!!
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

    def changeSwitch(self, inLine, inBlock):
        return

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

    # take away middle man window
    def openTrackUpload(self):
        self.uploadWindow = UploadFile()
        self.uploadWindow.show()

    def showFaultWindow(self):
        self.faultWindow = FaultDisplay(self.track)
        self.faultWindow.show()
# end main UI class

# class for row objects that go in the scroll window
class RowWidget():
    def __init__(self, section, blockLabel, trainCount, occupied, button):
        self.section = section
        self.blockLabel = blockLabel
        self.trainCount = trainCount
        self.occupied = occupied
        self.button = button