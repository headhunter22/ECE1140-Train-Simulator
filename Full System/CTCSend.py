import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic

class CTCSend(QObject):
    # signals sent from the CTC office to the Wayside Controller
    authorityToWayside = pyqtSignal(int)

    def __init__(self) -> None:
        super().__init__()

    def sendInfo(self):
        self.authorityToWayside.emit(50)
        print('send info ctc')