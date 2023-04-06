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

        self.serviceBrake = False
        self.timeWaiting = 0

        # connect signals
        signals.trainModelDispatchTrain.connect(self.dispatchTrain)
        signals.trainModelUpdateCommandedSpeed.connect(self.updateCommandedSpeed)
        signals.trainModelGetPower.connect(self.updatedPower)
        signals.trainModelGetTrack.connect(self.trackReceived)
        signals.trainControllerServiceBrake.connect(self.serviceBrakeActive)

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

    def updatedPower(self, train, power):
        # get current line, block and the associated length, speed limit
        currLine = train.line
        currBlock = train.block
        if currBlock == train.destBlock:
            train.reachedDest = True

        print('power received: ' + str(power))

        currBlockSize = float(currLine.getBlock(currBlock).length)
        blockSpeedLimit = currLine.getBlock(currBlock).speedLimit

        # calculate dist to stop
        distToStop = 0
        tempBlock = currBlock
        offset = 1
        while tempBlock != train.destBlock and not train.reachedDest:
            distToStop += float(currLine.getBlock(tempBlock).length)
            tempBlock = train.route[offset]
            offset += 1

        train.authority = distToStop - train.position
        
        # update authority for ctc occupancy view
        ############### CHNAGE THIS CALC TO WAYSIDE BC SHE CALCULATES AUTH #####################
        signals.ctcUpdateGUIAuthority.emit(train.authority)

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
        
        if self.serviceBrake == True: #TRAIN CONTROLLER: DONT FORGET TO CHANGE THIS SIGNAL BACK TO FALSE
            train.An = -1.2 


        print('An: ' + str(train.An))
        train.actSpeed = train.actSpeed_1 + train.T/2 * (train.An + train.An_1)

        if (train.actSpeed < 0):
            train.actSpeed = 0
            #print(" done waiting")
            
            #train.An = 0.5
            self.serviceBrake = False
            #train.actSpeed = 1
            
            

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

        #sending all signals to the display
        signals.trainModelUpdateGUISpeed.emit(str(train.actSpeed))
        signals.trainModelGUIBlock.emit(str(train.block))
        signals.trainModelGUIcommandedSpeed.emit(str(train.commandedSpeed))
        signals.trainModelGUIpower.emit(str(power))
    
    def trackReceived(self, track):
        self.track = track

    def updateCommandedSpeed(self, train, speed):
        train.commandedSpeed = speed
    
    def serviceBrakeActive(self, serviceBrake):
        self.serviceBrake = serviceBrake
        print(int(self.serviceBrake))
    
    def stopped30Sec(self,hrs,min,sec):
        self.timeWaiting = self.timeWaiting + 1
        print('timewaiting = ' + str(self.timeWaiting))
        if self.timeWaiting == 30:
            print("train waited 30 seconds")
            return True
        else:
            return False
