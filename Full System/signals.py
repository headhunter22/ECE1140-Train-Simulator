from PyQt6.QtCore import QObject, pyqtSignal
from Line import Line
from Train import Train

class Signals(QObject):
    # timer signal
    timerTicked = pyqtSignal(int, int, int) # hrs, mins, secs to send to CTC
    
    # ctc signals
    # trackCTCToWayside = pyqtSignal(Track)
    # authorityToWayside = pyqtSignal(Train)
    # suggSpeedToWayside = pyqtSignal(Train)
    # trainObjectToWayside = pyqtSignal(Train)
    # switchStates = pyqtSignal(int, bool)

    # wayside controller signals
    waysideDispatchTrain = pyqtSignal(Train) # trainID, suggSpeed, authority, Line, destination

    # signals to track model
    # suggSpeedWaysideToTrackModel = pyqtSignal(Train)
    # trainObjectWaysideToTrackModel = pyqtSignal(Train)
    # commandedSpeedWaysideToTrackModel = pyqtSignal(int)
    # trackWaysideToTrackModel = pyqtSignal(Track)
    # greenLineSwitches = pyqtSignal(int)
    # signals to CTC
    # passengersToCTC = pyqtSignal(int)

    # track model signals
    # # signals to be sent
    # blockOccupancyToWayside = pyqtSignal(Block)
    # trackTrackModelToTrainModel = pyqtSignal(Track)
    # trainTrackModelToTrainModel = pyqtSignal(Train)
    # totalPassengersToWayside = pyqtSignal(int)
    trackModelUpdateOccupancy = pyqtSignal(int, Line, int, bool) # trainID, line, blockNumber, 0 = not occupied, 1 = occupied
    trackModelUpdateCommandedSpeed = pyqtSignal(int, int) # trainID, commandedSpeed
    trackModelDispatchTrain = pyqtSignal(Train) # trainID, destinationBlock, commandedSpeed, authority, Line

    # train model signals
    trainModelDispatchTrain = pyqtSignal(Train) # trainID, Line, destination, commandedSpeed, authority, route
    trainModelGetPower = pyqtSignal(Train, float) # trainID, commandedPower
    trainModelUpdateCommandedSpeed = pyqtSignal(Train, float) # trainID, commandedSpeed
    #getBlockInfo(Line, int, int, float, int, ) # line, blockNumber, length, grade, speedLimit, infrastructure, stationSide (0 = no station, 1 = station), elevation, cumElevation, secsToTraverse
 
    # train controller signals
    trainControllerDispatch = pyqtSignal(float) # currSpeed
    trainControllerUpdateCurrSpeed = pyqtSignal(int, float) # trainID, currSpeed
    trainControllerUpdateCommSpeed = pyqtSignal(int, float) # trainID, commandedSpeed
    trainControllerUpdateAuthority = pyqtSignal(int, int) # trainID, authority

signals = Signals()