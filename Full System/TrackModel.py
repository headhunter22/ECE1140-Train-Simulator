import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic

class TrackModel(QObject):
    def __init__(self, waysideController):
        super().__init__()
        self.wayside = waysideController
        self.wayside.suggSpeedWaysideToTrackModel.connect(self.suggSpeedReceived)

    def suggSpeedReceived(self, train):
        print("suggested speed from Wayside to Track Model " + str(train.suggSpeed) + "\n\n") 