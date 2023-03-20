import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from PyQt6.QtCore import QSize

class Wayside:
    def __init__(self, ctcOffice):
        self.CTC = ctcOffice
        self.CTC.authorityToWayside.connect(self.authorityReceived)
        self.authority = 0

    def authorityReceived(self, a):
        self.authority = a
        print("authority from CTC to Wayside: " + str(self.authority))

    def suggSpeedReceived(self, s):
        self.authority = s
        print("authority from CTC to Wayside: " + str(self.authority))

    def switchStateReceived(self, sw):
        self.authority = sw
        print("authority from CTC to Wayside: " + str(self.authority))
        