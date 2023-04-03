from PyQt6.QtCore import QObject, pyqtSignal
from Line import Line

class Signals(QObject):
    # timer signal
    timerTicked = pyqtSignal(int, int, int) # hrs, mins, secs to send to CTC
    
    # ctc signals

    # wayside controller signals
    waysideDispatchTrain = pyqtSignal(int, int, int, Line, int) # trainID, suggSpeed, authority, Line, destination

    # track model signals
    trackModelUpdateOccupancy = pyqtSignal(Line, int, bool) # line, blockNumber, 0 = not occupied, 1 = occupied
    trackModelUpdateCommandedSpeed = pyqtSignal(int, int) # trainID, commandedSpeed
    trackModelDispatchTrain = pyqtSignal(int, int, int, Line) # trainID, commandedSpeed, authority, Line

    # train model signals
    trainModelDispatch = pyqtSignal(int, Line, int) # trainID, Line, destination
    trainModelGetPower = pyqtSignal(int, float) # trainID, commandedPower
    #getBlockInfo(Line, int, int, float, int, ) # line, blockNumber, length, grade, speedLimit, infrastructure, stationSide (0 = no station, 1 = station), elevation, cumElevation, secsToTraverse
 
    # train controller signals
    trainControllerDispatch = pyqtSignal(float) # currSpeed
    trainControllerUpdateCurrSpeed = pyqtSignal(int, float) # trainID, currSpeed
    trainControllerUpdateCommSpeed = pyqtSignal(int, float) # trainID, commandedSpeed
    trainControllerUpdateAuthority = pyqtSignal(int, int) # trainID, authority

signals = Signals()