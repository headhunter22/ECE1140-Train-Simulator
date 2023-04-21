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

    def __init__(self, ctcOffice, mainui):
        super().__init__()
        self.CTC = ctcOffice
        self.ui = mainui
        self.greenSwitchStates = [1, 1, 0, 0, 0, 0]

        # connect signals
        signals.waysideDispatchTrain.connect(self.dispatchTrain)
        signals.trackCTCToWayside.connect(self.trackReceived)
        signals.waysideUpdateOccupancy.connect(self.blockOccupancyReceived)
        signals.waysideUpdateVacancy.connect(self.blockVacancyReceived)
        #signals.waysideCommandedSpeed.connect(self.commspeed)
        signals.waysideinstances.connect(self.plcinfo)

        signals.switchStatesFromCTCtoWayside.connect(self.switchSignalTest)
        
    # function to dispatch a train
    # hard coded for green line for the time being

        #get switch change from ctc
        #pass on switch state pass stem and branch (int, int)
        #authority start at 8 and decrement if next next next ... is a stop,or switch in wrong direction

    def plcinfo(self, wayside1range, wayside1sectionrange, wayside2range, wayside2sectionrange, wayside3range, wayside3sectionrange, wayside4range, wayside4sectionrange):#, range):
        signals.sections.emit(wayside1sectionrange, wayside2sectionrange, wayside3sectionrange, wayside4sectionrange)
        signals.ranges.emit(wayside1range, wayside2range, wayside3range, wayside4range)
        
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

    def sendAuthority(self, blocks):
        print("authority from Wayside to Track:", str(blocks))
        signals.waysideAuthority.emit(blocks)
        
    def suggSpeedReceived(self, train):
        print("speed from CTC to Wayside: " + str(train.suggSpeed))

    def trainReceived(self, train):
        # pass train onto track model
        self.trainObjectWaysideToTrackModel.emit(train)

    def trackReceived(self, track):
        self.track = track

        # pass track onto track model
        signals.trackWaysideToTrackModel.emit(track)

    def blockOccupancyReceived(self, line, block):
        #print(". py block", block, "is occupied")
        signals.wtowOccupancy.emit(block)
        
        #occupancy sent to the CTC Office
        signals.ctcUpdateGUIOccupancy.emit(line, block)
    
    def blockVacancyReceived(self, line, block):
        #print(".py block", block, "is vacant")
        signals.wtowVacancy.emit(block)

        #vacancy sent to the CTC Office
        signals.ctcUpdateGUIOccupancy.emit(line, block)

    def passengersReceived(self, passengers): #dont touch send to CTC
        self.passengers = passengers
        signals.passengersToCTC.emit(passengers)

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

    def switchSignalTest(self, greenStates, redStates):
        print("Green:")
        print("C:" , greenStates[0])
        print("G:" , greenStates[1])
        print("J:" , greenStates[2])
        print("J:" , greenStates[3])
        print("M:" , greenStates[4])
        print("N:" , greenStates[5])
        print("\n\nRed:")
        print("C:" , redStates[0])
        print("H:" , redStates[1])
        print("H:" , redStates[2])
        print("H:" , redStates[3])
        print("H:" , redStates[4])
        print("H:" , redStates[5])
        print("J:" , redStates[6])
        print("\n\n")