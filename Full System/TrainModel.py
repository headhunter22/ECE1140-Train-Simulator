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
import time

class TrainModel(QObject):
    #its a comment

    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        
        # array to hold trains
        self.trainList = []

        self.serviceBrake = False
        self.emerBrake = False
        self.manualMode = False
        self.manualCommSpeed = 0
        self.timeWaiting = 0

        # connect signals
        signals.trainModelDispatchTrain.connect(self.dispatchTrain)
        signals.trainModelUpdateCommandedSpeed.connect(self.updateCommandedSpeed)
        signals.trainModelGetPower.connect(self.updatedPower)
        signals.trainModelGetTrack.connect(self.trackReceived)
        signals.trainControllerServiceBrake.connect(self.serviceBrakeActive)
        signals.trainModelEmerBrake.connect(self.emerBrakeActive)
        signals.waysideAuthoritytoTrack.connect(self.newAuthority)
        signals.trainControllerManualModeToTrainModel.connect(self.manualModeFunc)
        signals.trainControllerEmerBrake.connect(self.emerBrakeActive)

    # function to dispatch a train
    def dispatchTrain(self, train):

        # add train to current trains list
        self.trainList.append(train)
        train.commandedSpeed = self.track.getLine(train.line.lineName).getBlock(train.block).speedLimit * .27777

        # update occupancy of block 
        signals.trackModelUpdateOccupancy.emit(train, train.line, train.route[0], True)
        
        # emit dispatched signal to train controller
        signals.trainControllerDispatchedSignal.emit(train)

        #displaying train destination
        signals.trainModelDestinationSignal.emit(train.destBlock)
        #displaying trainLine and train name
        signals.trainModelLineSignal.emit(train.line)
        
        signals.trainControllerUpdateCommSpeed.emit(self.track.getLine(train.line.lineName).getBlock(train.block).speedLimit)

    def updatedPower(self, train, power):
        if len(self.trainList) == 0:
            return
        # get current line, block and the associated length, speed limit
        currLine = train.line
        currBlock = train.block

        # if the train has stopped at all given destination, go to yard
        if not train.destBlock:
            train.destBlock.append(57)

        if currBlock == train.destBlock[0]:
            train.reachedDest = True

        currBlockSize = float(currLine.getBlock(currBlock).length)

        if (self.manualMode == False):
            commSpeed = currLine.getBlock(train.route[1]).speedLimit #GET RID OF PLUS 2!! USE ROUTE[]
        else:
            commSpeed = self.manualCommSpeed *1.609
           
        currBlockSpeedLimit = currLine.getBlock(currBlock).speedLimit 
        if (commSpeed > currBlockSpeedLimit):
            commSpeed = currBlockSpeedLimit

        signals.trainModelGUISpeedLim.emit(str(currBlockSpeedLimit))

        # calculate dist to stop
        distToStop = 0
        tempBlock = currBlock
        offset = 1
        while tempBlock != train.destBlock[0] and not train.reachedDest:
            distToStop += float(currLine.getBlock(tempBlock).length)
            tempBlock = train.route[offset]
            offset += 1
        
        train.authority = distToStop - train.position

        M = (train.numPassengers*150) + train.baseMass
        theta = math.atan(float(self.track.getLine('Green').getBlock(train.block).elevation)/currBlockSize)
        g = 9.8 # m/s^2
        friction = .006

        # calculating acceleration
        # if starting off at 0m/s, set acceleration to medium

        if train.actSpeed_1 == 0 | self.emerBrake != 1:
            train.An = 0.5
        elif self.emerBrake == 1:
            train.An = -2.73
            if (train.actSpeed == 0):
                train.An = 0
            power = 0
        #elif self.serviceBrake == 1:
            #train.An = -1.2
            #power = 0
        # if moving, calculate acceleration
        else:
            if (train.actSpeed*3.6) > commSpeed:
                train.An = -1.2
                #train.An = ((-1*M*g*math.cos(theta)*friction) + (M*g*math.sin(theta)))/M
            else:
                trainForce = power / train.actSpeed_1
                train.An = ((1*M*g*math.cos(theta)*friction) + (M*g*math.sin(theta)) + (trainForce))/M
        
        # if acceleration is too high, cap at 0.5
        if train.An > 0.5:
            train.An = 0.5
        
        if self.serviceBrake == True: #TRAIN CONTROLLER: DONT FORGET TO CHANGE THIS SIGNAL BACK TO FALSE
            train.An = -1.2 

        train.actSpeed = train.actSpeed_1 + train.T/2 * (train.An + train.An_1)

        if (train.actSpeed < 0):
            train.actSpeed = 0
            self.serviceBrake = False
            train.destBlock.pop(0)

        prevPos = train.position

        currPos = prevPos + (train.actSpeed)

        # we have traversed more than the current block length
        if currPos > int(currBlockSize):

            train.block = train.route[1]
            prevBlock = train.route[0]
            if (train.block == 57):
                self.actSpeed = 0
                print("REACHED THE END OF THE LINE!!")
            else:
                currPos = currPos - int(currBlockSize)
                train.position = currPos
                train.route.pop(0)

            #if len(train.route) == 0:
                # update train speed to 0 and delete train

            # update track model occupancy to unoccupied for currBlock
            signals.trackModelUpdateOccupancy.emit(train, train.line, prevBlock, False)

            # update track model occupancy to occupied for next block in route
            signals.trackModelUpdateOccupancy.emit(train, train.line, train.route[0], True)

            signals.trainControllerUpdateCommSpeed.emit(train.line.getBlock(train.route[0]).speedLimit)
           
        # we have not traversed more than the current block length
        else:
            # still in current block, update train position
            train.position = currPos

        # set previous variables
        train.An_1 = train.An
        train.actSpeed_1 = train.actSpeed

        # train at the end of the track
        if (train.block == 57):
            train.actSpeed = 0

        #sending all signals to the display
        signals.trainModelUpdateGUISpeed.emit(str(train.actSpeed))
        signals.trainModelGUIBlock.emit(str(train.block))
        signals.trainModelGUIcommandedSpeed.emit(str(commSpeed))

        signals.trainModelGUIpower.emit(str(power))
        signals.trainModelGUIacc.emit(str(train.An))

    
    def trackReceived(self, track):
        self.track = track

    def updateCommandedSpeed(self, train, speed):
        train.commandedSpeed = speed
    
    def serviceBrakeActive(self, serviceBrake):
        self.serviceBrake = serviceBrake
    
    def emerBrakeActive(self, emerBrake):
        self.emerBrake = emerBrake
    
    def newAuthority(self,blocks, currentblock): #blocks is int allowed, currentblock is 
        currLine = self.trainList[0].line
        self.trainList[0].authority = blocks

        auth = 0
        for i in range(blocks):
            print('currLine: ' +str(currLine.getBlock(self.trainList[0].route[i]).length))
                  
            if (str(currLine.getBlock(self.trainList[0].route[i]).length) == '86.6'):
                newAuth = 87
            else:
                newAuth = int(currLine.getBlock(self.trainList[0].route[i]).length)
            auth += newAuth
        print("new authority")
        #currblock = self.track0.index(currentblock)
        #next1 = self.track0[currblock+1]
        #next2 = self.track0[currblock+2]
        #next3 = self.track0[currblock+3]
        #next4 = self.track0[currblock+4]
        #next5 = self.track0[currblock+5]
        #next6 = self.track0[currblock+6]
        #next7 = self.track0[currblock+7]
        #next8 = self.track0[currblock+8]

        #signals.trainModelAuthorityToTrainController.emit(auth)
    
    def manualModeFunc(self, manualMode, commSpeed):
        self.manualMode = manualMode
        self.manualCommSpeed = commSpeed