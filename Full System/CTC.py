import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Train import Train
from Track import Track
from TrainController import TrainController

class CTC(QObject):
    trackCTCToWayside = pyqtSignal(Track)
    authorityToWayside = pyqtSignal(Train)
    suggSpeedToWayside = pyqtSignal(Train)
    trainObjectToWayside = pyqtSignal(Train)
    switchStates = pyqtSignal(int, bool)

    def __init__(self, track, clock):
        super().__init__()
        self.track = track
        self.wayside = None
        self.clock = clock
        
    def dispatch(self, a, s, id, line, track, clock):
        train = Train(a, s, id, line, 120, 0, TrainController(), track, clock)
        self.authorityToWayside.emit(train)
        self.suggSpeedToWayside.emit(train)
        self.trainObjectToWayside.emit(train)
        self.wayside.changeRoute(train)

    def propagateTrack(self):
        self.trackCTCToWayside.emit(self.track)

    def addWayside(self, Wayside):
        self.wayside = Wayside