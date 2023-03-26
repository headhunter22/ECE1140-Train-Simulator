import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from CTC import CTC
from Wayside import Wayside
from TrackModel import TrackModel
from TrainModel import TrainModel
# from TrainController import TrainController
from Train import Train
from Track import Track
#from TrainModel import TrainModel
#from TrainController import TrainController
import TrackParser
import random

# create the track before the program starts
# - do we pass track into each module in constructor? - for now, just in track model, later maybe start in CTC and propagate
# - or do we have an addTrack function that can be called each time we reparse?
# - reparsing will be needed when a new layout is uploaded to track model
track = TrackParser.parseTrack("TrackLayout.csv")

ctcOffice = CTC(track)
waysideController = Wayside(ctcOffice)
trackModel = TrackModel(waysideController)
trainModel = TrainModel(trackModel)
<<<<<<< HEAD
trainContoller = TrainController(trainModel)
=======
>>>>>>> 2bbdde8f835d8897a06d8fba955040a8e627fe75

# propagate track model
ctcOffice.propagateTrack()

ctcOffice.dispatch(10, 50, 1, 'Green')