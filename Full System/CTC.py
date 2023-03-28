import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Train import Train
from Track import Track

#to commit

class CTC(QObject):
    trackCTCToWayside = pyqtSignal(Track)
    authorityToWayside = pyqtSignal(Train)
    suggSpeedToWayside = pyqtSignal(Train)
    trainObjectToWayside = pyqtSignal(Train)
    switchStates = pyqtSignal(int, bool)

    def __init__(self, track):
        super().__init__()
        self.track = track
        
    def dispatch(self, a, s, id, line):
        train = Train(a, s, id, line)
        self.authorityToWayside.emit(train)
        self.suggSpeedToWayside.emit(train)
        self.trainObjectToWayside.emit(train)

    def propagateTrack(self):
        self.trackCTCToWayside.emit(self.track)