import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Train import Train
from Track import Track
from Line import Line
from signals import signals
sys.dont_write_bytecode = True

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

        # signals from ctc UI
        signals.greenLineTrainDispatchFromCtcUI.connect(self.greenDispatch)
        signals.ctcSwitchStates.connect(self.sendSwitchStates)
        
    # function to dispatch the train
    def dispatch(self, line, destBlock):
        # create a new track object and emit to wayside
        train = Train(self.nextID, self.track.getLine(line), destBlock)
        train.authority = 3
        train.suggSpeed = 70
        print('ctc dispatched')

        signals.waysideDispatchTrain.emit(train)

        # update the next ID of the next train
        self.nextID += 1

    # function to dispatch the train
    def greenDispatch(self, destBlock):
        # create a new track object and emit to wayside
        print(destBlock[0])
        train = Train(self.nextID, self.track.getLine('Green'), destBlock)
        train.authority = 3
        train.suggSpeed = 70
        print('ctc dispatched')

        signals.waysideDispatchTrain.emit(train)
        signals.ctcCreateGUITrainInfo.emit(train.line.lineName, train.ID, train.block, train.authority, train.destBlock)

        # update the next ID of the next train
        self.nextID += 1

    def calculateThroughput(self, tickets, line):
        
        if line == "Green":
            self.greenTotalTickets += tickets
            signals.ctcGetPassengersPerLine.emit(self.greenTotalTickets, "Green")

        elif line == "Red":
            self.redTotalTickets += tickets
            signals.ctcGetPassengersPerLine.emit(self.redTotalTickets, "Red")

        else:
            print("error")

    def sendSwitchStates(self, greenSwitches, redSwitches):
        signals.switchStatesFromCTCtoWayside.emit(greenSwitches, redSwitches)

    def propagateTrack(self):
        signals.trackCTCToWayside.emit(self.track)

    def addWayside(self, Wayside):
        self.wayside = Wayside