# modules to make code run
import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic

# train system module imports
from CTC import CTC
from Wayside import Wayside
from TrackModel import TrackModel
from TrainModel import TrainModel
from SWTrainController import SWTrainController
from TrainController import TrainController

# general classes and functions
from Train import Train
from Track import Track
from ClockThreaded import clock
import TrackParser

# import UIs
from ctcUI import ctcMainUI
from TrackModelUI import TrackModelUI
from TrainControllerUI import TrainControllerUI

track = TrackParser.parseTrack("TrackLayout.csv")
app = QtWidgets.QApplication(sys.argv)
clock.startTimer()

ctcOffice = CTC(track)
waysideController = Wayside(ctcOffice)
ctcOffice.addWayside(waysideController)
trackModel = TrackModel(waysideController)
trainModel = TrainModel()
tc = SWTrainController()

# propagate track model
ctcOffice.propagateTrack()

# instantiate UIs
trackUI = TrackModelUI(track)
trainUI = TrainControllerUI()

# dispatch a test train
ctcOffice.dispatch('Green', 1)

trackUI.show()
trainUI.show()
app.exec()

# show CTC window

# notes:
# train physics
# beacons (switch created)
# parse line into linked list that models the track connections??
# - or do we have an addTrack function that can be called each time we reparse?