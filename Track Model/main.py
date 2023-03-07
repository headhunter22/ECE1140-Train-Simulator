import sys
from PyQt6 import QtWidgets
import TrackParser
from MainWindow import MainWindow
from TestUI import TestUI

track = TrackParser.parseTrack('Track Layout.csv')
app = QtWidgets.QApplication(sys.argv)

# create main UI window
window = MainWindow(track)
testWindow = TestUI(track)

# show window
window.show()
testWindow.show()

app.exec()