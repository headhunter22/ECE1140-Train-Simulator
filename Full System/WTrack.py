from WBlock import WBlock
from signals import signals

# class WTrack:
#     def __init__(self):
#         super().__init__()
#         print("wrtack instanced")
#         self.track = []
#         self.sections = []
#         self.allsection = []
#         self.switches = []
#         self.switchStates = []

#         self.wayside1range = []
#         self.wayside1sectionrange = []
#         self.wayside2range = []
#         self.wayside2sectionrange = []
#         self.wayside3range = []
#         self.wayside3sectionrange = []
#         self.wayside4range = []
#         self.wayside4sectionrange = []

#         # connect signals
#         # signals.waysideSwitchStates.connect(self.wholeTrack)
#         # signals.waysideSwitchLocationsfromPLC.connect(self.wholeTrack)
#         # signals.waysideTrackfromPLC.connect(self.wholeTrack)
#         # signals.waysideSectionsfromPLC.connect(self.wholeTrack)

#         signals.please.connect(self.imoverthis)
        
#     # function to dispatch a train
#     # hard coded for green line for the time being

#     def imoverthis(self):#, range):
#         print("im over this in wtrack")
        
        

#     def addBlock(self, block):
#         self.track.append(int(block.blockNumber))
#         self.allsection.append(block.section)
#         contains = 0
#         #lensw = len()
#         for i in self.sections:
#             if i == block.section:
#                 contains = 1
#         if contains == 0:
#             self.sections.append(block.section)
#         #check if section already exists
#         #print("added block", block.blockNumber)
#         #print("added section", block.section)
#         if (block.switch == '1'):
#             self.addSwitch(block)

#     def addSwitch(self, block):
#         self.switches.append(int(block.blockNumber))
#         self.switchStates.append(int(block.switchState))
#         #print("added switch to block", block.blockNumber, " state is:", block.switchState)

#     def Waysides(self):
#         print("waysides in wtrack start")
#         full = int(len(self.track))-1
#         half = int(full / 2)
#         quarter = int(half / 2)
#         threefourths = int(quarter+half)
#         last = self.track[int(len(self.track))-1]
#         lastsection = self.allsection[int(len(self.allsection))-1]
#         #print("last", last)
#         #print("we need waysides at", quarter, half, threefourths, full)
#         self.wayside1range = [last] + self.track[0:half+1]
#         self.wayside1sectionrange = [lastsection] + self.allsection[0:half+1]
#         #print("1 range", self.wayside1range)
#         self.wayside2range = self.track[quarter:threefourths+1]
#         self.wayside2sectionrange = self.allsection[quarter:threefourths+1]
#         #print("2 range", self.wayside2range)
#         self.wayside3range = self.track[half:full+1] + [1]
#         self.wayside3sectionrange = self.allsection[half:full+1] + ['A']
#         #print("3 range", self.wayside3range)
#         self.wayside4range = self.track[threefourths:full] + self.track[1:quarter+1]
#         self.wayside4sectionrange = self.allsection[threefourths:full] + self.allsection[1:quarter+1]
#         #print("4 range", self.wayside4range)
#         print("wtrack rage 1", self.wayside1range)
#         signals.waysideinstances.emit(self.wayside1range, self.wayside1sectionrange, self.wayside2range, self.wayside2sectionrange, self.wayside3range, self.wayside3sectionrange, self.wayside4range, self.wayside4sectionrange)
#         print("wtrack rage 2", self.wayside1range)
       
#         print("wayside added in wtrack")
#         #signals.actuallyshutup.emit()

#     def wholeTrack(self):
#         #print("track:", self.track)
#         signals.waysideTrackfromPLC.emit(self.track)
#         #print("sections:", self.sections)
#         signals.waysideSectionsfromPLC.emit(self.sections)
#         #print("switches:", self.switches)
#         signals.waysideSwitchLocationsfromPLC.emit(self.switches)
#         #print("switchStates:", self.switchStates)
#         signals.waysideSwitchStates.emit(self.switchStates)

#         #print("wtrack" )
#         #signals.actuallyshutup.emit()
#         #signals.waysideinstance2.emit(self.wayside2range)#, self.wayside2sectionrange)
#         # signals.waysideinstance3.emit(self.wayside3range, self.wayside3sectionrange)
#         # signals.waysideinstance4.emit(self.wayside4range, self.wayside4sectionrange)

    