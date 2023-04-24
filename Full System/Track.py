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

    def addFault(self, fault):
        self.faults[fault.type].append(fault)

    def faultExists(self, fault):
        for f in self.faults[fault.type]:
            if f.line == fault.line and f.block == fault.block:
                return True
            
        return False

    def faultsToString(self, faultType):
        faultString = ''

        for fault in self.faults[faultType]:
            faultString += fault.line + ' ' + fault.block

        return faultString