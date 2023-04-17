import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Block import Block
from Track import Track
from signals import signals
import math
import time
from TrainModelUI import TrainModelUI
import TrackParser

class TrainModelTestUI(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("TrainModelTestUI_v2.ui", self)


track = TrackParser.parseTrack("TrackLayout.csv")
app = QtWidgets.QApplication(sys.argv)

testUI = TrainModelTestUI()
trainModUI = TrainModelUI()

testUI.show()
trainModUI.show()

app.exec()