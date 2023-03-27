import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Train import Train

class CTC (QObject):
    authorityToWayside = pyqtSignal(Train)
    suggSpeedToWayside = pyqtSignal(Train)
    switchStates = pyqtSignal(int, bool)

    def __init__(self):
        super().__init__()

    def send(self, a, s):
        self.authorityToWayside.emit(a)
        self.suggSpeedToWayside.emit(s)

    def dispatch(self, a, s, id):
        train = Train(a, s, id)
        self.authorityToWayside.emit(train)
        self.suggSpeedToWayside.emit(train)