import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic

class CTC (QObject):
    authorityToWayside = pyqtSignal(int)
    suggSpeedToWayside = pyqtSignal(int)
    switchStates = pyqtSignal(int, bool)

    def __init__(self):
        super().__init__()

    def receive(self):
        self.Rx.pullInfo()

    def send(self, a, s, sw):
        self.authorityToWayside.emit(a)
        self.suggSpeedToWayside.emit(s)
        self.switchStates.emit(sw)