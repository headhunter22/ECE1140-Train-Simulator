from PyQt6.QtCore import QObject, pyqtSignal
from Line import Line
from Train import Train
import sys
sys.dont_write_bytecode = True

class Signals(QObject):

    # train model signals
    trainModelDispatchTrain = pyqtSignal(Train) # trainID, Line, destination, commandedSpeed, authority, route
    trainModelGetPower = pyqtSignal(Train, float) # trainID, commandedPower
    trainModelUpdateCommandedSpeed = pyqtSignal(Train, float) # trainID, commandedSpeed
    trainModelUpdateGUISpeed = pyqtSignal(str)
    trainModelGUIcommandedSpeed = pyqtSignal(str)
    trainModelGUIBlock = pyqtSignal(str)
    trainModelGUIpower = pyqtSignal(str)