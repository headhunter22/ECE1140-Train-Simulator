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
from TrainModelUI import TrainModelUI
from ctcUI import ctcMainUI
from TrackModelUI import TrackModelUI
from TrainControllerUI import TrainControllerUI
from WaysideUI import WMainWindowA, WMainWindowB, WaysideUIFunctions

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
ctcUI = ctcMainUI(track)
trackUI = TrackModelUI(track)

trainModUI = TrainModelUI()
trainConUI = TrainControllerUI()
waysideUIA = WMainWindowA()
waysideUIB = WMainWindowB()
#funcA = WaysideUIFunctions(waysideUIA)
#funcB = WaysideUIFunctions(waysideUIB)

# dispatch a test train
#ctcOffice.dispatch('Green', 1)
if len(sys.argv) == 1:
    ctcUI.show()
    waysideUIA.show()
    waysideUIB.show()
    trackUI.show()
    trainModUI.show()
    trainConUI.show()
elif sys.argv[1] == 'ctc':
    ctcUI.show()
elif sys.argv[1] == 'wayside':
    waysideUIA.show()
    waysideUIB.show() 
elif sys.argv[1] == 'track':
    trackUI.show()
elif sys.argv[1] == 'train':
    trainModUI.show()
elif sys.argv[1] == 'controller':
    trainConUI.show()
    
app.exec()

# show CTC window

# notes:
# train physics
# beacons (switch created)
# parse line into linked list that models the track connections??
# - or do we have an addTrack function that can be called each time we reparse?