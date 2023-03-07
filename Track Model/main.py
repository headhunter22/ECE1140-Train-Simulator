import sys
from PyQt6 import QtWidgets
import TrackParser
from MainWindow import MainWindow
from TestUI import TestUI

class Connected():
    def __init__(self, track):
        # instantiate windows
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = MainWindow(track)
        self.testWindow = TestUI(track)

        # connect signals
        self.testWindow.occupancyPressed.connect(self.window.updateOccupancy)
        self.testWindow.vacancyPressed.connect(self.window.updateVacancy)
        self.testWindow.crossingChanged.connect(self.window.changeCrossings)

    def run(self):
        self.window.show()
        self.testWindow.show()
        self.app.exec()

track = TrackParser.parseTrack('Track Layout.csv')

program = Connected(track)
program.run()