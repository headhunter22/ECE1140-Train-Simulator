from PyQt6.QtCore import QObject, pyqtSignal
from Line import Line
from Block import Block
from Train import Train
from Track import Track
from Beacon import Beacon
from Fault import Fault
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
    switchStatesFromCTCtoWayside = pyqtSignal(list, list) # green switch states for blocks [C, G, J, J, M, N], red switch states for blocks [C, E, H, H, H, H, J]

    # ctc frontend emission signals
    ctcSwitchStates = pyqtSignal(list, list) # green line switches, red line switches
    greenLineTrainDispatchFromCtcUI = pyqtSignal(list) # desination blocks
    redLineTrainDispatchFromCtcUI = pyqtSignal(list) # desination blocks
    blockMaintenanceFromCTCtoWayside = pyqtSignal(str, int, bool) # line, block, maintenance(true/false)
    ctcCreateGUITrainInfo = pyqtSignal(str, int, int, int, int) # line, id, block, commanded speed, authority, destination block
    ctcUpdateGUITrainInfo = pyqtSignal(Train) # Train object
    ctcGetPassengersPerLine = pyqtSignal(int, Line) # passengers offloaded, line

    # wayside controller signals
    waysideAuthorityToCTC = pyqtSignal(str, list, int) # line, route, authority
    waysideDispatchTrain = pyqtSignal(Train) # trainID, suggSpeed, authority, Line, destination
    trackWaysideToTrackModel = pyqtSignal(Track)
    waysideUpdateOccupancy = pyqtSignal(str, int, list) # line, block
    waysideUpdateVacancy = pyqtSignal(str, int, list) # line, block
    waysideCommandedSpeed = pyqtSignal(int)
    waysideAuthoritytoTrack = pyqtSignal(int, int)
    waysideSwitchtoTrack = pyqtSignal(int, int)#change switch to send to track "stem" of switch, stem connects to
    waysideWait = pyqtSignal(bool)
    #plc
    waysideTrackfromPLC = pyqtSignal(list, list, list, list)
    waysideStationsfromPLC = pyqtSignal(list, list)
    waysideSwitchLocationsfromPLC = pyqtSignal(list, list, list, list) # 
    waysideSectionsfromPLC = pyqtSignal(list, list)
    waysideAllSectionsfromPLC = pyqtSignal(list, list)
    waysideSwitchStatesfromPLC = pyqtSignal(list, list)
    waysideinstances = pyqtSignal(list, list, list, list, list, list, list, list, list, list, list, list, list, list, list, list) #from plc

    ranges = pyqtSignal(list, list, list, list, list, list, list, list)
    sections = pyqtSignal(list, list, list, list, list, list, list, list)
    waysidefirst = pyqtSignal(int) #from showmain in ui
    waysidesetup = pyqtSignal(int)

    # wayside UI signals
    wtowOccupancy = pyqtSignal(str, int, str) # block
    wtowVacancy = pyqtSignal(str, int, str) # block
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
    trackModelTrainInfoToWayside = pyqtSignal(Train) # Train object

    ##### PASSES TRACK CIRCUIT SIGNALS #####
    trackModelDispatchTrain = pyqtSignal(Train) # trainID, destinationBlock, commandedSpeed, authority, Line
    authorityTrackModelToTrainModel = pyqtSignal(int, int) # blocks of authority, current block
    ########################################

    trackModelTempUpdated = pyqtSignal(int) # temperature
    trackModelBrokenRail = pyqtSignal(str, str, str) # line, block, 'Broken Rail'
    trackModelPowerFailure = pyqtSignal() # emit power failed
    trackModelCircuitFailure = pyqtSignal() # emit track circuit failed
    trackModelPassengersChanging = pyqtSignal(Train) # train, emit to signal passengers on and off
    trackModelBeaconSending = pyqtSignal(Block) # emitting Beacon to train model

    # track model gui signals
    trackModelUpdateGUIOccupancy = pyqtSignal(str, str)
    trackModelUpdateGUIVacancy = pyqtSignal(str, str)
    trackModelUpdateGUICrossings = pyqtSignal(int)
    trackModelUpdateGUISwitches = pyqtSignal(int, int) # source, dest
    trackModelUpdateGUIFaults = pyqtSignal(Fault)

    # track model test ui signals
    trackModelTestUIUpdateGUIOccupancy = pyqtSignal(str, str) # line, block
    trackModelTestUIUpdateGUIVacancy = pyqtSignal(str, str) # line, block
    trackModelTestUIUpdateGUICrossings = pyqtSignal(int) # 1-4 for crossing statuses
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
    trainModelGUIacc = pyqtSignal(str)
    trainModelPassengers = pyqtSignal(int)
    trainModelDestinationSignal = pyqtSignal(list)
    trainModelLineSignal= pyqtSignal(Line)
    trainModelGUISpeedLim = pyqtSignal(str)
    trainModelAuthorityToTrainController = pyqtSignal(int)

    # train model UI signals
    trainModelEmerBrake = pyqtSignal(bool)
    
    # train controller signals
    trainControllerDispatch = pyqtSignal(float) # currSpeed
    trainControllerUpdateCurrSpeed = pyqtSignal(Train, float) # train, currSpeed
    trainControllerUpdateCommSpeed = pyqtSignal(int) # commandedSpeed
    trainControllerUpdateAuthority = pyqtSignal(int, int) # trainID, authority
    trainControllerTimeTrigger = pyqtSignal() # trigger to call send power
    trainControllerDispatchedSignal = pyqtSignal(Train) # when dispatched, send signal to train controller
    trainWaiting = pyqtSignal()
    trainGo = pyqtSignal()

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
    trainControllerManualModeToTrainModel = pyqtSignal(bool, int)

signals = Signals()