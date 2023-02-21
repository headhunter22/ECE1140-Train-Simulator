from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QIntValidator
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from ctcUiImport import Ui_MainWindow
import TrackParser

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        greenBlocks = QIntValidator()
        redBlocks = QIntValidator()
        greenBlocks.setRange(1, 150)
        redBlocks.setRange(1, 76)

        for line in track.lines:
            self.ui.lineSelect.addItem(line.lineName)

        

        #automatically put the TestUI in auto mode and enable the inputs
        self.autoMode()
        self.ui.autoSelect.setChecked(True)
        self.trainLocation()
        self.ui.lineSelect.setCurrentIndex(1)

        self.ui.lineSelect.currentTextChanged.connect(self.trainLocation)

        #switch which mode the test UI is in
        self.ui.autoSelect.clicked.connect(self.autoSwitch)
        self.ui.autoSelect.clicked.connect(self.autoMode)
        self.ui.manualSelect.clicked.connect(self.manualSwitch)
        self.ui.manualSelect.clicked.connect(self.manualMode)
        self.ui.maintenanceSelect.clicked.connect(self.maintenanceSwitch)
        self.ui.maintenanceSelect.clicked.connect(self.maintenanceMode)

        #suggested speed input shown as output
        self.ui.enterButton.clicked.connect(self.showInputs)

        #clear button clears all text fields
        self.ui.clearButton.clicked.connect(self.clearInputs)
        
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

        
        
        self.show()

    def dynamicBlocks(self, line):
        for section in track.lines[0].sections:
            for block in section.blocks:
                self.ui.enterLocation.addItem(block.blockName)
                #

        
    def toggleColor(self, button1, button2):
        button1.setEnabled(False)
        button2.setEnabled(True)
        button1.setStyleSheet('background-color: SkyBlue; color: black')
        button2.setStyleSheet('background-color: white; color: gray')

    def trainLocation(self):
        #only allowing certain inputs for the inputs section
        if self.ui.lineSelect.currentText == "Green":
            #self.ui.enterLocation.setRange(1, 150)
            #self.ui.enterLocation.setValue(1)
            print()
        elif self.ui.lineSelect.currentText == "red":
            self.ui.enterSpeed.setRange(1, 76)
            #self.ui.enterLocation.setValue(1)
    
    def clearInputs(self):
        #self.ui.enterLocation.setValue(1)
        self.ui.enterSpeed.setValue(0)
        self.ui.suggSpeedOutput.setText("Suggested Speed: --mph")
        self.ui.authority.setText("Authority: --mi")

    def showInputs(self):
        entSpeed = self.ui.enterSpeed.value()
        self.ui.suggSpeedOutput.setText("Suggested Speed: {0}mph".format(entSpeed))
        #self.ui.enterLocation.setValue(1)
        self.ui.enterSpeed.setValue(0)

    def autoSwitch(self):
        if self.ui.autoSelect.isChecked:
            self.ui.autoSelect.setChecked(True)
        
        self.ui.manualSelect.setChecked(False)
        self.ui.maintenanceSelect.setChecked(False)
        self.ui.greenLine_2.setStyleSheet("background-color: none")
        self.ui.greenLine_2.setStyleSheet("color: black")
        self.ui.redLineText.setStyleSheet("background-color: none")
        self.ui.redLineText.setStyleSheet("color: black")
        print("\nauto switch state: " + str(self.ui.autoSelect.isChecked()))
        print("manual switch state: " + str(self.ui.manualSelect.isChecked()))
        print("maintenance switch state: " + str(self.ui.maintenanceSelect.isChecked()))

    def manualSwitch(self):
        if self.ui.manualSelect.isChecked:
            self.ui.manualSelect.setChecked(True)
        
        self.ui.autoSelect.setChecked(False)
        self.ui.maintenanceSelect.setChecked(False)
        self.ui.greenLine_2.setStyleSheet("background-color: none")
        self.ui.greenLine_2.setStyleSheet("color: black")
        self.ui.redLineText.setStyleSheet("background-color: none")
        self.ui.redLineText.setStyleSheet("color: black")
        

    def maintenanceSwitch(self):
        if self.ui.maintenanceSelect.isChecked:
            self.ui.maintenanceSelect.setChecked(True)
        
        self.ui.manualSelect.setChecked(False)
        self.ui.autoSelect.setChecked(False)
        self.ui.greenLine_2.setStyleSheet("background-color: green")
        self.ui.greenLine_2.setStyleSheet("color: green")
        self.ui.redLineText.setStyleSheet("background-color: pink")
        self.ui.redLineText.setStyleSheet("color: red")
        print("\nauto switch state: " + str(self.ui.autoSelect.isChecked()))
        print("manual switch state: " + str(self.ui.manualSelect.isChecked()))
        print("maintenance switch state: " + str(self.ui.maintenanceSelect.isChecked()))

    def maintenanceMode(self):
        self.ui.enterLocation.setEnabled(False)
        self.ui.enterSpeed.setEnabled(False)
        self.ui.lineSelect.setEnabled(False)
        self.ui.enterButton.setEnabled(False)
        self.ui.clearButton.setEnabled(False)

        self.ui.green_C1.setEnabled(True)
        self.ui.green_C2.setEnabled(True)
        self.ui.green_G1.setEnabled(True)
        self.ui.green_G2.setEnabled(True)
        self.ui.green_J1_1.setEnabled(True)
        self.ui.green_J1_2.setEnabled(True)
        self.ui.green_J2_1.setEnabled(True)
        self.ui.green_J2_2.setEnabled(True)
        self.ui.green_M1.setEnabled(True)
        self.ui.green_M2.setEnabled(True)
        self.ui.green_N1.setEnabled(True)
        self.ui.green_N2.setEnabled(True)

        self.ui.red_C1.setEnabled(True)
        self.ui.red_C2.setEnabled(True)
        self.ui.red_E1.setEnabled(True)
        self.ui.red_E2.setEnabled(True)
        self.ui.red_H1_1.setEnabled(True)
        self.ui.red_H1_2.setEnabled(True)
        self.ui.red_H2_1.setEnabled(True)
        self.ui.red_H2_2.setEnabled(True)
        self.ui.red_H3_1.setEnabled(True)
        self.ui.red_H3_2.setEnabled(True)
        self.ui.red_H4_1.setEnabled(True)
        self.ui.red_H4_2.setEnabled(True)
        self.ui.red_J1.setEnabled(True)
        self.ui.red_J2.setEnabled(True)

    def autoMode(self):
        self.ui.enterLocation.setEnabled(False)
        self.ui.enterSpeed.setEnabled(False)
        self.ui.lineSelect.setEnabled(False)
        self.ui.enterButton.setEnabled(False)
        self.ui.clearButton.setEnabled(False)

        self.ui.green_C1.setEnabled(False)
        self.ui.green_C2.setEnabled(False)
        self.ui.green_G1.setEnabled(False)
        self.ui.green_G2.setEnabled(False)
        self.ui.green_J1_1.setEnabled(False)
        self.ui.green_J1_2.setEnabled(False)
        self.ui.green_J2_1.setEnabled(False)
        self.ui.green_J2_2.setEnabled(False)
        self.ui.green_M1.setEnabled(False)
        self.ui.green_M2.setEnabled(False)
        self.ui.green_N1.setEnabled(False)
        self.ui.green_N2.setEnabled(False)

        self.ui.red_C1.setEnabled(False)
        self.ui.red_C2.setEnabled(False)
        self.ui.red_E1.setEnabled(False)
        self.ui.red_E2.setEnabled(False)
        self.ui.red_H1_1.setEnabled(False)
        self.ui.red_H1_2.setEnabled(False)
        self.ui.red_H2_1.setEnabled(False)
        self.ui.red_H2_2.setEnabled(False)
        self.ui.red_H3_1.setEnabled(False)
        self.ui.red_H3_2.setEnabled(False)
        self.ui.red_H4_1.setEnabled(False)
        self.ui.red_H4_2.setEnabled(False)
        self.ui.red_J1.setEnabled(False)
        self.ui.red_J2.setEnabled(False)


    def manualMode(self):
        self.ui.enterLocation.setEnabled(True)
        self.ui.enterSpeed.setEnabled(True)
        self.ui.lineSelect.setEnabled(True)
        self.ui.enterButton.setEnabled(True)
        self.ui.clearButton.setEnabled(True)

        self.ui.green_C1.setEnabled(False)
        self.ui.green_C2.setEnabled(False)
        self.ui.green_G1.setEnabled(False)
        self.ui.green_G2.setEnabled(False)
        self.ui.green_J1_1.setEnabled(False)
        self.ui.green_J1_2.setEnabled(False)
        self.ui.green_J2_1.setEnabled(False)
        self.ui.green_J2_2.setEnabled(False)
        self.ui.green_M1.setEnabled(False)
        self.ui.green_M2.setEnabled(False)
        self.ui.green_N1.setEnabled(False)
        self.ui.green_N2.setEnabled(False)

        self.ui.red_C1.setEnabled(False)
        self.ui.red_C2.setEnabled(False)
        self.ui.red_E1.setEnabled(False)
        self.ui.red_E2.setEnabled(False)
        self.ui.red_H1_1.setEnabled(False)
        self.ui.red_H1_2.setEnabled(False)
        self.ui.red_H2_1.setEnabled(False)
        self.ui.red_H2_2.setEnabled(False)
        self.ui.red_H3_1.setEnabled(False)
        self.ui.red_H3_2.setEnabled(False)
        self.ui.red_H4_1.setEnabled(False)
        self.ui.red_H4_2.setEnabled(False)
        self.ui.red_J1.setEnabled(False)
        self.ui.red_J2.setEnabled(False)

if __name__ == '__main__':
    track = TrackParser.parseTrack('Track Layout.csv')
    app = QApplication([])
    window = MainWindow()
    app.exec()