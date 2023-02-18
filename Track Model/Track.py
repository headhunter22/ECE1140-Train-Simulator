import Line

class Track:
    # declare attributes
    def __init__(self):
        self.lines = []

    def addLine(self, line):
        self.lines.append(line)

    def lineExists(self, lineID):
        for l in self.lines:
            if l.lineName == lineID:
                return True