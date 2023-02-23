import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, uic
from Wayside_Test import Ui_MainWindow
from Track_Configuration import Ui_TrackConfig
from blockwidget import Ui_Form
from pathlib import Path

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Wayside Test UI')

        #set all switch buttons to disabled
        self.ca.setEnabled(False)
        self.cb.setEnabled(False)
        self.ga.setEnabled(False)
        self.gb.setEnabled(False)
        self.j1a.setEnabled(False)
        self.j1b.setEnabled(False)
        self.j2a.setEnabled(False)
        self.j2b.setEnabled(False)
        self.automaticmode.setDown(True)

        #pop up windows
        self.trackconfiguration.clicked.connect(self.configurationWindow)
        self.pusha.clicked.connect(self.blocksWindow)
        self.pushb.clicked.connect(self.blocksWindow)
        self.pushc.clicked.connect(self.blocksWindow)
        self.pushd.clicked.connect(self.blocksWindow)
        self.pushe.clicked.connect(self.blocksWindow)
        self.pushf.clicked.connect(self.blocksWindow)
        self.pushg.clicked.connect(self.blocksWindow)
        self.pushh.clicked.connect(self.blocksWindow)
        self.pushi.clicked.connect(self.blocksWindow)
        self.pushj.clicked.connect(self.blocksWindow)
        self.pushk.clicked.connect(self.blocksWindow)
        self.pushl.clicked.connect(self.blocksWindow)

        #set up gate buttons
        self.maintenancemode.toggled.connect(self.maintenanceMode)
        self.automaticmode.toggled.connect(self.automaticMode)

        #set up drop down menus
        self.sectionbox.currentTextChanged.connect(self.setBlockOptions)
        #self.sectionbox.currentTextChanged.connect(self.text_changed)
        
        



    #function for maintenance mode 
    def maintenanceMode(self):   
        if self.maintenancemode.isChecked:
            #enable all the buttons
            self.ca.setEnabled(True)
            self.cb.setEnabled(True)
            self.ga.setEnabled(True)
            self.gb.setEnabled(True)
            self.j1a.setEnabled(True)
            self.j1b.setEnabled(True)
            self.j2a.setEnabled(True)
            self.j2b.setEnabled(True)

    def automaticMode(self):
        self.ca.setEnabled(False)
        self.cb.setEnabled(False)
        self.ga.setEnabled(False)
        self.gb.setEnabled(False)
        self.j1a.setEnabled(False)
        self.j1b.setEnabled(False)
        self.j2a.setEnabled(False)
        self.j2b.setEnabled(False)

    #function for pop up window for track configuration
    def configurationWindow(self):
        self.tc = TrackConfig()
        self.tc.show() 
        
        #qfiledialogue adam and jake both use it
        
    #function for pop up window for seeing blocks in sections
    def blocksWindow(self):
        self.bl = Ui_Form()
        #layout = QVBoxLayout()
        self.bl.show()
    
    def setBlockOptions(self):
        content = self.sectionbox.currentText()
        if content == 'A':
            self.blockbox.clear()
            self.blockbox.addItems(['1' , '2', '3'])
        elif content == 'B':
            self.blockbox.clear()
            self.blockbox.addItems(['4', '5', '6'])
        elif content == 'C':
            self.blockbox.clear()
            self.blockbox.addItems(['7', '8', '9'])
        elif content == 'D':
            self.blockbox.clear()
            self.blockbox.addItems(['10', '11', '12'])
        elif content == 'E':
            self.blockbox.clear()
            self.blockbox.addItems(['13', '14', '15'])
        elif content == 'F':
            self.blockbox.clear()
            self.blockbox.addItems(['16', '17', '18', '19', '20'])
        elif content == 'G':
            self.blockbox.clear()
            self.blockbox.addItems(['21', '22', '23'])
        elif content == 'H':
            self.blockbox.clear()
            self.blockbox.addItems(['24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45'])
        elif content == 'I':
            self.blockbox.clear()
            self.blockbox.addItems(['46', '47', '48'])
        elif content == 'J':
            self.blockbox.clear()
            self.blockbox.addItems(['49', '50', '51', '52', '53', '54'])
        elif content == 'K':
            self.blockbox.clear()
            self.blockbox.addItems(['55', '56', '57'])
        elif content == 'L':
            self.blockbox.clear()
            self.blockbox.addItems(['58', '59', '60'])


    #function for toggle switch colors but see if you can do labels instead of buttons??
    def toggleColor(self, button1, button2): #adams
        button1.setEnabled(False)
        button2.setEnabled(True)
        button1.setStyleSheet('background-color: SkyBlue')
        button2.setStyleSheet('background-color: white; color: gray')
        #self.toggleColor(self.ca,self.cb)
        #self.toggleColor(self.cb,self.ca)

    def clickBox(self): #laurens
        #internal lights
        if self.intLights.isChecked():
                self.intLightLabel.setStyleSheet("background-color: green")
                self.intLightLabel.setText("ON")
        else:
            self.intLightLabel.setStyleSheet("background-color: red")
            self.intLightLabel.setText("OFF")

    #function for section occupancy 
    #were going to have to be able to change labels somehow
    def clickBox(self): #laurens
        if self.sigFault.isChecked():
                sigIcon = QtGui.QIcon("sigON.png")
                self.sigFaultLabel.setIcon(sigIcon)
                self.sigFaultLabel.setIconSize(QSize(50, 50))
        else:
            sigIcon = QtGui.QIcon("sigOFF.png")
            self.sigFaultLabel.setIcon(sigIcon)
            self.sigFaultLabel.setIconSize(QSize(50, 50))

    #function for number of active trains
    #somehow count the number of times the red train label comes up

    #function for light colors
    #just a variation of click box from lauren that makes all but one a white circle with a black outline
    
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
                print("data: ", data)
                self.plcdisplay.setText(data)
                        
class Ui_Form(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ui_Form, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Block Information')

# app = QtWidgets.QApplication(sys.argv)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    app.exec()