import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from CTC import CTC
from Wayside import Wayside

ctcOffice = CTC()
waysideController = Wayside(ctcOffice)

ctcOffice.send(500000)
ctcOffice.send(6969)
ctcOffice.send(5, 0)
