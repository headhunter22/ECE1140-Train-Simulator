import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from CTC import CTC
from Wayside import Wayside
from TrackModel import TrackModel
from Train import Train
from Track import Track
import TrackParser
import random

# create the track before the program starts
# - do we pass track into each module in constructor?
# - or do we have an addTrack function that can be called each time we reparse?
# - reparsing will be needed when a new layout is uploaded to track model
track = TrackParser.parseTrack("TrackLayout.csv")

ctcOffice = CTC()
waysideController = Wayside(ctcOffice)
trackModel = TrackModel(waysideController)

# add track model to the Wayside Controller
waysideController.addTrackModel(trackModel)

ctcOffice.dispatch(random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000))
ctcOffice.dispatch(random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000))

