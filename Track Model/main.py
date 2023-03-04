import sys
from PyQt6 import QtWidgets
import TrackParser
from MainWindow import MainWindow

track = TrackParser.parseTrack('Track Layout.csv')
app = QtWidgets.QApplication(sys.argv)

# create main UI window
window = MainWindow(track)

# show window
window.show()

app.exec()