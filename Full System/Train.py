from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from threading import Thread
import time
import math
import sys
sys.dont_write_bytecode = True

class Train(QObject):
    trainCounter = 0

    def __init__(self, id, line, destBlocks):
        super().__init__()

        self.route = []

        # id
        self.ID = id

        # location attributes
        self.line = line
        self.block = 63
        self.position = 0.0
        self.destBlock = destBlocks
        self.reachedDest = False

        # authority and speeds
        self.authority = 0
        self.currentSpeed = 0
        self.suggSpeed = 70
        self.commandedSpeed = 0
        self.commandedPower = 0
        self.actSpeed = 0
        self.numPassengers = 0
        self.serviceBrake = 0
        self.emBrake = 0

        #power calculation vars
        self.An_1 = 0
        self.An = 0
        self.actSpeed_1 = 0
        self.T = 1

        # mass info
        self.baseMass = 81950 # kgs