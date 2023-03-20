import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from PyQt6.QtCore import QSize
from CTCSend import CTCSend

class WaysideReceive:
    def __init__(self) -> None:
        self.CTC = CTCSend()

    