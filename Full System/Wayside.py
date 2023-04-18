import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Train import Train
from Track import Track
from Block import Block
from signals import signals
import sys
sys.dont_write_bytecode = True

class Wayside(QObject):

    def __init__(self, ctcOffice):
        super().__init__()
        self.CTC = ctcOffice
        self.greenSwitchStates = [1, 1, 0, 0, 0, 0]

        # connect signals
        signals.waysideDispatchTrain.connect(self.dispatchTrain)
        signals.trackCTCToWayside.connect(self.trackReceived)
        signals.waysideUpdateOccupancy.connect(self.blockOccupancyReceived)
        signals.waysideUpdateVacancy.connect(self.blockVacancyReceived)
        #signals.waysideCommandedSpeed.connect(self.commspeed)
        signals.actuallyshutup.connect(self.imoverthis)
        # signals.waysideinstance1.connect(self.wayside1range)#TODO
        # signals.waysideinstance2.connect(self.wayside2range)#TODO
        # signals.waysideinstance3.connect(self.wayside3range)#TODO
        # signals.waysideinstance4.connect(self.wayside4range)#TODO
        
    # function to dispatch a train
    # hard coded for green line for the time being

    def imoverthis(self):
        print("make it stop")
        signals.please.emit()
        
    def commspeed(self, train):
        if (train.authority == '0'):
            commSpeed = 0
        else:
            commSpeed = train.suggSpeed

        signals.waysideCommandedSpeed.emit(commSpeed)

    def dispatchTrain(self, train):
        # set occupancy of first block
        #self.setOccupancy(train.line, 63, 1)

        print('wayside dispatched')
        # compare suggSpeed to commandedSpeed
        #speedLimit = self.track.getLine('Green').getBlock(63).speedLimit
        self.commspeed(train)
        # emit dispatched train to track model
        signals.trackModelDispatchTrain.emit(train)
        signals.count = signals.count + 1
        signals.wtowTrainCount.emit(signals.count)
        

    # function to set block occupancies
    #def setOccupancy(self, line, blockNumber, occupied):
        #line.getBlock(blockNumber).occupancy = occupied

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
        signals.trackWaysideToTrackModel.emit(track)

    def blockOccupancyReceived(self, block):
        print("wayside block occupancy from track model")
        #print(". py block", block, "is occupied")
        signals.wtowOccupancy.emit(block)
    
    def blockVacancyReceived(self, block):
        print("wayside block vacancy from track model")
        #print(".py block", block, "is vacant")
        signals.wtowVacancy.emit(block)

    def passengersReceived(self, passengers): #dont touch send to CTC
        self.passengers = passengers
        self.passengersToCTC.emit(passengers)

    def addTrackModel(self, trackModel):
        self.trackModel = trackModel
        #self.trackModel.blockOccupancyToWayside.connect(self.blockOccupancyReceived)
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