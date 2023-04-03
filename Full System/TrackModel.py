import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from PyQt6 import uic
from Block import Block
from Track import Track
from Train import Train
from TicketSystem import TicketSystem
from MainTrackModelUI import MainWindow

class TrackModel(QObject):

    # signals to be sent
    blockOccupancyToWayside = pyqtSignal(Block)
    trackTrackModelToTrainModel = pyqtSignal(Track)
    trainTrackModelToTrainModel = pyqtSignal(Train)
    totalPassengersToWayside = pyqtSignal(int)

    def __init__(self, waysideController):
        super().__init__()
        
        # connect wayside signals
        self.wayside = waysideController
        self.wayside.suggSpeedWaysideToTrackModel.connect(self.suggSpeedReceived)
        self.wayside.trainObjectWaysideToTrackModel.connect(self.trainReceived)
        self.wayside.trackWaysideToTrackModel.connect(self.trackReceived)

        # create ticketing system
        self.ticketSystem = TicketSystem()

    def suggSpeedReceived(self, train):
        print("suggested speed from Wayside to Track Model " + str(train.suggSpeed)) 

    def trainReceived(self, train):
        # pass train to train model
        self.trainTrackModelToTrainModel.emit(train)

        # put the train in the first block out of yard
        #self.mainWindow.updateOccupancy('Green', 63)

    def trackReceived(self, track):
        self.track = track
        #self.mainWindow = MainWindow(track)

        # pass track onto train model
        self.trackTrackModelToTrainModel.emit(track)
        
    #def occupancyReceived(self, block):

    #def showModel(self):
    #    self.mainWindow.show()