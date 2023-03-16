import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, uic
from Wayside_Test import Ui_MainWindow
from Track_Configuration import Ui_TrackConfig
from blockwidget import Ui_Section
from pathlib import Path

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Wayside Test UI')

        #set all switch buttons to disabled
        self.ca.setEnabled(False)
        #self.ca.setStyleSheet("background-color: sky blue")
        self.cb.setEnabled(False)
        # self.ga.setEnabled(False)
        # self.gb.setEnabled(False)
        # self.j1a.setEnabled(False)
        # self.j1b.setEnabled(False)
        # self.j2a.setEnabled(False)
        # self.j2b.setEnabled(False)
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
        # self.pushd.clicked.connect(self.blocksWindow)
        # self.pushe.clicked.connect(self.blocksWindow)
        # self.pushf.clicked.connect(self.blocksWindow)
        # self.pushg.clicked.connect(self.blocksWindow)
        # self.pushh.clicked.connect(self.blocksWindow)
        # self.pushi.clicked.connect(self.blocksWindow)
        # self.pushj.clicked.connect(self.blocksWindow)
        # self.pushk.clicked.connect(self.blocksWindow)
        # self.pushl.clicked.connect(self.blocksWindow)

        #set up gate buttons
        self.maintenancemode.toggled.connect(self.maintenanceMode)
        self.automaticmode.toggled.connect(self.automaticMode)

        #set up drop down menus
        self.sectionbox.currentTextChanged.connect(self.setBlockOptions)
        self.occupancybox.currentTextChanged.connect(self.changeIcon)
        self.sectionbox.setPlaceholderText('Section')
        self.blockbox.setPlaceholderText('Block')
        self.occupancybox.setPlaceholderText('Occupancy')

        #active trains
        self.aicon.setPixmap(QPixmap('redtrain.png'))
        #self.activetrains.display(counts)
        counts = 2
        self.activetrains.display(counts)
        #self.occupancybox.currentTextChanged.connect(self.changeIcon)
        #self.occupancybox.currentTextChanged.connect(self.activeTrains)

        #lights
        self.reda.setPixmap(QPixmap('redlight.png'))
        self.greenb.setPixmap(QPixmap('greenlight.png'))
        self.redbutton.toggled.connect(self.changeLights)
        self.yellowbutton.toggled.connect(self.changeLights)
        self.greenbutton.toggled.connect(self.changeLights)
        
    #function for maintenance mode 
    def maintenanceMode(self):   
        self.ca.setEnabled(True)
        self.cb.setEnabled(True)
        # self.ga.setEnabled(True)
        # self.gb.setEnabled(True)
        # self.j1a.setEnabled(True)
        # self.j1b.setEnabled(True)
        # self.j2a.setEnabled(True)
        # self.j2b.setEnabled(True)

    def automaticMode(self):
        self.ca.setEnabled(False)
        #self.ca.setStyleSheet('QPushButton::Pressed; color: SkyBlue')
        self.cb.setEnabled(False)
        #self.cb.setStyleSheet('QPushButton::Pressed; color: SkyBlue')
        # self.ga.setEnabled(False)
        # self.gb.setEnabled(False)
        # self.j1a.setEnabled(False)
        # self.j1b.setEnabled(False)
        # self.j2a.setEnabled(False)
        # self.j2b.setEnabled(False)

    #function for pop up window for track configuration
    def configurationWindow(self):
        self.tc = TrackConfig()
        self.tc.show() 
        
    #function for pop up window for seeing blocks in sections
    def blocksWindow(self):
        self.bl = Ui_Section()
        #layout = QVBoxLayout()
        self.bl.show()
    
    def setBlockOptions(self):
        content = self.sectionbox.currentText()
        if content == 'A':
            self.blockbox.clear()
            self.blockbox.addItems(['1' , '2', '3', '4', '5'])
        elif content == 'B':
            self.blockbox.clear()
            self.blockbox.addItems(['6', '7', '8', '9', '10'])
        elif content == 'C':
            self.blockbox.clear()
            self.blockbox.addItems(['11', '12', '13', '14', '15'])
        # elif content == 'D':
        #     self.blockbox.clear()
        #     self.blockbox.addItems(['10', '11', '12'])
        # elif content == 'E':
        #     self.blockbox.clear()
        #     self.blockbox.addItems(['13', '14', '15'])
        # elif content == 'F':
        #     self.blockbox.clear()
        #     self.blockbox.addItems(['16', '17', '18', '19', '20'])
        # elif content == 'G':
        #     self.blockbox.clear()
        #     self.blockbox.addItems(['21', '22', '23'])
        # elif content == 'H':
        #     self.blockbox.clear()
        #     self.blockbox.addItems(['24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45'])
        # elif content == 'I':
        #     self.blockbox.clear()
        #     self.blockbox.addItems(['46', '47', '48'])
        # elif content == 'J':
        #     self.blockbox.clear()
        #     self.blockbox.addItems(['49', '50', '51', '52', '53', '54'])
        # elif content == 'K':
        #     self.blockbox.clear()
        #     self.blockbox.addItems(['55', '56', '57'])
        # elif content == 'L':
        #     self.blockbox.clear()
        #     self.blockbox.addItems(['58', '59', '60'])


    #function for toggle switch colors but see if you can do labels instead of buttons??
    def toggleColor(self, button1, button2): #adams
        button1.setEnabled(False)
        button2.setEnabled(True)
        button1.setStyleSheet('background-color: SkyBlue; color: black')
        button2.setStyleSheet('background-color: white; color: gray')

    def changeIcon(self): #laurens
        section = self.sectionbox.currentText()
        block = self.blockbox.currentText()
        occupation = self.occupancybox.currentText()
        if section == 'A':
            if occupation == 'Occupied':
                self.aicon.setPixmap(QPixmap('redtrain.png'))
                #counts = counts + 1
            else:
                self.aicon.setPixmap(QPixmap('tracks.png'))
                #counts = counts - 1
            # if block == '1':
            #     if occupation == "Occupied":
            #         self.aicon.setPixmap("redtrain.png")
            #     else:
            #         self.aicon.setPixmap("tracks.png")
            # elif block == '2':
            #     if occupation == "Occupied":
            #         self.aicon.setPixmap("redtrain.png")
            #     else:
            #         self.aicon.setPixmap("tracks.png")
        elif section == 'B':
            if occupation == 'Occupied':
                self.bicon.setPixmap(QPixmap('redtrain.png'))
                #counts = counts + 1
            else:
                self.bicon.setPixmap(QPixmap('tracks.png'))
                #counts = counts - 1
        elif section == 'C':
            if occupation == 'Occupied':
                self.cicon.setPixmap(QPixmap('redtrain.png'))
                #counts = counts + 1
            else:
                self.cicon.setPixmap(QPixmap('tracks.png'))
                #counts = counts - 1

    #function for number of active trains
    #somehow counts the number of times the red train label comes up
    def activeTrains(self, counts):
        self.activetrains.display(counts)

    #function for light colors
    #just a variation of click box from lauren that makes all but one a white circle with a black outline
    def changeLights(self):
        gate = self.crossingbox.currentText()
        redbutton = self.redbutton.isChecked()
        yellowbutton = self.yellowbutton.isChecked()
        greenbutton = self.greenbutton.isChecked()
        if gate == '1':
            if redbutton == True:
                self.reda.setPixmap(QPixmap('redlight.png'))
                self.yellowa.setPixmap(QPixmap('offlight.png'))
                self.greena.setPixmap(QPixmap('offlight.png'))
                self.positiona.setText('Active')
            elif yellowbutton == True:
                self.reda.setPixmap(QPixmap('offlight.png'))
                self.yellowa.setPixmap(QPixmap('yellowlight.png'))
                self.greena.setPixmap(QPixmap('offlight.png'))
                self.positiona.setText('Active')
            elif greenbutton == True:
                self.reda.setPixmap(QPixmap('offlight.png'))
                self.yellowa.setPixmap(QPixmap('offlight.png'))
                self.greena.setPixmap(QPixmap('greenlight.png'))
                self.positiona.setText('Inactive')
        elif gate == '2':
            if redbutton == True:
                self.redb.setPixmap(QPixmap('redlight.png'))
                self.yellowb.setPixmap(QPixmap('offlight.png'))
                self.greenb.setPixmap(QPixmap('offlight.png'))
                self.positionb.setText('Active')
            elif yellowbutton == True:
                self.redb.setPixmap(QPixmap('offlight.png'))
                self.yellowb.setPixmap(QPixmap('yellowlight.png'))
                self.greenb.setPixmap(QPixmap('offlight.png'))
                self.positionb.setText('Active')
            elif greenbutton == True:
                self.redb.setPixmap(QPixmap('offlight.png'))
                self.yellowb.setPixmap(QPixmap('offlight.png'))
                self.greenb.setPixmap(QPixmap('greenlight.png'))
                self.positionb.setText('Inactive')


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
                        
class Ui_Section(QtWidgets.QMainWindow, Ui_Section):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ui_Section, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Block Information')

# app = QtWidgets.QApplication(sys.argv)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    app.exec()