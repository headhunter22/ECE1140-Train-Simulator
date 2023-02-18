import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QSize


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("TestUI.ui", self)
        self.setWindowTitle('Track Model Test UI')

        # connect crossing checkboxes
        self.RedXing.toggled.connect(self.getCrossingStatuses)
        self.GreenXing.toggled.connect(self.getCrossingStatuses)

        # add default dropdown blocks for RED line -- CHANGE TO DYNAMIC
        self.SwitchBlockDropDown.addItems(map(str, range(1, 77)))
        self.OccBlockSel.addItems(map(str, range(1, 77)))

        # connect dropdowns to switching functions
        self.SwitchBlockDropDown.currentTextChanged.connect(self.switchBlockChange)
        self.OccLineSel.currentTextChanged.connect(self.switchBlockChange)

        # connect occupied/vacant buttons -- CHANGE TO CONNECT TO CLASSES
        #self.setOccupied.clicked.connect(self.setOcc)
        #self.setVacant.clicked.connect(self.setVac)

        # connect enter temperature button
        self.EnterTemp.clicked.connect(self.tempChanged)

        # FUNCTIONS
        # function to change the track heater status based on temp input
    def tempChanged(self):
        if not self.tempEntry.text().isnumeric(): 
            return
        if int(self.tempEntry.text()) >= 39:
            self.HeaterStatus.setText("Heater Status: OFF")
        else:
            self.HeaterStatus.setText("Heater Status: ON")

    # function to get crossing statuses when they change
    def getCrossingStatuses(self):
        print([self.RedXing.isChecked(), self.GreenXing.isChecked()])

    # function to change dropdowns for switch selection
    def switchLineChanged(self, selection):
        # clear current options in the dropdowns 
        self.SwitchBlockDropDown.clear()

        # for each line, add correct blocks
        if selection == 'Red':
            self.SwitchBlockDropDown.addItems(map(str, range(1, 77)))
        if selection == 'Blue':
            self.SwitchBlockDropDown.addItems(map(str, range(1, 16)))
        if selection == 'Green':
            self.SwitchBlockDropDown.addItems(map(str, range(1, 151)))

    def switchBlockChange(self):
        # update the label for the connection
        rawtext = SwitchQuery.selectSwitches(self.SwitchLine.currentText(), self.SwitchBlockDropDown.currentText())
        
        self.SwitchSectionDropDown.clear()

        # for each line, add correct sections and blocks
        if selection == 'Red':
            self.SwitchBlockDropDown.addItems(map(str, range(1, 77)))
        if selection == 'Blue':
            self.SwitchBlockDropDown.addItems(map(str, range(1, 16)))
        if selection == 'Green':
            self.SwitchBlockDropDown.addItems(map(str, range(1, 151)))

    def switchBlockChange(self):
        # update the label for the connection
        rawtext = SwitchQuery.selectSwitches(self.SwitchLine.currentText(), self.SwitchBlockDropDown.currentText())
        charRemove = ['[', ']', ',', '\'', '(', ')']

        # remove unnecessary characters from query
        for char in charRemove:
            rawtext = rawtext.replace(char, '')

        # set the label text
        self.Connection.setText(rawtext)    

    def occLineChanged(self, selection):
        # clear current options in the dropdowns 
        self.OccBlockSel.clear()

        # for each line, add correct sections and blocks
        if selection == 'Red':
            self.OccBlockSel.addItems(map(str, range(1, 77)))
        if selection == 'Blue':
            self.OccBlockSel.addItems(map(str, range(1, 16)))
        if selection == 'Green':
            self.OccBlockSel.addItems(map(str, range(1, 151)))

#end class definition


#defining the app and the window
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()