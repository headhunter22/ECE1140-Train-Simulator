import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from CTC import CTC
from Wayside import Wayside
from TrackModel import TrackModel
from Train import Train
import random

ctcOffice = CTC()
waysideController = Wayside(ctcOffice)
trackModel = TrackModel(waysideController)

ctcOffice.dispatch(random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000))
ctcOffice.dispatch(random.randint(1, 1000), random.randint(1, 1000), random.randint(1, 1000))
