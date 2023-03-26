import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Train import Train
from Track import Track

class Wayside(QObject):

    suggSpeedWaysideToTrackModel = pyqtSignal(Train)
    trainObjectWaysideToTrackModel = pyqtSignal(Train)
    commandedSpeedWaysideToTrackModel = pyqtSignal(int)
    trackWaysideToTrackModel = pyqtSignal(Track)

    def __init__(self, ctcOffice):
        super().__init__()
        self.CTC = ctcOffice
        self.trackModel = 0

        self.CTC.authorityToWayside.connect(self.authorityReceived)
        self.CTC.suggSpeedToWayside.connect(self.suggSpeedReceived)
        self.CTC.trainObjectToWayside.connect(self.trainReceived)
        self.CTC.trackCTCToWayside.connect(self.trackReceived)
        #self.switchStatesToWayside.connect(self.switchStateReceived)
        

    def authorityReceived(self, a):
        self.authority = a
        print("authority from CTC to Wayside: " + str(self.authority))
        
    def suggSpeedReceived(self, train):
        print("speed from CTC to Wayside: " + str(train.suggSpeed))
        print("authority from CTC to Wayside: " + str(train.authority))
        self.suggSpeedWaysideToTrackModel.emit(train)

    def trainReceived(self, train):
        # pass train onto track model
        self.trainObjectWaysideToTrackModel.emit(train)

    def trackReceived(self, track):
        self.track = track

        # pass track onto track model
        self.trackWaysideToTrackModel.emit(track)

    def blockOccupancyReceived(self, Block):
        print("block occupancy from track model")

    def addTrackModel(self, trackModel):
        self.trackModel = trackModel
        self.trackModel.blockOccupancyToWayside.connect(self.blockOccupancyReceived)

    # def switchStateReceived(self, bl, updw):
    #     self.switch = sw
    #     print("authority from CTC to Wayside: " + str(self.authority))
        