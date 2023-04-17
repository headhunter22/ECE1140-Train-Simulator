import sys
from PyQt6 import QtWidgets
sys.path.append('../Full System')

import TrackParser
from TrackModelUI import TrackModelUI
from TestUI import TestUI

app = QtWidgets.QApplication(sys.argv)
track = TrackParser.parseTrack('Track Layout.csv')

testui = TestUI(track)
model = TrackModelUI(track)

# show windows
testui.show()
model.show()

app.exec()