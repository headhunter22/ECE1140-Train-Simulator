from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QIntValidator
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from ctcMainUiImport import Ui_MainWindow
import TrackParser
import pandas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ##################################
        ########STARTUP FUNCTIONS#########
        ##################################

        #main ui starts up in auto mode
        self.autoMode()
        self.ui.autoSelect.setChecked(True)


        ##################################
        ########DISPATCHING TRAINS########
        ##################################



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
        self.ui.maintenanceSelect.clicked.connect(self.maintenanceSwitch)
        self.ui.maintenanceSelect.clicked.connect(self.showPages)

        #dispatch buttons
        self.ui.dispatchGreen.clicked.connect(self.showPages)
        self.ui.dispatchGreen.clicked.connect(self.greenDispatch)
        self.ui.dispatchRed.clicked.connect(self.showPages)
        self.ui.dispatchRed.clicked.connect(self.redDispacth)
        self.ui.scheduledTrains.clicked.connect(self.showPages)
        self.ui.scheduledTrains.clicked.connect(self.schedTrains)

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


        self.show()

    ############################################
    ########OCCUPANCY WINDOWS FUNCTIONS#########
    ############################################

    #toggles the color and boolean value of buttons in maintenance mode
    def toggleColor(self, button1, button2):
        button1.setEnabled(False)
        button2.setEnabled(True)
        button1.setStyleSheet('background-color: SkyBlue')
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
        self.ui.blockCurrentState.setStyleSheet("color: LightGrey")
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
        self.ui.blockCurrentState.setStyleSheet("color: LightGrey")
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
        self.ui.blockCurrentState.setStyleSheet("color: Black")
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