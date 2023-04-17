import csv

class Schedule:
    def __init__(self):
        self.stops = []
        self.arrivalTimes = []
        self.line = ""

    def addStop(self, stop):
        self.stops.append(stop)
    
    def addTime(self, time):
        self.arrivalTimes.append(time)

    def addLine(self, lineName):
        self.line = lineName


def parseScedule(filename):

    trainSchedule = Schedule()
    
    with open(filename, newline='') as csvfile:
        schedule = csv.reader(csvfile)

        for row in schedule:
            if row[2] == "Green" or row[2] == "Red":
                trainSchedule.line = row[2]
                continue

            trainSchedule.addStop(row[0])
            trainSchedule.addTime(row[1])

    return trainSchedule