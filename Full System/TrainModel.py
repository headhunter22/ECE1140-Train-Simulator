import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Block import Block
from Track import Track
from Train import Train
from TrainController import TrainController
from signals import signals
import math

class TrainModel(QObject):

    def __init__(self):
        super().__init__()
        
        # array to hold trains
        self.trainList = []

        # connect signals
        signals.trainModelDispatchTrain.connect(self.dispatchTrain)
        #signals.trainModelUpdateCommandedSpeed.connect(self.updateCommandedSpeed)
        signals.trainModelGetPower.connect(self.updatedPower)
        signals.trainModelGetTrack.connect(self.trackReceived)

    # function to dispatch a train
    def dispatchTrain(self, train):
        print('train model dispatched')

        # add train to current trains list
        self.trainList.append(train)
        train.commandedSpeed = self.track.getLine(train.line.lineName).getBlock(train.block).speedLimit
        train.actSpeed_1 = self.track.getLine(train.line.lineName).getBlock(train.block).speedLimit

        # update occupancy of block 
        signals.trackModelUpdateOccupancy.emit(train.ID, train.line, 0, True)
        
        # emit dispatched signal to train controller
        signals.trainControllerDispatchedSignal.emit(train)

    # function to update commanded speed
    #def updateCommandedSpeed(self, trainID, commandedSpeed):
    #

    def updatedPower(self, train, power):
        # get current line, block and the associated length, speed limit
        currLine = train.line
        currBlock = train.block

        currBlockSize = currLine.getBlock(currBlock).length
        blockSpeedLimit = currLine.getBlock(currBlock).speedLimit

        # convert speed limit, commSpeed to m/s
        blockSpeedLimit *= 0.27777
        commSpeed = train.commandedSpeed * 0.27777

        M = (train.numPassengers*150) + train.baseMass
        theta = math.degrees(math.atan(train.track.getLine('Green').getBlock(str(train.location)).elevation))
        g = 9.8 # m/s^2
        friction = .006

        # calculating the braking force
        if self.emBrake == 1:
            F_b = -2.73
        elif self.serviceBrake == 1:
            F_b = -1.2
        else:
            F_b = 0

        # calculating acceleration
        train.An = ((M*g*math.cos(theta)*friction) + (M*g*math.cos(theta)) + F_b + (power/train.actSpeed_1))/M
        train.actSpeed = train.actSpeed_1 + train.T/2 *(train.An - train.An_1)
        
        signals.actSpeedtoTrainModelUI.emit(train.actSpeed) #send to UI

        # set previous variables
        train.An_1 = train.An
        train.actSpeed_1 = train.actSpeed

        # calculate force
        force = 0.5 * train.baseMass

        train.actualSpeed = train.commandedPower / force

        prevPos = train.prevPos

        currPos = 0
        currPos = prevPos + (train.actualSpeed * 0.2)

        # we have traversed more than the current block length
        if currPos > currBlockSize:
            currPos = currPos - currBlockSize
            train.prevPos = currPos
            train.route.pop(0)

            #if len(train.route) == 0:
                # update train speed to 0 and delete train

            # update track model occupancy to unoccupied for currBlock
            signals.trackModelUpdateOccupancy(train.trainID, train.line, currBlock, False)

            # update track model occupancy to occupied for next block in route
            signals.trackModelUpdateOccupancy(train.trainID, train.line, train.route[0], True)

        # we have not traversed more than the current block length
        else:
            # still in current block, update train position
            train.position = currPos

        print(train.actSpeed)

        # emit current speed back to train controller
        #signals.trainControllerUpdateCurrSpeed.emit(train, train.actualSpeed)
    
    def trackReceived(self, track):
        self.track = track