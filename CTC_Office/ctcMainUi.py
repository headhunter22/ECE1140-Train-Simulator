from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QIntValidator
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QTableWidgetItem
from ctcMainUiImport import Ui_MainWindow
import TrackParser
import pandas as pd

trackCSV = pd.read_csv('Track Layout.csv')
trackDict = trackCSV.to_dict()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        ########STARTUP FUNCTIONS#########
        ##################################

        #main ui starts up in auto mode
        self.autoMode()
        self.ui.autoSelect.setChecked(True)
        self.fillOccupancy("Green")
        self.fillOccupancy("Red")
        self.greenView()


        ##################################
        ########DISPATCHING TRAINS########
        ##################################

        #connecting the green station buttons
        self.greenStations = []
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
        #self.ui.greenDispatch.clicked.connect(self.dipatchGreenTrain)
        self.ui.greenClear.clicked.connect(self.clearGreenDispatch)

        #self.ui.redDispatch.clicked.connect(self.dipatchRedTrain)
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

        #occupancy buttons
        self.ui.greenOccupancyView.clicked.connect(lambda: self.toggleView(self.ui.greenOccupancyView, self.ui.redOccupancyView))
        self.ui.greenOccupancyView.setStyleSheet('background-color: LightGreen; color: black')
        self.ui.redOccupancyView.clicked.connect(lambda: self.toggleView(self.ui.redOccupancyView, self.ui.greenOccupancyView))
        self.ui.redOccupancyView.setStyleSheet('background-color: white; color: gray')

        self.ui.greenOccupancyView.clicked.connect(self.greenView)
        self.ui.redOccupancyView.clicked.connect(self.redView)

        #mode buttons
        self.ui.autoSelect.clicked.connect(self.autoSwitch)
        self.ui.manualSelect.clicked.connect(self.manualSwitch)
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
        self.ui.time1x.clicked.connect(lambda: self.toggleColor(self.ui.time1x, self.ui.time10x))
        self.ui.time1x.setStyleSheet('background-color: SkyBlue; color: gray')
        self.ui.time10x.clicked.connect(lambda: self.toggleColor(self.ui.time10x, self.ui.time1x))
        self.ui.time10x.setStyleSheet('background-color: white; color: gray')

        ##################################
        ########TRAINS INFO###############
        ##################################



        ##################################
        ########OPTIONS / XINGS###########
        ##################################

        self.ui.greenXingStatus.setStyleSheet("border: 2px solid rgb(0, 221, 109); color: rgb(15, 125, 0); background-color: rgb(159, 255, 157)")
        self.ui.redXingStatus.setStyleSheet("border: 2px solid rgb(188, 6, 0); color: rgb(148, 0, 17); background-color: rgb(255, 135, 119); Text-Align: center")

        self.ui.lineSelectMaintenance.currentTextChanged.connect(self.switchLineChanged)
        self.ui.xButton.clicked.connect(self.clearBlockOptions)
        self.ui.checkButton.clicked.connect(self.updateBlockStatus)


        self.show()

    ############################################
    ########DISPATCHING TRAINS FUNCTIONS########
    ############################################

    #def dipatchGreenTrain(self): 
        

    #def dipatchRedTrain(self): 
        

    def clearGreenDispatch(self):
        #clear the station selections
        # Set the selected property of all buttons to False
        for button in self.greenStations:
            button.setProperty("selected", False)

        # Update the background color of all buttons to white
        for button in self.greenStations:
            button.setStyleSheet("background-color: white;")

        self.ui.greenBlockDispatch.setCurrentIndex(0)

    def clearRedDispatch(self):
        #clear the station selections
        # Set the selected property of all buttons to False
        for button in self.redStations:
            button.setProperty("selected", False)

        # Update the background color of all buttons to white
        for button in self.redStations:
            button.setStyleSheet("background-color: white;")

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
        print(self.ui.greenBlockDispatch.currentIndex())
        self.ui.greenBlockDispatch.setCurrentIndex(0)

    def addRedTentBlock(self):
        print(self.ui.redBlockDispatch.currentIndex())
        self.ui.redBlockDispatch.setCurrentIndex(0)
        redTime = self.ui.redArrivalInput.time()
        redTime.toString("hh:mm:ss")
        print('arrival time: ', redTime)

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

    ############################################
    ########OCCUPANCY WINDOWS FUNCTIONS#########
    ############################################

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

                if (rowCount > 6 and rowCount < 12) or (rowCount > 48 and rowCount < 59):
                    authority = QTableWidgetItem('')
                    authority.setBackground(QColor('red'))
                    self.ui.greenOccupancy.setItem(rowCount, 0, authority)

    def greenView(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)

    def redView(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)

    #toggles the color and boolean value of buttons in maintenance mode
    def toggleColor(self, button1, button2):
        button1.setEnabled(False)
        button2.setEnabled(True)
        button1.setStyleSheet('background-color: SkyBlue')
        button2.setStyleSheet('background-color: white; color: gray')

    def toggleView(self, button1, button2):
        if button1 == self.ui.greenOccupancyView:
            button1.setEnabled(False)
            button2.setEnabled(True)
            button1.setStyleSheet('background-color: LightGreen; color: black')
            button2.setStyleSheet('background-color: white; color: gray')
        else:
            button1.setEnabled(False)
            button2.setEnabled(True)
            button1.setStyleSheet('background-color: LightCoral; color: Black')
            button2.setStyleSheet('background-color: white; color: gray')


    ############################################
    ########UTILITY BUTTONS FUNCTIONS###########
    ############################################

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
    track = TrackParser.parseTrack('Track Layout.csv')
    app = QApplication([])
    window = MainWindow()
    app.exec()