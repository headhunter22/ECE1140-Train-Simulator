from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QIntValidator
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QTableWidgetItem, QTableWidget, QAbstractItemView
from ctcMainUiImport import Ui_MainWindow

import ScheduleParser
import pandas as pd
from signals import signals
import sys, os, re, ast, datetime
sys.dont_write_bytecode = True

trackCSV = pd.read_csv('TrackLayout.csv')
trackDict = trackCSV.to_dict()
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

class ctcMainUI(QMainWindow):
    def __init__(self, track):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.funcTrack = track

        ###################################
        ########SIGNAL CONNECTIONS#########
        ###################################

        signals.timerTicked.connect(self.changeLabel)
        signals.ctcCreateGUITrainInfo.connect(self.addTrainInfoLine)
        signals.ctcUpdateGUITrainInfo.connect(self.updateTrainInfo)
        signals.waysideAuthorityToCTC.connect(self.updateOccupancyAuthority)

        ##################################
        ########STARTUP FUNCTIONS#########
        ##################################

        # ui starts up in auto mode
        self.ui.autoSelect.click()
        self.autoModeSwitch()
        self.ui.autoSelect.setChecked(True)
        self.fillOccupancy("Green")
        self.fillOccupancy("Red")
        self.setColors()

        self.greenStations = ["Pioneer", "Edgebrook", "Whited", "South Bank", "Central", "Inglewood", "Overbrook", "Glenbury", "Dormont", "Mt Lebanon", "Poplar", "Castle Shannon"]
        self.greenStopsBlocks = [2, 9, 22, 31, 39, 48, 57, 65, 73, 77, 88, 96]
        greenBlocks = list(range(1, 151))

        self.redStations = ["Shadyside", "Herron Ave", "Swissville", "Penn Station", "Steel Plaza", "First Ave", "Station Square", "South Hills"]
        self.redStopsBlocks = [7, 16, 21, 25, 35, 45, 48, 60]
        redBlocks = list(range(1, 77))

        for i in range(0, 150):
            self.greenStations.append(str(greenBlocks[i]))
            self.greenStopsBlocks.append(int(greenBlocks[i]))

        for i in range(0, 76):
            self.greenStations.append(str(redBlocks[i]))
            self.greenStopsBlocks.append(int(redBlocks[i]))

        for line in track.lines:
            self.ui.lineSelectMaintenance.addItem(line.lineName)
        
        # add blocks to maintenance select
        for section in track.getLine("Red").sections:
            for block in section.blocks:
                self.ui.blockSelectMaintenance.addItem(block.blockName)

        ##################################
        ########DISPATCHING TRAINS########
        ##################################

        # button to send a train to dormont and then the yard
        self.ui.thisIsATest.clicked.connect(self.iterDispatch)

        # manually dispatching trains
        self.ui.greenAddStop.clicked.connect(self.addGreenStop)
        self.ui.greenDispatch.clicked.connect(self.addGreenScheduledTrain)
        self.ui.redAddStop.clicked.connect(self.addRedStop)
        self.ui.redDispatch.clicked.connect(self.addRedScheduledTrain)
        self.ui.greenClear.clicked.connect(self.univClear)
        self.ui.redClear.clicked.connect(self.univClear)

        #upload schedule
        self.ui.uploadSchedule.clicked.connect(self.openFile)

        ##################################
        ########OCCUPANCY WINDOWS#########
        ##################################

        #initilizing green buttons
        self.greenSwitchStates = [1, 1, 0, 0, 0, 0]
        self.ui.green_C1.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.green_C1, self.ui.green_C2))
        self.ui.green_C2.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.green_C2, self.ui.green_C1))
        self.ui.green_G1.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.green_G1, self.ui.green_G2))
        self.ui.green_G2.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.green_G2, self.ui.green_G1))
        self.ui.green_J1_1.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.green_J1_1, self.ui.green_J1_2))
        self.ui.green_J1_2.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.green_J1_2, self.ui.green_J1_1))
        self.ui.green_J2_1.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.green_J2_1, self.ui.green_J2_2))
        self.ui.green_J2_2.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.green_J2_2, self.ui.green_J2_1))
        self.ui.green_M1.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.green_M1, self.ui.green_M2))
        self.ui.green_M2.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.green_M2, self.ui.green_M1))
        self.ui.green_N1.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.green_N1, self.ui.green_N2))
        self.ui.green_N2.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.green_N2, self.ui.green_N1))
        self.ui.green_C1.clicked.connect(self.emitSwitchStates)
        self.ui.green_C2.clicked.connect(self.emitSwitchStates)
        self.ui.green_G1.clicked.connect(self.emitSwitchStates)
        self.ui.green_G2.clicked.connect(self.emitSwitchStates)
        self.ui.green_J1_1.clicked.connect(self.emitSwitchStates)
        self.ui.green_J1_2.clicked.connect(self.emitSwitchStates)
        self.ui.green_J2_1.clicked.connect(self.emitSwitchStates)
        self.ui.green_J2_2.clicked.connect(self.emitSwitchStates)
        self.ui.green_M1.clicked.connect(self.emitSwitchStates)
        self.ui.green_M2.clicked.connect(self.emitSwitchStates)
        self.ui.green_N1.clicked.connect(self.emitSwitchStates)
        self.ui.green_N2.clicked.connect(self.emitSwitchStates)

        #initilizing red buttons
        self.redSwitchStates = [0, 0, 0, 0, 0, 0, 0]
        self.ui.red_C1.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.red_C1, self.ui.red_C2))
        self.ui.red_C2.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.red_C2, self.ui.red_C1))
        self.ui.red_E1.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.red_E1, self.ui.red_E2))
        self.ui.red_E2.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.red_E2, self.ui.red_E1))
        self.ui.red_H1_1.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.red_H1_1, self.ui.red_H1_2))
        self.ui.red_H1_2.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.red_H1_2, self.ui.red_H1_1))
        self.ui.red_H2_1.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.red_H2_1, self.ui.red_H2_2))
        self.ui.red_H2_2.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.red_H2_2, self.ui.red_H2_1))
        self.ui.red_H3_1.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.red_H3_1, self.ui.red_H3_2))
        self.ui.red_H3_2.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.red_H3_2, self.ui.red_H3_1))
        self.ui.red_H4_1.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.red_H4_1, self.ui.red_H4_2))
        self.ui.red_H4_2.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.red_H4_2, self.ui.red_H4_1))
        self.ui.red_J1.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.red_J1, self.ui.red_J2))
        self.ui.red_J2.clicked.connect(lambda: self.toggleColorMaintenance(self.ui.red_J2, self.ui.red_J1))
        self.ui.red_C1.clicked.connect(self.emitSwitchStates)
        self.ui.red_C2.clicked.connect(self.emitSwitchStates)
        self.ui.red_E1.clicked.connect(self.emitSwitchStates)
        self.ui.red_E2.clicked.connect(self.emitSwitchStates)
        self.ui.red_H1_1.clicked.connect(self.emitSwitchStates)
        self.ui.red_H1_2.clicked.connect(self.emitSwitchStates)
        self.ui.red_H2_1.clicked.connect(self.emitSwitchStates)
        self.ui.red_H2_2.clicked.connect(self.emitSwitchStates)
        self.ui.red_H3_1.clicked.connect(self.emitSwitchStates)
        self.ui.red_H3_2.clicked.connect(self.emitSwitchStates)
        self.ui.red_H4_1.clicked.connect(self.emitSwitchStates)
        self.ui.red_H4_2.clicked.connect(self.emitSwitchStates)
        self.ui.red_J1.clicked.connect(self.emitSwitchStates)
        self.ui.red_J2.clicked.connect(self.emitSwitchStates)

        ##################################
        ########UTILITY BUTTONS###########
        ##################################

        # mode buttons
        self.ui.autoSelect.clicked.connect(self.autoModeSwitch)
        self.ui.manualSelect.clicked.connect(self.manualModeSwitch)
        self.ui.maintenanceSelect.clicked.connect(self.maintenanceModeSwitch)

        self.ui.dispatchGreen.clicked.connect(self.greenCheckbox)
        self.ui.dispatchRed.clicked.connect(self.redCheckbox)
        self.ui.scheduledTrains.clicked.connect(self.schedCheckbox)

        #time speed buttons
        self.timeButtons = [self.ui.timePause, self.ui.time1x, self.ui.time10x, self.ui.time50x]
        self.ui.time1x.clicked.connect(self.timeSelect)
        self.ui.time1x.setStyleSheet('background-color: SkyBlue; color: black')
        self.ui.time10x.clicked.connect(self.timeSelect)
        self.ui.time10x.setStyleSheet('background-color: white; color: black')
        self.ui.timePause.clicked.connect(self.timeSelect)
        self.ui.timePause.setStyleSheet('background-color: white; color: black')
        self.ui.time50x.clicked.connect(self.timeSelect)
        self.ui.time50x.setStyleSheet('background-color: white; color: black')
        self.ui.time1x.clicked.connect(self.oneTimeSpeed)
        self.ui.time10x.clicked.connect(self.tenTimeSpeed)
        self.ui.timePause.clicked.connect(self.timePause)
        self.ui.time50x.clicked.connect(self.fiftyTimeSpeed)

        self.ui.lineSelectMaintenance.currentTextChanged.connect(lambda: self.switchLineChanged(track))
        self.ui.xButton.clicked.connect(self.univClear)
        self.ui.checkButton.clicked.connect(self.updateBlockStatus)

    ############################################
    ############## MISC FUNCTIONS ##############
    ############################################

    def setColors(self):
        self.ui.green_C1.setStyleSheet('background-color: SkyBlue')
        self.ui.green_C2.setStyleSheet('background-color: white; color: gray')
        self.ui.green_G1.setStyleSheet('background-color: white; color: gray')
        self.ui.green_G2.setStyleSheet('background-color: SkyBlue')
        self.ui.green_J1_1.setStyleSheet('background-color: SkyBlue')
        self.ui.green_J1_2.setStyleSheet('background-color: white; color: gray')
        self.ui.green_J2_1.setStyleSheet('background-color: white; color: gray')
        self.ui.green_J2_2.setStyleSheet('background-color: SkyBlue')
        self.ui.green_M1.setStyleSheet('background-color: SkyBlue')
        self.ui.green_M2.setStyleSheet('background-color: white; color: gray')
        self.ui.green_N1.setStyleSheet('background-color: SkyBlue')
        self.ui.green_N2.setStyleSheet('background-color: white; color: gray')

        self.ui.red_C1.setStyleSheet('background-color: white; color: gray')
        self.ui.red_C2.setStyleSheet('background-color: SkyBlue')
        self.ui.red_E1.setStyleSheet('background-color: white; color: gray')
        self.ui.red_E2.setStyleSheet('background-color: SkyBlue')
        self.ui.red_H1_1.setStyleSheet('background-color: SkyBlue')
        self.ui.red_H1_2.setStyleSheet('background-color: white; color: gray')
        self.ui.red_H2_1.setStyleSheet('background-color: SkyBlue')
        self.ui.red_H2_2.setStyleSheet('background-color: white; color: gray')
        self.ui.red_H3_1.setStyleSheet('background-color: SkyBlue')
        self.ui.red_H3_2.setStyleSheet('background-color: white; color: gray')
        self.ui.red_H4_1.setStyleSheet('background-color: SkyBlue')
        self.ui.red_H4_2.setStyleSheet('background-color: white; color: gray')
        self.ui.red_J1.setStyleSheet('background-color: SkyBlue')
        self.ui.red_J2.setStyleSheet('background-color: white; color: gray')

        self.ui.greenOccupancy.setColumnWidth(0,65)
        self.ui.greenOccupancy.setColumnWidth(1,195)
        self.ui.greenOccupancy.setColumnWidth(2,85)
        self.ui.redOccupancy.setColumnWidth(0,65)
        self.ui.redOccupancy.setColumnWidth(1,195)
        self.ui.redOccupancy.setColumnWidth(2,85)
        self.ui.greenTentSchedule.setColumnWidth(0,90)
        self.ui.greenTentSchedule.setColumnWidth(1,20)

    def iterDispatch(self):
        self.ui.greenTrainInfoTable.setRowCount(0)
        stops = [73]
        signals.greenLineTrainDispatchFromCtcUI.emit(stops)
    
    def timeSelect(self):
        # Get the button that was clicked
        clickedButton = self.sender()

        # Set the selected property of the clicked button to True
        clickedButton.setProperty("selected", True)

        # Set the selected property of all other buttons to False
        for button in self.timeButtons:
            if button != clickedButton:
                button.setProperty("selected", False)

        # Update the background color of all buttons based on their selected state
        for button in self.timeButtons:
            if button.property("selected"):
                button.setStyleSheet("background-color: SkyBlue;")
            else:
                button.setStyleSheet("background-color: white;")
        
    def changeLabel(self, hrs, mins, secs):
        self.ui.dataTime.setText(f'{int(hrs):02d}' + ':' + f'{int(mins):02d}' + ':' + f'{int(secs):02d}')
        self.dispatchGreenLine()
        self.dispatchRedLine()

    def timePause(self):
        signals.CTCTimePause.emit()
    
    def oneTimeSpeed(self):
        signals.CTCOneTimesSpeed.emit()

    def tenTimeSpeed(self):
        signals.CTCTenTimesSpeed.emit()

    def fiftyTimeSpeed(self):
        signals.CTCFiftyTimesSpeed.emit()

    ############################################
    ########## AUTO MODE FUNCTIONS #############
    ############################################

    def dispatchGreenLine(self):
        try:
            for rows in range(0, self.ui.greenScheduledTrains.rowCount()):
                if self.ui.greenScheduledTrains.item(rows, 2).text() == self.ui.dataTime.text():
                    destlist = ast.literal_eval(self.ui.greenScheduledTrains.item(rows, 0).text())

                    stops = []

                    # iterate through the tent schedule table
                    for i in range(0, len(destlist)):
                        # iterate through the stations list to see if the text in that cell is one of the stations
                        for item in range(0, len(self.greenStations)):
                            if destlist[i] == self.greenStations[item]:
                                stops.append(self.greenStopsBlocks[item])
                    
                    signals.greenLineTrainDispatchFromCtcUI.emit(stops)
                    self.ui.greenScheduledTrains.removeRow(rows)
        except:
            self.ui.greenScheduledTrains.setRowCount(0)
            return
        
    def dispatchRedLine(self):
        try:
            for rows in range(0, self.ui.redScheduledTrains.rowCount()):
                print(self.ui.redScheduledTrains.item(rows, 2).text())
                if self.ui.redScheduledTrains.item(rows, 2).text() == self.ui.dataTime.text():
                    destlist = ast.literal_eval(self.ui.redScheduledTrains.item(rows, 0).text())

                    stops = []

                    # iterate through the tent schedule table
                    for i in range(0, len(destlist)):
                        # iterate through the stations list to see if the text in that cell is one of the stations
                        for item in range(0, len(self.redStations)):
                            if destlist[i] == self.redStations[item]:
                                stops.append(self.redStopsBlocks[item])
                    
                    signals.redLineTrainDispatchFromCtcUI.emit(stops)
                    self.ui.redScheduledTrains.removeRow(rows)
        except:
            self.ui.redScheduledTrains.setRowCount(0)
            return
        
    ############################################
    ######### MANUAL MODE FUNCTIONS ############
    ############################################

    def calculateDispatchTime(self, line, destBlock):
        iterr = greenRouteArr.index(destBlock)
        disTime = 0

        for i in range(0, iterr + 1):
            disTime += float(self.funcTrack.getLine(line).getBlock(greenRouteArr[i]).secsToTraverse)
        return disTime

    # if the entry is correct a stop is added to the tentative schedule
    def addGreenStop(self):
        pattern = r"^(?:0\d|1\d|2[0-3]):(?:[0-5]\d)$"

        if (self.ui.greenDestination.text() not in self.greenStations) or (not re.match(pattern, self.ui.greenTime.text())):
            self.ui.greenDestination.clear()
            self.ui.greenTime.clear()
            return
        else:
            try:
                greenTempBlock = int(self.ui.greenDestination.text())
                destTemp = str(greenTempBlock)
            except:
                destTemp = self.ui.greenDestination.text()

            time = self.ui.greenTime.text().split(":")
            temp = time[0] + ":" + time[1]

            rowCount = self.ui.greenTentSchedule.rowCount()
            self.ui.greenTentSchedule.insertRow(rowCount)

            dest = QTableWidgetItem(destTemp)
            at = QTableWidgetItem(temp)
            self.ui.greenTentSchedule.setItem(rowCount, 0, dest)
            self.ui.greenTentSchedule.setItem(rowCount, 1, at)
            self.ui.greenDestination.clear()
            self.ui.greenTime.clear()

    # reads the green tentative scheule and dispatches it to the scheduled trains list to be dispatched
    def addGreenScheduledTrain(self):
        try:
            rowCount = self.ui.greenScheduledTrains.rowCount()
            self.ui.greenScheduledTrains.insertRow(rowCount)

            destList = []
            atList = []

            for rows in range(0, self.ui.greenTentSchedule.rowCount()):
                destList.append(self.ui.greenTentSchedule.item(rows,0).text())
                atList.append(self.ui.greenTentSchedule.item(rows,1).text())

            stops = []

            # iterate through the tent schedule table
            for rows in range(0, len(destList)):
                # iterate through the stations list to see if the text in that cell is one of the stations
                for item in range(0, len(self.greenStations)):
                    if destList[rows] == self.greenStations[item]:
                        stops.append(self.greenStopsBlocks[item])

            disTime = self.calculateDispatchTime("Green", stops[0])

            temp = atList[0]
            time = temp.split(":")
            hours = int(time[0]) * 3600
            minutes = int(time[1]) * 60
            totalTime = hours + minutes - int(disTime)
            dispatchTime = str(datetime.timedelta(seconds=totalTime))

            if int(time[0]) < 10:
                dispatchTime = "0" + dispatchTime


            dest = QTableWidgetItem(str(destList))
            at = QTableWidgetItem(str(atList))
            dt = QTableWidgetItem(dispatchTime)
            self.ui.greenScheduledTrains.setItem(rowCount, 0, dest)
            self.ui.greenScheduledTrains.setItem(rowCount, 1, at)
            self.ui.greenScheduledTrains.setItem(rowCount, 2, dt)

            self.ui.greenTentSchedule.setRowCount(0)
        except:
            return
        
    # if the entry is correct a stop is added to the tentative schedule
    def addRedStop(self):
        pattern = r"^(?:0\d|1\d|2[0-3]):(?:[0-5]\d)$"

        if (self.ui.redDestination.text() not in self.redStations) or (not re.match(pattern, self.ui.redTime.text())):
            self.ui.redDestination.clear()
            self.ui.redTime.clear()
            return
        else:
            try:
                redTempBlock = int(self.ui.redDestination.text())
                destTemp = str(redTempBlock)
            except:
                destTemp = self.ui.redDestination.text()

            time = self.ui.redTime.text().split(":")
            temp = time[0] + ":" + time[1]

            rowCount = self.ui.redTentSchedule.rowCount()
            self.ui.redTentSchedule.insertRow(rowCount)

            dest = QTableWidgetItem(destTemp)
            at = QTableWidgetItem(temp)
            self.ui.redTentSchedule.setItem(rowCount, 0, dest)
            self.ui.redTentSchedule.setItem(rowCount, 1, at)
            self.ui.redDestination.clear()
            self.ui.redTime.clear()
    
    def addRedScheduledTrain(self):
        try:
            rowCount = self.ui.redScheduledTrains.rowCount()
            self.ui.redScheduledTrains.insertRow(rowCount)

            destList = []
            atList = []

            for rows in range(0, self.ui.redTentSchedule.rowCount()):
                destList.append(self.ui.redTentSchedule.item(rows,0).text())
                atList.append(self.ui.redTentSchedule.item(rows,1).text())

            stops = []

            # iterate through the tent schedule table
            for rows in range(0, len(destList)):
                # iterate through the stations list to see if the text in that cell is one of the stations
                for item in range(0, len(self.redStations)):
                    if destList[rows] == self.redStations[item]:
                        stops.append(self.redStopsBlocks[item])

            dest = QTableWidgetItem(str(destList))
            at = QTableWidgetItem(str(atList))
            dt = QTableWidgetItem(str(atList[0]+":00"))
            self.ui.redScheduledTrains.setItem(rowCount, 0, dest)
            self.ui.redScheduledTrains.setItem(rowCount, 1, at)
            self.ui.redScheduledTrains.setItem(rowCount, 2, dt)

            self.ui.redTentSchedule.setRowCount(0)
        except:
            return
    
    ############################################
    ####### MAINTENANCE MODE FUNCTIONS #########
    ############################################

    # handles changing the color of the switch buttons and disables the selected button from being unselected
    def toggleColorMaintenance(self, button1, button2):
        button1.setEnabled(False)
        button2.setEnabled(True)
        button1.setStyleSheet('background-color: SkyBlue')
        button2.setStyleSheet('background-color: white; color: gray')
    
    # emits the current switch states to the wayside
    def emitSwitchStates(self):
        clickedButton = self.sender()

        if clickedButton == self.ui.green_C1:
            self.greenSwitchStates[0] = 1
        elif clickedButton == self.ui.green_C2:
            self.greenSwitchStates[0] = 0
        elif clickedButton == self.ui.green_G1:
            self.greenSwitchStates[1] = 0
        elif clickedButton == self.ui.green_G2:
            self.greenSwitchStates[1] = 1
        elif clickedButton == self.ui.green_J1_1:
            self.greenSwitchStates[2] = 0
        elif clickedButton == self.ui.green_J1_2:
            self.greenSwitchStates[2] = 1
        elif clickedButton == self.ui.green_J2_1:
            self.greenSwitchStates[3] = 1
        elif clickedButton == self.ui.green_J2_2:
            self.greenSwitchStates[3] = 0
        elif clickedButton == self.ui.green_M1:
            self.greenSwitchStates[4] = 0
        elif clickedButton == self.ui.green_M2:
            self.greenSwitchStates[4] = 1
        elif clickedButton == self.ui.green_N1:
            self.greenSwitchStates[5] = 0
        elif clickedButton == self.ui.green_N2:
            self.greenSwitchStates[5] = 1
        elif clickedButton == self.ui.red_C1:
            self.redSwitchStates[0] = 1
        elif clickedButton == self.ui.red_C2:
            self.redSwitchStates[0] = 0
        elif clickedButton == self.ui.red_E1:
            self.redSwitchStates[1] = 1
        elif clickedButton == self.ui.red_E2:
            self.redSwitchStates[1] = 0
        elif clickedButton == self.ui.red_H1_1:
            self.redSwitchStates[2] = 0
        elif clickedButton == self.ui.red_H1_2:
            self.redSwitchStates[2] = 1
        elif clickedButton == self.ui.red_H2_1:
            self.redSwitchStates[3] = 0
        elif clickedButton == self.ui.red_H2_2:
            self.redSwitchStates[3] = 1
        elif clickedButton == self.ui.red_H3_1:
            self.redSwitchStates[4] = 0
        elif clickedButton == self.ui.red_H3_2:
            self.redSwitchStates[4] = 1
        elif clickedButton == self.ui.red_H4_1:
            self.redSwitchStates[5] = 0
        elif clickedButton == self.ui.red_H4_2:
            self.redSwitchStates[5] = 1
        elif clickedButton == self.ui.red_J1:
            self.redSwitchStates[6] = 0
        elif clickedButton == self.ui.red_J2:
            self.redSwitchStates[6] = 1

        signals.ctcSwitchStates.emit(self.greenSwitchStates, self.redSwitchStates)
    
    # opens and parses a file selected by the user
    def openFile(self):
        # Open a file dialog and get the path of the selected file
            filePath, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'CSV files (*.csv)')
            if filePath:
                fileName = os.path.basename(filePath)
                schedule = ScheduleParser.parseScedule(fileName)
                self.addScheduledTrain(schedule)

    # adds a train to the scheduled trains list to wait to be dispatched
    def addScheduledTrain(self, schedule):
        if schedule.line == "Green":
            
            rowCount = self.ui.greenScheduledTrains.rowCount()
            self.ui.greenScheduledTrains.insertRow(rowCount)

            stops = []

            # iterate through the tent schedule table
            for rows in range(0, len(schedule.stops)):
                # iterate through the stations list to see if the text in that cell is one of the stations
                for item in range(0, len(self.greenStations)):
                    if schedule.stops[rows] == self.greenStations[item]:
                        stops.append(self.greenStopsBlocks[item])

            disTime = self.calculateDispatchTime(schedule.line, stops[0])

            temp = schedule.arrivalTimes[0]
            time = temp.split(":")
            hours = int(time[0]) * 3600
            minutes = int(time[1]) * 60
            totalTime = hours + minutes - int(disTime)
            dispatchTime = str(datetime.timedelta(seconds=totalTime))

            if int(time[0]) < 10:
                dispatchTime = "0" + dispatchTime

            dest = QTableWidgetItem(str(schedule.stops))
            at = QTableWidgetItem(str(schedule.arrivalTimes))
            dt = QTableWidgetItem(dispatchTime)

            self.ui.greenScheduledTrains.setItem(rowCount, 0, dest)
            self.ui.greenScheduledTrains.setItem(rowCount, 1, at)
            self.ui.greenScheduledTrains.setItem(rowCount, 2, dt)
    
    # resets all options in the Track Block Options section
    def clearBlockOptions(self):
        self.ui.lineSelectMaintenance.setCurrentIndex(0)
        self.ui.blockSelectMaintenance.setCurrentIndex(0)
        self.ui.modeSelect.setCurrentIndex(0)
    
    def updateBlockStatus(self):

        if self.ui.lineSelectMaintenance.currentIndex() == 0: # red line
            if self.ui.modeSelect.currentIndex() == 0: # open
                open = QTableWidgetItem('Open')
                open.setBackground(QColor('White'))
                self.ui.redOccupancy.setItem(self.ui.blockSelectMaintenance.currentIndex(), 2, open)

                signals.blockMaintenanceFromCTCtoWayside.emit("Red", self.ui.blockSelectMaintenance.currentIndex()+1, True)
            else: # maintenance
                maintenance = QTableWidgetItem('Maintenance')
                maintenance.setBackground(QColor('Gold'))
                self.ui.redOccupancy.setItem(self.ui.blockSelectMaintenance.currentIndex(), 2, maintenance)

                signals.blockMaintenanceFromCTCtoWayside.emit("Red", self.ui.blockSelectMaintenance.currentIndex()+1, False)
        else: # green line
            if self.ui.modeSelect.currentIndex() == 0: # open
                open = QTableWidgetItem('Open')
                open.setBackground(QColor('White'))
                self.ui.greenOccupancy.setItem(self.ui.blockSelectMaintenance.currentIndex(), 2, open)

                signals.blockMaintenanceFromCTCtoWayside.emit("Green", self.ui.blockSelectMaintenance.currentIndex()+1, True)
            else: # maintenance
                maintenance = QTableWidgetItem('Maintenance')
                maintenance.setBackground(QColor('Gold'))
                self.ui.greenOccupancy.setItem(self.ui.blockSelectMaintenance.currentIndex(), 2, maintenance)

                signals.blockMaintenanceFromCTCtoWayside.emit("Green", self.ui.blockSelectMaintenance.currentIndex()+1, False)
    
    #when the line is switched this replaced the block selection to the correct amount for the given line
    def switchLineChanged(self, track): #########
        # clear current options in the dropdowns 
        self.ui.blockSelectMaintenance.clear()

        if self.ui.blockSelectMaintenance.currentIndex() == 0:
            line = "Red"
        else:
            line = "Green"

        # add the appropriate blocks
        for section in track.getLine(line).sections:
            for block in section.blocks:
                self.ui.blockSelectMaintenance.addItem(block.blockName)
    
    ############################################
    ######## OCCUPANCY VIEW FUNCTIONS ##########
    ############################################

    def updateOccupancyAuthority(self, line, route, auth):
        if line == "Green":
            for i in range(0, 149):
                if i in route[:auth+1]:
                    if i == route[0]:
                        location = QTableWidgetItem('')
                        location.setBackground(QColor('green'))
                        self.ui.greenOccupancy.setItem(i-1, 0, location)
                    else:
                        authority = QTableWidgetItem('')
                        authority.setBackground(QColor('red'))
                        self.ui.greenOccupancy.setItem(i-1, 0, authority)
                else:
                    vacancy = QTableWidgetItem('')
                    vacancy.setBackground(QColor('white'))
                    self.ui.greenOccupancy.setItem(i-1, 0, vacancy)
        elif line == "Red":
            for i in range(0, 75):
                if i in route[:auth+1]:
                    if i == route[0]:
                        location = QTableWidgetItem('')
                        location.setBackground(QColor('green'))
                        self.ui.redOccupancy.setItem(i-1, 0, location)
                    else:
                        authority = QTableWidgetItem('')
                        authority.setBackground(QColor('red'))
                        self.ui.redOccupancy.setItem(i-1, 0, authority)
                else:
                    vacancy = QTableWidgetItem('')
                    vacancy.setBackground(QColor('white'))
                    self.ui.redOccupancy.setItem(i-1, 0, vacancy)

    def fillOccupancy(self, line):

        #self.ui.greenOccupancy.setVerticalHeader().setVisible(False)

        if line == 'Red':
            startIndex = 0
            endIndex = 76

            for rows in range(startIndex, endIndex):
                rowCount = self.ui.redOccupancy.rowCount()

                #insert a new row at the bottom of the table
                self.ui.redOccupancy.insertRow(rowCount)

                #stage item name to be added
                blockNumberItem = QTableWidgetItem(str(trackDict['Block Number'][rows]))

                if str(trackDict['Infrastructure'][rows]) == 'nan':
                    infrastructureText = QTableWidgetItem("")
                else:
                    infrastructureText = QTableWidgetItem(str(trackDict['Infrastructure'][rows]))

                blockStatus = QTableWidgetItem("Open")
                
                self.ui.redOccupancy.setItem(rowCount, 1, infrastructureText)
                self.ui.redOccupancy.setItem(rowCount, 2, blockStatus)
        else:
            startIndex = 76
            endIndex = 226

            for rows in range(startIndex, endIndex):
                rowCount = self.ui.greenOccupancy.rowCount()

                #insert a new row at the bottom of the table
                self.ui.greenOccupancy.insertRow(rowCount)

                #stage item name to be added
                blockNumberItem = QTableWidgetItem(str(trackDict['Block Number'][rows]))

                if str(trackDict['Infrastructure'][rows]) == 'nan':
                    infrastructureText = QTableWidgetItem("")
                else:
                    infrastructureText = QTableWidgetItem(str(trackDict['Infrastructure'][rows]))

                blockStatus = QTableWidgetItem("Open")
                
                self.ui.greenOccupancy.setItem(rowCount, 1, infrastructureText)
                self.ui.greenOccupancy.setItem(rowCount, 2, blockStatus)

    def addTrainInfoLine(self, line, id, block, auth, dest):
        if line == 'Green':
            rowCount = self.ui.greenTrainInfoTable.rowCount()

            self.ui.greenTrainInfoTable.insertRow(rowCount)

            greenTrainID = QTableWidgetItem(str(id))
            greenTrainBlock = QTableWidgetItem(str(block))
            greenTrainAuth = QTableWidgetItem(str(auth))
            greenTrainDest = QTableWidgetItem(str(dest))

            self.ui.greenTrainInfoTable.setItem(rowCount, 0, greenTrainID)
            self.ui.greenTrainInfoTable.setItem(rowCount, 1, greenTrainBlock)
            self.ui.greenTrainInfoTable.setItem(rowCount, 2, greenTrainAuth)
            self.ui.greenTrainInfoTable.setItem(rowCount, 3, greenTrainDest)

        elif line == 'Red':
            rowCount = self.ui.redTrainInfoTable.rowCount()

            self.ui.redTrainInfoTable.insertRow(rowCount)

            greenTrainID = QTableWidgetItem(str(id))
            greenTrainBlock = QTableWidgetItem(str(block))
            greenTrainAuth = QTableWidgetItem(str(auth))
            greenTrainDest = QTableWidgetItem(str(dest))

            self.ui.redTrainInfoTable.setItem(rowCount, 0, greenTrainID)
            self.ui.redTrainInfoTable.setItem(rowCount, 1, greenTrainBlock)
            self.ui.redTrainInfoTable.setItem(rowCount, 2, greenTrainAuth)
            self.ui.redTrainInfoTable.setItem(rowCount, 3, greenTrainDest)

    def updateTrainInfo(self, train):
        if train.line.lineName == 'Green':
            for rows in range(0, self.ui.greenTrainInfoTable.rowCount()):
                if int(self.ui.greenTrainInfoTable.item(rows, 0).text()) == train.ID:

                    greenTrainBlock = QTableWidgetItem(str(train.block))
                    greenTrainAuth = QTableWidgetItem(str(train.authorityBlocks))
                    greenTrainDest = QTableWidgetItem(str(train.destBlock[0]))

                    self.ui.greenTrainInfoTable.setItem(rows, 1, greenTrainBlock)
                    self.ui.greenTrainInfoTable.setItem(rows, 2, greenTrainAuth)
                    self.ui.greenTrainInfoTable.setItem(rows, 3, greenTrainDest)
        elif train.line.lineName == "Red":
            for rows in range(0, self.ui.redTrainInfoTable.rowCount()):
                if int(self.ui.redTrainInfoTable.item(rows, 0).text()) == train.ID:

                    greenTrainBlock = QTableWidgetItem(str(train.block))
                    greenTrainAuth = QTableWidgetItem(str(train.authorityBlocks))
                    greenTrainDest = QTableWidgetItem(str(train.destBlock[0]))

                    self.ui.redTrainInfoTable.setItem(rows, 1, greenTrainBlock)
                    self.ui.redTrainInfoTable.setItem(rows, 2, greenTrainAuth)
                    self.ui.redTrainInfoTable.setItem(rows, 3, greenTrainDest)

    ############################################
    ########UTILITY BUTTONS FUNCTIONS###########
    ############################################

    def autoModeSwitch(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        # doesnt allow the user to uncheck the mode and in turn having no mode selected
        if self.ui.autoSelect.isChecked:
            self.ui.autoSelect.setChecked(True)
        self.ui.manualSelect.setChecked(False)
        self.ui.maintenanceSelect.setChecked(False)
        # disabling the ability to see the dispatch windows in auto mode
        self.ui.dispatchGreen.setEnabled(False)
        self.ui.dispatchRed.setEnabled(False)
        self.ui.scheduledTrains.setEnabled(False)
        self.ui.scheduledTrains.setChecked(True)
        self.ui.uploadSchedule.setEnabled(False)
        self.ui.thisIsATest.setEnabled(False)
        # disabling track block options
        self.ui.lineSelectMaintenance.setEnabled(False)
        self.ui.blockSelectMaintenance.setEnabled(False)
        self.ui.modeSelect.setEnabled(False)
        self.ui.checkButton.setEnabled(False)
        self.ui.xButton.setEnabled(False)
        self.ui.lineLabel.setStyleSheet("color: LightGrey")
        self.ui.blockLabel_2.setStyleSheet("color: LightGrey")
        self.ui.optionsLabel.setStyleSheet("color: GhostWhite")
        self.ui.xButton.setStyleSheet("background-color: None")
        self.ui.checkButton.setStyleSheet("background-color: None")
    
    def manualModeSwitch(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        # doesnt allow the user to uncheck the mode and in turn having no mode selected
        if self.ui.manualSelect.isChecked:
            self.ui.manualSelect.setChecked(True)
        self.ui.autoSelect.setChecked(False)
        self.ui.maintenanceSelect.setChecked(False)
        # enabling dispatch buttons
        self.ui.dispatchGreen.setEnabled(True)
        self.ui.dispatchRed.setEnabled(True)
        self.ui.scheduledTrains.setEnabled(True)
        self.ui.uploadSchedule.setEnabled(True)
        # setting the default manual to green line
        self.ui.dispatchGreen.setChecked(True)
        self.ui.dispatchRed.setChecked(False)
        self.ui.dispatchGreen.setChecked(False)
        # disabling track block options
        self.ui.lineSelectMaintenance.setEnabled(False)
        self.ui.blockSelectMaintenance.setEnabled(False)
        self.ui.modeSelect.setEnabled(False)
        self.ui.checkButton.setEnabled(False)
        self.ui.xButton.setEnabled(False)
        self.ui.lineLabel.setStyleSheet("color: LightGrey")
        self.ui.blockLabel_2.setStyleSheet("color: LightGrey")
        self.ui.optionsLabel.setStyleSheet("color: GhostWhite")
        self.ui.xButton.setStyleSheet("background-color: None")
        self.ui.checkButton.setStyleSheet("background-color: None")
    
    def maintenanceModeSwitch(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        #doesnt allow the user to uncheck the mode and in turn having no mode selected
        if self.ui.maintenanceSelect.isChecked:
            self.ui.maintenanceSelect.setChecked(True)
        self.ui.manualSelect.setChecked(False)
        self.ui.autoSelect.setChecked(False)
        self.ui.dispatchGreen.setChecked(False)
        self.ui.dispatchRed.setChecked(False)
        self.ui.scheduledTrains.setChecked(False)
        self.ui.dispatchGreen.setEnabled(False)
        self.ui.dispatchRed.setEnabled(False)
        self.ui.scheduledTrains.setEnabled(False)
        self.ui.thisIsATest.setEnabled(False)
        # enabling track block options
        self.ui.lineSelectMaintenance.setEnabled(True)
        self.ui.blockSelectMaintenance.setEnabled(True)
        self.ui.modeSelect.setEnabled(True)
        self.ui.checkButton.setEnabled(True)
        self.ui.xButton.setEnabled(True)
        self.ui.lineLabel.setStyleSheet("color: Black")
        self.ui.blockLabel_2.setStyleSheet("color: Black")
        self.ui.optionsLabel.setStyleSheet("color: Black")
        self.ui.xButton.setStyleSheet("background-color: red")
        self.ui.checkButton.setStyleSheet("background-color: green")

    def greenCheckbox(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        if self.ui.dispatchGreen.isChecked:
            self.ui.dispatchGreen.setChecked(True)
            self.ui.dispatchRed.setChecked(False)
            self.ui.scheduledTrains.setChecked(False)

    def redCheckbox(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        if self.ui.dispatchRed.isChecked:
            self.ui.dispatchGreen.setChecked(False)
            self.ui.dispatchRed.setChecked(True)
            self.ui.scheduledTrains.setChecked(False)

    def schedCheckbox(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        if self.ui.scheduledTrains.isChecked:
            self.ui.dispatchGreen.setChecked(False)
            self.ui.dispatchRed.setChecked(False)
            self.ui.scheduledTrains.setChecked(True)

    def univClear(self):
        clickedButton = self.sender()

        if clickedButton == self.ui.xButton:
            self.ui.lineSelectMaintenance.setCurrentIndex(0)
            self.ui.blockSelectMaintenance.setCurrentIndex(0)
            self.ui.modeSelect.setCurrentIndex(0)
        elif clickedButton == self.ui.greenClear:
            self.ui.greenTentSchedule.setRowCount(0)
            self.ui.greenDestination.clear()
            self.ui.greenTime.clear()
        elif clickedButton == self.ui.redClear:
            self.ui.redTentSchedule.setRowCount(0)
            self.ui.redDestination.clear()
            self.ui.redTime.clear()
