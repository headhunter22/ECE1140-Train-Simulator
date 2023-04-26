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

#get switch change from ctc
#pass on switch state pass stem and branch (int, int)
#vacant signals need to be one behind occupied (is now sending one ahead))
#make switch array so you can display like section popups


class Wayside(QObject):

    def __init__(self, ctcOffice, mainui):
        super().__init__()
        self.CTC = ctcOffice
        self.ui = mainui
        self.greenSwitchStates = [1, 1, 0, 0, 0, 0]
        self.dest = []
        self.route = []

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
        self.everythingtrack0 = []
        self.everythingtrack1 = []
        self.section0 = []
        self.section1 = []
        self.allsection0 = []
        self.allsection1 = []
        self.stations0 = []
        self.stations1 = []
        self.switchLocations0 = []
        self.switchLocations1 = []
        self.switchStates0 = []
        self.switchStates1 = []
        self.switchDefaults0 = []
        self.switchDefaults1 = []
        self.switchMatrix0 = []
        self.switchMatrix1 = []

        # connect signals
        signals.waysideDispatchTrain.connect(self.dispatchTrain)
        signals.trackCTCToWayside.connect(self.trackReceived)
        signals.waysideUpdateOccupancy.connect(self.blockOccupancyReceived)
        signals.waysideUpdateVacancy.connect(self.blockVacancyReceived)
        #signals.waysideCommandedSpeed.connect(self.commspeed)
        signals.waysideinstances.connect(self.plcinfo)

        signals.switchStatesFromCTCtoWayside.connect(self.changeSwitchfromCTC)
        #signals.blockMaintenanceFromCTCtoWayside.connect(self.test)
        signals.trackModelTrainInfoToWayside.connect(self.trainInfoToCTC)

        signals.waysideTrackfromPLC.connect(self.setTracks)
        signals.waysideSectionsfromPLC.connect(self.setSections)
        signals.waysideSwitchLocationsfromPLC.connect(self.setSwitchLocations)
        signals.waysideSwitchStatesfromPLC.connect(self.setSwitchStates)
        signals.waysideStationsfromPLC.connect(self.setStations)
        signals.waysideAllSectionsfromPLC.connect(self.setAllSections)

        
    def setTracks(self, track0, track1, etrack0, etrack1):
        self.track0 = track0
        self.track1 = track1
        self.everythingtrack0 = etrack0
        self.everythingtrack1 = etrack1

    def setSections(self, section0, section1):
        self.section0 = section0
        self.section1 = section1

    def setAllSections(self, section0, section1):
        self.allsection0 = section0
        self.allsection1 = section1

    def setStations(self, s0, s1):
        #print("stations s0 s1", s0, s1)
        self.stations0 = s0
        self.stations1 = s1

    def setSwitchLocations(self, loc0, loc1, mat0, mat1):
        print("setswitchlocaitons .py")
        self.switchLocations0 = loc0
        self.switchLocations1 = loc1
        self.switchMatrix0 = mat0
        self.switchMatrix1 = mat1
        signals.wtowSwitchesSetup.emit(mat0, mat1)
        
    def setSwitchStates(self, state0, state1):
        print("defaults in set .py")
        self.switchStates0 = state0
        self.switchStates1 = state1
        self.switchDefaults0 = state0
        self.switchDefaults1 = state1
        
        signals.wtowSwitchDefaults.emit(self.switchDefaults0, self.switchDefaults1)
        

    def updateAuthority(self, line, block, route):
        #print("authority starts at 8")
        auth = 8
        #print("authority currblock", currblock)
        #print("authority line", line)
        if line == 'Green':
            #print("in green")
            currblock = self.track0.index(block)
            #print("current block", currblock)
            nextblock1 = int(self.everythingtrack0[currblock].nextBlock)
            nextindex1 = self.track0.index(nextblock1)
            #print("1 next block and index", nextblock1, nextindex1)
            nextblock2 = int(self.everythingtrack0[nextindex1].nextBlock)
            nextindex2 = self.track0.index(nextblock2)
            #print("2 next block and index", nextblock2, nextindex2)
            nextblock3 = int(self.everythingtrack0[nextindex2].nextBlock)
            nextindex3 = self.track0.index(nextblock3)
            #print("3 next block and index", nextblock3, nextindex3)
            nextblock4 = int(self.everythingtrack0[nextindex3].nextBlock)
            nextindex4 = self.track0.index(nextblock4)
            #print("4 next block and index", nextblock4, nextindex4)
            nextblock5 = int(self.everythingtrack0[nextindex4].nextBlock)
            nextindex5 = self.track0.index(nextblock5)
            #print("5 next block and index", nextblock5, nextindex5)
            nextblock6 = int(self.everythingtrack0[nextindex5].nextBlock)  
            nextindex6 = self.track0.index(nextblock6)
            #print("6 next block and index", nextblock6, nextindex6)
            nextblock7 = int(self.everythingtrack0[nextindex6].nextBlock)
            nextindex7 = self.track0.index(nextblock7)
            #print("7 next block and index", nextblock7, nextindex7)
            nextblock8 = int(self.everythingtrack0[nextindex7].nextBlock)
            nextindex8 = self.track0.index(nextblock8) 
            #print("8 next block and index", nextblock8, nextindex8)                                                                           
            #print("next blocks:", nextblock1, nextblock2, nextblock3,nextblock4, nextblock5, nextblock6, nextblock7, nextblock8)
            #print("stations", self.stations0)

            for i in self.dest:
                #print("i from inside loop as int", int(i))
                if int(i) == block:
                    auth = 0
                    #print("i = block0", int(i), block)
                    break
                elif int(i) == nextblock1:
                    auth = 1
                    #print("i = block1", int(i), nextblock1)
                    break
                elif int(i) == nextblock2:
                    auth = 2
                    #print("i = block2", int(i), nextblock2)
                    break
                elif int(i) == nextblock3:
                    auth = 3
                    #print("i = block3", int(i), nextblock3)
                    break
                elif int(i) == nextblock4:
                    auth = 4
                    #print("i = block4", int(i), nextblock4)
                    break
                elif int(i) == nextblock5:
                    auth = 5
                    #print("i = block5", int(i), nextblock5)
                    break
                elif int(i) == nextblock6:
                    auth = 6
                    #print("i = block6", int(i), nextblock6)
                    break
                elif int(i) == nextblock7:
                    auth = 7
                    #print("i = block7", int(i), nextblock7)
                    break
                elif int(i) == nextblock8:
                    auth = 8
                    #print("i = block8", int(i), nextblock8)
                    break
        elif line == 'Red':
            #print("in green")
            currblock = self.track1.index(block)
            #print("current block", currblock)
            nextblock1 = int(self.everythingtrack1[currblock].nextBlock)
            nextindex1 = self.track1.index(nextblock1)
            #print("1 next block and index", nextblock1, nextindex1)
            nextblock2 = int(self.everythingtrack1[nextindex1].nextBlock)
            nextindex2 = self.track1.index(nextblock2)
            #print("2 next block and index", nextblock2, nextindex2)
            nextblock3 = int(self.everythingtrack1[nextindex2].nextBlock)
            nextindex3 = self.track1.index(nextblock3)
            #print("3 next block and index", nextblock3, nextindex3)
            nextblock4 = int(self.everythingtrack1[nextindex3].nextBlock)
            nextindex4 = self.track1.index(nextblock4)
            #print("4 next block and index", nextblock4, nextindex4)
            nextblock5 = int(self.everythingtrack1[nextindex4].nextBlock)
            nextindex5 = self.track1.index(nextblock5)
            #print("5 next block and index", nextblock5, nextindex5)
            nextblock6 = int(self.everythingtrack1[nextindex5].nextBlock)  
            nextindex6 = self.track1.index(nextblock6)
            #print("6 next block and index", nextblock6, nextindex6)
            nextblock7 = int(self.everythingtrack1[nextindex6].nextBlock)
            nextindex7 = self.track1.index(nextblock7)
            #print("7 next block and index", nextblock7, nextindex7)
            nextblock8 = int(self.everythingtrack1[nextindex7].nextBlock)
            nextindex8 = self.track1.index(nextblock8) 
            #print("8 next block and index", nextblock8, nextindex8)   
            #print("next blocks:", nextblock1, nextblock2, nextblock3,nextblock4, nextblock5, nextblock6, nextblock7, nextblock8)
            for i in self.dest:
                if int(i) == block:
                    auth = 0
                elif int(i) == nextblock1:
                    auth = 1
                elif int(i) == nextblock2:
                    auth = 2
                elif int(i) == nextblock3:
                    auth = 3
                elif int(i) == nextblock4:
                    auth = 4
                elif int(i) == nextblock5:
                    auth = 5
                elif int(i) == nextblock6:
                    auth = 6
                elif int(i) == nextblock7:
                    auth = 7
                elif int(i) == nextblock8:
                    auth = 8
        #print("wayside.py update authority auth", auth)
        signals.waysideAuthoritytoTrack.emit(auth, currblock)
        signals.waysideAuthorityToCTC.emit(line, route, auth)

    def plcinfo(self, range1, section1, range2, section2, range3, section3, range4, section4, range5, section5, range6, section6, range7, section7, range8, section8):#, range):
        #print("plcinfo start")
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
        #print(".py plcinfo 1 range self.", self.wayside1range)
        self.wayside2range = range2
        self.wayside3range = range3
        self.wayside4range = range4
        self.wayside5range = range5
        self.wayside6range = range6
        self.wayside7range = range7
        self.wayside8range = range8
        #print("signals sent in .py plcinfo")
        
    # def commspeed(self, train):
    #     if (train.authority == '0'):
    #         commSpeed = 0
    #     else:
    #         commSpeed = train.suggSpeed

    #     signals.waysideCommandedSpeed.emit(commSpeed)

    def dispatchTrain(self, train):
        # set occupancy of first block
        #self.setOccupancy(train.line, 63, 1)

        print('wayside dispatched')
        # compare suggSpeed to commandedSpeed
        #speedLimit = self.track.getLine('Green').getBlock(63).speedLimit
        #self.commspeed(train)
        self.dest = train.destBlock
        #print("dest from train obejct", train.destBlock)
        self.route = train.route
        #print("route from train obejct", train.route)
        #print("destblock", self.dest)
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
        
        id = self.track0.index(block)
        sec = self.allsection0[id]
        self.updateAuthority(line, block, route)
        self.changeSwitch(line, block)
        signals.wtowOccupancy.emit(line, block, sec)
    
    def blockVacancyReceived(self, line, block):
        #print(".py block", block, "is vacant")
        id = self.track0.index(block)
        sec = self.allsection0[id]
        signals.wtowVacancy.emit(line, block, sec)

    def passengersReceived(self, passengers): #dont touch send to CTC
        self.passengers = passengers
        signals.passengersToCTC.emit(passengers)

    def addTrackModel(self, trackModel):
        self.trackModel = trackModel
        #self.trackModel.blockOccupancyToWayside.connect(self.blockOccupancyReceived)
        self.trackModel.totalPassengersToWayside.connect(self.passengersReceived)

    def changeSwitchfromCTC(self, sw0, sw1):
        if self.switchStates0 == sw0:
            print("sw0 did not change")
            change = 1
        if self.switchStates1 == sw1:
            print("sw0 did not change")
            change = 0

        self.switchStates0 = sw0
        self.switchStates1 = sw1

        signals.wtowSwitchChange.emit(self.switchStates0, self.switchStates1, change)
        

    def changeSwitch(self, line, block):
        #print("CHANGESWITCH", line)
        if line == 'Green':
            print("")
            #print("line ==0")
            currblock = self.route.index(block)
            #print("current block", block, "index", currblock)
            #print("route", self.route)
            nextblock1 = self.route[currblock+1]#int(self.everythingtrack0[currblock].nextBlock)
            #print("nextblock", nextblock1)
            #nextindex1 = self.route.index(nextblock1)
            #get next block from route or from jake
            #print("switch yes or no", self.everythingtrack0[nextblock1].switch)
            #print("switchmatrix0", self.switchMatrix0)
            counti = 0
            row = 0
            nb = 0
            shouldface = 0
            opposite = 0
            if self.everythingtrack0[nextblock1].switch == '1':
                #print("SWITCH next!!")
                for i in self.switchMatrix0:
                    try:
                        try:
                            cb = i.index(int(block))
                            #print("CURRENTshould be index for", block, "in row", cb)
                            if cb == 2:
                                shouldface = 1
                            elif cb == 1:
                                shouldface = 0
                        except:
                            nb = i.index(int(nextblock1))
                            nb1 = self.route[currblock+2]
                            nbindex = i.index(int(nb1))
                            #print("NEXTshould be index for", nextblock1, "in row", nb)
                            #print("NEXTshould be index for", nb, "in row", nbindex)
                            if nbindex == 2:
                                shouldface = 1
                            elif nbindex == 1:
                                shouldface = 0
                        row = counti
                        #print("final counti", counti)
                    except:
                        counti = counti+1
                #print("we need matrix row", self.switchMatrix0[row])
                #print("current state for switch", self.switchMatrix0[row][0], ":", self.switchStates0[row])
                #print("default switch state is :", self.switchDefaults0[row])
                #print("should be facing", shouldface)

                if self.switchDefaults0[row] == 0:
                    opposite = 1
                elif self.switchDefaults0[row] == 1:
                    opposite = 0

                if self.switchStates0[row] != self.switchDefaults0[row]:
                    #print("current:",self.switchStates0[row]," != default",  self.switchDefaults0[row])
                    self.switchStates0[row] = opposite
                    print("toggled switch", self.switchMatrix0[row][0]," since current state not == default. now is", opposite)
                if shouldface != self.switchStates0[row]:
                    #print("shouldface:",shouldface," != current",  self.switchStates0[row])
                    self.switchStates0[row] = opposite
                    print("toggled switch", self.switchMatrix0[row][0]," since should be facing not == current. now is", opposite)
                    #print("matrixindexint", matrixindexint) 
                signals.waysideSwitchtoTrack.emit(self.switchMatrix0[row][0], self.switchMatrix0[row][opposite+1])
                signals.waysideSwitchtoCTC.emit(self.switchStates0, self.switchStates1)
                signals.wtowSwitchChange.emit(self.switchStates0, self.switchStates1, 0)
                #print("signals to track", self.switchMatrix0[row][0], self.switchMatrix0[row][opposite+1])
                #print("signals to ctc", self.switchStates0, self.switchStates1)
        if line == 'Red':
            print("")
            currblock = self.route.index(block)
            nextblock1 = self.route[currblock+1]
            counti = 0
            row = 0
            nb = 0
            shouldface = 0
            opposite = 0
            if self.everythingtrack1[nextblock1].switch == '1':
                for i in self.switchMatrix1:
                    try:
                        try:
                            cb = i.index(int(block))
                            if cb == 2:
                                shouldface = 1
                            elif cb == 1:
                                shouldface = 0
                        except:
                            nb = i.index(int(nextblock1))
                            nb1 = self.route[currblock+2]
                            nbindex = i.index(int(nb1))
                            if nbindex == 2:
                                shouldface = 1
                            elif nbindex == 1:
                                shouldface = 0
                        row = counti
                    except:
                        counti = counti+1

                if self.switchDefaults1[row] == 0:
                    opposite = 1
                elif self.switchDefaults1[row] == 1:
                    opposite = 0

                if self.switchStates1[row] != self.switchDefaults1[row]:
                    self.switchStates1[row] = opposite
                    print("toggled switch", self.switchMatrix1[row][0]," since current state not == default. now is", opposite)
                if shouldface != self.switchStates1[row]:
                    self.switchStates1[row] = opposite
                    print("toggled switch", self.switchMatrix1[row][0]," since should be facing not == current. now is", opposite)
                signals.waysideSwitchtoTrack.emit(self.switchMatrix1[row][0], self.switchMatrix1[row][opposite+1])
                signals.waysideSwitchtoCTC.emit(self.switchStates0, self.switchStates1)
                signals.wtowSwitchChange.emit(self.switchStates0, self.switchStates1, 1)
                #print("signals to track", self.switchMatrix1[row][0], self.switchMatrix1[row][opposite+1])
                #print("signals to ctc", self.switchStates0, self.switchStates1)
        print("")
        self.route.pop(0)

    # def switchStateReceived(self, bl, updw):
    #     self.switch = sw
    #     print("authority from CTC to Wayside: " + str(self.authority))

    
    def trainInfoToCTC(self, train):
        signals.ctcUpdateGUITrainInfo.emit(train)