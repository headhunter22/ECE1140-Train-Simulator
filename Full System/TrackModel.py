import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic

class TrackModel(QObject):
    def __init__(self, waysideController):
        super().__init__()
        self.wayside = waysideController
        self.suggSpeed = 0

    def suggSpeedReceived(self, suggSpeed):
        self.suggSpeed = suggSpeed
        print("suggested speed from Wayside to Track Model " + str(self.suggSpeed)) 