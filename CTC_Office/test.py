from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from work import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #switch which mode the test UI is in
        self.ui.autoSelect.clicked.connect(self.autoSwitch)
        self.ui.autoSelect.clicked.connect(self.otherModes)
        self.ui.manualSelect.clicked.connect(self.manualSwitch)
        self.ui.manualSelect.clicked.connect(self.otherModes)
        self.ui.maintenanceSelect.clicked.connect(self.maintenanceSwitch)
        self.ui.maintenanceSelect.clicked.connect(self.maintenanceMode)
        self.ui.autoSelect.setChecked(True) #always initially in auto mode

        #suggested speed set
        self.ui.enterButton.clicked.connect(self.showSuggSpeed)

        #clear button clears all text fields
        self.ui.clearButton.clicked.connect(self.clearInputs)
        
        self.ui.green_C1.clicked.connect(lambda: self.toggleColor(self.ui.green_C1))
        self.ui.green_C1.setStyleSheet('background-color: blue')
        self.green_C1_state = True
        self.ui.green_C2.clicked.connect(lambda: self.toggleColor(self.ui.green_C2))
        self.ui.green_C2.setStyleSheet('background-color: white')
        self.green_C2_state = False
        
        self.show()


    #################################TRYING TO TOGGLE THE BUTTONS/initialize STATES/THE REST##################################
    
        
    def toggleColor(self, button):
        if button.styleSheet() == 'background-color: white':
            button.setStyleSheet('background-color: blue')
            
            if button == self.ui.green_C1:
                self.ui.green_C2.setStyleSheet('background-color: white')
            else:
                self.ui.green_C1.setStyleSheet('background-color: white')
        else:
            button.setStyleSheet('background-color: white')

    def switchStates(self):
        if self.ui.green_C1.isChecked:
            self.ui.green_C1.setStyleSheet("background-color: #ADD8E6")
            self.ui.green_C2.setStyleSheet("background-color: None")
        else:
            self.ui.green_C1.setStyleSheet("background-color: None")
            self.ui.green_C2.setStyleSheet("background-color: #ADD8E6")


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


    def otherModes(self):
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

    def clearInputs(self):
        self.ui.enterLocation.setText("{0}".format(""))
        self.ui.enterSpeed.setText("{0}".format(""))
        self.ui.suggSpeedOutput.setText("Suggested Speed: --mph")
        self.ui.authority.setText("Authority: --mi")

    def showSuggSpeed(self):
        entSpeed = self.ui.enterSpeed.text()
        self.ui.suggSpeedOutput.setText("Suggested Speed: {0}mph".format(entSpeed))
        self.ui.enterLocation.setText("{0}".format(""))
        self.ui.enterSpeed.setText("{0}".format(""))

    def autoSwitch(self):
        self.ui.manualSelect.setChecked(False)
        self.ui.maintenanceSelect.setChecked(False)
        self.ui.greenLine_2.setStyleSheet("background-color: none")
        self.ui.greenLine_2.setStyleSheet("color: black")
        self.ui.redLineText.setStyleSheet("background-color: none")
        self.ui.redLineText.setStyleSheet("color: black")

    def manualSwitch(self):
        self.ui.autoSelect.setChecked(False)
        self.ui.maintenanceSelect.setChecked(False)
        self.ui.greenLine_2.setStyleSheet("background-color: none")
        self.ui.greenLine_2.setStyleSheet("color: black")
        self.ui.redLineText.setStyleSheet("background-color: none")
        self.ui.redLineText.setStyleSheet("color: black")

    def maintenanceSwitch(self):
        self.ui.manualSelect.setChecked(False)
        self.ui.autoSelect.setChecked(False)
        self.ui.greenLine_2.setStyleSheet("background-color: green")
        self.ui.greenLine_2.setStyleSheet("color: green")
        self.ui.redLineText.setStyleSheet("background-color: pink")
        self.ui.redLineText.setStyleSheet("color: red")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()