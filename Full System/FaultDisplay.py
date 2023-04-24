import sys, os
from signals import signals
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtCore import QSize

# Fault Display Class
class FaultDisplay(QtWidgets.QMainWindow):
    def __init__(self, track, *args, **kwargs):
        self.track = track

        super().__init__(*args, **kwargs)
        uic.loadUi("FaultDisplay.ui", self)
        self.setWindowTitle('Fault Display')
        
        signals.trackModelUpdateGUIFaults.connect(self.addFault)

    def addFault(self, fault):
        return

# end fault display class