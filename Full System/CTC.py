import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Train import Train
from Track import Track
from TrainController import TrainController

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
        self.wayside = None
        
    def dispatch(self, a, s, id, line):
        print("1")
        train = Train(a, s, id, line, 120, 0, TrainController())
        print("2")
        self.authorityToWayside.emit(train)
        print("3")
        self.suggSpeedToWayside.emit(train)
        print("4")
        self.trainObjectToWayside.emit(train)
        print("5")
        self.wayside.changeRoute(train)
        print("after dispatch")

    def propagateTrack(self):
        self.trackCTCToWayside.emit(self.track)

    def addWayside(self, Wayside):
        self.wayside = Wayside