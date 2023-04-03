import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Block import Block
from Track import Track
from Train import Train
from TrainController import TrainController

class TrainModel(QObject):

    def __init__(self, trackModel):
        super().__init__()
        
        #self.TrainController = trainController        
        # connect track model
        self.trackModel = trackModel
        
        # array to hold trains
        self.trainList = []

        # connect signals
        signals.trainModelDispatchTrain.connect(self.dispatchTrain)
        signals.trainModelUpdateCommandedSpeed.connect(self.updateCommandedSpeed)
        signals.trainModelGetPower.connect(self.updatedPower)

    # function to dispatch a train
    def dispatchTrain(self, train):
        # add train to current trains list
        self.trainList.append(train)

        # update occupancy of block 
        signals.trackModelUpdateOccupancy.emit(trainID, train.line, 0, True)

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

        prevPos = train.prevPos

        currPos = 0
        currPos = prevPos + (movement * samplePeriod)

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
        

    def trainReceived(self, train):
        # set train speed to speed limit
        print(self.track.getLine(train.line).getBlock('63').speedLimit)
        train.commandedSpeed = self.track.getLine(train.line).getBlock('63').speedLimit
        #train.sendSpeeds()

        # send authority to controller
        train.trainController.authority = train.authority

    def trackReceived(self, track):
        self.track = track