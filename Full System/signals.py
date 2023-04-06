from PyQt6.QtCore import QObject, pyqtSignal
from Line import Line
from Train import Train
from Track import Track
import sys
sys.dont_write_bytecode = True

class Signals(QObject):
    # timer signal
    timerTicked = pyqtSignal(int, int, int) # hrs, mins, secs to send to CTC
    
    # ctc backend signals
    trackCTCToWayside = pyqtSignal(Track)
    CTCTimePause = pyqtSignal()
    CTCOneTimesSpeed = pyqtSignal()
    CTCTenTimesSpeed = pyqtSignal()
    CTCFiftyTimesSpeed = pyqtSignal()
    # authorityToWayside = pyqtSignal(Train)
    # suggSpeedToWayside = pyqtSignal(Train)
    # trainObjectToWayside = pyqtSignal(Train)
    # switchStates = pyqtSignal(int, bool)

    # ctc frontend emission signals
    greenLineTrainDispatchFromCtcUI = pyqtSignal(int) # desination block
    redLineTrainDispatch = pyqtSignal(Train)
    blockMaintenanceOption = pyqtSignal(Track)
    ctcUpdateGUIOccupancy = pyqtSignal(str, int) # train.line, train.block
    ctcUpdateGUIAuthority = pyqtSignal(float) #train.authority
    ctcCreateGUITrainInfo = pyqtSignal(str, int, int, int, int, int) # line, id, block, commanded speed, aithority, destination block
    ctcUpdateGUITrainInfo = pyqtSignal(str, int, int, int, int, int) # line, id, block, commanded speed, aithority, destination block

    # wayside controller signals
    waysideDispatchTrain = pyqtSignal(Train) # trainID, suggSpeed, authority, Line, destination
    trackWaysideToTrackModel = pyqtSignal(Track)
    waysideUpdateOccupancy = pyqtSignal(int)
    waysideUpdateVacancy = pyqtSignal(int)

    # wayside UI signals
    wtowOccupancy = pyqtSignal(int) # block
    wtowVacancy = pyqtSignal(int) # block
    count = 0
    wtowTrainCount = pyqtSignal(int) # number of active trains

    # signals to track model
    # suggSpeedWaysideToTrackModel = pyqtSignal(Train)
    # trainObjectWaysideToTrackModel = pyqtSignal(Train)
    # commandedSpeedWaysideToTrackModel = pyqtSignal(int)

    # greenLineSwitches = pyqtSignal(int)
    # signals to CTC
    # passengersToCTC = pyqtSignal(int)

    # track model signals
    trackModelUpdateOccupancy = pyqtSignal(Train, Line, int, bool) # trainID, line, blockNumber, 0 = not occupied, 1 = occupied
    trackModelUpdateCommandedSpeed = pyqtSignal(int, int) # trainID, commandedSpeed
    trackModelDispatchTrain = pyqtSignal(Train) # trainID, destinationBlock, commandedSpeed, authority, Line
    trackModelUpdateGUIOccupancy = pyqtSignal(str, str)
    trackModelUpdateGUIVacancy = pyqtSignal(str, str)
    trackModelUpdateGUICrossings = pyqtSignal(int)
    trackModelUpateGUISwitches = pyqtSignal()

    # train model signals
    trainModelDispatchTrain = pyqtSignal(Train) # trainID, Line, destination, commandedSpeed, authority, route
    trainModelGetPower = pyqtSignal(Train, float) # trainID, commandedPower
    trainModelUpdateCommandedSpeed = pyqtSignal(Train, float) # trainID, commandedSpeed
    trainModelGetTrack = pyqtSignal(Track)
    trainModelUpdateGUISpeed = pyqtSignal(str)
    trainModelGUIcommandedSpeed = pyqtSignal(str)
    trainModelGUIBlock = pyqtSignal(str)
    trainModelGUIpower = pyqtSignal(str)
    #getBlockInfo(Line, int, int, float, int, ) # line, blockNumber, length, grade, speedLimit, infrastructure, stationSide (0 = no station, 1 = station), elevation, cumElevation, secsToTraverse
 
    # train controller signals
    trainControllerDispatch = pyqtSignal(float) # currSpeed
    trainControllerUpdateCurrSpeed = pyqtSignal(Train, float) # train, currSpeed
    trainControllerUpdateCommSpeed = pyqtSignal(int, float) # trainID, commandedSpeed
    trainControllerUpdateAuthority = pyqtSignal(int, int) # trainID, authority
    trainControllerTimeTrigger = pyqtSignal() # trigger to call send power
    trainControllerDispatchedSignal = pyqtSignal(Train) # when dispatched, send signal to train controller

    # Train Controller UI Signals #
    trainControllerEmerBrake = pyqtSignal(bool) # Emergency Brake On/Off
    trainControllerServiceBrake = pyqtSignal(bool)
    trainControllerPower = pyqtSignal(float)
    trainControllerSpeed = pyqtSignal(float)
    trainControllerAuthority = pyqtSignal(float)
    trainControllerKP = pyqtSignal(float)
    trainControllerKI = pyqtSignal(float)
    trainControllerUIKP = pyqtSignal(float)
    trainControllerUIKI = pyqtSignal(float)



signals = Signals()