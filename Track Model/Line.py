import Section

class Line:
    # constructor
    def __init__(self, lineName):
        self.sections = []
        self.lineName = lineName

    # declare methods
    def addSection(self, section):
        self.sections.append(section)

    def removeSection(self, section):
        self.sections.remove(section)

    def clearSection(self):
        self.sections.clear()

    def hasSection(self, sectionID):
        for s in self.sections:
            if s.sectionName == sectionID:
                return True

    def getSection(self, sectionID):
        for s in self.sections:
            if s.sectionName == sectionID:
                return s