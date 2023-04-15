# modules to make code run
import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic

# train system module imports
from TrainModel import TrainModel

# general classes and functions
from Train import Train
from Track import Track
import TrackParser

# import UIs
from trainModel_Ui_Final import TrainModelUI
from trainModel_testUi_Final import MainWindowTestUI

track = TrackParser.parseTrack("TrackLayout.csv")
app = QtWidgets.QApplication(sys.argv)

trainModel = TrainModel()


# instantiate UIs
trainModUI = TrainModelUI()
trainModTest = MainWindowTestUI()
   
trainModUI.show()
trainModTest.show()   

app.exec()

# show CTC window

# notes:
# train physics
# beacons (switch created)
# parse line into linked list that models the track connections??
# - or do we have an addTrack function that can be called each time we reparse?