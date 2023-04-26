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
from WaysideUI import selectionWindow, WMainWindowA#, WMainWindowB, WaysideUIFunctions

class Main(QtWidgets.QMainWindow):
    def __init__(self, ctcUI, trackUI, trainModUI, trainConUI, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("fullsystem.ui", self)
        self.setWindowTitle('North Shore Extension Home')

        self.ctcUI = ctcUI
        self.trackUI = trackUI
        self.trainModUI = trainModUI
        self.trainConUI = trainConUI

        self.ctcOffice.clicked.connect(self.showCTC)
        self.trackModel.clicked.connect(self.showTrack)
        self.trainModel.clicked.connect(self.showTrain)
        self.trainController.clicked.connect(self.showController)
        #self.waysideController.clicked.connect(self.showWayside)

    def showCTC(self):
        self.ctcUI.show()
    def showTrack(self):
        self.trackUI.show()
    def showTrain(self):
        self.trainModUI.show()
    def showController(self):
        self.trainConUI.show()

track = TrackParser.parseTrack("TrackLayout.csv")
app = QtWidgets.QApplication(sys.argv)
clock.startTimer()

waysidestartUI = selectionWindow()

ctcOffice = CTC(track)
waysideController = Wayside(ctcOffice, waysidestartUI)
ctcOffice.addWayside(waysideController)
trackModel = TrackModel()
trainModel = TrainModel()
tc = SWTrainController()

# propagate track model
ctcOffice.propagateTrack()

# instantiate UIs
ctcUI = ctcMainUI(track)
trackUI = TrackModelUI(track)
trainModUI = TrainModelUI()
trainConUI = TrainControllerUI()

waysidestartUI.show()

mainProgram = Main(ctcUI, trackUI, trainModUI, trainConUI)
mainProgram.show()
app.exec()