import Line

class Track:
    # declare attributes
    def __init__(self):
        self.lines = []
        self.faults = {'Power': [],
                    'Broken Rail': [],
                    'Broken Circuit': []
                    }

    def addLine(self, line):
        self.lines.append(line)

    def hasLine(self, lineID):
        for l in self.lines:
            if l.lineName == lineID:
                return True

    def getLine(self, lineID):
        for l in self.lines:
            if l.lineName == lineID:
                return l