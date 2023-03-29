import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from CTC import CTC
from Wayside import Wayside
from TrackModel import TrackModel
from TrainModel import TrainModel
from TrainController import TrainController
from Train import Train
from Track import Track
#from TrainModel import TrainModel
#from TrainController import TrainController
import TrackParser
import random

# notes:
# train physics
# beacons (switch created)
# parse line into linked list that models the track connections??

# - or do we have an addTrack function that can be called each time we reparse?
track = TrackParser.parseTrack("TrackLayout.csv")

ctcOffice = CTC(track)
waysideController = Wayside(ctcOffice)
ctcOffice.addWayside(waysideController)
trackModel = TrackModel(waysideController)
trainModel = TrainModel(trackModel)

# propagate track model
ctcOffice.propagateTrack()
ctcOffice.dispatch(10, 50, 1, 'Green')