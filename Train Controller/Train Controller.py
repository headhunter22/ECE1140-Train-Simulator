import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QSize


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("mainwindow.ui", self)
        self.setWindowTitle("Train Controller")
        self.EmerBrake.clicked.connect(self.EBClick)
        self.Headlights.stateChanged.connect(self.clickBox)

    def EBClick(self):
        self.EmerBrake.setStyleSheet("{background-color : red};")

    def clickBox(self):
        if self.Headlights.isChecked():
            self.Headlights.setStyleSheet("{background-color : green};")




# Needed to open the window #
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()