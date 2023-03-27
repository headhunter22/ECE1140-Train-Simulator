from PyQt6 import QtCore
import sys

class Clock():
    def __init__(self):
        self.clock = QtCore.QTimer()
        self.time = 0

    def tenTimesSpeed(self):
        self.clock.setInterval(100)

    def fiftyTimesSpeed(self):
        self.clock.setInterval(20)
    
    def changeLabel(self):
        self.time += 1

        hrs = self.time / 3600
        mins = (hrs - int(hrs)) * 60
        secs = (mins - int(mins)) * 60

        self.label.setText(f'{int(hrs):02d}' + ':' + f'{int(mins):02d}' + ':' + f'{int(secs):02d}')