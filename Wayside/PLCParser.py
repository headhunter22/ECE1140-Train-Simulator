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


fname = "plcLogic"
with open(fname, newline=''):

    f = open(fname, 'r')
    with f:
        #data = f.read()
        #print("the beginning: ", data)
        #job = f.read(3)
        #print("job: ", job)
        
        for x in f:
            newblock = Block()
                #while x != "BLK" or "TSK":
            if x[:3] == "BLK":
                print("this is a block")
                for i in range(9):
                    print("x ",x)
                    if x[:2] == "ID":
                        newblock.ID = x[3:]
                        print("ID", x[:2])
                    elif x[:2] == "ST":
                        newblock.station = x[3:]
                        print("ST", x[:2])
                    elif x[:3] == "RX":
                        newblock.crossing = x[3:]
                        print("RX", x[:2])
                    elif x[:3] == "RXS":
                        newblock.crossingState = x[3:]
                        print("RXS", x[:2])
                    elif x[:2] == "CL":
                        newblock.crossingLights = x[3:]
                        print("LT", x[:2])
                    elif x[:2] == "OC":
                        newblock.occupation = x[3:]
                        print("OC", x[:2])
                    elif x[:2] == "AU":
                        newblock.authority = x[3:]
                        print("AU", x[:2])
                    elif x[:3] == "SW":
                        newblock.switch = x[3:]
                        print("SW", x[:2])
                    elif x[:3] == "SWS":
                        newblock.switchState = x[3:]
                        print("SWS", x[:2])
                    elif x[:2] == "SL":
                        newblock.switchLights = x[3:]
                        print("LT", x[:2])
                    elif x[:2] == "FT":
                        print("FT", x[:2])
                        newblock.fault = x[3:]
                    elif x[:3] == "END":
                        break
            elif x[:3] == "TSK":
                print("this is a task")
                #newtask = Task()
                #skip the same amount of lines if task

            else:
                print("wrong")
