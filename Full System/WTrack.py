from WBlock import WBlock
from signals import signals

class WTrack:
    def __init__(self):
        super().__init__()
        self.track = []
        self.sections = []
        self.switches = []
        self.switchStates = []

        # connect signals
        # signals.waysideSwitchStates.connect(self.wholeTrack)
        # signals.waysideSwitchLocationsfromPLC.connect(self.wholeTrack)
        # signals.waysideTrackfromPLC.connect(self.wholeTrack)
        # signals.waysideSectionsfromPLC.connect(self.wholeTrack)
        
        

    def addBlock(self, block):
        self.track.append(int(block.blockNumber))
        contains = 0
        #lensw = len()
        for i in self.sections:
            if i == block.section:
                contains = 1
        if contains == 0:
            self.sections.append(block.section)
        #check if section already exists
        #print("added block", block.blockNumber)
        #print("added section", block.section)
        if (block.switch == '1'):
            self.addSwitch(block)

    def addSwitch(self, block):
        self.switches.append(int(block.blockNumber))
        self.switchStates.append(int(block.switchState))
        #print("added switch to block", block.blockNumber, " state is:", block.switchState)

    def Waysides(self):
        full = int(len(self.track))-1
        half = int(full / 2)
        quarter = int(half / 2)
        threefourths = int(quarter+half)
        last = self.track[int(len(self.track))-1]
        #print("last", last)
        #print("we need waysides at", quarter, half, threefourths, full)
        wayside1range = [last] + self.track[0:half+1]
        #print("1 range", wayside1range)
        wayside2range = self.track[quarter:threefourths+1]
        #print("2 range", wayside2range)
        wayside3range = self.track[half:full+1] + [1]
        #print("3 range", wayside3range)
        wayside4range = self.track[threefourths:full] + self.track[1:quarter+1]
        #print("4 range", wayside4range)
        #print("wayside added")

    def wholeTrack(self):
        #print("track:", self.track)
        signals.waysideTrackfromPLC.emit(self.track)
        #print("sections:", self.sections)
        signals.waysideSectionsfromPLC.emit(self.sections)
        #print("switches:", self.switches)
        signals.waysideSwitchLocationsfromPLC.emit(self.switches)
        #print("switchStates:", self.switchStates)
        signals.waysideSwitchStates.emit(self.switchStates)

        signals.waysideinstance1.emit(self.wayside1range)
        signals.waysideinstance2.emit(self.wayside2range)
        signals.waysideinstance3.emit(self.wayside3range)
        signals.waysideinstance4.emit(self.wayside4range)

    