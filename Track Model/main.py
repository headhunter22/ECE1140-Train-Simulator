import sys
from PyQt6 import QtWidgets
import TrackParser
from TrackModelUI import TrackModelUI
from TestUI import TestUI

class Connected():
    def __init__(self, track):
        # instantiate windows
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = TrackModelUI(track)
        self.testWindow = TestUI(track)

        # connect signals from test to main
        self.testWindow.occupancyPressed.connect(self.window.updateOccupancy)
        self.testWindow.vacancyPressed.connect(self.window.updateVacancy)
        self.testWindow.crossingChanged.connect(self.window.changeCrossings)
        self.testWindow.tempSignal.connect(self.window.tempUpdate)
        self.testWindow.faultSignal.connect(self.window.updateFaults)

        # connect signal from main to block info
        # connect all buttons to block pages
        for section in self.window.sectionDict:
            self.window.sectionDict[section].button.clicked.connect(lambda ch, i=self.window.sectionDict[section].section: self.window.generateBlockInfoPage(i))

    def run(self):
        self.window.show()
        self.testWindow.show()
        self.app.exec()

track = TrackParser.parseTrack('Track Layout.csv')

program = Connected(track)
program.run()