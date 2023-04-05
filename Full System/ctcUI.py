from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QIntValidator
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QTableWidgetItem, QListWidgetItem
from ctcMainUiImport import Ui_MainWindow
import TrackParser
import pandas as pd
from signals import signals
import sys
sys.dont_write_bytecode = True

trackCSV = pd.read_csv('TrackLayout.csv')
trackDict = trackCSV.to_dict()
greenStationStates = []

class ctcMainUI(QMainWindow):
    def __init__(self, track):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ##################################
        ########STARTUP FUNCTIONS#########
        ##################################

        signals.timerTicked.connect(self.changeLabel)

        #main ui starts up in auto mode
        self.autoMode()
        self.ui.autoSelect.setChecked(True)
        self.fillOccupancy("Green")
        self.fillOccupancy("Red")
        self.uneditable()
        
        for line in track.lines:
            self.ui.lineSelectMaintenance.addItem(line.lineName)

        # add green blocks to dispatch page
        for section in track.getLine("Green").sections:
            for block in section.blocks:
                self.ui.greenBlockDispatch.addItem(block.blockName)

        # add red blocks to dispatch page
        for section in track.getLine("Red").sections:
            for block in section.blocks:
                self.ui.redBlockDispatch.addItem(block.blockName)

        ##################################
        ########DISPATCHING TRAINS########
        ##################################

        #iteration 3 button
        self.ui.dormontDispatch.clicked.connect(self.iterDispatch)

        #connecting the green station buttons
        self.greenStations = []
        self.greenStaionStates = []
        self.ui.pioneerStation.clicked.connect(self.handleGreenStationClicked)
        self.greenStations.append(self.ui.pioneerStation)
        self.ui.edgebrookStation.clicked.connect(self.handleGreenStationClicked)
        self.greenStations.append(self.ui.edgebrookStation)
        self.ui.whitedStation.clicked.connect(self.handleGreenStationClicked)
        self.greenStations.append(self.ui.whitedStation)
        self.ui.southBankStation.clicked.connect(self.handleGreenStationClicked)
        self.greenStations.append(self.ui.southBankStation)
        self.ui.centralStation.clicked.connect(self.handleGreenStationClicked)
        self.greenStations.append(self.ui.centralStation)
        self.ui.inglewoodStation.clicked.connect(self.handleGreenStationClicked)
        self.greenStations.append(self.ui.inglewoodStation)
        self.ui.overbrookStation.clicked.connect(self.handleGreenStationClicked)
        self.greenStations.append(self.ui.overbrookStation)
        self.ui.glenburyStation.clicked.connect(self.handleGreenStationClicked)
        self.greenStations.append(self.ui.glenburyStation)
        self.ui.dormontStation.clicked.connect(self.handleGreenStationClicked)
        self.greenStations.append(self.ui.dormontStation)
        self.ui.lebanonStation.clicked.connect(self.handleGreenStationClicked)
        self.greenStations.append(self.ui.lebanonStation)
        self.ui.poplarStation.clicked.connect(self.handleGreenStationClicked)
        self.greenStations.append(self.ui.poplarStation)
        self.ui.castleShannonStation.clicked.connect(self.handleGreenStationClicked)
        self.greenStations.append(self.ui.castleShannonStation)

        #connecting the green station buttons
        self.redStations = []
        self.ui.shadysideStation.clicked.connect(self.handleRedStationClicked)
        self.redStations.append(self.ui.shadysideStation)
        self.ui.herronStation.clicked.connect(self.handleRedStationClicked)
        self.redStations.append(self.ui.herronStation)
        self.ui.swissvilleStation.clicked.connect(self.handleRedStationClicked)
        self.redStations.append(self.ui.swissvilleStation)
        self.ui.pennStation.clicked.connect(self.handleRedStationClicked)
        self.redStations.append(self.ui.pennStation)
        self.ui.steelPlazaStaion.clicked.connect(self.handleRedStationClicked)
        self.redStations.append(self.ui.steelPlazaStaion)
        self.ui.firstAveStation.clicked.connect(self.handleRedStationClicked)
        self.redStations.append(self.ui.firstAveStation)
        self.ui.staionSquareStation.clicked.connect(self.handleRedStationClicked)
        self.redStations.append(self.ui.staionSquareStation)
        self.ui.southHillsStation.clicked.connect(self.handleRedStationClicked)
        self.redStations.append(self.ui.southHillsStation)

        #add station buttons
        self.ui.greenAddStation.clicked.connect(self.addGreenTentStation)
        self.ui.redAddStation.clicked.connect(self.addRedTentStation)

        #add block buttons
        self.ui.greenAddBlock.clicked.connect(self.addGreenTentBlock)
        self.ui.redAddBlock.clicked.connect(self.addRedTentBlock)

        #dispatch and clear buttons for red and green line
        self.ui.greenDispatch.clicked.connect(self.dipatchGreenTrain)
        self.ui.greenClear.clicked.connect(self.clearGreenDispatch)

        self.ui.redDispatch.clicked.connect(self.dipatchRedTrain)
        self.ui.redClear.clicked.connect(self.clearRedDispatch)

        ##################################
        ########OCCUPANCY WINDOWS#########
        ##################################

        #initilizing green buttons
        self.ui.green_C1.clicked.connect(lambda: self.toggleColor(self.ui.green_C1, self.ui.green_C2))
        self.ui.green_C1.setStyleSheet('background-color: SkyBlue')
        self.ui.green_C2.clicked.connect(lambda: self.toggleColor(self.ui.green_C2, self.ui.green_C1))
        self.ui.green_C2.setStyleSheet('background-color: white; color: gray')
        self.ui.green_G1.clicked.connect(lambda: self.toggleColor(self.ui.green_G1, self.ui.green_G2))
        self.ui.green_G1.setStyleSheet('background-color: SkyBlue')
        self.ui.green_G2.clicked.connect(lambda: self.toggleColor(self.ui.green_G2, self.ui.green_G1))
        self.ui.green_G2.setStyleSheet('background-color: white; color: gray')
        self.ui.green_J1_1.clicked.connect(lambda: self.toggleColor(self.ui.green_J1_1, self.ui.green_J1_2))
        self.ui.green_J1_1.setStyleSheet('background-color: SkyBlue')
        self.ui.green_J1_2.clicked.connect(lambda: self.toggleColor(self.ui.green_J1_2, self.ui.green_J1_1))
        self.ui.green_J1_2.setStyleSheet('background-color: white; color: gray')
        self.ui.green_J2_1.clicked.connect(lambda: self.toggleColor(self.ui.green_J2_1, self.ui.green_J2_2))
        self.ui.green_J2_1.setStyleSheet('background-color: SkyBlue')
        self.ui.green_J2_2.clicked.connect(lambda: self.toggleColor(self.ui.green_J2_2, self.ui.green_J2_1))
        self.ui.green_J2_2.setStyleSheet('background-color: white; color: gray')
        self.ui.green_M1.clicked.connect(lambda: self.toggleColor(self.ui.green_M1, self.ui.green_M2))
        self.ui.green_M1.setStyleSheet('background-color: SkyBlue')
        self.ui.green_M2.clicked.connect(lambda: self.toggleColor(self.ui.green_M2, self.ui.green_M1))
        self.ui.green_M2.setStyleSheet('background-color: white; color: gray')
        self.ui.green_N1.clicked.connect(lambda: self.toggleColor(self.ui.green_N1, self.ui.green_N2))
        self.ui.green_N1.setStyleSheet('background-color: SkyBlue')
        self.ui.green_N2.clicked.connect(lambda: self.toggleColor(self.ui.green_N2, self.ui.green_N1))
        self.ui.green_N2.setStyleSheet('background-color: white; color: gray')

        #initilizing red buttons
        self.ui.red_C1.clicked.connect(lambda: self.toggleColor(self.ui.red_C1, self.ui.red_C2))
        self.ui.red_C1.setStyleSheet('background-color: SkyBlue')
        self.ui.red_C2.clicked.connect(lambda: self.toggleColor(self.ui.red_C2, self.ui.red_C1))
        self.ui.red_C2.setStyleSheet('background-color: white; color: gray')
        self.ui.red_E1.clicked.connect(lambda: self.toggleColor(self.ui.red_E1, self.ui.red_E2))
        self.ui.red_E1.setStyleSheet('background-color: SkyBlue')
        self.ui.red_E2.clicked.connect(lambda: self.toggleColor(self.ui.red_E2, self.ui.red_E1))
        self.ui.red_E2.setStyleSheet('background-color: white; color: gray')
        self.ui.red_H1_1.clicked.connect(lambda: self.toggleColor(self.ui.red_H1_1, self.ui.red_H1_2))
        self.ui.red_H1_1.setStyleSheet('background-color: SkyBlue')
        self.ui.red_H1_2.clicked.connect(lambda: self.toggleColor(self.ui.red_H1_2, self.ui.red_H1_1))
        self.ui.red_H1_2.setStyleSheet('background-color: white; color: gray')
        self.ui.red_H2_1.clicked.connect(lambda: self.toggleColor(self.ui.red_H2_1, self.ui.red_H2_2))
        self.ui.red_H2_1.setStyleSheet('background-color: SkyBlue')
        self.ui.red_H2_2.clicked.connect(lambda: self.toggleColor(self.ui.red_H2_2, self.ui.red_H2_1))
        self.ui.red_H2_2.setStyleSheet('background-color: white; color: gray')
        self.ui.red_H3_1.clicked.connect(lambda: self.toggleColor(self.ui.red_H3_1, self.ui.red_H3_2))
        self.ui.red_H3_1.setStyleSheet('background-color: SkyBlue')
        self.ui.red_H3_2.clicked.connect(lambda: self.toggleColor(self.ui.red_H3_2, self.ui.red_H3_1))
        self.ui.red_H3_2.setStyleSheet('background-color: white; color: gray')
        self.ui.red_H4_1.clicked.connect(lambda: self.toggleColor(self.ui.red_H4_1, self.ui.red_H4_2))
        self.ui.red_H4_1.setStyleSheet('background-color: SkyBlue')
        self.ui.red_H4_2.clicked.connect(lambda: self.toggleColor(self.ui.red_H4_2, self.ui.red_H4_1))
        self.ui.red_H4_2.setStyleSheet('background-color: white; color: gray')
        self.ui.red_J1.clicked.connect(lambda: self.toggleColor(self.ui.red_J1, self.ui.red_J2))
        self.ui.red_J1.setStyleSheet('background-color: SkyBlue')
        self.ui.red_J2.clicked.connect(lambda: self.toggleColor(self.ui.red_J2, self.ui.red_J1))
        self.ui.red_J2.setStyleSheet('background-color: white; color: gray')

        ##################################
        ########UTILITY BUTTONS###########
        ##################################

        #mode buttons
        self.ui.autoSelect.clicked.connect(self.autoSwitch)
        self.ui.manualSelect.clicked.connect(self.manualSwitch)
        self.ui.manualSelect.clicked.connect(self.showPages)
        self.ui.maintenanceSelect.clicked.connect(self.maintenanceSwitch)
        self.ui.maintenanceSelect.clicked.connect(self.showPages)

        #dispatch buttons
        self.ui.dispatchGreen.clicked.connect(self.showPages)
        #self.ui.dispatchGreen.clicked.connect(self.greenDispatch)
        self.ui.dispatchRed.clicked.connect(self.showPages)
        #self.ui.dispatchRed.clicked.connect(self.redDispacth)
        self.ui.scheduledTrains.clicked.connect(self.showPages)
        #self.ui.scheduledTrains.clicked.connect(self.schedTrains)

        #upload schedule
        self.ui.uploadSchedule.clicked.connect(self.openFile)
        
        #time speed buttons
        self.timeButtons = [self.ui.timePause, self.ui.time1x, self.ui.time10x, self.ui.time50x]

        self.ui.time1x.clicked.connect(self.timeSelect)
        self.ui.time1x.setStyleSheet('background-color: SkyBlue; color: gray')
        self.ui.time10x.clicked.connect(self.timeSelect)
        self.ui.time10x.setStyleSheet('background-color: white; color: gray')
        self.ui.timePause.clicked.connect(self.timeSelect)
        self.ui.timePause.setStyleSheet('background-color: white; color: gray')
        self.ui.time50x.clicked.connect(self.timeSelect)
        self.ui.time50x.setStyleSheet('background-color: white; color: gray')
        

        self.ui.time1x.clicked.connect(self.oneTimeSpeed)
        self.ui.time10x.clicked.connect(self.tenTimeSpeed)

        ##################################
        ########TRAINS INFO###############
        ##################################

        ##################################
        ########OPTIONS / XINGS###########
        ##################################

        self.ui.lineSelectMaintenance.currentTextChanged.connect(self.switchLineChanged)
        self.ui.xButton.clicked.connect(self.clearBlockOptions)
        self.ui.checkButton.clicked.connect(self.updateBlockStatus)

        self.show()

    ############################################
    ########DISPATCHING TRAINS FUNCTIONS########
    ############################################

    def iterDispatch(self):
        signals.greenLineTrainDispatchFromCtcUI.emit(73)

    def dipatchGreenTrain(self):
        if self.ui.greenTentSchedule.item(0).text() == '':
            return

        for button in self.greenStations:
            button.setProperty("selected", False)

        # Update the background color of all buttons to white
        for button in self.greenStations:
            button.setStyleSheet("background-color: white;")
        
        nextTrain = self.ui.greenTentSchedule.item(0).text()

        slicedText = str(self.ui.greenScheduledTrains.count() + 1) + nextTrain[nextTrain.find('.'):nextTrain.find('\n')] + '\n   Departure: hh:mm\n   ' + nextTrain[nextTrain.find('A'):]  + '\n'

        item = QListWidgetItem(slicedText)

        self.ui.greenScheduledTrains.addItem(item)
        self.ui.greenTentSchedule.clear()

    def dipatchRedTrain(self):
        for button in self.redStations:
            button.setProperty("selected", False)

        # Update the background color of all buttons to white
        for button in self.redStations:
            button.setStyleSheet("background-color: white;")
        
        nextTrain = self.ui.redTentSchedule.item(0).text()

        slicedText = str(self.ui.redTentSchedule_3.count() + 1) + nextTrain[nextTrain.find('.'):nextTrain.find('\n')] + '\n   Departure: hh:mm\n   ' + nextTrain[nextTrain.find('A'):]  + '\n'

        item = QListWidgetItem(slicedText)

        self.ui.redTentSchedule_3.addItem(item)
        self.ui.redTentSchedule.clear()

    def clearGreenDispatch(self):
        #clear the station selections
        # Set the selected property of all buttons to False
        for button in self.greenStations:
            button.setProperty("selected", False)
            self.greenStaionStates.append(button.property("selected"))

        # Update the background color of all buttons to white
        for button in self.greenStations:
            button.setStyleSheet("background-color: white;")

        self.ui.greenTentSchedule.clear()

        self.ui.greenBlockDispatch.setCurrentIndex(0)

    def clearRedDispatch(self):
        #clear the station selections
        # Set the selected property of all buttons to False
        for button in self.redStations:
            button.setProperty("selected", False)

        # Update the background color of all buttons to white
        for button in self.redStations:
            button.setStyleSheet("background-color: white;")

        self.ui.redTentSchedule.clear()

        self.ui.redBlockDispatch.setCurrentIndex(0)

    def addGreenTentStation(self):
        if self.ui.greenBlockDispatch.currentIndex() != 0:
            return

        # Set the selected property of all buttons to False
        for button in self.greenStations:
            button.setProperty("selected", False)

        # Update the background color of all buttons to white
        for button in self.greenStations:
            button.setStyleSheet("background-color: white;")

        pioneer = self.ui.pioneerStation.property("selected")
        print(pioneer)

        state = self.sender()
        state.property("selected")

    def addRedTentStation(self):
        if self.ui.redBlockDispatch.currentIndex() != 0:
            return

        # Set the selected property of all buttons to False
        for button in self.redStations:
            button.setProperty("selected", False)

        # Update the background color of all buttons to white
        for button in self.redStations:
            button.setStyleSheet("background-color: white;")

    def addGreenTentBlock(self):
        if self.ui.greenBlockDispatch.currentIndex() != 0:
            
            greenTime = self.ui.greenArrivalInput.time()
            blockString = str(self.ui.greenTentSchedule.count() + 1) + '. Block: ' + str(self.ui.greenBlockDispatch.currentIndex()) + '\n    Arrival Time: ' + greenTime.toString("hh:mm")
            item = QListWidgetItem(blockString)
            self.ui.greenTentSchedule.addItem(item)

        self.ui.greenBlockDispatch.setCurrentIndex(0)

    def addRedTentBlock(self):
        if self.ui.redBlockDispatch.currentIndex() != 0:
            
            redTime = self.ui.redArrivalInput.time()
            blockString = str(self.ui.redTentSchedule.count() + 1) + '. Block: ' + str(self.ui.redBlockDispatch.currentIndex()) + '\n    Arrival Time: ' + redTime.toString("hh:mm")
            item = QListWidgetItem(blockString)
            self.ui.redTentSchedule.addItem(item)

        self.ui.redBlockDispatch.setCurrentIndex(0)

    
        if self.ui.redBlockDispatch.currentIndex() == 0:
            yardTime = self.ui.redArrivalInput.time()
            yardString = str(self.ui.redTentSchedule.count() + 1) + '. Yard' + '\n    Arrival Time: ' + yardTime.toString("hh:mm")
            item = QListWidgetItem(yardString)
            self.ui.redTentSchedule.addItem(item)

    def handleGreenStationClicked(self):
        # Get the button that was clicked
        clickedButton = self.sender()

        # Set the selected property of the clicked button to True
        clickedButton.setProperty("selected", True)

        # Set the selected property of all other buttons to False
        for button in self.greenStations:
            if button != clickedButton:
                button.setProperty("selected", False)

        # Update the background color of all buttons based on their selected state
        for button in self.greenStations:
            if button.property("selected"):
                button.setStyleSheet("background-color: blue;")
            else:
                button.setStyleSheet("background-color: white;")

        greenStationStates = [
            self.ui.pioneerStation.property("selected")   , self.ui.edgebrookStation.property("selected") , self.ui.whitedStation.property("selected"), 
            self.ui.southBankStation.property("selected") , self.ui.centralStation.property("selected")   , self.ui.inglewoodStation.property("selected"), 
            self.ui.overbrookStation.property("selected") , self.ui.glenburyStation.property("selected")  , self.ui.dormontStation.property("selected"), 
            self.ui.lebanonStation.property("selected")   , self.ui.poplarStation.property("selected")    , self.ui.castleShannonStation.property("selected")
        ]

        print('\n\nPioneer Station       : ' + str(greenStationStates[0]))
        print('Edgebrook Station     : ' + str(greenStationStates[1]))
        print('Whited Station        : ' + str(greenStationStates[2]))
        print('South Bank Station    : ' + str(greenStationStates[3]))
        print('Central Station       : ' + str(greenStationStates[4]))
        print('Inglewood Station     : ' + str(greenStationStates[5]))
        print('Overbrook Station     : ' + str(greenStationStates[6]))
        print('Glenbury Station      : ' + str(greenStationStates[7]))
        print('Dormont Station       : ' + str(greenStationStates[8]))
        print('Mt. Lebanon Station   : ' + str(greenStationStates[9]))
        print('Poplar Station        : ' + str(greenStationStates[10]))
        print('Castle Shannon Station: ' + str(greenStationStates[11]))

        #return greenStationStates

    def handleRedStationClicked(self):
        # Get the button that was clicked
        clickedButton = self.sender()

        # Set the selected property of the clicked button to True
        clickedButton.setProperty("selected", True)

        # Set the selected property of all other buttons to False
        for button in self.redStations:
            if button != clickedButton:
                button.setProperty("selected", False)

        # Update the background color of all buttons based on their selected state
        for button in self.redStations:
            if button.property("selected"):
                button.setStyleSheet("background-color: blue;")
            else:
                button.setStyleSheet("background-color: white;")

        redStationStates = [
            self.ui.shadysideStation.property("selected")   , self.ui.herronStation.property("selected")     , self.ui.swissvilleStation.property("selected"), 
            self.ui.pennStation.property("selected")        , self.ui.steelPlazaStaion.property("selected")  , self.ui.firstAveStation.property("selected"), 
            self.ui.staionSquareStation.property("selected"), self.ui.southHillsStation.property("selected")
        ]

        print('\n\nShady Side Station     : ' + str(redStationStates[0]))
        print('Herron Ave Station     : ' + str(redStationStates[1]))
        print('Swissville Station     : ' + str(redStationStates[2]))
        print('Penn Station           : ' + str(redStationStates[3]))
        print('Steel Plaza Station    : ' + str(redStationStates[4]))
        print('First Ave Station      : ' + str(redStationStates[5]))
        print('Station Square Station : ' + str(redStationStates[6]))
        print('South Hills Station    : ' + str(redStationStates[7]))

    ############################################
    ########OCCUPANCY WINDOWS FUNCTIONS#########
    ############################################

    def updateOccupancy(self, train):
        if train.line == 'Green':
            startIndex = 76
            endIndex = 226

            for rows in range(startIndex, endIndex):
                if rows == train.block:
                    trainItem = QTableWidgetItem('')
                    trainItem.setBackground(QColor('green'))
                    self.ui.greenOccupancy.setItem(rows, 0, trainItem)
        elif train.line == "Red":
            return
        else:
            print("error")

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

                if rowCount == 21 or rowCount == 43:
                    train = QTableWidgetItem('')
                    train.setBackground(QColor('green'))
                    self.ui.redOccupancy.setItem(rowCount, 0, train)

                if (rowCount > 21 and rowCount < 27) or (rowCount > 43 and rowCount < 47):
                    authority = QTableWidgetItem('')
                    authority.setBackground(QColor('red'))
                    self.ui.redOccupancy.setItem(rowCount, 0, authority)
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

                if rowCount == 6 or rowCount == 48:
                    train = QTableWidgetItem('')
                    train.setBackground(QColor('green'))
                    self.ui.greenOccupancy.setItem(rowCount, 0, train)

                if (rowCount > 6 and rowCount < 12) or (rowCount > 48 and rowCount < 58):
                    authority = QTableWidgetItem('')
                    authority.setBackground(QColor('red'))
                    self.ui.greenOccupancy.setItem(rowCount, 0, authority)

    def uneditable(self):
        self.ui.greenOccupancy.setColumnWidth(0,65)
        self.ui.greenOccupancy.setColumnWidth(1,195)
        self.ui.greenOccupancy.setColumnWidth(2,85)
        self.ui.redOccupancy.setColumnWidth(0,65)
        self.ui.redOccupancy.setColumnWidth(1,195)
        self.ui.redOccupancy.setColumnWidth(2,85)

    #toggles the color and boolean value of buttons in maintenance mode
    def toggleColor(self, button1, button2):
        button1.setEnabled(False)
        button2.setEnabled(True)
        button1.setStyleSheet('background-color: SkyBlue')
        button2.setStyleSheet('background-color: white; color: gray')


    ############################################
    ########TRAINS INFO FUNCTIONS###############
    ############################################

    def addTrainInfo(self, train):
        if train.line == 'Green':
            self.ui.greenTrainInfoTable.insertRow()
        elif train.line == 'Red':
            self.ui.redTrainInfoTable.insertRow()
        else:
            print("error")


    ############################################
    ########UTILITY BUTTONS FUNCTIONS###########
    ############################################

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

        #if clickedButton == self.timeButtons[0]:
        #    self.oneTimeSpeed()
        #elif clickedButton == self.timeButtons[1]:
        #    self.oneTimeSpeed()
        #elif clickedButton == self.timeButtons[2]:
        #    self.tenTimesSpeed()
        #elif clickedButton == self.timeButtons[3]:
        #    self.oneTimeSpeed()
        
    def changeLabel(self, hrs, mins, secs):
        self.ui.dataTime.setText(f'{int(hrs):02d}' + ':' + f'{int(mins):02d}' + ':' + f'{int(secs):02d}')

    def oneTimeSpeed(self):
        signals.CTCOneTimesSpeed.emit()

    def tenTimeSpeed(self):
        signals.CTCTenTimesSpeed.emit()

    def autoSwitch(self):
        #doesnt allow the user to uncheck the mode and in turn having no mode selected
        if self.ui.autoSelect.isChecked:
            self.ui.autoSelect.setChecked(True)
        
        self.ui.manualSelect.setChecked(False)
        self.ui.maintenanceSelect.setChecked(False)

        #disabling the ability to see the dispatch windows in auto mode
        self.ui.dispatchGreen.setEnabled(False)
        self.ui.dispatchRed.setEnabled(False)
        self.ui.scheduledTrains.setEnabled(False)
        self.ui.scheduledTrains.setChecked(True)

        
        self.ui.stackedWidget.setCurrentIndex(2)

        #disabling track block options
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

    def autoMode(self):
        self.autoSwitch()
        self.ui.stackedWidget.setCurrentIndex(2)

    def manualSwitch(self):
        #doesnt allow the user to uncheck the mode and in turn having no mode selected
        if self.ui.manualSelect.isChecked:
            self.ui.manualSelect.setChecked(True)
        
        self.ui.autoSelect.setChecked(False)
        self.ui.maintenanceSelect.setChecked(False)

        self.ui.dispatchGreen.setEnabled(True)
        self.ui.dispatchRed.setEnabled(True)
        self.ui.scheduledTrains.setEnabled(True)

        self.ui.dispatchGreen.setChecked(True)
        self.ui.dispatchRed.setChecked(False)
        self.ui.dispatchGreen.setChecked(False)
        self.ui.stackedWidget.setCurrentIndex(0)

        #disabling track block options
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

    def maintenanceSwitch(self):
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

        #enabling track block options
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
    
    def greenDispatch(self):
        #doesnt allow the user to uncheck the mode and in turn having no mode selected
        if self.ui.dispatchGreen.isChecked():
            self.ui.dispatchGreen.setChecked(True)
        
        self.ui.dispatchRed.setChecked(False)
        self.ui.scheduledTrains.setChecked(False)

    def redDispacth(self):
        #doesnt allow the user to uncheck the mode and in turn having no mode selected
        if self.ui.redDispatch.isChecked():
            self.ui.redDispatch.setChecked(True)
        
        self.ui.greenDispatch.setChecked(False)
        self.ui.scheduledTrains.setChecked(False)

    def schedTrains(self):
        #doesnt allow the user to uncheck the mode and in turn having no mode selected
        if self.ui.scheduledTrains.isChecked():
            self.ui.scheduledTrains.setChecked(True)
        
        self.ui.dispatchRed.setChecked(False)
        self.ui.greenDispatch.setChecked(False)

    def openFile(self):
        # Open a file dialog and get the path of the selected file
        filePath, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'CSV files (*.csv)')

        # Do something with the selected file
        print('Selected file:', filePath)

    ############################################
    ########OPTIONS / XINGS FUNCTIONS###########
    ############################################

    def updateBlockStatus(self):
        if self.ui.lineSelectMaintenance.currentIndex() == 0:
            if self.ui.modeSelect.currentIndex() == 0:

                open = QTableWidgetItem('Open')
                open.setBackground(QColor('White'))
                self.ui.redOccupancy.setItem(self.ui.blockSelectMaintenance.currentIndex(), 2, open)
            else:
                maintenance = QTableWidgetItem('Maintenance')
                maintenance.setBackground(QColor('Gold'))
                self.ui.redOccupancy.setItem(self.ui.blockSelectMaintenance.currentIndex(), 2, maintenance)
        else:
            if self.ui.modeSelect.currentIndex() == 0:

                open = QTableWidgetItem('Open')
                open.setBackground(QColor('White'))
                self.ui.greenOccupancy.setItem(self.ui.blockSelectMaintenance.currentIndex(), 2, open)
            else:
                maintenance = QTableWidgetItem('Maintenance')
                maintenance.setBackground(QColor('Gold'))
                self.ui.greenOccupancy.setItem(self.ui.blockSelectMaintenance.currentIndex(), 2, maintenance)

    def clearBlockOptions(self):
        self.ui.lineSelectMaintenance.setCurrentIndex(0)
        self.ui.blockSelectMaintenance.setCurrentIndex(0)
        self.ui.modeSelect.setCurrentIndex(0)

    #when the line is switched this replaced the block selection to the correct amount for the given line
    def switchLineChanged(self, line):
        # clear current options in the dropdowns 
        self.ui.blockSelectMaintenance.clear()

        # add the appropriate blocks
        for section in track.getLine(line).sections:
            for block in section.blocks:
                self.ui.blockSelectMaintenance.addItem(block.blockName)

    ############################################
    ##############SHARED FUNCITONS##############
    ############################################

    def showPages(self):
        if self.ui.dispatchGreen.isChecked():
            self.ui.stackedWidget.setCurrentIndex(0)
        elif self.ui.dispatchRed.isChecked():
            self.ui.stackedWidget.setCurrentIndex(1)
        elif self.ui.autoSelect.isChecked() or self.ui.scheduledTrains.isChecked():
            self.ui.stackedWidget.setCurrentIndex(2)
        elif self.ui.maintenanceSelect.isChecked():
            self.ui.stackedWidget.setCurrentIndex(3)

if __name__ == '__main__':
    track = TrackParser.parseTrack('TrackLayout.csv')
    app = QApplication([])
    window = ctcMainUI(track)
    app.exec()