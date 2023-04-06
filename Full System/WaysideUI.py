import sys
from pathlib import Path
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, uic
from signals import signals

#sys.path.append('/Users/Public/Documents/VSCode/ECE1140-Team-1/Wayside')
#print(sys.path)
#from Track_Configuration import Ui_TrackConfig 
from blockwidget import Ui_Section
from Wayside_Main_B import Ui_MainWindowB
from Wayside_Main_A import Ui_MainWindowA
#from test2 import Ui_testpopup
import PLCParser as PLCParser

# MainWindowA N-Z
# MainWindowB A-M

class WMainWindowA(QtWidgets.QMainWindow, Ui_MainWindowA):
    def __init__(self, *args, obj=None, **kwargs):
        super(WMainWindowA, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Wayside Main UI')

        #signals
        signals.wtowOccupancy.connect(WaysideUIFunctions.changeOccupancy)
        signals.wtowVacancy.connect(WaysideUIFunctions.changeVacancy)
        
        #set all switch buttons to disabled
        self.ca.setEnabled(False)
        self.cb.setEnabled(False)
        self.ga.setEnabled(False)
        self.gb.setEnabled(False)

        #switch button colors
        self.automaticmode.setDown(True)
        self.ca.clicked.connect(lambda: WaysideUIFunctions.toggleColor(self.ca, self.cb))
        self.ca.setStyleSheet('background-color: SkyBlue')
        self.cb.clicked.connect(lambda: WaysideUIFunctions.toggleColor(self.cb, self.ca))
        self.cb.setStyleSheet('background-color: white; color: gray')
        self.ga.clicked.connect(lambda: WaysideUIFunctions.toggleColor(self.ga, self.gb))
        self.ga.setStyleSheet('background-color: SkyBlue')
        self.gb.clicked.connect(lambda: WaysideUIFunctions.toggleColor(self.gb, self.ga))
        self.gb.setStyleSheet('background-color: white; color: gray')

        #pop up windows
        self.trackconfiguration.clicked.connect(WaysideUIFunctions.configurationWindow)
        self.pushn.clicked.connect(lambda ch, i= 'N': WaysideUIFunctions.makeSectionWindow(i))
        self.pusho.clicked.connect(lambda ch, i= 'O': WaysideUIFunctions.makeSectionWindow(i))
        self.pushp.clicked.connect(lambda ch, i= 'P': WaysideUIFunctions.makeSectionWindow(i))
        self.pushq.clicked.connect(lambda ch, i= 'Q': WaysideUIFunctions.makeSectionWindow(i))
        self.pushr.clicked.connect(lambda ch, i= 'R': WaysideUIFunctions.makeSectionWindow(i))
        self.pushs.clicked.connect(lambda ch, i= 'S': WaysideUIFunctions.makeSectionWindow(i))
        self.pusht.clicked.connect(lambda ch, i= 'T': WaysideUIFunctions.makeSectionWindow(i))
        self.pushu.clicked.connect(lambda ch, i= 'U': WaysideUIFunctions.makeSectionWindow(i))
        self.pushv.clicked.connect(lambda ch, i= 'V': WaysideUIFunctions.makeSectionWindow(i))
        self.pushw.clicked.connect(lambda ch, i= 'W': WaysideUIFunctions.makeSectionWindow(i))
        self.pushx.clicked.connect(lambda ch, i= 'X': WaysideUIFunctions.makeSectionWindow(i))
        self.pushy.clicked.connect(lambda ch, i= 'Y': WaysideUIFunctions.makeSectionWindow(i))
        self.pushz.clicked.connect(lambda ch, i= 'Z': WaysideUIFunctions.makeSectionWindow(i))

        #set up gate buttons
        self.maintenancemode.toggled.connect(WaysideUIFunctions.maintenanceMode)
        self.automaticmode.toggled.connect(WaysideUIFunctions.automaticMode)

        #active trains
        self.qicon.setPixmap(QPixmap('tracks.png'))
        self.wicon.setPixmap(QPixmap('tracks.png'))
        # self.cicon.setPixmap(QPixmap('redtracks.png'))
        # self.dicon.setPixmap(QPixmap('tracks.png'))
        # #self.eicon.setPixmap(QPixmap('redtracks.png'))
        # #self.ficon.setPixmap(QPixmap('redtracks.png'))
        # self.jicon.setPixmap(QPixmap('tracks.png'))
        
        counts = 2
        self.activetrains.display(counts)

        #lights
        self.reda.setPixmap(QPixmap('redlight.png'))
        self.greenb.setPixmap(QPixmap('greenlight.png'))

# MainWindowB A-M
class WMainWindowB(QtWidgets.QMainWindow, Ui_MainWindowB):
    def __init__(self, *args, obj=None, **kwargs):
        super(WMainWindowB, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Wayside Main UI')

        #signals
        signals.wtowOccupancy.connect(WaysideUIFunctions.changeOccupancy)
        signals.wtowVacancy.connect(WaysideUIFunctions.changeVacancy)
        
        #set all switch buttons to disabled
        self.ca.setEnabled(False)
        self.cb.setEnabled(False)
        self.ga.setEnabled(False)
        self.gb.setEnabled(False)

        #switch button colors
        self.automaticmode.setDown(True)
        self.ca.clicked.connect(lambda: WaysideUIFunctions.toggleColor(self.ca, self.cb))
        self.ca.setStyleSheet('background-color: SkyBlue')
        self.cb.clicked.connect(lambda: WaysideUIFunctions.toggleColor(self.cb, self.ca))
        self.cb.setStyleSheet('background-color: white; color: gray')
        self.ga.clicked.connect(lambda: WaysideUIFunctions.toggleColor(self.ga, self.gb))
        self.ga.setStyleSheet('background-color: SkyBlue')
        self.gb.clicked.connect(lambda: WaysideUIFunctions.toggleColor(self.gb, self.ga))
        self.gb.setStyleSheet('background-color: white; color: gray')

        #pop up windows
        self.trackconfiguration.clicked.connect(WaysideUIFunctions.configurationWindow)
        self.pusha.clicked.connect(lambda: WaysideUIFunctions.makeSectionWindow('A'))
        self.pushb.clicked.connect(lambda ch, i= 'B': WaysideUIFunctions.makeSectionWindow(i))
        self.pushc.clicked.connect(lambda ch, i= 'C': WaysideUIFunctions.makeSectionWindow(i))
        self.pushd.clicked.connect(lambda ch, i= 'D': WaysideUIFunctions.makeSectionWindow(i))
        self.pushe.clicked.connect(lambda ch, i= 'E': WaysideUIFunctions.makeSectionWindow(i))
        self.pushf.clicked.connect(lambda ch, i= 'F': WaysideUIFunctions.makeSectionWindow(i))
        self.pushg.clicked.connect(lambda ch, i= 'G': WaysideUIFunctions.makeSectionWindow(i))
        self.pushh.clicked.connect(lambda ch, i= 'H': WaysideUIFunctions.makeSectionWindow(i))
        self.pushi.clicked.connect(lambda ch, i= 'I': WaysideUIFunctions.makeSectionWindow(i))
        self.pushj.clicked.connect(lambda ch, i= 'J': WaysideUIFunctions.makeSectionWindow(i))
        self.pushk.clicked.connect(lambda: WaysideUIFunctions.makeSectionWindow('A'))
        self.pushm.clicked.connect(lambda ch, i= 'B': WaysideUIFunctions.makeSectionWindow(i))

        #set up gate buttons
        self.maintenancemode.toggled.connect(WaysideUIFunctions.maintenanceMode)
        self.automaticmode.toggled.connect(WaysideUIFunctions.automaticMode)

        #active trains
        self.aicon.setPixmap(QPixmap('tracks.png'))
        self.bicon.setPixmap(QPixmap('tracks.png'))
        self.cicon.setPixmap(QPixmap('tracks.png'))
        self.dicon.setPixmap(QPixmap('tracks.png'))
        #self.eicon.setPixmap(QPixmap('redtracks.png'))
        #self.ficon.setPixmap(QPixmap('redtracks.png'))
        self.jicon.setPixmap(QPixmap('tracks.png'))
        
        counts = 2
        self.activetrains.display(counts)

        #lights
        self.reda.setPixmap(QPixmap('redlight.png'))
        self.greenb.setPixmap(QPixmap('greenlight.png'))

class WaysideUIFunctions(QtWidgets.QMainWindow, Ui_MainWindowA, Ui_MainWindowB):
    #function for maintenance mode 
    def maintenanceMode(self):   
        windowA.ca.setEnabled(True)
        windowA.cb.setEnabled(True)
        windowA.ga.setEnabled(True)
        windowA.gb.setEnabled(True)
        windowB.ca.setEnabled(True)
        windowB.cb.setEnabled(True)
        windowB.ga.setEnabled(True)
        windowB.gb.setEnabled(True)

    def automaticMode(self):
        windowA.ca.setEnabled(False)
        windowA.cb.setEnabled(False)
        windowA.ga.setEnabled(False)
        windowA.gb.setEnabled(False)
        windowB.ca.setEnabled(False)
        windowB.cb.setEnabled(False)
        windowB.ga.setEnabled(False)
        windowB.gb.setEnabled(False)

    #function for pop up window for track configuration
    def configurationWindow(self):
        #self.tc = TrackConfig()
        windowA.trackconfiguration.clicked.connect(self.runParser)
        windowB.trackconfiguration.clicked.connect(self.runParser)
        #self.tc.show()

    def runParser(self):
        PLCParser.parse(self)

    #function for pop up window for seeing blocks in sections
    def makeSectionWindow(self, whichsection):
        self.bl = Ui_Section()
        self.bl.sectionname.setText("Section", whichsection)

        if whichsection == 'A':
            #'1' or '2'or '3':
            self.bl.label_5.setText('1')
            self.bl.label_5.setText('2')
            self.bl.label_5.setText('3')
        elif whichsection == 'B':
            #'4'or '5'or '6':
            windowB.bicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'C':
            #'7' or '8' or '9' or '10' or '11' or '12':
            windowB.cicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'D':
            #'13' or '14' or '15' or '16':
            windowB.dicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'E':
            #'17' or '18' or '19' or '20':
            windowB.eicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'F':
            #'21' or '22' or '23' or '24' or '25' or '26' or '27' or '28':
            windowB.ficon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'G':
            #'29' or '30' or '31' or '32':
            windowB.gicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'H':
            #'33' or '34' or '35':
            windowB.hicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'I':
            #'36' or '37' or '38' or '39' or '40' or '41' or '42' or '43' or '44' or '45' or '46' or '47' or '48' or '49' or '50' or '44' or '45' or '46' or '47' or '48' or '49' or '50'or '51' or '52' or '53' or '54' or '55' or '56' or '57':
            windowB.iicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'J':
            #'58' or '59' or '60' or '61' or '62':
            windowB.jicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'K':
            #'63' or '64' or '65' or '67' or '68':
            windowB.kicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'L':
            #'69' or '70' or '71' or '72' or '73':
            windowB.licon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'M':
            #'74' or '75' or '76':
            windowB.micon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'N':
            #'77' or '78' or '79' or '80' or '81' or '83' or '84' or '85':
            windowA.nicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'O':
            #'86' or '87' or '88':
            windowA.oicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'P':
            #'89' or '90' or '91' or '92' or '93' or '94' or '95' or '96' or '97':
            windowA.picon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'Q':
            #'98' or '99' or '100':
            windowA.qicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'R':
            #'101':
            windowA.ricon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'S':
            #'102' or '103' or '104':
            windowA.sicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'T':
            #'105' or '106' or '107' or '108' or '109':
            windowA.ticon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'U':
            #'110' or '111' or '112' or '113' or '114' or '115' or '116':
            windowA.uicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'V':
            #'117' or '118' or '119' or '120' or '121':
            windowA.vicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'W':
            #'122' or '123' or '124' or '125' or '126' or '127' or '128' or '129' or '130' or '131' or '132' or '133' or '134' or '135' or '136' or '137' or '138' or '139' or '140' or '141' or '142' or '143':
            windowA.vicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'X':
            #'144' or '145' or '146':
            windowA.xicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'Y':
            #'147' or '148' or '149':
            windowA.yicon.setPixmap(QPixmap('greentrain.png'))
        elif whichsection == 'Z':
            #'150':
            windowA.zicon.setPixmap(QPixmap('greentrain.png'))

        self.bl.show()

    #function for toggle switch colors but see if you can do labels instead of buttons??
    def toggleColor(button1, button2): #adams
        button1.setEnabled(False)
        button2.setEnabled(True)
        button1.setStyleSheet('background-color: SkyBlue; color: black')
        button2.setStyleSheet('background-color: white; color: gray')

    #occupation 2 blocks ahead for now
    #!!!!!! TO DO !!!!!!!!!
    def changeOccupancy(self, block):
        #print("UI block", block, "is occupied")
        if block == '1' or '2'or '3':
            windowB.aicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '4'or '5'or '6':
            windowB.bicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '7' or '8' or '9' or '10' or '11' or '12':
            windowB.cicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '13' or '14' or '15' or '16':
            windowB.dicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '17' or '18' or '19' or '20':
            windowB.eicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '21' or '22' or '23' or '24' or '25' or '26' or '27' or '28':
            windowB.ficon.setPixmap(QPixmap('greentrain.png'))
        elif block == '29' or '30' or '31' or '32':
            windowB.gicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '33' or '34' or '35':
            windowB.hicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '36' or '37' or '38' or '39' or '40' or '41' or '42' or '43' or '44' or '45' or '46' or '47' or '48' or '49' or '50' or '44' or '45' or '46' or '47' or '48' or '49' or '50'or '51' or '52' or '53' or '54' or '55' or '56' or '57':
            windowB.iicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '58' or '59' or '60' or '61' or '62':
            windowB.jicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '63' or '64' or '65' or '67' or '68':
            windowB.kicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '69' or '70' or '71' or '72' or '73':
            windowB.licon.setPixmap(QPixmap('greentrain.png'))
        elif block == '74' or '75' or '76':
            windowB.micon.setPixmap(QPixmap('greentrain.png'))
        elif block == '77' or '78' or '79' or '80' or '81' or '83' or '84' or '85':
            windowA.nicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '86' or '87' or '88':
            windowA.oicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '89' or '90' or '91' or '92' or '93' or '94' or '95' or '96' or '97':
            windowA.picon.setPixmap(QPixmap('greentrain.png'))
        elif block == '98' or '99' or '100':
            windowA.qicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '101':
            windowA.ricon.setPixmap(QPixmap('greentrain.png'))
        elif block == '102' or '103' or '104':
            windowA.sicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '105' or '106' or '107' or '108' or '109':
            windowA.ticon.setPixmap(QPixmap('greentrain.png'))
        elif block == '110' or '111' or '112' or '113' or '114' or '115' or '116':
            windowA.uicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '117' or '118' or '119' or '120' or '121':
            windowA.vicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '122' or '123' or '124' or '125' or '126' or '127' or '128' or '129' or '130' or '131' or '132' or '133' or '134' or '135' or '136' or '137' or '138' or '139' or '140' or '141' or '142' or '143':
            windowA.vicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '144' or '145' or '146':
            windowA.xicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '147' or '148' or '149':
            windowA.yicon.setPixmap(QPixmap('greentrain.png'))
        elif block == '150':
            windowA.zicon.setPixmap(QPixmap('greentrain.png'))

    def changeVacancy(self, block):
        print("UI block", block, "is vacant")
        if block == '1' or '2'or '3':
            windowB.aicon.setPixmap(QPixmap('tracks.png'))
        elif block == '4'or '5'or '6':
            windowB.bicon.setPixmap(QPixmap('tracks.png'))
        elif block == '7' or '8' or '9' or '10' or '11' or '12':
            windowB.cicon.setPixmap(QPixmap('tracks.png'))
        elif block == '13' or '14' or '15' or '16':
            windowB.dicon.setPixmap(QPixmap('tracks.png'))
        elif block == '17' or '18' or '19' or '20':
            windowB.eicon.setPixmap(QPixmap('tracks.png'))
        elif block == '21' or '22' or '23' or '24' or '25' or '26' or '27' or '28':
            windowB.ficon.setPixmap(QPixmap('tracks.png'))
        elif block == '29' or '30' or '31' or '32':
            windowB.gicon.setPixmap(QPixmap('tracks.png'))
        elif block == '33' or '34' or '35':
            windowB.hicon.setPixmap(QPixmap('tracks.png'))
        elif block == '36' or '37' or '38' or '39' or '40' or '41' or '42' or '43' or '44' or '45' or '46' or '47' or '48' or '49' or '50' or '44' or '45' or '46' or '47' or '48' or '49' or '50'or '51' or '52' or '53' or '54' or '55' or '56' or '57':
            windowB.iicon.setPixmap(QPixmap('tracks.png'))
        elif block == '58' or '59' or '60' or '61' or '62':
            windowB.jicon.setPixmap(QPixmap('tracks.png'))
        elif block == '63' or '64' or '65' or '67' or '68':
            windowB.kicon.setPixmap(QPixmap('tracks.png'))
        elif block == '69' or '70' or '71' or '72' or '73':
            windowB.licon.setPixmap(QPixmap('tracks.png'))
        elif block == '74' or '75' or '76':
            windowB.micon.setPixmap(QPixmap('tracks.png'))
        elif block == '77' or '78' or '79' or '80' or '81' or '83' or '84' or '85':
            windowA.nicon.setPixmap(QPixmap('tracks.png'))
        elif block == '86' or '87' or '88':
            windowA.oicon.setPixmap(QPixmap('tracks.png'))
        elif block == '89' or '90' or '91' or '92' or '93' or '94' or '95' or '96' or '97':
            windowA.picon.setPixmap(QPixmap('tracks.png'))
        elif block == '98' or '99' or '100':
            windowA.qicon.setPixmap(QPixmap('tracks.png'))
        elif block == '101':
            windowA.ricon.setPixmap(QPixmap('tracks.png'))
        elif block == '102' or '103' or '104':
            windowA.sicon.setPixmap(QPixmap('tracks.png'))
        elif block == '105' or '106' or '107' or '108' or '109':
            windowA.ticon.setPixmap(QPixmap('tracks.png'))
        elif block == '110' or '111' or '112' or '113' or '114' or '115' or '116':
            windowA.uicon.setPixmap(QPixmap('tracks.png'))
        elif block == '117' or '118' or '119' or '120' or '121':
            windowA.vicon.setPixmap(QPixmap('tracks.png'))
        elif block == '122' or '123' or '124' or '125' or '126' or '127' or '128' or '129' or '130' or '131' or '132' or '133' or '134' or '135' or '136' or '137' or '138' or '139' or '140' or '141' or '142' or '143':
            windowA.vicon.setPixmap(QPixmap('tracks.png'))
        elif block == '144' or '145' or '146':
            windowA.xicon.setPixmap(QPixmap('tracks.png'))
        elif block == '147' or '148' or '149':
            windowA.yicon.setPixmap(QPixmap('tracks.png'))
        elif block == '150':
            windowA.zicon.setPixmap(QPixmap('tracks.png'))

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

app = QtWidgets.QApplication(sys.argv)
windowA = WMainWindowA()
windowB = WMainWindowB()
windowA.show()
windowB.show()
app.exec()

#test = Ui_testpopup()
#test.show()
# class Ui_testpopup(QtWidgets.QMainWindow, Ui_testpopup):
#     def __init__(self, *args, obj=None, **kwargs):
#         super(Ui_testpopup, self).__init__(*args, **kwargs)
#         self.setupUi(self)
#         self.setWindowTitle('Block Information')

#         #set up drop down menus
#         self.sectionbox.currentTextChanged.connect(self.setBlockOptions)
        
#         #toggle lights
#         self.reda.toggled.connect(self.changeLights)
#         self.yellowa.toggled.connect(self.changeLights)
#         self.greena.toggled.connect(self.changeLights)
#         self.redb.toggled.connect(self.changeLights)
#         self.yellowb.toggled.connect(self.changeLights)
#         self.greenb.toggled.connect(self.changeLights)

#         #start with reda greenb
#         self.reda.setDown(True)
#         self.greenb.setDown(True)

#         #set up change icon
#         self.sectionbox.currentTextChanged.connect(self.setBlockOptions)
#         self.occupancybox.currentTextChanged.connect(self.changeIcon)

#         #change gates in auto
#         #self.autoC0.toggled.

#     def setBlockOptions(self):
#         content = self.sectionbox.currentText()
#         if content == 'A':
#             self.blockbox.clear()
#             self.blockbox.addItems(['1' , '2', '3'])
#         elif content == 'B':
#             self.blockbox.clear()
#             self.blockbox.addItems(['4', '5', '6'])
#         elif content == 'C':
#             self.blockbox.clear()
#             self.blockbox.addItems(['7', '8', '9'])
#         elif content == 'D':
#             self.blockbox.clear()
#             self.blockbox.addItems(['10', '11', '12'])
#         elif content == 'E':
#             self.blockbox.clear()
#             self.blockbox.addItems(['13', '14', '15'])
#         elif content == 'F':
#             self.blockbox.clear()
#             self.blockbox.addItems(['16', '17', '18', '19', '20'])
#         elif content == 'G':
#             self.blockbox.clear()
#             self.blockbox.addItems(['21', '22', '23'])
#         elif content == 'H':
#             self.blockbox.clear()
#             self.blockbox.addItems(['24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45'])
#         elif content == 'I':
#             self.blockbox.clear()
#             self.blockbox.addItems(['46', '47', '48'])
#         elif content == 'J':
#             self.blockbox.clear()
#             self.blockbox.addItems(['49', '50', '51', '52', '53', '54'])

#     def changeLights(self):
#         #gate = self.crossingbox.currentText()
#         redbuttona = self.reda.isChecked()
#         yellowbuttona = self.yellowa.isChecked()
#         greenbuttona = self.greena.isChecked()
#         redbuttonb = self.redb.isChecked()
#         yellowbuttonb = self.yellowb.isChecked()
#         greenbuttonb = self.greenb.isChecked()
#         #if gate == '1':
#         if redbuttona == True:
#             window.reda.setPixmap(QPixmap('redlight.png'))
#             window.yellowa.setPixmap(QPixmap('offlight.png'))
#             window.greena.setPixmap(QPixmap('offlight.png'))
#             window.gatepositiona.setText('Active')
#         elif yellowbuttona == True:
#             self.reda.setDown(False)
#             window.reda.setPixmap(QPixmap('offlight.png'))
#             window.yellowa.setPixmap(QPixmap('yellowlight.png'))
#             window.greena.setPixmap(QPixmap('offlight.png'))
#             window.gatepositiona.setText('Active')
#         elif greenbuttona == True:
#             self.reda.setDown(False)
#             window.reda.setPixmap(QPixmap('offlight.png'))
#             window.yellowa.setPixmap(QPixmap('offlight.png'))
#             window.greena.setPixmap(QPixmap('greenlight.png'))
#             window.gatepositiona.setText('Inactive')
#         if redbuttonb == True:
#             self.greenb.setDown(False)
#             window.redb.setPixmap(QPixmap('redlight.png'))
#             window.yellowb.setPixmap(QPixmap('offlight.png'))
#             window.greenb.setPixmap(QPixmap('offlight.png'))
#             window.gatepositionb.setText('Active')
#         elif yellowbuttonb == True:
#             self.greenb.setDown(False)
#             window.redb.setPixmap(QPixmap('offlight.png'))
#             window.yellowb.setPixmap(QPixmap('yellowlight.png'))
#             window.greenb.setPixmap(QPixmap('offlight.png'))
#             window.gatepositionb.setText('Active')
#         elif greenbuttonb == True:
#             window.redb.setPixmap(QPixmap('offlight.png'))
#             window.yellowb.setPixmap(QPixmap('offlight.png'))
#             window.greenb.setPixmap(QPixmap('greenlight.png'))
#             window.gatepositionb.setText('Inactive')

#     def changeIcon(self): #laurens
#         section = self.sectionbox.currentText()
#         block = self.blockbox.currentText()
#         occupation = self.occupancybox.currentText()
#         if section == 'A':
#             if occupation == 'Occupied':
#                 window.aicon.setPixmap(QPixmap('greentrain.png'))
#                 window.bicon.setPixmap(QPixmap('redtracks.png'))
#                 window.cicon.setPixmap(QPixmap('redtracks.png'))
#                 #counts = counts + 1
#             else:
#                 window.aicon.setPixmap(QPixmap('tracks.png'))
#                 #counts = counts - 1
#             # if block == '1':
#             #     if occupation == "Occupied":
#             #         self.aicon.setPixmap("greentrain.png")
#             #     else:
#             #         self.aicon.setPixmap("tracks.png")
#             # elif block == '2':
#             #     if occupation == "Occupied":
#             #         self.aicon.setPixmap("greentrain.png")
#             #     else:
#             #         self.aicon.setPixmap("tracks.png")
#         elif section == 'B':
#             if occupation == 'Occupied':
#                 window.bicon.setPixmap(QPixmap('greentrain.png'))
#                 window.cicon.setPixmap(QPixmap('redtracks.png'))
#                 window.dicon.setPixmap(QPixmap('redtracks.png'))
#                 #counts = counts + 1
#             if occupation == 'Unoccupied':
#                 window.bicon.setPixmap(QPixmap('tracks.png'))
#                 #counts = counts - 1
#         elif section == 'C':
#             if occupation == 'Occupied':
#                 window.cicon.setPixmap(QPixmap('greentrain.png'))
#                 window.dicon.setPixmap(QPixmap('redtracks.png'))
#                 window.eicon.setPixmap(QPixmap('redtracks.png'))
#                 #counts = counts + 1
#             if occupation == 'Unoccupied':
#                 window.cicon.setPixmap(QPixmap('tracks.png'))
#                 #counts = counts - 1
#         elif section == 'D':
#             if occupation == 'Occupied':
#                 window.dicon.setPixmap(QPixmap('greentrain.png'))
#                 window.eicon.setPixmap(QPixmap('redtracks.png'))
#                 window.ficon.setPixmap(QPixmap('redtracks.png'))
#             if occupation == 'Unoccupied':
#                 window.dicon.setPixmap(QPixmap('tracks.png'))
#         elif section == 'E':
#             if occupation == 'Occupied':
#                 window.eicon.setPixmap(QPixmap('greentrain.png'))
#                 window.ficon.setPixmap(QPixmap('redtracks.png'))
#                 window.gicon.setPixmap(QPixmap('redtracks.png'))
#             if occupation == 'Unoccupied':
#                 window.eicon.setPixmap(QPixmap('tracks.png'))
#         elif section == 'F':
#             if occupation == 'Occupied':
#                 window.ficon.setPixmap(QPixmap('greentrain.png'))
#                 window.gicon.setPixmap(QPixmap('redtracks.png'))
#                 window.hicon.setPixmap(QPixmap('redtracks.png'))
#             if occupation == 'Unoccupied':
#                 window.ficon.setPixmap(QPixmap('tracks.png'))
#         elif section == 'G':
#             if occupation == 'Occupied':
#                 window.gicon.setPixmap(QPixmap('greentrain.png'))
#                 window.hicon.setPixmap(QPixmap('redtracks.png'))
#                 window.iicon.setPixmap(QPixmap('redtracks.png'))
#             if occupation == 'Unoccupied':
#                 window.gicon.setPixmap(QPixmap('tracks.png'))
#         elif section == 'H':
#             if occupation == 'Occupied':
#                 window.hicon.setPixmap(QPixmap('greentrain.png'))
#                 window.iicon.setPixmap(QPixmap('redtracks.png'))
#                 window.jicon.setPixmap(QPixmap('redtracks.png'))
#             if occupation == 'Unoccupied':
#                 window.hicon.setPixmap(QPixmap('tracks.png'))
#         elif section == 'I':
#             if occupation == 'Occupied':
#                 window.iicon.setPixmap(QPixmap('greentrain.png'))
#                 window.jicon.setPixmap(QPixmap('redtracks.png'))
#             if occupation == 'Unoccupied':
#                 window.iicon.setPixmap(QPixmap('tracks.png'))
#         elif section == 'J':
#             if occupation == 'Occupied':
#                 window.jicon.setPixmap(QPixmap('greentrain.png'))
#             if occupation == 'Unoccupied':
#                 window.jicon.setPixmap(QPixmap('tracks.png'))
    





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