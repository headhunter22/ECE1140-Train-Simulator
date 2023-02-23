import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, uic
from Track_Configuration import Ui_TrackConfig
from blockwidget import Ui_Form
from pathlib import Path
from Wayside_Main_B import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Wayside Main UI')

        #set all switch buttons to disabled
        self.ca.setEnabled(False)
        self.cb.setEnabled(False)

        #switch button colors
        self.automaticmode.setDown(True)
        self.ca.clicked.connect(lambda: self.toggleColor(self.ca, self.cb))
        self.ca.setStyleSheet('background-color: SkyBlue')
        self.cb.clicked.connect(lambda: self.toggleColor(self.cb, self.ca))
        self.cb.setStyleSheet('background-color: white; color: gray')

        #pop up windows
        self.trackconfiguration.clicked.connect(self.configurationWindow)
        self.pusha.clicked.connect(self.blocksWindow)
        self.pushb.clicked.connect(self.blocksWindow)
        self.pushc.clicked.connect(self.blocksWindow)

        #set up gate buttons
        self.maintenancemode.toggled.connect(self.maintenanceMode)
        self.automaticmode.toggled.connect(self.automaticMode)

        #active trains
        self.aicon.setPixmap(QPixmap('redtrain.png'))
        counts = 2
        self.activetrains.display(counts)

        #lights
        self.reda.setPixmap(QPixmap('redlight.png'))
        self.greenb.setPixmap(QPixmap('greenlight.png'))

    #function for maintenance mode 
    def maintenanceMode(self):   
        self.ca.setEnabled(True)
        self.cb.setEnabled(True)

    def automaticMode(self):
        self.ca.setEnabled(False)
        self.cb.setEnabled(False)

    #function for pop up window for track configuration
    def configurationWindow(self):
        self.tc = TrackConfig()
        self.tc.show()

    #function for pop up window for seeing blocks in sections
    def blocksWindow(self):
        self.bl = Ui_Form()
        self.bl.show()

    #function for toggle switch colors but see if you can do labels instead of buttons??
    def toggleColor(self, button1, button2): #adams
        button1.setEnabled(False)
        button2.setEnabled(True)
        button1.setStyleSheet('background-color: SkyBlue; color: black')
        button2.setStyleSheet('background-color: white; color: gray')

    #function for number of active trains
    #somehow counts the number of times the red train label comes up
    def activeTrains(self, counts):
        self.activetrains.display(counts)

class TrackConfig(QtWidgets.QMainWindow, Ui_TrackConfig):
    def __init__(self, *args, obj=None, **kwargs):
        super(TrackConfig, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Track Configuration')

        self.uploadplc.clicked.connect(self.readplc)

        self.ladderlogic.setDown(True)

    def readplc(self):
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                #print("data: ", data)
                self.plcdisplay.setText(data)

class Ui_Form(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ui_Form, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Block Information')






app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()