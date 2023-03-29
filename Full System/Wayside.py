import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Train import Train
from Track import Track

class Wayside(QObject):

    # signals to track model
    suggSpeedWaysideToTrackModel = pyqtSignal(Train)
    trainObjectWaysideToTrackModel = pyqtSignal(Train)
    commandedSpeedWaysideToTrackModel = pyqtSignal(int)
    trackWaysideToTrackModel = pyqtSignal(Track)
    greenLineSwitches = pyqtSignal(int)

    

    # signals to CTC
    passengersToCTC = pyqtSignal(int)

    def __init__(self, ctcOffice):
        super().__init__()
        self.CTC = ctcOffice
        self.trackModel = 0
        self.greenSwitchStates = [1, 1, 0, 0, 0, 0]

        self.CTC.authorityToWayside.connect(self.authorityReceived)
        self.CTC.suggSpeedToWayside.connect(self.suggSpeedReceived)
        self.CTC.trainObjectToWayside.connect(self.trainReceived)
        self.CTC.trackCTCToWayside.connect(self.trackReceived)
        #self.switchStatesToWayside.connect(self.switchStateReceived)
        

    def authorityReceived(self, train):
        print("authority from CTC to Wayside: " + str(train.authority))
        
    def suggSpeedReceived(self, train):
        print("speed from CTC to Wayside: " + str(train.suggSpeed))

    def trainReceived(self, train):
        # pass train onto track model
        self.trainObjectWaysideToTrackModel.emit(train)

    def trackReceived(self, track):
        self.track = track

        # pass track onto track model
        self.trackWaysideToTrackModel.emit(track)

    def blockOccupancyReceived(self, Block):
        print("block occupancy from track model")

    def passengersReceived(self, passengers):
        self.passengers = passengers
        self.passengersToCTC.emit(passengers)

    def addTrackModel(self, trackModel):
        self.trackModel = trackModel
        self.trackModel.blockOccupancyToWayside.connect(self.blockOccupancyReceived)
        self.trackModel.totalPassengersToWayside.connect(self.passengersReceived)

    def changeRoute(self, train):

        print(str(train.location))

        if train.location == 3:
            self.greenSwitchStates[0] = 0
        if train.location == 15:
            self.greenSwitchStates[0] = 1


        if train.location == 27:
            self.greenSwitchStates[1] = 0
        if train.location == 148:
            self.greenSwitchStates[1] = 1


        if train.location == 55:
            self.greenSwitchStates[2] = 0
        if train.location == 60: # wont be on 60 for now
            self.greenSwitchStates[2] = 1


        if train.location == 60: # wont be on 60 for now
            self.greenSwitchStates[3] = 1
        else:
            self.greenSwitchStates[3] = 0


        if train.location == 74:
            self.greenSwitchStates[4] = 0
        if train.location == 79:
            self.greenSwitchStates[4] = 1


        if train.location == 83:
            self.greenSwitchStates[5] = 0
        if train.location == 98:
            self.greenSwitchStates[5] = 1

        self.greenLineSwitches.emit(self.greenSwitchStates)

        print("sw 1: " + str(self.greenSwitchStates[0]))
        print("sw 2: " + str(self.greenSwitchStates[1]))
        print("sw 3: " + str(self.greenSwitchStates[2]))
        print("sw 4: " + str(self.greenSwitchStates[3]))
        print("sw 5: " + str(self.greenSwitchStates[4]))
        print("sw 6: " + str(self.greenSwitchStates[5]))





        

    # def switchStateReceived(self, bl, updw):
    #     self.switch = sw
    #     print("authority from CTC to Wayside: " + str(self.authority))