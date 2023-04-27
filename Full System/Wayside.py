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
        self.dest = []
        self.route = []
        self.auth = 8

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
        self.cross0 = []
        self.cross1 = []

        # connect signals
        signals.waysideDispatchTrain.connect(self.dispatchTrain)
        signals.trackCTCToWayside.connect(self.trackReceived)
        signals.waysideUpdateOccupancy.connect(self.blockOccupancyReceived)
        signals.waysideUpdateVacancy.connect(self.blockVacancyReceived)
        signals.waysideCommandedSpeed.connect(self.suggSpeedReceived)
        signals.waysideinstances.connect(self.plcinfo)

        signals.switchStatesFromCTCtoWayside.connect(self.changeSwitchfromCTC)
        signals.wtowSwitchfromUI.connect(self.changeSwitchfromwayside)
        #signals.blockMaintenanceFromCTCtoWayside.connect(self.test)
        signals.trackModelTrainInfoToWayside.connect(self.trainInfoToCTC)
        signals.trackModelBrokenRail.connect(self.brokenRain)# line, block, 'Broken Rail

        signals.waysideTrackfromPLC.connect(self.setTracks)
        signals.waysideSectionsfromPLC.connect(self.setSections)
        signals.waysideSwitchLocationsfromPLC.connect(self.setSwitchLocations)
        signals.waysideSwitchStatesfromPLC.connect(self.setSwitchStates)
        signals.waysideStationsfromPLC.connect(self.setStations)
        signals.waysideAllSectionsfromPLC.connect(self.setAllSections)

        
    def crossinglights(self, block, line): # 1 both active 2 red active 3 green active 4 both inactive
        #print("checking crossing")
        currblock = self.track0.index(block)
        nextblock1 = int(self.everythingtrack0[currblock].nextBlock)
        signalfortrack = 4
        #if line == 'Green':
        if ((nextblock1 == self.cross0[0]) or (block == self.cross0[0])) and line == 'Green':
            #print("coming up on crossing green")
            signals.wtowCrossing.emit(0, False)
            signalfortrack = 3
        #elif line == 'Red':
        elif ((nextblock1 == self.cross1[0]) or (block == self.cross1[0])) and line == 'Red':
            #print("coming up on crossing red")
            signals.wtowCrossing.emit(1, False)
            signalfortrack = 2
        else:
            #print("no crossings")
            signals.wtowCrossing.emit(0, True)
            signals.wtowCrossing.emit(1, True)
            signalfortrack = 4

        signals.waysideUpdateCrossingLights.emit(signalfortrack)

    def brokenRain(self,line, block, name):
        #print(name)
        if line == 'Green':
            #print("brokenrail track0", self.track0)
            id = self.track0.index(int(block))
            sec = self.allsection0[id]
            signals.wtowOccupancy.emit(line, block, sec, self.route)
        elif line == 'Red':
            id = self.track1.index(int(block))
            sec = self.allsection0[id]
            signals.wtowOccupancy.emit(line, block, sec, self.route)


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
        #print("setswitchlocaitons .py")
        self.switchLocations0 = loc0
        self.switchLocations1 = loc1
        self.switchMatrix0 = mat0
        self.switchMatrix1 = mat1
        signals.wtowSwitchesSetup.emit(mat0, mat1)
        
    def setSwitchStates(self, state0, state1):
        #print("defaults in set .py")
        self.switchStates0 = state0
        self.switchStates1 = state1
        self.switchDefaults0 = state0
        self.switchDefaults1 = state1
        
        signals.wtowSwitchDefaults.emit(self.switchDefaults0, self.switchDefaults1)
        
    def updateAuthority(self, line, block, route):
        #print("authority starts at 8")
        self.auth= 8
        authoritylist = []
        #print("authority currblock", currblock)
        #print("authority line", line)
        if line == 'Green':
            id = self.track0.index(block)
            sec = self.allsection0[id]
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
                    self.auth= 0
                    #print("i = block0", int(i), block)
                    break
                elif int(i) == nextblock1:
                    self.auth= 1
                    authoritylist = [nextblock1]
                    #print("i = block1", int(i), nextblock1)
                    break
                elif int(i) == nextblock2:
                    self.auth= 2
                    authoritylist = [nextblock1, nextblock2]
                    #print("i = block2", int(i), nextblock2)
                    break
                elif int(i) == nextblock3:
                    self.auth= 3
                    authoritylist = [nextblock1, nextblock2, nextblock3]
                    #print("i = block3", int(i), nextblock3)
                    break
                elif int(i) == nextblock4:
                    self.auth= 4
                    authoritylist = [nextblock1, nextblock2, nextblock3, nextblock4]
                    #print("i = block4", int(i), nextblock4)
                    break
                elif int(i) == nextblock5:
                    self.auth= 5
                    authoritylist = [nextblock1, nextblock2, nextblock3, nextblock4, nextblock5]
                    #print("i = block5", int(i), nextblock5)
                    break
                elif int(i) == nextblock6:
                    self.auth= 6
                    authoritylist = [nextblock1, nextblock2, nextblock3, nextblock4, nextblock5, nextblock6]
                    #print("i = block6", int(i), nextblock6)
                    break
                elif int(i) == nextblock7:
                    self.auth= 7
                    authoritylist = [nextblock1, nextblock2, nextblock3, nextblock4, nextblock5, nextblock6, nextblock7]
                    #print("i = block7", int(i), nextblock7)
                    break
                elif int(i) == nextblock8:
                    self.auth= 8
                    authoritylist = [nextblock1, nextblock2, nextblock3, nextblock4, nextblock5, nextblock6, nextblock7, nextblock8]
                    #print("i = block8", int(i), nextblock8)
                    break
        elif line == 'Red':
            id = self.track1.index(block)
            sec = self.allsection0[id]
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
                    self.auth= 0
                elif int(i) == nextblock1:
                    self.auth= 1
                    authoritylist = [nextblock1]
                elif int(i) == nextblock2:
                    self.auth= 2
                    authoritylist = [nextblock1, nextblock2]
                elif int(i) == nextblock3:
                    self.auth= 3
                    authoritylist = [nextblock1, nextblock2, nextblock3]
                elif int(i) == nextblock4:
                    self.auth= 4
                    authoritylist = [nextblock1, nextblock2, nextblock3, nextblock4]
                elif int(i) == nextblock5:
                    self.auth= 5
                    authoritylist = [nextblock1, nextblock2, nextblock3, nextblock4, nextblock5]
                elif int(i) == nextblock6:
                    self.auth= 6
                    authoritylist = [nextblock1, nextblock2, nextblock3, nextblock4, nextblock5, nextblock6]
                elif int(i) == nextblock7:
                    self.auth= 7
                    authoritylist = [nextblock1, nextblock2, nextblock3, nextblock4, nextblock5, nextblock6, nextblock7]
                elif int(i) == nextblock8:
                    self.auth= 8
                    authoritylist = [nextblock1, nextblock2, nextblock3, nextblock4, nextblock5, nextblock6, nextblock7, nextblock8]
            
        #print("wayside.py update authority auth", auth)
        signals.waysideAuthoritytoTrack.emit(self.auth, currblock)
        signals.waysideAuthorityToCTC.emit(line, route, self.auth)
        signals.wtowAuthority.emit(authoritylist, sec)

    def plcinfo(self, range1, section1, range2, section2, range3, section3, range4, section4, range5, section5, range6, section6, range7, section7, range8, section8, cross0, cross1):#, range):
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

        self.cross0 = cross0
        self.cross1 = cross1
        #print("signals sent in .py plcinfo")

    def dispatchTrain(self, train):
        # set occupancy of first block
        #self.setOccupancy(train.line, 63, 1)

        #print('wayside dispatched')
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
        auth = train
        #print("authority from CTC to Wayside: " + str(train.authority))

    def sendAuthority(self, blocks):
        #print("authority from Wayside to Track:", str(blocks))
        signals.waysideAuthority.emit(blocks)
        
    def suggSpeedReceived(self, speed):
        signals.waysideSuggestedSpeed.emit(speed)

    def trainReceived(self, train):
        # pass train onto track model
        self.trainObjectWaysideToTrackModel.emit(train)

    def trackReceived(self, track):
        self.track = track

        # pass track onto track model
        signals.trackWaysideToTrackModel.emit(track)

    def blockOccupancyReceived(self, line, block, route):
        #print(". py block", block, "is occupied")
        self.route = route
        self.updateAuthority(line, block, self.route)
        self.changeSwitch(line, block) 
        currblock = self.track0.index(block)
        nextblock1 = int(self.everythingtrack0[currblock].nextBlock)
        # if ((nextblock1 == self.cross0[0]) or (block == self.cross0[0])) and line == 'Green':
        #     self.crossinglights(block, line)
        # elif ((nextblock1 == self.cross1[0]) or (block == self.cross1[0])) and line == 'Red':
        self.crossinglights(block, line)
        if line == 'Green':
            id = self.track0.index(block)
            sec = self.allsection0[id]
            signals.wtowOccupancy.emit(line, block, sec, self.auth)
        elif line == 'Red':
            id = self.track1.index(block)
            sec = self.allsection0[id]
            signals.wtowOccupancy.emit(line, block, sec, self.auth)
    
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
        #print("current",self.switchStates0, self.switchStates1 )
        #print("incoming", sw0, sw1)
        loc = 0
        state = 0
        facing = 0
        counti = 0
        for i in sw0:
            if i != self.switchStates0[counti]:
                loc = self.switchLocations0[counti]
                state = self.switchStates0[counti]
                if state ==0:
                    facing = self.switchMatrix0[counti][2]
                elif state ==1:
                    facing = self.switchMatrix0[counti][1]
                #print("switch", loc, "now facing", facing)
            else:
                change = 1
                #greenline did not change
            counti = counti+1
        #print("switch", loc, "now facing", facing)
        countk = 0

        for i in sw1:
            if i != self.switchStates1[countk]:
                loc = self.switchLocations1[countk]
                state = self.switchStates1[countk]
                if state ==0:
                    facing = self.switchMatrix1[countk][2]
                elif state ==1:
                    facing = self.switchMatrix1[countk][1]
                #print("switch", loc, "now facing", facing)
            else:
                change = 1
                #greenline did not change
            countk = countk+1

        self.switchStates0 = sw0
        self.switchStates1 = sw1

        signals.wtowSwitchChange.emit(self.switchStates0, self.switchStates1, change)
        signals.waysideSwitchtoTrack.emit(loc, facing)
        #print("to track in ctc", loc, facing)
        #signals.waysideSwitchtoCTC.emit(self.switchStates0, self.switchStates1)

    def changeSwitchfromwayside(self, sw0, sw1):
        #print("current",self.switchStates0, self.switchStates1 )
        #print("incoming", sw0, sw1)
        loc = 0
        state = 0
        facing = 0
        counti = 0
        for i in sw0:
            if i != self.switchStates0[counti]:
                loc = self.switchLocations0[counti]
                state = self.switchStates0[counti]
                if state ==0:
                    facing = self.switchMatrix0[counti][2]
                elif state ==1:
                    facing = self.switchMatrix0[counti][1]
                #print("switch", loc, "now facing", facing)
            else:
                change = 1
                #greenline did not change
            counti = counti+1
        #print("switch", loc, "now facing", facing)
        countk = 0

        for i in sw1:
            if i != self.switchStates1[countk]:
                loc = self.switchLocations1[countk]
                state = self.switchStates1[countk]
                if state ==0:
                    facing = self.switchMatrix1[countk][2]
                elif state ==1:
                    facing = self.switchMatrix1[countk][1]
                #print("switch", loc, "now facing", facing)
            else:
                change = 1
                #greenline did not change
            countk = countk+1

        self.switchStates0 = sw0
        self.switchStates1 = sw1

        #signals.wtowSwitchChange.emit(self.switchStates0, self.switchStates1, change)
        signals.waysideSwitchtoTrack.emit(loc, facing)
        #print("to track in ctc", loc, facing)
        signals.waysideSwitchtoCTC.emit(self.switchStates0, self.switchStates1)
        
    def changeSwitch(self, line, block):
        #print("CHANGESWITCH", line)
        if line == 'Green':
            #print("")
            #print("line ==0")
            try:
                currblock = self.route.index(block)
            except:
                pass
            #print("current block", block, "index", currblock)
            #print("route", self.route)
            try:
                nextblock1 = self.route[currblock+1]#int(self.everythingtrack0[currblock].nextBlock)
            except:
                pass
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
            try:
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
                        #print("toggled switch", self.switchMatrix0[row][0]," since current state not == default. now is", opposite)
                    if shouldface != self.switchStates0[row]:
                        #print("shouldface:",shouldface," != current",  self.switchStates0[row])
                        self.switchStates0[row] = opposite
                        #print("toggled switch", self.switchMatrix0[row][0]," since should be facing not == current. now is", opposite)
                        #print("matrixindexint", matrixindexint) 
                    signals.waysideSwitchtoTrack.emit(self.switchMatrix0[row][0], self.switchMatrix0[row][opposite+1])
                    #print("to track in change", self.switchMatrix0[row][0], self.switchMatrix0[row][opposite+1])
                    signals.waysideSwitchtoCTC.emit(self.switchStates0, self.switchStates1)
                    signals.wtowSwitchChange.emit(self.switchStates0, self.switchStates1, 0)
                    #print("signals to track", self.switchMatrix0[row][0], self.switchMatrix0[row][opposite+1])
                    #print("signals to ctc", self.switchStates0, self.switchStates1)
            except:
                pass
        if line == 'Red':
            #print("")
            currblock = self.route.index(block)
            nextblock1 = self.route[currblock+1]
            counti = 0
            row = 0
            nb = 0
            shouldface = 0
            opposite = 0
            try:
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
                        #print("toggled switch", self.switchMatrix1[row][0]," since current state not == default. now is", opposite)
                    if shouldface != self.switchStates1[row]:
                        self.switchStates1[row] = opposite
                        #print("toggled switch", self.switchMatrix1[row][0]," since should be facing not == current. now is", opposite)
                    signals.waysideSwitchtoTrack.emit(self.switchMatrix1[row][0], self.switchMatrix1[row][opposite+1])
                    signals.waysideSwitchtoCTC.emit(self.switchStates0, self.switchStates1)
                    signals.wtowSwitchChange.emit(self.switchStates0, self.switchStates1, 1)
                    #print("signals to track", self.switchMatrix1[row][0], self.switchMatrix1[row][opposite+1])
                    #print("signals to ctc", self.switchStates0, self.switchStates1)
            #print("")
            except:
                pass
        try:
            self.route.pop(0)
        except:
            pass
   
    def trainInfoToCTC(self, train):
        signals.ctcUpdateGUITrainInfo.emit(train)