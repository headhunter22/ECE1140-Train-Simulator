import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QSize


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("TrainModelTestUI_v1.ui", self)
        self.setWindowTitle('Train Model Test UI')
        #temperature set
        self.tempButton.clicked.connect(self.tempInputfunc)
        #power set 
        self.powButton.clicked.connect(self.powInputfunc)

        #icon change
        icon = QtGui.QIcon("switch_off.jpg")
        self.checkBox.stateChanged.connect(self.clickBox)
        self.checkBox.setIcon(icon)
        self.checkBox.setIconSize(QSize(300, 300))

        #light status change
        self.intLights.stateChanged.connect(self.clickBox)
        self.extLights.stateChanged.connect(self.clickBox)
        self.headlights.stateChanged.connect(self.clickBox)
        self.leftDoor.stateChanged.connect(self.clickBox)
        self.rightDoor.stateChanged.connect(self.clickBox)

    #temp set function
    def tempInputfunc(self):
        inputTemp = self.inputTemp.text()
        self.outputTemp.setText("{0} degrees F".format(inputTemp))
    
    #power set function
    def powInputfunc(self):
        inputPow = self.inputPow.text()
        self.outputPow.setText("{0} Watts".format(inputPow))

    #changing box 
    def clickBox(self):
        if self.checkBox.isChecked():
            icon = QtGui.QIcon("switch_on.jpg")
            self.checkBox.setIcon(icon)
            self.checkBox.setIconSize(QSize(300, 300))
        else:
            icon = QtGui.QIcon("switch_off.jpg")
            self.checkBox.setIcon(icon)
            self.checkBox.setIconSize(QSize(300, 300))

        #internal lights
        if self.intLights.isChecked():
                self.intLightLabel.setStyleSheet("background-color: green")
                self.intLightLabel.setText("ON")
        else:
            self.intLightLabel.setStyleSheet("background-color: red")
            self.intLightLabel.setText("OFF")

        #external lights
        if self.extLights.isChecked():
                self.extLightLabel.setStyleSheet("background-color: green")
                self.extLightLabel.setText("ON")
        else:
            self.extLightLabel.setStyleSheet("background-color: red")
            self.extLightLabel.setText("OFF")

        #headlights
        if self.headlights.isChecked():
                self.headlightLabel.setStyleSheet("background-color: green")
                self.headlightLabel.setText("ON")
        else:
            self.headlightLabel.setStyleSheet("background-color: red")
            self.headlightLabel.setText("OFF")

        #Left doors
        if self.leftDoor.isChecked():
                self.lDoorLabel.setStyleSheet("background-color: green")
                self.lDoorLabel.setText("ON")
        else:
            self.lDoorLabel.setStyleSheet("background-color: red")
            self.lDoorLabel.setText("OFF")

        #Right doors
        if self.rightDoor.isChecked():
                self.rDoorLabel.setStyleSheet("background-color: green")
                self.rDoorLabel.setText("ON")
        else:
            self.rDoorLabel.setStyleSheet("background-color: red")
            self.rDoorLabel.setText("OFF")
    

#end class definition


#defining the app and the window
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()