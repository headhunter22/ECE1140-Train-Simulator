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
        #self.extLights.stateChanged.connect(self.clickBox)

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

        if self.intLights.isChecked():
                self.intLightLabel.setStyleSheet("background-color: green")
        else:
            self.intLightLabel.setStyleSheet("background-color: red")

       # if self.extLights.isChecked():
       #         self.extLightLabel.setStyleSheet("background-color: green")
       # else:
       #     self.extLightLabel.setStyleSheet("background-color: red")



            
    

#end class definition


#defining the app and the window
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()