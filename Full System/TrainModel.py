import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Block import Block
from Track import Track

class TrainModel(QObject):

    # signals to be sent
    
    def __init__(self, trackModel):
        super().__init__()
        
        # connect track model
        self.trackModel = trackModel

        self.trackModel.trackTrackModelToTrainModel.connect(self.trackReceived)
        self.trackModel.trainTrackModelToTrainModel.connect(self.trainReceived)

    def trainReceived(self, train):
        # set train speed to speed limit
        train.commandedSpeed = self.track.getLine(train.line).getBlock('63').speedLimit
        print(train.commandedSpeed)

    def trackReceived(self, track):
        self.track = track
        print(track.lines)
        