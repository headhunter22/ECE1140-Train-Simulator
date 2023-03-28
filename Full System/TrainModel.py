import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Block import Block
from Track import Track
from Train import Train
from TrainController import TrainController

class TrainModel(QObject):
    
    def __init__(self, trackModel):
        super().__init__()
        
        #self.TrainController = trainController        
        # connect track model
        self.trackModel = trackModel

        self.trackModel.trackTrackModelToTrainModel.connect(self.trackReceived)
        self.trackModel.trainTrackModelToTrainModel.connect(self.trainReceived)

    def trainReceived(self, train):
        # set train speed to speed limit
        train.commandedSpeed = self.track.getLine(train.line).getBlock('63').speedLimit
        train.sendActualSpeed()

    def trackReceived(self, track):
        self.track = track