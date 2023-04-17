from WBlock import WBlock

class WTrack:
    def __init__(self):
        super().__init__()
        self.track = []
        self.sections = []
        self.switches = []
        self.switchStates = []
        

    def addBlock(self, block):
        self.track.append(block.blockNumber)
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
        self.switches.append(block.blockNumber)
        self.switchStates.append(block.switchState)
        #print("added switch to block", block.blockNumber, " state is:", block.switchState)

    def addWayside(self):
        wayside4 = int(len(self.track))-1
        wayside2 = int(wayside4 / 2)
        wayside1 = int(wayside2 / 2)
        wayside3 = int(wayside1+wayside2)
        print("we need waysides at", wayside1, wayside2, wayside3, wayside4)
        #print("wayside added")

    def wholeTrack(self):
        print("track:", self.track)
        print("sections:", self.sections)
        print("switches:", self.switches)
        print("switchStates:", self.switchStates)

    