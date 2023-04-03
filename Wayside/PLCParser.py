from Block import Block

#ID = ID
#ST = Station
#RX = Crossing
#RXS = Crossing State
#CL = Crossing Lights
#OC = Occupancy
#AU = Authority
#SW = Switch
#SWS = Switch State
#SL = Switch Lights
#FT = Fault


def parse(self):
    fname = "plcLogic"
    with open(fname, 'r+') as f: #newline='',    
        for count, x in enumerate(f): #for count, line in enumerate(fp):
            if x[:3] == "BLK":
                newblock = Block()
                print("this is a block")
                print("x ",x)
                #for i in range(12):
                #x = f.next()
                line = f.readline()
                print("line : ", "{", x, "}")
            elif x[:2] == "ID":
                newblock.ID = x[3:]
                print("ID", x[2:]) 
            elif x[:2] == "SC":
                newblock.section = x[3:]
                print("SC", x[2:])
            elif x[:2] == "BN":
                newblock.blockNumber = x[3:]
                print("BN", x[2:])             # print("{"  + id + "}")
            elif x[:2] == "ST":
                newblock.station = x[3:]
                print("ST", x[:2])
            elif x[:2] == "RX":
                newblock.crossing = x[3:]
                print("RX", x[:2])
            elif x[:2] == "RS":
                newblock.crossingState = x[3:]
                print("RS", x[:2])
            elif x[:2] == "RL":
                newblock.crossingLights = x[3:]
                print("RL", x[:2])
            elif x[:2] == "OC":
                newblock.occupation = x[3:]
                print("OC", x[:2])
            elif x[:2] == "AU":
                newblock.authority = x[3:]
                print("AU", x[:2])
            elif x[:2] == "SW":
                newblock.switch = x[3:]
                print("SW", x[:2])
            elif x[:2] == "SS":
                newblock.switchState = x[3:]
                print("SS", x[:2])
            elif x[:2] == "SL":
                newblock.switchLights = x[3:]
                print("SL", x[:2])
            elif x[:2] == "FT":
                print("FT", x[:2])
                newblock.fault = x[3:]
            elif x[:3] == "END":
                #break
                print("end")
            elif x[:3] == "TSK":
                print("this is a task")
                #newtask = Task()
                #skip the same amount of lines if task
            else:
                print("wrong")

            print("count",count)

#parse(self)
