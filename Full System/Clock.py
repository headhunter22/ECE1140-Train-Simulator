from PyQt6 import QtCore
import sys

class Clock():
    def __init__(self):
        self.clock = QtCore.QTimer()
        self.time = 25200
        #self.clock.timeout.connect(self.changeLabel)

    def start(self):
        self.clock.start(1000)

    def tenTimesSpeed(self):
        self.clock.setInterval(100)

    def fiftyTimesSpeed(self):
        self.clock.setInterval(20)
    
#    def changeLabel(self, label):
#        self.time += 1
#
#        hrs = self.time / 3600
#        mins = (hrs - int(hrs)) * 60
#        secs = (mins - int(mins)) * 60
#
#        label.setText(f'{int(hrs):02d}' + ':' + f'{int(mins):02d}' + ':' + f'{int(secs):02d}')