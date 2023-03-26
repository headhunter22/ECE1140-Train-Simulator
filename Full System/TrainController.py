import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Train import Train
from Track import Track
from TrainModel import TrainModel

class TrainController(QObject):
    
    def __init__(self, trainModel):
        super().__init__()