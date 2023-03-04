import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QSize

# Fault Display Class
class FaultDisplay(QtWidgets.QMainWindow):
    def __init__(self, track, *args, **kwargs):
        self.track = track

        super().__init__(*args, **kwargs)
        uic.loadUi("FaultDisplay.ui", self)
        self.setWindowTitle('Fault Display')

        # connect dropdowns changing to function to pull up locations with that fault type
        self.FaultSelect.currentTextChanged.connect(self.getLocation)
        self.LocationLabel.setText(', '.join(self.track.faults['Power']))

    def getLocation(self):
        # line block select
        faultType = self.FaultSelect.currentText()

        # search faultDict for faults of that type
        self.LocationLabel.setText(', '.join(self.track.faults['Power']))

# end fault display class