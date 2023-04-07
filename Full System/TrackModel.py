import sys, os
from copy import deepcopy
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Block import Block
from Track import Track
from Train import Train
from TicketSystem import TicketSystem
from signals import signals

# green route array
greenRouteArr = [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
                82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 85, 84,
                83, 82, 81, 80, 79, 78, 77, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
                12, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128,
                129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145,
                146, 147, 148, 149, 150, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15,
                14, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
                43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]

class TrackModel(QObject):

    def __init__(self):
        super().__init__()

        # attributes
        self.numTrains = 0
        
        # connect wayside signals
        signals.trackModelDispatchTrain.connect(self.dispatchTrain)
        signals.trackWaysideToTrackModel.connect(self.trackReceived)
    
        # connect train model signals
        signals.trackModelUpdateOccupancy.connect(self.updateOccupancy)

        # create ticketing system
        self.ticketSystem = TicketSystem()

    # function to dispatch train
    def dispatchTrain(self, train):
        print('track model dispatched')
        
        # increment trains on system
        self.numTrains += 1
        train.route = deepcopy(greenRouteArr)

        # update occupancy in gui
        signals.trackModelUpdateGUIOccupancy.emit(train.line.lineName, str(train.block))
        signals.ctcUpdateGUIOccupancy.emit(train.line.lineName, train.block)
        #signals.waysideUpdateOccupancy.emit(train.block)

        # dispatch train with route to train model
        signals.trainModelDispatchTrain.emit(train)

    def trackReceived(self, track):
        self.track = track
        #self.mainWindow = MainWindow(track)

        # pass track onto train model
        signals.trainModelGetTrack.emit(track)
        
    def updateOccupancy(self, train, line, block, occupied):
        # send new commanded speed
        speedLimit = self.track.getLine(line.lineName).getBlock(block).speedLimit
        signals.trainModelUpdateCommandedSpeed.emit(train, speedLimit)

        # send signal to gui to update
        if occupied:
            signals.trackModelUpdateGUIOccupancy.emit(line.lineName, str(block))
            signals.ctcUpdateGUIOccupancy.emit(train.line.lineName, train.block)
            signals.ctcUpdateGUITrainInfo.emit(train.line.lineName, train.ID, train.block, train.commandedSpeed, train.authority, train. destBlock)
            signals.waysideUpdateOccupancy.emit(block)
        else:
            signals.trackModelUpdateGUIVacancy.emit(line.lineName, str(block))
            signals.ctcUpdateGUIOccupancy.emit(train.line.lineName, train.block)
            signals.ctcUpdateGUITrainInfo.emit(train.line.lineName, train.ID, train.block, train.commandedSpeed, train.authority, train. destBlock)
            signals.waysideUpdateVacancy.emit(block)