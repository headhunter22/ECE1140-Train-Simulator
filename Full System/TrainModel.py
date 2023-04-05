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

    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        # array to hold trains
        self.trainList = []

        # connect signals
        signals.trainModelDispatchTrain.connect(self.dispatchTrain)
        signals.trainModelUpdateCommandedSpeed.connect(self.updateCommandedSpeed)
        signals.trainModelGetPower.connect(self.updatedPower)
        signals.trainModelGetTrack.connect(self.trackReceived)

    # function to dispatch a train
    def dispatchTrain(self, train):
        print('train model dispatched')

        # add train to current trains list
        self.trainList.append(train)
        train.commandedSpeed = self.track.getLine(train.line.lineName).getBlock(train.block).speedLimit * .27777

        # update occupancy of block 
        signals.trackModelUpdateOccupancy.emit(train, train.line, train.route[0], True)
        
        # emit dispatched signal to train controller
        signals.trainControllerDispatchedSignal.emit(train)

    # function to update commanded speed
    #def updateCommandedSpeed(self, trainID, commandedSpeed):
    #

    def updatedPower(self, train, power):
        # get current line, block and the associated length, speed limit
        currLine = train.line
        currBlock = train.block

        print('power received: ' + str(power))

        currBlockSize = float(currLine.getBlock(currBlock).length)
        blockSpeedLimit = currLine.getBlock(currBlock).speedLimit

        # calculate dist to stop
        distToStop = 0
        tempBlock = currBlock
        offset = 1
        while tempBlock != train.destBlock:
            distToStop += float(currLine.getBlock(tempBlock).length)
            tempBlock = train.route[offset]
            offset += 1

        train.authority = distToStop - train.position

        print('dist to stop: ' + str(train.authority))

        # convert speed limit, commSpeed to m/s
        commSpeed = train.commandedSpeed * 0.27777

        M = (train.numPassengers*150) + train.baseMass
        theta = math.atan(float(self.track.getLine('Green').getBlock(train.block).elevation)/currBlockSize)
        g = 9.8 # m/s^2
        friction = .006

        print('speed limit: ' + str(blockSpeedLimit))

        # calculating acceleration
        # if starting off at 0m/s, set acceleration to medium
        if train.actSpeed_1 == 0:
            print('not moving')
            train.An = 0.5
        elif train.emBrake == 1:
            train.An = -2.73
        elif train.serviceBrake == 1:
            train.An = -1.2
        # if moving, calculate acceleration
        else:
            if (train.actSpeed*3.6) > blockSpeedLimit:
                train.An = ((-1*M*g*math.cos(theta)*friction) + (M*g*math.sin(theta)))/M
                print('During Too Fast An: ' + str(train.An))
            else:
                trainForce = power / train.actSpeed_1
                train.An = ((-1*M*g*math.cos(theta)*friction) + (M*g*math.sin(theta)) + (trainForce))/M
        
        # if acceleration is too high, cap at 0.5
        if train.An > 0.5:
            train.An = 0.5

        print('An: ' + str(train.An))
        train.actSpeed = train.actSpeed_1 + train.T/2 * (train.An + train.An_1)

        prevPos = train.position

        currPos = prevPos + (train.actSpeed)

        # we have traversed more than the current block length
        if currPos > int(currBlockSize):
            train.block = train.route[1]
            currPos = currPos - int(currBlockSize)
            train.position = currPos
            train.route.pop(0)

            #if len(train.route) == 0:
                # update train speed to 0 and delete train

            # update track model occupancy to unoccupied for currBlock
            signals.trackModelUpdateOccupancy.emit(train, train.line, currBlock, False)

            # update track model occupancy to occupied for next block in route
            signals.trackModelUpdateOccupancy.emit(train, train.line, train.route[0], True)

        # we have not traversed more than the current block length
        else:
            # still in current block, update train position
            train.position = currPos

        # print('speed: ' + str(train.actSpeed * 3.6))
        # print('position: ' + str(train.position))
        # print('block number: ' + str(train.block))
        # print('commanded speed: ' + str(train.commandedSpeed))

        # set previous variables
        train.An_1 = train.An
        train.actSpeed_1 = train.actSpeed

        signals.trainModelUpdateGUISpeed.emit(str(train.actSpeed))
        #signals.trackModelUpdateGUIVacancy.emit(line.lineName, str(block))
    
    def trackReceived(self, track):
        self.track = track

    def updateCommandedSpeed(self, train, speed):
        train.commandedSpeed = speed