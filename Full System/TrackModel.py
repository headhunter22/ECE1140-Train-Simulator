# system imports
import sys, os
from copy import deepcopy
import random

# pyqt imports 
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic

# class imports
from Block import Block
from Track import Track
from Train import Train
from TicketSystem import TicketSystem
import TrackParser
from signals import signals

# green route array
greenRouteArr = [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
                82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 85, 84,
                83, 82, 81, 80, 79, 78, 77, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
                112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128,
                129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145,
                146, 147, 148, 149, 150, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15,
                14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
                43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]

redRouteArr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
               31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
               53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 52, 51, 50, 49, 48, 47, 46, 45,
               44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 
               22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]

greenStations = {2: "Pioneer", 9: "Edgebrook", 22: "Whited", 31: "South Bank", 
                 39: "Central", 48: "Inglewood", 57: "Overbrook", 65: "Glenbury", 
                 73: "Dormont", 77: "Mt Lebanon", 88: "Poplar", 96: "Castle Shannon"}

redStations = {7: "Shadyside", 16: "Herron Ave", 21: "Swissville", 25: "Penn Station", 
               35: "Steel Plaza", 45: "First Ave", 48: "Station Square", 60: "South Hills"}

class TrackModel(QObject):

    def __init__(self):
        super().__init__()

        # attributes
        self.numTrains = 0

        # create ticket system
        self.ticketSystem = TicketSystem()
        
        # connect wayside signals
        signals.trackModelDispatchTrain.connect(self.dispatchTrain)
        signals.trackWaysideToTrackModel.connect(self.trackReceived)
    
        # connect train model signals
        signals.trackModelUpdateOccupancy.connect(self.updateOccupancy)
        signals.trackModelPassengersChanging.connect(self.board)
        signals.waysideSwitchtoTrack.connect(self.switchChanged)
        signals.waysideAuthoritytoTrack.connect(self.passAuthority)

        # create ticketing system
        self.ticketSystem = TicketSystem()

    # function to pass authority to train model
    def passAuthority(self, blocks, currentBlock):
        signals.authorityTrackModelToTrainModel.emit(blocks, currentBlock)

    # function to dispatch train
    def dispatchTrain(self, train):
        # increment trains on system
        self.numTrains += 1
        if train.line.lineName == "Green":
            train.route = deepcopy(greenRouteArr)
        elif train.line.lineName == "Red":
            train.route = deepcopy(redRouteArr)

        # generate passengers for each station
        passengers = {}
        for stop in train.destBlock:
            if stop in greenStations:
                numPassengers = random.randint(1,222)
                passengers[greenStations[stop]] = numPassengers
            if stop in redStations:
                numPassengers = random.randint(1,222)
                passengers[redStations[stop]] = numPassengers

        # check for last station on green line
        if 'Overbrook' in passengers:
            passengers['Overbrook'] = 0
        # check for last station on red line
        if 'Edgebrook' in passengers:
            passengers['Edgebrook'] = 0
        
        signals.trackModelGUIWaitingPassengers.emit(passengers)

        # update occupancy in gui
        signals.trackModelUpdateGUIOccupancy.emit(train.line.lineName, str(train.block))
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
            signals.waysideUpdateOccupancy.emit(train.line.lineName, train.block, train.route)
            #signals.testAuthTrackModelToWayside.emit(train.line.lineName, train.route)
            signals.trackModelBeaconSending.emit(self.track.getLine(line.lineName).getBlock(block))
            signals.trackModelTrainInfoToWayside.emit(train)
        else:
            signals.trackModelUpdateGUIVacancy.emit(line.lineName, str(block))
            signals.waysideUpdateVacancy.emit(train.line.lineName, train.block, train.route)

    def board(self, train):
        # load new passengers
        self.ticketSystem.boardTrain(train)
        print('passengers on:', train.numPassengers)
        signals.trainModelPassengers.emit(train.numPassengers)      
        self.ticketSystem.releasePassengers(train)

    def switchChanged(self, stem, dest):
        return
        # receive switch state from wayside
        # update gui

    def tempChanged(self):
        # if entry is nonsense, do nothing
        if not self.tempEntry.text().isnumeric(): 
            return

        signals.trackModelTempUpdated.emit(int(self.tempEntry.text()))