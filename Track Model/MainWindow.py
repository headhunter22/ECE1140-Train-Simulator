import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QSize

class MainWindow(QtWidgets.QMainWindow):
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                uic.loadUi("MainTrackModel.ui", self)
                self.setWindowTitle('Track Model UI')

                #self.pushButton.clicked.connect(self.getInfoPage)

        def getInfoPage(self):
                self.openBlockInfo()

        def openBlockInfo(self):
                self.window = QtWidgets.QMainWindow()
                self.ui = BlockInfo()
                self.ui.setupUi(self.window)
                self.window.show()

# end class

#defining the app and the window
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()