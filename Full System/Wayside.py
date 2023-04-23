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

        self.wayside1range = []#GREEN
        self.wayside1sectionrange = []
        self.wayside2range = []
        self.wayside2sectionrange = []
        self.wayside3range = []
        self.wayside3sectionrange = []
        self.wayside4range = []
        self.wayside4sectionrange = []
        self.wayside5range = []#RED
        self.wayside5sectionrange = []
        self.wayside6range = []
        self.wayside6sectionrange = []
        self.wayside7range = []
        self.wayside7sectionrange = []
        self.wayside8range = []
        self.wayside8sectionrange = []

        self.track0 = []
        self.track1 = []
        self.section0 = []
        self.section1 = []
        self.stations0 = []
        self.stations1 = []
        self.switchLocations0 = []
        self.switchLocations1 = []
        self.switchStates0 = []
        self.switchStates1 = []

        # connect signals
        signals.waysideDispatchTrain.connect(self.dispatchTrain)
        signals.trackCTCToWayside.connect(self.trackReceived)
        signals.waysideUpdateOccupancy.connect(self.blockOccupancyReceived)
        signals.waysideUpdateVacancy.connect(self.blockVacancyReceived)
        #signals.waysideCommandedSpeed.connect(self.commspeed)
        signals.waysideinstances.connect(self.plcinfo)

        signals.switchStatesFromCTCtoWayside.connect(self.switchSignalTest)
        signals.testAuthTrackModelToWayside.connect(self.testAuthority)

        signals.waysideTrackfromPLC.connect(self.setTracks)
        signals.waysideSectionsfromPLC.connect(self.setSections)
        signals.waysideSwitchLocationsfromPLC.connect(self.setSwitchLocations)
        signals.waysideSwitchStatesfromPLC.connect(self.setSwitchStates)
        signals.waysideStationsfromPLC.connect(self.setStations)

        #get switch change from ctc
        #pass on switch state pass stem and branch (int, int)
        #authority start at 8 and decrement if next next next ... is a stop,or switch in wrong direction
        #have CTC send authority as 0 and 1 not red and green
        #vacant signals need to be one behind occupied
        #send section with occupancy

    def setTracks(self, track0, track1):
        self.track0 = track0
        self.track1 = track1

    def setSections(self, section0, section1):
        self.section0 = section0
        self.section1 = section1

    def setStations(self, s0, s1):
        self.stations0 = s0
        self.stations1 = s1

    def setSwitchLocations(self, loc0, loc1):
        self.switchLocations0 = loc0
        self.switchLocations1 = loc1

    def setSwitchStates(self, state0, state1):
        self.switchStates0 = state0
        self.switchStates1 = state1

    def updateAuthority(self, line, block, route):
        #print("authority starts at 8")
        auth = 8
        currblock = self.track0.index(block)
        
        print("authority currblock", currblock)
        print("authority line", line)
        
        
        if line == 'Green':
            #print("in green")
            next1 = self.track0[currblock+1]
            #print("authority next1", next1)
            next2 = self.track0[currblock+2]
            #print("authority next2", next2)
            next3 = self.track0[currblock+3]
            next4 = self.track0[currblock+4]
            next5 = self.track0[currblock+5]
            next6 = self.track0[currblock+6]
            next7 = self.track0[currblock+7]
            next8 = self.track0[currblock+8]

            for i in self.stations0:
                if i == next8:
                    auth = 7
                elif i == next7:
                    auth = 6
                elif i == next6:
                    auth = 5
                elif i == next5:
                    auth = 4
                elif i == next4:
                    auth = 3
                elif i == next3:
                    auth = 2
                elif i == next2:
                    auth = 1
                elif i == next1:
                    auth = 0
                else:
                    auth = 8
        elif line == 'Red':
            #print("in red")
            next1 = self.track1[currblock+1]
            #print("authority next1", next1)
            next2 = self.track1[currblock+2]
            #print("authority next2", next2)
            next3 = self.track1[currblock+3]
            next4 = self.track1[currblock+4]
            next5 = self.track1[currblock+5]
            next6 = self.track1[currblock+6]
            next7 = self.track1[currblock+7]
            next8 = self.track1[currblock+8]

            for i in self.stations1:
                if i == next8:
                    auth = 7
                elif i == next7:
                    auth = 6
                elif i == next6:
                    auth = 5
                elif i == next5:
                    auth = 4
                elif i == next4:
                    auth = 3
                elif i == next3:
                    auth = 2
                elif i == next2:
                    auth = 1
                elif i == next1:
                    auth = 0
                else:
                    auth = 8

        signals.waysideAuthoritytoTrack.emit(auth, currblock)
        signals.testWaysideAuthorityToCTC.emit(line, route, auth)

    def plcinfo(self, range1, section1, range2, section2, range3, section3, range4, section4, range5, section5, range6, section6, range7, section7, range8, section8):#, range):
        signals.sections.emit(section1, section2, section3, section4, section5, section6, section7, section8)
        self.wayside1sectionrange = section1
        self.wayside2sectionrange = section2
        self.wayside3sectionrange = section3
        self.wayside4sectionrange = section4
        self.wayside5sectionrange = section5
        self.wayside6sectionrange = section6
        self.wayside7sectionrange = section7
        self.wayside8sectionrange = section8

        signals.ranges.emit(range1, range2, range3, range4, range5, range6, range7, range8)
        self.wayside1range = range1
        self.wayside2range = range2
        self.wayside3range = range3
        self.wayside4range = range4
        self.wayside5range = range5
        self.wayside6range = range6
        self.wayside7range = range7
        self.wayside8range = range8
        #print("signals sent in .py plcinfo")
        
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

    def blockOccupancyReceived(self, line, block, route):
        #print(". py block", block, "is occupied")
        signals.wtowOccupancy.emit(block)
        self.updateAuthority(line, block, route)
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

    def testAuthority(self, line, route):
        #signals.testWaysideAuthorityToCTC.emit(line, route)
        pass

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