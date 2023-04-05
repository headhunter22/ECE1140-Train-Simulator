import sys
from pathlib import Path
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, uic

#sys.path.append('/Users/Public/Documents/VSCode/ECE1140-Team-1/Wayside')
#print(sys.path)
#from Track_Configuration import Ui_TrackConfig 
from blockwidget import Ui_Section
from Wayside_Main_B import Ui_MainWindow
from test2 import Ui_testpopup
import PLCParser as PLCParser

class WMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(WMainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Wayside Main UI')

        #set all switch buttons to disabled
        self.ca.setEnabled(False)
        self.cb.setEnabled(False)
        self.ga.setEnabled(False)
        self.gb.setEnabled(False)

        #switch button colors
        self.automaticmode.setDown(True)
        self.ca.clicked.connect(lambda: self.toggleColor(self.ca, self.cb))
        self.ca.setStyleSheet('background-color: SkyBlue')
        self.cb.clicked.connect(lambda: self.toggleColor(self.cb, self.ca))
        self.cb.setStyleSheet('background-color: white; color: gray')
        self.ga.clicked.connect(lambda: self.toggleColor(self.ga, self.gb))
        self.ga.setStyleSheet('background-color: SkyBlue')
        self.gb.clicked.connect(lambda: self.toggleColor(self.gb, self.ga))
        self.gb.setStyleSheet('background-color: white; color: gray')

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

        #set up gate buttons
        self.maintenancemode.toggled.connect(self.maintenanceMode)
        self.automaticmode.toggled.connect(self.automaticMode)

        #active trains
        self.aicon.setPixmap(QPixmap('greentrain.png'))
        self.bicon.setPixmap(QPixmap('redtracks.png'))
        self.cicon.setPixmap(QPixmap('redtracks.png'))
        self.dicon.setPixmap(QPixmap('tracks.png'))
        #self.eicon.setPixmap(QPixmap('redtracks.png'))
        #self.ficon.setPixmap(QPixmap('redtracks.png'))
        self.jicon.setPixmap(QPixmap('tracks.png'))
        
        counts = 2
        self.activetrains.display(counts)

        #lights
        self.reda.setPixmap(QPixmap('redlight.png'))
        self.greenb.setPixmap(QPixmap('greenlight.png'))

    #function for maintenance mode 
    def maintenanceMode(self):   
        self.ca.setEnabled(True)
        self.cb.setEnabled(True)
        self.ga.setEnabled(True)
        self.gb.setEnabled(True)
        test.autoC0.setEnabled(True)
        test.autoC1.setEnabled(True)
        test.autoG0.setEnabled(True)
        test.autoG1.setEnabled(True)

    def automaticMode(self):
        self.ca.setEnabled(False)
        self.cb.setEnabled(False)
        self.ga.setEnabled(False)
        self.gb.setEnabled(False)
        test.autoC0.setEnabled(False)
        test.autoC1.setEnabled(False)
        test.autoG0.setEnabled(False)
        test.autoG1.setEnabled(False)

    #function for pop up window for track configuration
    def configurationWindow(self):
        #self.tc = TrackConfig()
        self.trackconfiguration.clicked.connect(self.runParser)
        #self.tc.show()

    def runParser(self):
        PLCParser.parse(self)

    #function for pop up window for seeing blocks in sections
    def blocksWindow(self):
        self.bl = Ui_Section()
        self.bl.show()

    #function for toggle switch colors but see if you can do labels instead of buttons??
    def toggleColor(self, button1, button2): #adams
        button1.setEnabled(False)
        button2.setEnabled(True)
        button1.setStyleSheet('background-color: SkyBlue; color: black')
        button2.setStyleSheet('background-color: white; color: gray')

    #occupation 2 blocks ahead for now
    #!!!!!! TO DO !!!!!!!!!
    def changeOccupation(self):
        if self.aicon.Pixmap() == 'greentrain.png':
            self.bicon.setPixmap('redtracks.png')

    #change train icons
    def changeIcon(self): #laurens
        section = self.sectionbox.currentText()
        block = self.blockbox.currentText()
        occupation = self.occupancybox.currentText()
        if section == 'A':
            if occupation == 'Occupied':
                self.aicon.setPixmap(QPixmap('greentrain.png'))
                #counts = counts + 1
            else:
                self.aicon.setPixmap(QPixmap('tracks.png'))
                #counts = counts - 1
            # if block == '1':
            #     if occupation == "Occupied":
            #         self.aicon.setPixmap("greentrain.png")
            #     else:
            #         self.aicon.setPixmap("tracks.png")
            # elif block == '2':
            #     if occupation == "Occupied":
            #         self.aicon.setPixmap("greentrain.png")
            #     else:
            #         self.aicon.setPixmap("tracks.png")
        elif section == 'B':
            if occupation == 'Occupied':
                self.bicon.setPixmap(QPixmap('greentrain.png'))
                #counts = counts + 1
            else:
                self.bicon.setPixmap(QPixmap('tracks.png'))
                #counts = counts - 1
        elif section == 'C':
            if occupation == 'Occupied':
                self.cicon.setPixmap(QPixmap('greentrain.png'))
                #counts = counts + 1
            else:
                self.cicon.setPixmap(QPixmap('tracks.png'))
                #counts = counts - 1
        elif section == 'D':
            if occupation == 'Occupied':
                self.dicon.setPixmap(QPixmap('greentrain.png'))
            else:
                self.dicon.setPixmap(QPixmap('tracks.png'))
        elif section == 'E':
            if occupation == 'Occupied':
                self.eicon.setPixmap(QPixmap('greentrain.png'))
            else:
                self.eicon.setPixmap(QPixmap('tracks.png'))
        elif section == 'F':
            if occupation == 'Occupied':
                self.ficon.setPixmap(QPixmap('greentrain.png'))
            else:
                self.ficon.setPixmap(QPixmap('tracks.png'))
        elif section == 'G':
            if occupation == 'Occupied':
                self.gicon.setPixmap(QPixmap('greentrain.png'))
            else:
                self.gicon.setPixmap(QPixmap('tracks.png'))
        elif section == 'H':
            if occupation == 'Occupied':
                self.hicon.setPixmap(QPixmap('greentrain.png'))
            else:
                self.hicon.setPixmap(QPixmap('tracks.png'))
        elif section == 'I':
            if occupation == 'Occupied':
                self.iicon.setPixmap(QPixmap('greentrain.png'))
            else:
                self.iicon.setPixmap(QPixmap('tracks.png'))
        elif section == 'J':
            if occupation == 'Occupied':
                self.jicon.setPixmap(QPixmap('greentrain.png'))
            else:
                self.jicon.setPixmap(QPixmap('tracks.png'))

    #function for number of active trains
    #somehow counts the number of times the red train label comes up
    def activeTrains(self, counts):
        self.activetrains.display(counts)

class Ui_Section(QtWidgets.QMainWindow, Ui_Section):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ui_Section, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Block Information')

class Ui_testpopup(QtWidgets.QMainWindow, Ui_testpopup):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ui_testpopup, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Block Information')

        #set up drop down menus
        self.sectionbox.currentTextChanged.connect(self.setBlockOptions)
        
        #toggle lights
        self.reda.toggled.connect(self.changeLights)
        self.yellowa.toggled.connect(self.changeLights)
        self.greena.toggled.connect(self.changeLights)
        self.redb.toggled.connect(self.changeLights)
        self.yellowb.toggled.connect(self.changeLights)
        self.greenb.toggled.connect(self.changeLights)

        #start with reda greenb
        self.reda.setDown(True)
        self.greenb.setDown(True)

        #set up change icon
        self.sectionbox.currentTextChanged.connect(self.setBlockOptions)
        self.occupancybox.currentTextChanged.connect(self.changeIcon)

        #change gates in auto
        #self.autoC0.toggled.

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

    def changeLights(self):
        #gate = self.crossingbox.currentText()
        redbuttona = self.reda.isChecked()
        yellowbuttona = self.yellowa.isChecked()
        greenbuttona = self.greena.isChecked()
        redbuttonb = self.redb.isChecked()
        yellowbuttonb = self.yellowb.isChecked()
        greenbuttonb = self.greenb.isChecked()
        #if gate == '1':
        if redbuttona == True:
            window.reda.setPixmap(QPixmap('redlight.png'))
            window.yellowa.setPixmap(QPixmap('offlight.png'))
            window.greena.setPixmap(QPixmap('offlight.png'))
            window.gatepositiona.setText('Active')
        elif yellowbuttona == True:
            self.reda.setDown(False)
            window.reda.setPixmap(QPixmap('offlight.png'))
            window.yellowa.setPixmap(QPixmap('yellowlight.png'))
            window.greena.setPixmap(QPixmap('offlight.png'))
            window.gatepositiona.setText('Active')
        elif greenbuttona == True:
            self.reda.setDown(False)
            window.reda.setPixmap(QPixmap('offlight.png'))
            window.yellowa.setPixmap(QPixmap('offlight.png'))
            window.greena.setPixmap(QPixmap('greenlight.png'))
            window.gatepositiona.setText('Inactive')
        if redbuttonb == True:
            self.greenb.setDown(False)
            window.redb.setPixmap(QPixmap('redlight.png'))
            window.yellowb.setPixmap(QPixmap('offlight.png'))
            window.greenb.setPixmap(QPixmap('offlight.png'))
            window.gatepositionb.setText('Active')
        elif yellowbuttonb == True:
            self.greenb.setDown(False)
            window.redb.setPixmap(QPixmap('offlight.png'))
            window.yellowb.setPixmap(QPixmap('yellowlight.png'))
            window.greenb.setPixmap(QPixmap('offlight.png'))
            window.gatepositionb.setText('Active')
        elif greenbuttonb == True:
            window.redb.setPixmap(QPixmap('offlight.png'))
            window.yellowb.setPixmap(QPixmap('offlight.png'))
            window.greenb.setPixmap(QPixmap('greenlight.png'))
            window.gatepositionb.setText('Inactive')

    def changeIcon(self): #laurens
        section = self.sectionbox.currentText()
        block = self.blockbox.currentText()
        occupation = self.occupancybox.currentText()
        if section == 'A':
            if occupation == 'Occupied':
                window.aicon.setPixmap(QPixmap('greentrain.png'))
                window.bicon.setPixmap(QPixmap('redtracks.png'))
                window.cicon.setPixmap(QPixmap('redtracks.png'))
                #counts = counts + 1
            else:
                window.aicon.setPixmap(QPixmap('tracks.png'))
                #counts = counts - 1
            # if block == '1':
            #     if occupation == "Occupied":
            #         self.aicon.setPixmap("greentrain.png")
            #     else:
            #         self.aicon.setPixmap("tracks.png")
            # elif block == '2':
            #     if occupation == "Occupied":
            #         self.aicon.setPixmap("greentrain.png")
            #     else:
            #         self.aicon.setPixmap("tracks.png")
        elif section == 'B':
            if occupation == 'Occupied':
                window.bicon.setPixmap(QPixmap('greentrain.png'))
                window.cicon.setPixmap(QPixmap('redtracks.png'))
                window.dicon.setPixmap(QPixmap('redtracks.png'))
                #counts = counts + 1
            if occupation == 'Unoccupied':
                window.bicon.setPixmap(QPixmap('tracks.png'))
                #counts = counts - 1
        elif section == 'C':
            if occupation == 'Occupied':
                window.cicon.setPixmap(QPixmap('greentrain.png'))
                window.dicon.setPixmap(QPixmap('redtracks.png'))
                window.eicon.setPixmap(QPixmap('redtracks.png'))
                #counts = counts + 1
            if occupation == 'Unoccupied':
                window.cicon.setPixmap(QPixmap('tracks.png'))
                #counts = counts - 1
        elif section == 'D':
            if occupation == 'Occupied':
                window.dicon.setPixmap(QPixmap('greentrain.png'))
                window.eicon.setPixmap(QPixmap('redtracks.png'))
                window.ficon.setPixmap(QPixmap('redtracks.png'))
            if occupation == 'Unoccupied':
                window.dicon.setPixmap(QPixmap('tracks.png'))
        elif section == 'E':
            if occupation == 'Occupied':
                window.eicon.setPixmap(QPixmap('greentrain.png'))
                window.ficon.setPixmap(QPixmap('redtracks.png'))
                window.gicon.setPixmap(QPixmap('redtracks.png'))
            if occupation == 'Unoccupied':
                window.eicon.setPixmap(QPixmap('tracks.png'))
        elif section == 'F':
            if occupation == 'Occupied':
                window.ficon.setPixmap(QPixmap('greentrain.png'))
                window.gicon.setPixmap(QPixmap('redtracks.png'))
                window.hicon.setPixmap(QPixmap('redtracks.png'))
            if occupation == 'Unoccupied':
                window.ficon.setPixmap(QPixmap('tracks.png'))
        elif section == 'G':
            if occupation == 'Occupied':
                window.gicon.setPixmap(QPixmap('greentrain.png'))
                window.hicon.setPixmap(QPixmap('redtracks.png'))
                window.iicon.setPixmap(QPixmap('redtracks.png'))
            if occupation == 'Unoccupied':
                window.gicon.setPixmap(QPixmap('tracks.png'))
        elif section == 'H':
            if occupation == 'Occupied':
                window.hicon.setPixmap(QPixmap('greentrain.png'))
                window.iicon.setPixmap(QPixmap('redtracks.png'))
                window.jicon.setPixmap(QPixmap('redtracks.png'))
            if occupation == 'Unoccupied':
                window.hicon.setPixmap(QPixmap('tracks.png'))
        elif section == 'I':
            if occupation == 'Occupied':
                window.iicon.setPixmap(QPixmap('greentrain.png'))
                window.jicon.setPixmap(QPixmap('redtracks.png'))
            if occupation == 'Unoccupied':
                window.iicon.setPixmap(QPixmap('tracks.png'))
        elif section == 'J':
            if occupation == 'Occupied':
                window.jicon.setPixmap(QPixmap('greentrain.png'))
            if occupation == 'Unoccupied':
                window.jicon.setPixmap(QPixmap('tracks.png'))

#class Communications():
    #print("communicating from wayside.py")
    #get suggest speed
        #signal emits from .py
        #not actually needed for UI
    #get authority
        #signal emits from .py
    #get switch state in maintenance mode
        #signal emits from .py

    #send suggested speed
        #not actually needed for UI
    #send authority
    #send block occupancy
    #send rr crossings
    #send switches
    
app = QtWidgets.QApplication(sys.argv)
window = WMainWindow()
test = Ui_testpopup()
#window.show()
#test.show()
#app.exec()




#track configuration pop up so hold a funeral

# class TrackConfig(QtWidgets.QMainWindow, Ui_TrackConfig):
#     def __init__(self, *args, obj=None, **kwargs):
#         super(TrackConfig, self).__init__(*args, **kwargs)
#         self.setupUi(self)
#         self.setWindowTitle('Track Configuration')

#         #self.uploadplc.clicked.connect(self.readplc)
#         self.uploadplc.clicked.connect(self.runParser)
#         self.ladderlogic.setDown(True)



#     def readplc(self):
#         home_dir = str(Path.home())
#         fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

#         if fname[0]:
#             f = open(fname[0], 'r')
#             with f:
#                 data = f.read()
#                 #print("data: ", data)
#                 self.plcdisplay.setText(data)