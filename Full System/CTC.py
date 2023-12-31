import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Train import Train
from Track import Track
from Line import Line
from signals import signals
from copy import deepcopy
sys.dont_write_bytecode = True

greenRouteArr = [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
                82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 85, 84,
                83, 82, 81, 80, 79, 78, 77, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
                112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128,
                129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145,
                146, 147, 148, 149, 150, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15,
                14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
                43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]

redRouteArr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
               31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
               53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 52, 51, 50, 49, 48, 47, 46, 45,
               44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 
               22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]

class CTC(QObject):
    def __init__(self, track):
        super().__init__()
        self.track = track
        self.wayside = None
        self.nextID = 1
        self.greenTotalTickets = 0
        self.redTotalTickets = 0
        self.greenThroughput = 0
        self.redThroughput = 0
        self.totalElapsedSeconds = 1
        self.totalElapsedHours = 0

        # signals from ctc UI
        signals.greenLineTrainDispatchFromCtcUI.connect(self.greenDispatch)
        signals.redLineTrainDispatchFromCtcUI.connect(self.redDispatch)
        signals.ctcSwitchStates.connect(self.sendSwitchStates)
        signals.trackModelPassengersToCTC.connect(self.incrementTickets)
        signals.timerTicked.connect(self.incrementTime)

    # function to dispatch the train
    def greenDispatch(self, destBlock):
        # create a new track object and emit to wayside
        destBlock.append(57)
        train = Train(self.nextID, self.track.getLine('Green'), destBlock)
        train.authority = 8
        train.suggSpeed = 70
        train.route = deepcopy(greenRouteArr)

        signals.waysideDispatchTrain.emit(train)
        signals.ctcCreateGUITrainInfo.emit(train.line.lineName, train.ID, train.block, train.authority, train.destBlock[0])

        # update the next ID of the next train
        self.nextID += 1

    # function to dispatch the train
    def redDispatch(self, destBlock):
        # create a new track object and emit to wayside
        destBlock.append(9)
        train = Train(self.nextID, self.track.getLine('Red'), destBlock)
        train.authority = 8
        train.suggSpeed = 40
        train.route = deepcopy(redRouteArr)

        signals.waysideDispatchTrain.emit(train)
        signals.ctcCreateGUITrainInfo.emit(train.line.lineName, train.ID, train.block, train.authority, train.destBlock)

        # update the next ID of the next train
        self.nextID += 1

    def incrementTickets(self, tickets, line):
        if line == "Green":
            self.greenTotalTickets += tickets

        elif line == "Red":
            self.redTotalTickets += tickets
    
    def incrementTime(self):
        if self.totalElapsedSeconds == 3600:
            self.totalElapsedSeconds = 1
            self.totalElapsedHours += 1
        else:
            self.totalElapsedSeconds += 1
        self.calculateThroughput()

    def calculateThroughput(self):
        self.greenThroughput = self.greenTotalTickets / (self.totalElapsedHours + (float(self.totalElapsedSeconds) /100))
        self.redThroughput = self.redTotalTickets / (self.totalElapsedHours + (float(self.totalElapsedSeconds) /100))
        greenFormatted = "{:.2f}".format(self.greenThroughput)
        redFormatted = "{:.2f}".format(self.redThroughput)
        signals.ctcThroughput.emit(greenFormatted, "Green")
        signals.ctcThroughput.emit(redFormatted, "Red")

    def sendSwitchStates(self, greenSwitches, redSwitches):
        signals.switchStatesFromCTCtoWayside.emit(greenSwitches, redSwitches)

    def propagateTrack(self):
        signals.trackCTCToWayside.emit(self.track)

    def addWayside(self, Wayside):
        self.wayside = Wayside