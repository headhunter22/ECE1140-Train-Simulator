import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Train import Train
from Track import Track
from Line import Line
from signals import signals
sys.dont_write_bytecode = True

#please work please

class CTC(QObject):
    def __init__(self, track):
        super().__init__()
        self.track = track
        self.wayside = None
        self.nextID = 1

        # signals from ctc UI
        signals.greenLineTrainDispatchFromCtcUI.connect(self.greenDispatch)
        
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
        train = Train(self.nextID, self.track.getLine('Green'), destBlock)
        train.authority = 3
        train.suggSpeed = 70
        print('ctc dispatched')

        signals.waysideDispatchTrain.emit(train)

        # update the next ID of the next train
        self.nextID += 1

    def propagateTrack(self):
        signals.trackCTCToWayside.emit(self.track)

    def addWayside(self, Wayside):
        self.wayside = Wayside