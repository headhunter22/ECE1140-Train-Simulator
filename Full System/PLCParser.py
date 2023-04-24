from WBlock import WBlock
#from WTrack import WTrack
from signals import signals
#from WaysideUI import WMainWindowA

#SC = Section
#BN = Block Number
#NB = Next Block
#PB = Previous Block
#LI = Line
#ST = Station
#RX = Crossing
#RS = Crossing State
#RL = Crossing Lights
#OC = Occupancy
#AU = Authority
#SW = Switch
#SS = Switch State
#SL = Switch Lights
#FT = Fault

class WTrack:
    def __init__(self):
        super().__init__()
        self.track0 = []
        self.sections0 = []
        self.allsection0 = []
        self.switches0 = []
        self.switchState0 = []
        self.crossing0 = []
        self.stations0 = []

        self.track1 = []
        self.sections1 = []
        self.allsection1 = []
        self.switches1 = []
        self.switchState1 = []
        self.crossing1 = []
        self.stations1 = []

        self.wayside1range = []
        self.wayside1sectionrange = []
        self.wayside2range = []
        self.wayside2sectionrange = []
        self.wayside3range = []
        self.wayside3sectionrange = []
        self.wayside4range = []
        self.wayside4sectionrange = []

        self.wayside5range = []
        self.wayside5sectionrange = []
        self.wayside6range = []
        self.wayside6sectionrange = []
        self.wayside7range = []
        self.wayside7sectionrange = []
        self.wayside8range = []
        self.wayside8sectionrange = []
        #self.main = WMainWindowA()

        #self.parse()

        # connect signals
        # signals.waysideSwitchStates.connect(self.wholeTrack)
        # signals.waysideSwitchLocationsfromPLC.connect(self.wholeTrack)
        # signals.waysideTrackfromPLC.connect(self.wholeTrack)
        # signals.waysideSectionsfromPLC.connect(self.wholeTrack)

        
    # function to dispatch a train
    # hard coded for green line for the time being

    def addBlock(self, block, line):
        if line == 0:
            self.track0.append(int(block.blockNumber))
            self.allsection0.append(block.section)
            contains = 0
            #lensw = len()
            for i in self.sections0:
                if i == block.section:
                    contains = 1
            if contains == 0:
                self.sections0.append(block.section)
            #check if section already exists
            #print("added block", block.blockNumber)
            #print("added section", block.section)
            if block.crossing == '1':
                self.crossing0.append(int(block.blockNumber))

            if block.switch == '1':
                self.switches0.append(int(block.blockNumber))
                self.switchState0.append(int(block.switchState))

            if block.station == '1':
                self.stations0.append(block.blockNumber)

        elif line == 1:
            self.track1.append(int(block.blockNumber))
            self.allsection1.append(block.section)
            contains = 0
            #lensw = len()
            for i in self.sections1:
                if i == block.section:
                    contains = 1
            if contains == 0:
                self.sections1.append(block.section)
            #check if section already exists
            #print("added block", block.blockNumber)
            #print("added section", block.section)
            if block.crossing == '1':
                self.crossing1.append(int(block.blockNumber))

            if block.switch == '1':
                self.switches0.append(int(block.blockNumber))
                self.switchState0.append(int(block.switchState))

            if block.station == '1':
                self.stations1.append(block.blockNumber)

    def Waysides(self):
        #print("waysides in plcparser start")
        full0 = int(len(self.track0))-1
        half0 = int(full0 / 2)
        quarter0 = int(half0 / 2)
        threefourths0 = int(quarter0+half0)
        #last = self.track[int(len(self.track))-1]
        #lastsection = self.allsection[int(len(self.allsection))-1]
        #print("last", last)
        #print("we need waysides at", quarter, half, threefourths, full)
        self.wayside1range =self.track0[0:half0+1]
        self.wayside1sectionrange =self.allsection0[0:half0+1]
        #print("1 range", self.wayside1range)
        #print("1 wayside1sectionrange", self.wayside1sectionrange)
        self.wayside2range = self.track0[quarter0:threefourths0+1]
        self.wayside2sectionrange = self.allsection0[quarter0:threefourths0+1]
        #print("2 range", self.wayside2range)
        #print("2 waysidesectionrange", self.wayside2sectionrange)
        self.wayside3range = self.track0[half0:full0+1] + [1]
        self.wayside3sectionrange = self.allsection0[half0:full0+1] + ['A']
        #print("3 range", self.wayside3range)
        #print("3 wayside1sectionrange", self.wayside3sectionrange)
        self.wayside4range = self.track0[threefourths0:full0+1] + self.track0[0:quarter0+1]
        self.wayside4sectionrange = self.allsection0[threefourths0:full0+1] + self.allsection0[0:quarter0+1]
        #print("4 range", self.wayside4range)
        #print("4 wayside1sectionrange", self.wayside4sectionrange)
        #print("plcparser rage 1", self.wayside1range)
        #signals.waysideinstances.emit(self.wayside1range, self.wayside1sectionrange, self.wayside2range, self.wayside2sectionrange, self.wayside3range, self.wayside3sectionrange, self.wayside4range, self.wayside4sectionrange)

        full1 = int(len(self.track1))-1
        half1 = int(full1 / 2)
        quarter1 = int(half1 / 2)
        threefourths1 = int(quarter1+half1)

        self.wayside5range =self.track1[0:half1+1]
        self.wayside5sectionrange =self.allsection1[0:half1+1]
        #print("5 range", self.wayside5range)
        #print("5 wayside5sectionrange", self.wayside5sectionrange)
        self.wayside6range = self.track1[quarter1:threefourths1+1]
        self.wayside6sectionrange = self.allsection1[quarter1:threefourths1+1]
        #print("6 range", self.wayside6range)
        #print("6 waysidesectionrange", self.wayside6sectionrange)
        self.wayside7range = self.track1[half1:full1+1] + [1]
        self.wayside7sectionrange = self.allsection1[half1:full1+1] + ['A']
        #print("7 range", self.wayside7range)
        #print("7 wayside1sectionrange", self.wayside7sectionrange)
        self.wayside8range = self.track1[threefourths1:full1+1] + self.track1[0:quarter1+1]
        self.wayside8sectionrange = self.allsection1[threefourths1:full1+1] + self.allsection1[0:quarter1+1]
        #print("8 range", self.wayside8range)
        #print("8 wayside1sectionrange", self.wayside8sectionrange)
        #print("plcparser rage 1", self.wayside1range)
        
        #add 5 6 7 8
        signals.waysideinstances.emit(self.wayside1range, self.wayside1sectionrange, self.wayside2range, self.wayside2sectionrange, self.wayside3range, self.wayside3sectionrange, self.wayside4range, self.wayside4sectionrange, 
                                    self.wayside5range, self.wayside5sectionrange, self.wayside6range, self.wayside6sectionrange, self.wayside7range, self.wayside7sectionrange, self.wayside8range, self.wayside8sectionrange)
        #print("signals sent from plcparser waysides")
        #self.main.setupinstances()
        #print("plcparsere rage 2", self.wayside1range)
       
        print("wayside added in plcparser")
        #signals.actuallyshutup.emit()

    def wholeTrack(self):
        print("track0:", self.track0)
        print("track1:", self.track1)
        signals.waysideTrackfromPLC.emit(self.track0, self.track1)
        #print("sections:", self.sections)
        signals.waysideSectionsfromPLC.emit(self.sections0, self.sections1)
        signals.waysideAllSectionsfromPLC.emit(self.allsection0, self.allsection1)
        #print("switches:", self.switches)
        signals.waysideSwitchLocationsfromPLC.emit(self.switches0, self.switches1)
        #print("switchStates:", self.switchStates)
        signals.waysideSwitchStatesfromPLC.emit(self.switchState0, self.switchState1)

        #signals.actuallyshutup.emit()
        #signals.waysiderange2.emit(self.wayside2range)
        #signals.waysidesectionrange2.emit(self.wayside2sectionrange)
        # signals.waysideinstance3.emit(self.wayside3range, self.wayside3sectionrange)
        # signals.waysideinstance4.emit(self.wayside4range, self.wayside4sectionrange)
        print("whole track sent")

    def parse(self, fname = "plcLogic_All"):
        print("parser instanced")
        #print("fname",fname)
        line = 0
        #fname = "plcLogic_Green"
        with open(fname, 'r+') as f: #newline='', 
             
            #while line == 0:
            #print("making line 0")
            newtrack0 = WTrack()  
            # newtrack1 = WTrack()  
            for count, x in enumerate(f): #for count, line in enumerate(fp):
                if x[:3] == "BLK":
                    newblock = WBlock()
                    #print("this is a block")
                elif x[:2] == "SC":
                    newblock.section = x[3:4]
                    #print("SC", x[3:4])
                elif x[:2] == "BN":
                    newblock.blockNumber = x[3:6]
                    #print("BN", x[3:6])             # print("{"  + id + "}")
                elif x[:2] == "NB":
                    newblock.nextBlock = x[3:6]
                    #print("NB", x[3:6])
                elif x[:2] == "PB":
                    newblock.previousBlock = x[3:6]
                    #Print("PB", x[3:6]) 
                elif x[:2] == "LI": 
                    newblock.line = x[3:6]
                    line = int(x[3:6])
                    #green is 0 red is 1        
                elif x[:2] == "ST":
                    newblock.station = x[3:4]
                    #print("ST", x[3:4])
                elif x[:2] == "RX":
                    newblock.crossing = x[3:4]
                    #print("RX", x[3:4])
                elif x[:2] == "RS":
                    newblock.crossingState = x[3:4]
                    #print("RS", x[3:4])
                elif x[:2] == "RL":
                    newblock.crossingLights = x[3:4]
                    #print("RL", x[3:4])
                elif x[:2] == "OC":
                    newblock.occupation = x[3:4]
                    #print("OC", x[3:4])
                elif x[:2] == "AU":
                    newblock.authority = x[3:4]
                    #print("AU", x[3:4])
                elif x[:2] == "SW":
                    newblock.switch = x[3:4]
                    #print("SW", x[3:4])
                elif x[:2] == "SS":
                    newblock.switchState = x[3:4]
                    #print("SS", x[3:4])
                elif x[:2] == "SL":
                    newblock.switchLights = x[3:4]
                    #print("SL", x[3:4])
                elif x[:2] == "FT":
                    newblock.fault = x[3:4]
                    #print("FT", x[3:4])
                elif x[:3] == "END":
                    newtrack0.addBlock(newblock, int(newblock.line))

                    #print("add block object to track")
            
            newtrack0.Waysides()
            newtrack0.wholeTrack()
            print("end of parser")
            