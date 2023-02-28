import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QSize

# Upload File Class
class UploadFile(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("UploadRoute.ui", self)
        self.setWindowTitle('Upload File')

        self.fileBrowser = QtWidgets.QFileDialog()
        self.SelectFileButton.clicked.connect(self.selectFile)
        self.CancelButton.clicked.connect(self.closeWindow)
        self.GoButton.clicked.connect(self.reparseTrack)

    def selectFile(self):
        response = self.fileBrowser.getOpenFileNames(
            caption='Select File',
            directory=os.getcwd(),
            initialFilter='Data File (*.csv)'
        )

        self.fileName = str(response[0][0])
        print(self.fileName)

    def closeWindow(self):
        self.close()

    def reparseTrack(self):
        return
        # this function needs to reparse the track and update the main window
# end upload file clas