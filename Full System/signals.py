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
    greenStationProperties = pyqtSignal(list) # a list of whether or not the buttons are pressed or not
    blockMaintenanceUpdateFromCTC = pyqtSignal(Track) # block that is updated from open -> maintenance or vice versa

    # ctc frontend emission signals
    greenLineTrainDispatchFromCtcUI = pyqtSignal(list) # desination blocks
    redLineTrainDispatch = pyqtSignal(Train)
    blockMaintenanceOption = pyqtSignal(Track)
    ctcUpdateGUIOccupancy = pyqtSignal(str, int) # train.line, train.block
    ctcUpdateGUIAuthority = pyqtSignal(str, int, float) #train.authority
    ctcCreateGUITrainInfo = pyqtSignal(str, int, int, int, int) # line, id, block, commanded speed, aithority, destination block
    ctcUpdateGUITrainInfo = pyqtSignal(str, int, int, int, int) # line, id, block, commanded speed, aithority, destination block
    ctcGetPassengersPerLine = pyqtSignal(int, Line) # passengers offloaded, line

    # wayside controller signals
    waysideDispatchTrain = pyqtSignal(Train) # trainID, suggSpeed, authority, Line, destination
    trackWaysideToTrackModel = pyqtSignal(Track)
    waysideUpdateOccupancy = pyqtSignal(int)
    waysideUpdateVacancy = pyqtSignal(int)
    waysideSwitchStates = pyqtSignal(list)
    waysideCommandedSpeed = pyqtSignal(int)
    #plc
    waysideSwitchLocationsfromPLC = pyqtSignal(list)
    waysideTrackfromPLC = pyqtSignal(list)
    waysideSectionsfromPLC = pyqtSignal(list)
    waysideinstances = pyqtSignal(list, list, list, list, list, list, list, list) #from wtrack
    actuallyshutup = pyqtSignal()
    please = pyqtSignal()
    # waysideinstance2 = pyqtSignal(list, list)
    # waysideinstance3 = pyqtSignal(list, list)
    # waysideinstance4 = pyqtSignal(list, list)
    waysidefirst = pyqtSignal(int) #from showmain in ui
    waysidesetup = pyqtSignal(int)

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

    ##### PASSES TRACK CIRCUIT SIGNALS #####
    trackModelDispatchTrain = pyqtSignal(Train) # trainID, destinationBlock, commandedSpeed, authority, Line
    ########################################

    trackModelTempUpdated = pyqtSignal(int) # temperature
    trackModelBrokenRail = pyqtSignal(str, str, str) # line, block, 'Broken Rail'
    trackModelPowerFailure = pyqtSignal() # emit power failed
    trackModelCircuitFailure = pyqtSignal() # emit track circuit failed
    trackModelPassengersChanging = pyqtSignal(Train) # train, emit to signal passengers on and off

    # track model gui signals
    trackModelUpdateGUIOccupancy = pyqtSignal(str, str)
    trackModelUpdateGUIVacancy = pyqtSignal(str, str)
    trackModelUpdateGUICrossings = pyqtSignal(int)
    trackModelUpdateGUISwitches = pyqtSignal()

    # track model block page signals

    # track model test ui signals
    trackModelTestUIUpdateGUIOccupancy = pyqtSignal(str, str) # line, block
    trackModelTestUIUpdateGUIVacancy = pyqtSignal(str, str) # line, block
    trackModelTestUIUpdateGUICrossings = pyqtSignal(int) # 1-4 for crossing statuses
    trackModelTestUIUpdateGUISwitches = pyqtSignal(str, str, str) # line, block, switch option
    trackModelTestUIUpdateFault = pyqtSignal(str, str, str) # line, block, fault type

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
    trainControllerRightDoors = pyqtSignal(bool)
    trainControllerLeftDoors = pyqtSignal(bool)
    trainControllerExteriorLights = pyqtSignal(bool)
    trainControllerInteriorLights = pyqtSignal(bool)
    trainControllerAC = pyqtSignal(bool)

signals = Signals()