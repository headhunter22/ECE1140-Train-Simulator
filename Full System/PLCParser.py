from WBlock import WBlock
from WTrack import WTrack

#SC = Section
#BN = Block Number
#NB = Next Block
#PB = Previous Block
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

#def parse(self):
fname = "plcLogic_Green"
with open(fname, 'r+') as f: #newline='', 
    newtrack = WTrack()   
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
            newtrack.addBlock(newblock)
            #print("add block object to track")
    newtrack.wholeTrack()
    newtrack.addWayside()