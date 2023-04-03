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
import TrackParser
import random
from threading import Thread
#from Clock import Clock
from ClockThreaded import clock

# import UIs
import ctcMainUi

track = TrackParser.parseTrack("TrackLayout.csv")
clock.startTimer()

ctcOffice = CTC(track, clock)
waysideController = Wayside(ctcOffice)
ctcOffice.addWayside(waysideController)
trackModel = TrackModel(waysideController)
trainModel = TrainModel(trackModel)

# propagate track model
ctcOffice.propagateTrack()

# dispatch a test train
ctcOffice.dispatch('Green', 1)

# show CTC window

# notes:
# train physics
# beacons (switch created)
# parse line into linked list that models the track connections??
# - or do we have an addTrack function that can be called each time we reparse?