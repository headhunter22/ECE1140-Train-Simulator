import sys
from pathlib import Path
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt, QObject
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

# MainWindowA N-Z blue
# MainWindowB A-M red


class WMainWindowA(QtWidgets.QMainWindow, Ui_MainWindowA):
    def __init__(self, *args, obj=None, **kwargs):
        super(WMainWindowA, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Wayside Main UI')

        #signals
        signals.wtowOccupancy.connect(self.changeOccupancy)
        signals.wtowVacancy.connect(self.changeVacancy)
        signals.timerTicked.connect(self.ticka)
        signals.wtowTrainCount.connect(self.activeTrains)
        
        #set all switch buttons to disabled
        self.gate20.setEnabled(False)
        self.gate21.setEnabled(False)
        self.gate50.setEnabled(False)
        self.gate51.setEnabled(False)
        self.gate60.setEnabled(False)
        self.gate61.setEnabled(False)

        #set up gate buttons
        self.maintenancemode.toggled.connect(self.maintenanceMode)
        self.automaticmode.toggled.connect(self.automaticMode)

        #switch button colors
        self.automaticmode.setDown(True)
        self.gate20.clicked.connect(lambda: self.toggleColor(self.gate20, self.gate21))
        self.gate21.setStyleSheet('background-color: SkyBlue')
        self.gate21.clicked.connect(lambda: self.toggleColor(self.gate21, self.gate20))
        self.gate20.setStyleSheet('background-color: white; color: gray')
        self.gate50.clicked.connect(lambda: self.toggleColor(self.gate50, self.gate51))
        self.gate51.setStyleSheet('background-color: SkyBlue')
        self.gate51.clicked.connect(lambda: self.toggleColor(self.gate51, self.gate50))
        self.gate50.setStyleSheet('background-color: white; color: gray')
        self.gate60.clicked.connect(lambda: self.toggleColor(self.gate60, self.gate61))
        self.gate61.setStyleSheet('background-color: SkyBlue')
        self.gate61.clicked.connect(lambda: self.toggleColor(self.gate61, self.gate60))
        self.gate60.setStyleSheet('background-color: white; color: gray')

        #pop up windows
        #self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))
        self.trackconfiguration.clicked.connect(self.configurationWindow)
        self.pushn.clicked.connect(lambda: self.makeSectionWindow('N'))
        self.pusho.clicked.connect(lambda: self.makeSectionWindow('O'))
        self.pushp.clicked.connect(lambda: self.makeSectionWindow('P'))
        self.pushq.clicked.connect(lambda: self.makeSectionWindow('Q'))
        self.pushr.clicked.connect(lambda: self.makeSectionWindow('R'))
        self.pushs.clicked.connect(lambda: self.makeSectionWindow('S'))
        self.pusht.clicked.connect(lambda: self.makeSectionWindow('T'))
        self.pushu.clicked.connect(lambda: self.makeSectionWindow('U'))
        self.pushv.clicked.connect(lambda: self.makeSectionWindow('V'))
        self.pushw.clicked.connect(lambda: self.makeSectionWindow('W'))
        self.pushx.clicked.connect(lambda: self.makeSectionWindow('X'))
        self.pushy.clicked.connect(lambda: self.makeSectionWindow('Y'))
        self.pushz.clicked.connect(lambda: self.makeSectionWindow('Z'))

        #active trains
        self.qicon.setPixmap(QPixmap('tracks.png'))
        self.wicon.setPixmap(QPixmap('tracks.png'))
        # self.cicon.setPixmap(QPixmap('redtracks.png'))
        # self.dicon.setPixmap(QPixmap('tracks.png'))
        # #self.eicon.setPixmap(QPixmap('redtracks.png'))
        # #self.ficon.setPixmap(QPixmap('redtracks.png'))
        # self.jicon.setPixmap(QPixmap('tracks.png'))
        counts = 0
        self.activetrains.display(counts)

        #lights
        self.reda.setPixmap(QPixmap('greenlight.png'))
        #self.greenb.setPixmap(QPixmap('greenlight.png'))

    def ticka(self, hrs, mins, secs):
        #print("wayside ticking in class a")
        timenow = str(hrs)+":"+str(mins)+":"+str(secs)
        #print(timenow)
        self.time.setText(f'{int(hrs):02d}' + ':' + f'{int(mins):02d}' + ':' + f'{int(secs):02d}')

    def maintenanceMode(self):  
        #print("in maintenance mode") 
        self.gate20.setEnabled(True)
        self.gate21.setEnabled(True)
        self.gate50.setEnabled(True)
        self.gate51.setEnabled(True)
        self.gate60.setEnabled(True)
        self.gate61.setEnabled(True)

    def automaticMode(self):
        #print("in automatic mode") 
        self.gate20.setEnabled(False)
        self.gate21.setEnabled(False)
        self.gate50.setEnabled(False)
        self.gate51.setEnabled(False)
        self.gate60.setEnabled(False)
        self.gate61.setEnabled(False)

    def configurationWindow(self):
        self.trackconfiguration.clicked.connect(self.runParser)

    def runParser(self):
        PLCParser.parse(self)

    def makeSectionWindow(self, whichsection):
        self.bl = Ui_Section()
        self.bl.sectionname.setText("Section "+ whichsection)
        
        image = QLabel()
        pic = QPixmap('tracks.png')
        image.setPixmap(pic.scaled(50, 50))
        image1 = QLabel()
        pic = QPixmap('tracks.png')
        image1.setPixmap(pic.scaled(50, 50))
        image2 = QLabel()
        pic = QPixmap('tracks.png')
        image2.setPixmap(pic.scaled(50, 50))
        image3 = QLabel()
        pic = QPixmap('tracks.png')
        image3.setPixmap(pic.scaled(50, 50))
        image4 = QLabel()
        pic = QPixmap('tracks.png')
        image4.setPixmap(pic.scaled(50, 50))
        image5 = QLabel()
        pic = QPixmap('tracks.png')
        image5.setPixmap(pic.scaled(50, 50))
        image6 = QLabel()
        pic = QPixmap('tracks.png')
        image6.setPixmap(pic.scaled(50, 50))
        image7 = QLabel()
        pic = QPixmap('tracks.png')
        image7.setPixmap(pic.scaled(50, 50))
        image8 = QLabel()
        pic = QPixmap('tracks.png')
        image8.setPixmap(pic.scaled(50, 50))
        image9 = QLabel()
        pic = QPixmap('tracks.png')
        image9.setPixmap(pic.scaled(50, 50))
        image10 = QLabel()
        pic = QPixmap('tracks.png')
        image10.setPixmap(pic.scaled(50, 50))
        image11 = QLabel()
        pic = QPixmap('tracks.png')
        image11.setPixmap(pic.scaled(50, 50))
        image12 = QLabel()
        pic = QPixmap('tracks.png')
        image12.setPixmap(pic.scaled(50, 50))
        image13 = QLabel()
        pic = QPixmap('tracks.png')
        image13.setPixmap(pic.scaled(50, 50))
        image14 = QLabel()
        pic = QPixmap('tracks.png')
        image14.setPixmap(pic.scaled(50, 50))
        image15 = QLabel()
        pic = QPixmap('tracks.png')
        image15.setPixmap(pic.scaled(50, 50))
        image16 = QLabel()
        pic = QPixmap('tracks.png')
        image16.setPixmap(pic.scaled(50, 50))
        image17 = QLabel()
        pic = QPixmap('tracks.png')
        image17.setPixmap(pic.scaled(50, 50))
        self.bl.bicon.setPixmap(QPixmap('tracks.png'))
        self.bl.bicon.setPixmap(QPixmap('tracks.png'))
        switch = QLabel("X")
        switch2 = QLabel("X")

        if whichsection == 'N':
            #'77' or '78' or '79' or '80' or '81' or '83' or '84' or '85':
            self.bl.label_5.setText('77')
            self.bl.gridLayout.addWidget(switch, 1,2)
            switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.label_6.setText('78')
            self.bl.label_7.setText('79')
            self.bl.label_8.setText('80')
            self.bl.label_9.setText('81')
            label_10 = QLabel('82')
            self.bl.gridLayout.addWidget(label_10, 6,0)
            label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image,6,1)
            label_11 = QLabel('83')
            self.bl.gridLayout.addWidget(label_11, 7,0)
            label_11.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image2,7,1)
            label_12 = QLabel('84')
            self.bl.gridLayout.addWidget(label_12, 8,0)
            label_12.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image3,8,1)
            label_13 = QLabel('85')
            self.bl.gridLayout.addWidget(label_13, 9,0)
            label_13.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image4,9,1)
            self.bl.gridLayout.addWidget(switch2, 9,2)
            switch2.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.show()
        elif whichsection == 'O':
            #'86' or '87' or '88':
            self.bl.label_5.setText('86')
            self.bl.gridLayout.addWidget(switch, 1,2)
            switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.label_6.setText('87')
            self.bl.label_7.setText('88')
            self.bl.label_8.hide()
            self.bl.dicon.hide()
            self.bl.label_9.hide()
            self.bl.eicon.hide()
            self.bl.show()
        elif whichsection == 'P':
            #'89' or '90' or '91' or '92' or '93' or '94' or '95' or '96' or '97':
            self.bl.label_5.setText('89')
            self.bl.label_6.setText('90')
            self.bl.label_7.setText('91')
            self.bl.label_8.setText('92')
            self.bl.label_9.setText('93')
            label_10 = QLabel('94')
            self.bl.gridLayout.addWidget(label_10, 6,0)
            label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image,6,1)
            label_11 = QLabel('95')
            self.bl.gridLayout.addWidget(label_11, 7,0)
            label_11.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image2,7,1)
            label_12 = QLabel('96')
            self.bl.gridLayout.addWidget(label_12, 8,0)
            label_12.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image3,8,1)
            label_13 = QLabel('97')
            self.bl.gridLayout.addWidget(label_13, 9,0)
            label_13.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image4,9,1)
            self.bl.show()
        elif whichsection == 'Q':
            #'98' or '99' or '100':
            self.bl.label_5.setText('98')
            self.bl.label_6.setText('99')
            self.bl.label_7.setText('100')
            self.bl.gridLayout.addWidget(switch, 3,2)
            switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.label_8.hide()
            self.bl.dicon.hide()
            self.bl.label_9.hide()
            self.bl.eicon.hide()
            self.bl.show()
        elif whichsection == 'R':
            #'101':
            self.bl.label_5.setText('101')
            self.bl.gridLayout.addWidget(switch, 1,2)
            switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.label_6.hide()
            self.bl.bicon.hide()
            self.bl.label_7.hide()
            self.bl.cicon.hide()
            self.bl.label_8.hide()
            self.bl.dicon.hide()
            self.bl.label_9.hide()
            self.bl.eicon.hide()
            self.bl.show()
        elif whichsection == 'S':
            #'102' or '103' or '104':
            self.bl.label_5.setText('102')
            self.bl.label_6.setText('103')
            self.bl.label_7.setText('104')
            self.bl.label_8.hide()
            self.bl.dicon.hide()
            self.bl.label_9.hide()
            self.bl.eicon.hide()
            self.bl.show()
        elif whichsection == 'T':
            #'105' or '106' or '107' or '108' or '109':
            self.bl.label_5.setText('105')
            self.bl.label_6.setText('106')
            self.bl.label_7.setText('107')
            self.bl.label_8.setText('108')
            self.bl.label_9.setText('109')
            self.bl.show()
        elif whichsection == 'U':
            #'110' or '111' or '112' or '113' or '114' or '115' or '116':
            self.bl.label_5.setText('110')
            self.bl.label_6.setText('111')
            self.bl.label_7.setText('112')
            self.bl.label_8.setText('113')
            self.bl.label_9.setText('114')
            label_10 = QLabel('115')
            self.bl.gridLayout.addWidget(label_10, 6,0)
            label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image,6,1)
            label_11 = QLabel('116')
            self.bl.gridLayout.addWidget(label_11, 7,0)
            label_11.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image2,7,1)
            self.bl.show()
        elif whichsection == 'V':
            #'117' or '118' or '119' or '120' or '121':
            self.bl.label_5.setText('117')
            self.bl.label_6.setText('118')
            self.bl.label_7.setText('119')
            self.bl.label_8.setText('120')
            self.bl.label_9.setText('121')
            self.bl.show()
        elif whichsection == 'W':
            #'122' or '123' or '124' or '125' or '126' or '127' or '128' or '129' or '130' 
            # or '131' or '132' or '133' or '134' or '135' or '136' or '137' or '138' or '139' or '140' or '141' or '142' or '143':
            self.bl.label_5.setText('122')
            self.bl.label_6.setText('123')
            self.bl.label_7.setText('124')
            self.bl.label_8.setText('125')
            self.bl.label_9.setText('126')
            label_10 = QLabel('127')
            self.bl.gridLayout.addWidget(label_10, 6,0)
            label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image,6,1)
            label_11 = QLabel('128')
            self.bl.gridLayout.addWidget(label_11, 7,0)
            label_11.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image2,7,1)
            label_12 = QLabel('129')
            self.bl.gridLayout.addWidget(label_12, 8,0)
            label_12.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image3,8,1)
            label_13 = QLabel('130')
            self.bl.gridLayout.addWidget(label_13, 9,0)
            label_13.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image4,9,1)
            label_14 = QLabel('131')
            self.bl.gridLayout.addWidget(label_14, 10,0)
            label_14.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image5,10,1)
            label_15 = QLabel('132')
            self.bl.gridLayout.addWidget(label_15, 11,0)
            label_15.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image6,11,1)
            label_16 = QLabel('133')
            self.bl.gridLayout.addWidget(label_16, 12,0)
            label_16.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image7,12,1)
            label_17 = QLabel('134')
            self.bl.gridLayout.addWidget(label_17, 13,0)
            label_17.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image8,13,1)
            label_18 = QLabel('135')
            self.bl.gridLayout.addWidget(label_18, 14,0)
            label_18.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image9,14,1)
            label_19 = QLabel('136')
            self.bl.gridLayout.addWidget(label_19, 15,0)
            label_19.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image10,15,1)
            label_20 = QLabel('137')
            self.bl.gridLayout.addWidget(label_20, 16,0)
            label_20.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image11,16,1)
            label_21 = QLabel('138')
            self.bl.gridLayout.addWidget(label_21, 17,0)
            label_21.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image12,17,1)
            label_22 = QLabel('139')
            self.bl.gridLayout.addWidget(label_22, 18,0)
            label_22.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image13,18,1)
            label_23 = QLabel('140')
            self.bl.gridLayout.addWidget(label_23, 19,0)
            label_23.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image14,19,1)
            label_24 = QLabel('141')
            self.bl.gridLayout.addWidget(label_24, 20,0)
            label_24.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image15,20,1)
            label_25 = QLabel('142')
            self.bl.gridLayout.addWidget(label_25, 21,0)
            label_25.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image16,21,1)
            label_26 = QLabel('143')
            self.bl.gridLayout.addWidget(label_26, 22,0)
            label_26.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image17,22,1)
            self.bl.show()
        elif whichsection == 'X':
            #'144' or '145' or '146':
            self.bl.label_5.setText('144')
            self.bl.label_6.setText('145')
            self.bl.label_7.setText('146')
            self.bl.label_8.hide()
            self.bl.dicon.hide()
            self.bl.label_9.hide()
            self.bl.eicon.hide()
            self.bl.show()
        elif whichsection == 'Y':
            #'147' or '148' or '149':
            self.bl.label_5.setText('147')
            self.bl.label_6.setText('148')
            self.bl.label_7.setText('149')
            self.bl.label_8.hide()
            self.bl.dicon.hide()
            self.bl.label_9.hide()
            self.bl.eicon.hide()
            self.bl.show()
        elif whichsection == 'Z':
            #'150':
            self.bl.label_5.setText('150')
            self.bl.gridLayout.addWidget(switch, 1,2)
            switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.label_6.hide()
            self.bl.bicon.hide()
            self.bl.label_7.hide()
            self.bl.cicon.hide()
            self.bl.label_8.hide()
            self.bl.dicon.hide()
            self.bl.label_9.hide()
            self.bl.eicon.hide()
            self.bl.show()

    #function for toggle switch colors but see if you can do labels instead of buttons??
    def toggleColor(self, button1, button2):
        button1.setEnabled(False)
        button2.setEnabled(True)
        button1.setStyleSheet('background-color: SkyBlue; color: black')
        button2.setStyleSheet('background-color: white; color: gray')

    #occupation 2 blocks ahead for now
    #!!!!!! TO DO !!!!!!!!!
    def changeOccupancy(self, block):
        print("wayside a UI block", block, "is occupied")
        if block > 76 and block < 86: #== '77' or '78' or '79' or '80' or '81' or '83' or '84' or '85':
            self.nicon.setPixmap(QPixmap('greentrain.png'))
        if block > 85 and block < 89: #== '86' or '87' or '88':
            self.oicon.setPixmap(QPixmap('greentrain.png'))
        if block > 88 and block < 98: #== '89' or '90' or '91' or '92' or '93' or '94' or '95' or '96' or '97':
            self.picon.setPixmap(QPixmap('greentrain.png'))
        if block > 97 and block < 101: #== '98' or '99' or '100':
            self.qicon.setPixmap(QPixmap('greentrain.png'))
        if block > 100 and block < 102: #== '101':
            self.ricon.setPixmap(QPixmap('greentrain.png'))
        if block > 101 and block < 105: #== '102' or '103' or '104':
            self.sicon.setPixmap(QPixmap('greentrain.png'))
        if block > 104 and block < 110: #== '105' or '106' or '107' or '108' or '109':
            self.ticon.setPixmap(QPixmap('greentrain.png'))
        if block > 109 and block < 117: #== '110' or '111' or '112' or '113' or '114' or '115' or '116':
            self.uicon.setPixmap(QPixmap('greentrain.png'))
        if block > 116 and block < 122: #== '117' or '118' or '119' or '120' or '121':
            self.vicon.setPixmap(QPixmap('greentrain.png'))
        if block > 121 and block < 144: #== '122' or '123' or '124' or '125' or '126' or '127' or '128' or '129' or '130' or '131' or '132' or '133' or '134' or '135' or '136' or '137' or '138' or '139' or '140' or '141' or '142' or '143':
            self.vicon.setPixmap(QPixmap('greentrain.png'))
        if block > 143 and block < 147: #== '144' or '145' or '146':
            self.xicon.setPixmap(QPixmap('greentrain.png'))
        if block > 146 and block < 150: #== '147' or '148' or '149':
            self.yicon.setPixmap(QPixmap('greentrain.png'))
        if block > 149 and block < 151: #== '150':
            self.zicon.setPixmap(QPixmap('greentrain.png'))
        if block == 74:
            self.gate50.setStyleSheet('background-color: SkyBlue')
            self.gate51.setStyleSheet('background-color: white; color: gray')
        if block == 83:
            self.gate60.setStyleSheet('background-color: SkyBlue')
            self.gate61.setStyleSheet('background-color: white; color: gray')
        if block == 98:
            self.gate61.setStyleSheet('background-color: SkyBlue')
            self.gate60.setStyleSheet('background-color: white; color: gray')
        if block == 79:
            self.gate51.setStyleSheet('background-color: SkyBlue')
            self.gate50.setStyleSheet('background-color: white; color: gray')
        if block == 148:
            self.gate20.setStyleSheet('background-color: SkyBlue')
            self.gate21.setStyleSheet('background-color: white; color: gray')
        
        

    def changeVacancy(self, block):
        print("wayside a UI block", block, "is vacant")
        if block > 76 and block < 86: #== '77' or '78' or '79' or '80' or '81' or '83' or '84' or '85':
            self.nicon.setPixmap(QPixmap('tracks.png'))
        if block > 85 and block < 89: #== '86' or '87' or '88':
            self.oicon.setPixmap(QPixmap('tracks.png'))
        if block > 88 and block < 98: #== '89' or '90' or '91' or '92' or '93' or '94' or '95' or '96' or '97':
            self.picon.setPixmap(QPixmap('tracks.png'))
        if block > 97 and block < 101: #== '98' or '99' or '100':
            self.qicon.setPixmap(QPixmap('tracks.png'))
        if block > 100 and block < 102: #== '101':
            self.ricon.setPixmap(QPixmap('tracks.png'))
        if block > 101 and block < 105: #== '102' or '103' or '104':
            self.sicon.setPixmap(QPixmap('tracks.png'))
        if block > 104 and block < 110: #== '105' or '106' or '107' or '108' or '109':
            self.ticon.setPixmap(QPixmap('tracks.png'))
        if block > 109 and block < 117: #== '110' or '111' or '112' or '113' or '114' or '115' or '116':
            self.uicon.setPixmap(QPixmap('tracks.png'))
        if block > 116 and block < 122: #== '117' or '118' or '119' or '120' or '121':
            self.vicon.setPixmap(QPixmap('tracks.png'))
        if block > 121 and block < 144: #== '122' or '123' or '124' or '125' or '126' or '127' or '128' or '129' or '130' or '131' or '132' or '133' or '134' or '135' or '136' or '137' or '138' or '139' or '140' or '141' or '142' or '143':
            self.vicon.setPixmap(QPixmap('tracks.png'))
        if block > 143 and block < 147: #== '144' or '145' or '146':
            self.xicon.setPixmap(QPixmap('tracks.png'))
        if block > 146 and block < 150: #== '147' or '148' or '149':
            self.yicon.setPixmap(QPixmap('tracks.png'))
        if block > 149 and block < 151: #== '150':
            self.zicon.setPixmap(QPixmap('tracks.png'))

     #function for number of active trains
    #somehow counts the number of times the red train label comes up
    def activeTrains(self, counts):
        self.activetrains.display(counts)
            




# MainWindowB A-M
class WMainWindowB(QtWidgets.QMainWindow, Ui_MainWindowB):
    def __init__(self, *args, obj=None, **kwargs):
        super(WMainWindowB, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Wayside Main UI')

        #signals
        signals.wtowVacancy.connect(self.changeVacancy)
        signals.wtowOccupancy.connect(self.changeOccupancy)
        signals.timerTicked.connect(self.tickb)
        signals.wtowTrainCount.connect(self.activeTrains)
        
        

        #set all switch buttons to disabled
        self.gate10.setEnabled(False)
        self.gate11.setEnabled(False)
        self.gate20.setEnabled(False)
        self.gate21.setEnabled(False)
        self.gate30.setEnabled(False)
        self.gate31.setEnabled(False)
        self.gate40.setEnabled(False)
        self.gate41.setEnabled(False)
        self.gate50.setEnabled(False)
        self.gate51.setEnabled(False)
        self.gate60.setEnabled(False)
        self.gate61.setEnabled(False)

        #switch button colors
        self.automaticmode.setDown(True)
        self.automaticmode.setDown(True)
        self.gate10.clicked.connect(lambda: self.toggleColor(self.gate10, self.gate11))
        self.gate10.setStyleSheet('background-color: SkyBlue')
        self.gate11.clicked.connect(lambda: self.toggleColor(self.gate11, self.gate10))
        self.gate11.setStyleSheet('background-color: white; color: gray')
        self.gate20.clicked.connect(lambda: self.toggleColor(self.gate20, self.gate21))
        self.gate21.setStyleSheet('background-color: SkyBlue')
        self.gate21.clicked.connect(lambda: self.toggleColor(self.gate21, self.gate20))
        self.gate20.setStyleSheet('background-color: white; color: gray')
        self.gate30.clicked.connect(lambda: self.toggleColor(self.gate30, self.gate31))
        self.gate30.setStyleSheet('background-color: SkyBlue')
        self.gate31.clicked.connect(lambda: self.toggleColor(self.gate31, self.gate30))
        self.gate31.setStyleSheet('background-color: white; color: gray')
        self.gate40.clicked.connect(lambda: self.toggleColor(self.gate40, self.gate41))
        self.gate41.setStyleSheet('background-color: SkyBlue')
        self.gate41.clicked.connect(lambda: self.toggleColor(self.gate41, self.gate40))
        self.gate40.setStyleSheet('background-color: white; color: gray')
        self.gate50.clicked.connect(lambda: self.toggleColor(self.gate50, self.gate51))
        self.gate51.setStyleSheet('background-color: SkyBlue')
        self.gate51.clicked.connect(lambda: self.toggleColor(self.gate51, self.gate50))
        self.gate50.setStyleSheet('background-color: white; color: gray')
        self.gate60.clicked.connect(lambda: self.toggleColor(self.gate60, self.gate61))
        self.gate61.setStyleSheet('background-color: SkyBlue')
        self.gate61.clicked.connect(lambda: self.toggleColor(self.gate61, self.gate60))
        self.gate60.setStyleSheet('background-color: white; color: gray')

        #pop up windows
        self.trackconfiguration.clicked.connect(self.configurationWindow)
        self.pusha.clicked.connect(lambda: self.makeSectionWindow('A'))
        self.pushb.clicked.connect(lambda: self.makeSectionWindow('B'))
        self.pushc.clicked.connect(lambda: self.makeSectionWindow('C'))
        self.pushd.clicked.connect(lambda: self.makeSectionWindow('D'))
        self.pushe.clicked.connect(lambda: self.makeSectionWindow('E'))
        self.pushf.clicked.connect(lambda: self.makeSectionWindow('F'))
        self.pushg.clicked.connect(lambda: self.makeSectionWindow('G'))
        self.pushh.clicked.connect(lambda: self.makeSectionWindow('H'))
        self.pushi.clicked.connect(lambda: self.makeSectionWindow('I'))
        self.pushj.clicked.connect(lambda: self.makeSectionWindow('J'))
        self.pushk.clicked.connect(lambda: self.makeSectionWindow('K'))
        self.pushl.clicked.connect(lambda: self.makeSectionWindow('L'))
        self.pushm.clicked.connect(lambda: self.makeSectionWindow('M'))
        #self.pushn.clicked.connect(lambda: self.makeSectionWindow('N'))

        #set up gate buttons
        self.maintenancemode.toggled.connect(self.maintenanceMode)
        self.automaticmode.toggled.connect(self.automaticMode)

        #active trains
        self.aicon.setPixmap(QPixmap('tracks.png'))
        self.bicon.setPixmap(QPixmap('tracks.png'))
        self.cicon.setPixmap(QPixmap('tracks.png'))
        self.dicon.setPixmap(QPixmap('tracks.png'))
        #self.eicon.setPixmap(QPixmap('redtracks.png'))
        #self.ficon.setPixmap(QPixmap('redtracks.png'))
        self.jicon.setPixmap(QPixmap('tracks.png'))
        
        counts = 0
        self.activetrains.display(counts)

        #lights
        self.reda.setPixmap(QPixmap('greenlight.png'))
        #self.greenb.setPixmap(QPixmap('greenlight.png'))

    def tickb(self, hrs, mins, secs):
        #print("wayside ticking in class b")
        timenow = str(hrs)+":"+str(mins)+":"+str(secs)
        #print(timenow)
        self.time.setText(f'{int(hrs):02d}' + ':' + f'{int(mins):02d}' + ':' + f'{int(secs):02d}')

    def maintenanceMode(self):  
        #print("in maintenance mode") 
        self.gate10.setEnabled(True)
        self.gate11.setEnabled(True)
        self.gate20.setEnabled(True)
        self.gate21.setEnabled(True)
        self.gate30.setEnabled(True)
        self.gate31.setEnabled(True)
        self.gate40.setEnabled(True)
        self.gate41.setEnabled(True)
        self.gate50.setEnabled(True)
        self.gate51.setEnabled(True)
        self.gate60.setEnabled(True)
        self.gate61.setEnabled(True)

    def automaticMode(self):
        #print("in automatic mode") 
        self.gate10.setEnabled(False)
        self.gate11.setEnabled(False)
        self.gate20.setEnabled(False)
        self.gate21.setEnabled(False)
        self.gate30.setEnabled(False)
        self.gate31.setEnabled(False)
        self.gate40.setEnabled(False)
        self.gate41.setEnabled(False)
        self.gate50.setEnabled(False)
        self.gate51.setEnabled(False)
        self.gate60.setEnabled(False)
        self.gate61.setEnabled(False)

    #function for pop up window for track configuration
    def configurationWindow(self):
        self.trackconfiguration.clicked.connect(self.runParser)

    def runParser(self):
        PLCParser.parse(self)

    def makeSectionWindow(self, whichsection):
        self.bl = Ui_Section()
        self.bl.sectionname.setText("Section "+ whichsection)
        
        image = QLabel()
        pic = QPixmap('tracks.png')
        image.setPixmap(pic.scaled(50, 50))
        image1 = QLabel()
        pic = QPixmap('tracks.png')
        image1.setPixmap(pic.scaled(50, 50))
        image2 = QLabel()
        pic = QPixmap('tracks.png')
        image2.setPixmap(pic.scaled(50, 50))
        image3 = QLabel()
        pic = QPixmap('tracks.png')
        image3.setPixmap(pic.scaled(50, 50))
        image4 = QLabel()
        pic = QPixmap('tracks.png')
        image4.setPixmap(pic.scaled(50, 50))
        image5 = QLabel()
        pic = QPixmap('tracks.png')
        image5.setPixmap(pic.scaled(50, 50))
        image6 = QLabel()
        pic = QPixmap('tracks.png')
        image6.setPixmap(pic.scaled(50, 50))
        image7 = QLabel()
        pic = QPixmap('tracks.png')
        image7.setPixmap(pic.scaled(50, 50))
        image8 = QLabel()
        pic = QPixmap('tracks.png')
        image8.setPixmap(pic.scaled(50, 50))
        image9 = QLabel()
        pic = QPixmap('tracks.png')
        image9.setPixmap(pic.scaled(50, 50))
        image10 = QLabel()
        pic = QPixmap('tracks.png')
        image10.setPixmap(pic.scaled(50, 50))
        image11 = QLabel()
        pic = QPixmap('tracks.png')
        image11.setPixmap(pic.scaled(50, 50))
        image12 = QLabel()
        pic = QPixmap('tracks.png')
        image12.setPixmap(pic.scaled(50, 50))
        image13 = QLabel()
        pic = QPixmap('tracks.png')
        image13.setPixmap(pic.scaled(50, 50))
        image14 = QLabel()
        pic = QPixmap('tracks.png')
        image14.setPixmap(pic.scaled(50, 50))
        image15 = QLabel()
        pic = QPixmap('tracks.png')
        image15.setPixmap(pic.scaled(50, 50))
        image16 = QLabel()
        pic = QPixmap('tracks.png')
        image16.setPixmap(pic.scaled(50, 50))
        image17 = QLabel()
        pic = QPixmap('tracks.png')
        image17.setPixmap(pic.scaled(50, 50))
        self.bl.gridLayout.addWidget(image1, 2,1)
        self.bl.gridLayout.addWidget(image1, 2,1)
        switch = QLabel("X")
        switch2 = QLabel("X")

        if whichsection == 'A':
            #'1' or '2'or '3':
            self.bl.label_5.setText('1')
            self.bl.gridLayout.addWidget(switch, 1,2)
            switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.label_6.setText('2')
            self.bl.label_7.setText('3')
            self.bl.label_8.hide()
            self.bl.dicon.hide()
            self.bl.label_9.hide()
            self.bl.eicon.hide()
            self.bl.show()
        elif whichsection == 'B':
            #'4'or '5'or '6':
            self.bl.label_5.setText('4')
            self.bl.label_6.setText('5')
            self.bl.label_7.setText('6')
            self.bl.label_8.hide()
            self.bl.dicon.hide()
            self.bl.label_9.hide()
            self.bl.eicon.hide()
            self.bl.show()
        elif whichsection == 'C':
            #'7' or '8' or '9' or '10' or '11' or '12':
            self.bl.label_5.setText('7')
            self.bl.label_6.setText('8')
            self.bl.label_7.setText('9')
            self.bl.label_8.setText('10')
            self.bl.label_9.setText('11')
            label_10 = QLabel('12')
            label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(label_10, 6,0)
            self.bl.gridLayout.addWidget(image2,6,1)
            self.bl.gridLayout.addWidget(switch, 6,2)
            switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.show()
        elif whichsection == 'D':
            #'13' or '14' or '15' or '16':
            self.bl.label_5.setText('13')
            self.bl.label_6.setText('14')
            self.bl.label_7.setText('15')
            self.bl.label_8.setText('16')
            self.bl.label_9.hide()
            self.bl.eicon.hide()
            self.bl.show()
        elif whichsection == 'E':
            #'17' or '18' or '19' or '20':
            self.bl.label_5.setText('17')
            self.bl.label_6.setText('18')
            self.bl.label_7.setText('19')
            self.bl.label_8.setText('20')
            self.bl.label_9.hide()
            self.bl.eicon.hide()
            self.bl.show()
        elif whichsection == 'F':
            #'21' or '22' or '23' or '24' or '25' or '26' or '27' or '28':
            self.bl.label_5.setText('21')
            self.bl.label_6.setText('22')
            self.bl.label_7.setText('23')
            self.bl.label_8.setText('24')
            self.bl.label_9.setText('25')
            label_10 = QLabel('26')
            self.bl.gridLayout.addWidget(label_10, 6,0)
            label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image,6,1)
            label_11 = QLabel('27')
            self.bl.gridLayout.addWidget(label_11, 7,0)
            label_11.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image2,7,1)
            label_12 = QLabel('28')
            self.bl.gridLayout.addWidget(label_12, 8,0)
            label_12.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image3,8,1)
            self.bl.gridLayout.addWidget(switch, 8,2)
            switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.show()
        elif whichsection == 'G':
            #'29' or '30' or '31' or '32':
            self.bl.label_5.setText('29')
            self.bl.gridLayout.addWidget(switch, 1,2)
            switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.label_6.setText('30')
            self.bl.label_7.setText('31')
            self.bl.label_8.setText('32')
            self.bl.label_9.hide()
            self.bl.eicon.hide()
            self.bl.show()
        elif whichsection == 'H':
            #'33' or '34' or '35':
            self.bl.label_5.setText('33')
            self.bl.label_6.setText('34')
            self.bl.label_7.setText('35')
            self.bl.label_8.hide()
            self.bl.dicon.hide()
            self.bl.label_9.hide()
            self.bl.eicon.hide()
            self.bl.show()
        elif whichsection == 'I':
            #'36' or '37' or '38' or '39' or '40' or '41' or '42' or '43' or '44' or '45' or '46' or '47' or '48' or '49' or '50' or '44' or '45' or '46' or '47' or '48' or '49' or '50'or '51' or '52' or '53' or '54' or '55' or '56' or '57':
            self.bl.label_5.setText('36')
            self.bl.label_6.setText('37')
            self.bl.label_7.setText('38')
            self.bl.label_8.setText('39')
            self.bl.label_9.setText('40')
            label_10 = QLabel('41')
            self.bl.gridLayout.addWidget(label_10, 6,0)
            label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image,6,1)
            label_11 = QLabel('42')
            self.bl.gridLayout.addWidget(label_11, 7,0)
            label_11.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image2,7,1)
            label_12 = QLabel('43')
            self.bl.gridLayout.addWidget(label_12, 8,0)
            label_12.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image3,8,1)
            self.bl.gridLayout.addWidget(switch, 1,2)
            switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            label_13 = QLabel('44')
            self.bl.gridLayout.addWidget(label_13, 9,0)
            label_13.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image4,9,1)
            label_14 = QLabel('45')
            self.bl.gridLayout.addWidget(label_14, 10,0)
            label_14.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image5,10,1)
            label_15 = QLabel('46')
            self.bl.gridLayout.addWidget(label_15, 11,0)
            label_15.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image6,11,1)
            label_16 = QLabel('47')
            self.bl.gridLayout.addWidget(label_16, 12,0)
            label_16.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image7,12,1)
            label_17 = QLabel('48')
            self.bl.gridLayout.addWidget(label_17, 13,0)
            label_17.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image8,13,1)
            label_18 = QLabel('49')
            self.bl.gridLayout.addWidget(label_18, 14,0)
            label_18.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image9,14,1)
            label_19 = QLabel('50')
            self.bl.gridLayout.addWidget(label_19, 15,0)
            label_19.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image10,15,1)
            label_20 = QLabel('51')
            self.bl.gridLayout.addWidget(label_20, 16,0)
            label_20.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image11,16,1)
            label_21 = QLabel('52')
            self.bl.gridLayout.addWidget(label_21, 17,0)
            label_21.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image12,17,1)
            label_22 = QLabel('53')
            self.bl.gridLayout.addWidget(label_22, 18,0)
            label_22.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image13,18,1)
            label_23 = QLabel('54')
            self.bl.gridLayout.addWidget(label_23, 19,0)
            label_23.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image14,19,1)
            label_24 = QLabel('55')
            self.bl.gridLayout.addWidget(label_24, 20,0)
            label_24.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image15,20,1)
            label_25 = QLabel('56')
            self.bl.gridLayout.addWidget(label_25, 21,0)
            label_25.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image16,21,1)
            label_26 = QLabel('57')
            self.bl.gridLayout.addWidget(label_26, 22,0)
            label_26.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.gridLayout.addWidget(image17,22,1)
            self.bl.gridLayout.addWidget(switch, 22,2)
            switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.show()
        elif whichsection == 'J':
            #'58' or '59' or '60' or '61' or '62':
            self.bl.label_5.setText('58')
            self.bl.gridLayout.addWidget(switch, 2,2)
            switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.label_6.setText('59')
            self.bl.label_7.setText('60')
            self.bl.label_8.setText('61')
            self.bl.label_9.setText('61')
            self.bl.gridLayout.addWidget(switch2, 5,2)
            switch2.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.show()
        elif whichsection == 'K':
            #'63' or '64' or '65' or '67' or '68':
            self.bl.label_5.setText('62')
            self.bl.gridLayout.addWidget(switch, 1,2)
            switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.label_6.setText('63')
            self.bl.label_7.setText('64')
            self.bl.label_8.setText('64')
            self.bl.label_9.setText('66')
            self.bl.show()
        elif whichsection == 'L':
            #'69' or '70' or '71' or '72' or '73':
            self.bl.label_5.setText('69')
            self.bl.label_6.setText('70')
            self.bl.label_7.setText('71')
            self.bl.label_8.setText('72')
            self.bl.label_9.setText('73')
            self.bl.show()
        elif whichsection == 'M':
            #'74' or '75' or '76':
            self.bl.label_5.setText('74')
            self.bl.label_6.setText('75')
            self.bl.label_7.setText('76')
            self.bl.label_8.setText('77')
            self.bl.gridLayout.addWidget(switch, 4,2)
            switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
            self.bl.label_9.hide()
            self.bl.eicon.hide()
            self.bl.show()
        

    #function for toggle switch colors but see if you can do labels instead of buttons??
    def toggleColor(self,button1, button2):
        button1.setEnabled(False)
        button2.setEnabled(True)
        button1.setStyleSheet('background-color: SkyBlue; color: black')
        button2.setStyleSheet('background-color: white; color: gray')

    #occupation 2 blocks ahead for now
    #!!!!!! TO DO !!!!!!!!!
    def changeOccupancy(self, block):
        print("wayside b UI block", block, "is occupied")
        if block > 0 and block < 4:
            self.aicon.setPixmap(QPixmap('greentrain.png'))
        if block > 3 and block < 7: #== '4'or '5'or '6':
            self.bicon.setPixmap(QPixmap('greentrain.png'))
        if block > 6 and block < 13: #== '7' or '8' or '9' or '10' or '11' or '12':
            self.cicon.setPixmap(QPixmap('greentrain.png'))
        if block > 12 and block < 16: #== '13' or '14' or '15' or '16':
            self.dicon.setPixmap(QPixmap('greentrain.png'))
        if block > 16 and block < 21: #== '17' or '18' or '19' or '20':
            self.eicon.setPixmap(QPixmap('greentrain.png'))
        if block > 20 and block < 29: #== '21' or '22' or '23' or '24' or '25' or '26' or '27' or '28':
            self.ficon.setPixmap(QPixmap('greentrain.png'))
        if block > 28 and block < 33: #== '29' or '30' or '31' or '32':
            self.gicon.setPixmap(QPixmap('greentrain.png'))
        if block > 32 and block < 36: #== '33' or '34' or '35':
            self.hicon.setPixmap(QPixmap('greentrain.png'))
        if block > 35 and block < 58: #== '36' or '37' or '38' or '39' or '40' or '41' or '42' or '43' or '44' or '45' or '46' or '47' or '48' or '49' or '50' or '44' or '45' or '46' or '47' or '48' or '49' or '50'or '51' or '52' or '53' or '54' or '55' or '56' or '57':
            self.iicon.setPixmap(QPixmap('greentrain.png'))
        if block > 57 and block < 63: #== '58' or '59' or '60' or '61' or '62':
            self.jicon.setPixmap(QPixmap('greentrain.png'))
        if block > 62 and block < 69: #== '63' or '64' or '65' or '67' or '68':
            self.kicon.setPixmap(QPixmap('greentrain.png'))
        if block > 68 and block < 74: #== '69' or '70' or '71' or '72' or '73':
            self.licon.setPixmap(QPixmap('greentrain.png'))
        if block > 73 and block < 77: #== '74' or '75' or '76':
            self.micon.setPixmap(QPixmap('greentrain.png'))
        if block == 74:
            self.gate50.setStyleSheet('background-color: SkyBlue')
            self.gate51.setStyleSheet('background-color: white; color: gray')
        if block == 83:
            self.gate60.setStyleSheet('background-color: SkyBlue')
            self.gate61.setStyleSheet('background-color: white; color: gray')
        if block == 98:
            self.gate61.setStyleSheet('background-color: SkyBlue')
            self.gate60.setStyleSheet('background-color: white; color: gray')
        if block == 79:
            self.gate51.setStyleSheet('background-color: SkyBlue')
            self.gate50.setStyleSheet('background-color: white; color: gray')
        if block == 148:
            self.gate20.setStyleSheet('background-color: SkyBlue')
            self.gate21.setStyleSheet('background-color: white; color: gray')
        if block == 11:
            self.gate11.setStyleSheet('background-color: SkyBlue')
            self.gate10.setStyleSheet('background-color: white; color: gray')
        if block == 2:
            self.gate10.setStyleSheet('background-color: SkyBlue')
            self.gate11.setStyleSheet('background-color: white; color: gray')
        if block == 27:
            self.gate21.setStyleSheet('background-color: SkyBlue')
            self.gate20.setStyleSheet('background-color: white; color: gray')
        if block == 55:
            self.gate31.setStyleSheet('background-color: SkyBlue')
            self.gate30.setStyleSheet('background-color: white; color: gray')

    def changeVacancy(self, block):
        print("wayside b UI block", block, "is vacant")
        if block > 0 and block < 4:
            self.aicon.setPixmap(QPixmap('tracks.png'))
        if block > 3 and block < 7: #== '4'or '5'or '6':
            self.bicon.setPixmap(QPixmap('tracks.png'))
        if block > 6 and block < 13: #== '7' or '8' or '9' or '10' or '11' or '12':
            self.cicon.setPixmap(QPixmap('tracks.png'))
        if block > 12 and block < 16: #== '13' or '14' or '15' or '16':
            self.dicon.setPixmap(QPixmap('tracks.png'))
        if block > 16 and block < 21: #== '17' or '18' or '19' or '20':
            self.eicon.setPixmap(QPixmap('tracks.png'))
        if block > 20 and block < 29: #== '21' or '22' or '23' or '24' or '25' or '26' or '27' or '28':
            self.ficon.setPixmap(QPixmap('tracks.png'))
        if block > 28 and block < 33: #== '29' or '30' or '31' or '32':
            self.gicon.setPixmap(QPixmap('tracks.png'))
        if block > 32 and block < 36: #== '33' or '34' or '35':
            self.hicon.setPixmap(QPixmap('tracks.png'))
        if block > 35 and block < 58: #== '36' or '37' or '38' or '39' or '40' or '41' or '42' or '43' or '44' or '45' or '46' or '47' or '48' or '49' or '50' or '44' or '45' or '46' or '47' or '48' or '49' or '50'or '51' or '52' or '53' or '54' or '55' or '56' or '57':
            self.iicon.setPixmap(QPixmap('tracks.png'))
        if block > 57 and block < 63: #== '58' or '59' or '60' or '61' or '62':
            self.jicon.setPixmap(QPixmap('tracks.png'))
        if block > 62 and block < 69: #== '63' or '64' or '65' or '67' or '68':
            self.kicon.setPixmap(QPixmap('tracks.png'))
        if block > 68 and block < 74: #== '69' or '70' or '71' or '72' or '73':
            self.licon.setPixmap(QPixmap('tracks.png'))
        if block > 73 and block < 77: #== '74' or '75' or '76':
            self.micon.setPixmap(QPixmap('tracks.png'))

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
#funcA = WaysideUIFunctions(windowA)
#funcB = WaysideUIFunctions(windowB)
# windowA.show()
# windowB.show()
# app.exec()

class WaysideUIFunctions(QObject):
    # def __init__(self, window):
    #     super().__init__()
    #     #signals.waysideUpdateOccupancy.connect(WaysideUIFunctions.changeOccupancy)
    #     #signals.waysideUpdateVacancy.connect(WaysideUIFunctions.changeVacancy)
    #     signals.wtowOccupancy.connect(WaysideUIFunctions.changeOccupancy)
    #     signals.wtowVacancy.connect(WaysideUIFunctions.changeVacancy)
    #     signals.timerTicked.connect(WaysideUIFunctions.tick)
    # #function for maintenance mode 

    # def tick(hrs, mins, secs):
    #     print("wayside ticking")
        
    #     timenow = str(hrs)+":"+str(mins)+":"+str(secs)
    #     print(timenow)
    #     windowA.time.setText(timenow)
    #     windowB.time.setText(timenow)
    #     #windowA.time.setText(f'{int(hrs):02d}' + ':' + f'{int(mins):02d}' + ':' + f'{int(secs):02d}')
    #     #windowB.time.setText(f'{int(hrs):02d}' + ':' + f'{int(mins):02d}' + ':' + f'{int(secs):02d}')

    # def maintenanceMode(self):  
    #     #print("in maintenance mode") 
    #     windowA.ca.setEnabled(True)
    #     windowA.cb.setEnabled(True)
    #     windowA.ga.setEnabled(True)
    #     windowA.gb.setEnabled(True)
    #     windowB.ca.setEnabled(True)
    #     windowB.cb.setEnabled(True)
    #     windowB.ga.setEnabled(True)
    #     windowB.gb.setEnabled(True)

    # def automaticMode(self):
    #     #print("in automatic mode") 
    #     windowA.ca.setEnabled(False)
    #     windowA.cb.setEnabled(False)
    #     windowA.ga.setEnabled(False)
    #     windowA.gb.setEnabled(False)
    #     windowB.ca.setEnabled(False)
    #     windowB.cb.setEnabled(False)
    #     windowB.ga.setEnabled(False)
    #     windowB.gb.setEnabled(False)

    # #function for pop up window for track configuration
    # def configurationWindow(self):
    #     #self.tc = TrackConfig()
    #     windowA.trackconfiguration.clicked.connect(WaysideUIFunctions.runParser)
    #     windowB.trackconfiguration.clicked.connect(WaysideUIFunctions.runParser)
    #     #self.tc.show()

    # def runParser(self):
    #     PLCParser.parse(self)

    # #function for pop up window for seeing blocks in sections
    # def makeSectionWindow(self, whichsection):
    #     windowA.bl = Ui_Section()
    #     windowB.bl = Ui_Section()
    #     windowA.bl.sectionname.setText("Section "+ whichsection)
    #     windowB.bl.sectionname.setText("Section "+ whichsection)
        
    #     image = QLabel()
    #     pic = QPixmap('tracks.png')
    #     image.setPixmap(pic.scaled(50, 50))
    #     windowB.bl.gridLayout.addWidget(image, 2,1)
    #     windowB.bl.gridLayout.addWidget(image, 2,1)

    #     if whichsection == 'A':
    #         #'1' or '2'or '3':
    #         windowB.bl.label_5.setText('1')
    #         windowB.bl.label_6.setText('2')
    #         windowB.bl.label_7.setText('3')
    #         windowB.bl.label_8.hide()
    #         windowB.bl.dicon.hide()
    #         windowB.bl.label_9.hide()
    #         windowB.bl.eicon.hide()
    #         windowB.bl.show()
    #     elif whichsection == 'B':
    #         #'4'or '5'or '6':
    #         windowB.bl.label_5.setText('4')
    #         windowB.bl.label_6.setText('5')
    #         windowB.bl.label_7.setText('6')
    #         windowB.bl.label_8.hide()
    #         windowB.bl.dicon.hide()
    #         windowB.bl.label_9.hide()
    #         windowB.bl.eicon.hide()
    #         windowB.bl.show()
    #     elif whichsection == 'C':
    #         #'7' or '8' or '9' or '10' or '11' or '12':
    #         windowB.bl.label_5.setText('7')
    #         windowB.bl.label_6.setText('8')
    #         windowB.bl.label_7.setText('9')
    #         windowB.bl.label_8.setText('10')
    #         windowB.bl.label_9.setText('11')
    #         label_10 = QLabel('12')
    #         label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowB.bl.gridLayout.addWidget(label_10, 6,0)
    #         windowB.bl.gridLayout.addWidget(image,6,1)
    #         windowB.bl.show()
    #     elif whichsection == 'D':
    #         #'13' or '14' or '15' or '16':
    #         windowB.bl.label_5.setText('13')
    #         windowB.bl.label_6.setText('14')
    #         windowB.bl.label_7.setText('15')
    #         windowB.bl.label_8.setText('16')
    #         windowB.bl.label_9.hide()
    #         windowB.bl.eicon.hide()
    #         windowB.bl.show()
    #     elif whichsection == 'E':
    #         #'17' or '18' or '19' or '20':
    #         windowB.bl.label_5.setText('17')
    #         windowB.bl.label_6.setText('18')
    #         windowB.bl.label_7.setText('19')
    #         windowB.bl.label_8.setText('20')
    #         windowB.bl.label_9.hide()
    #         windowB.bl.eicon.hide()
    #         windowB.bl.show()
    #     elif whichsection == 'F':
    #         #'21' or '22' or '23' or '24' or '25' or '26' or '27' or '28':
    #         windowB.bl.label_5.setText('21')
    #         windowB.bl.label_6.setText('22')
    #         windowB.bl.label_7.setText('23')
    #         windowB.bl.label_8.setText('24')
    #         windowB.bl.label_9.setText('25')
    #         label_10 = QLabel('26')
    #         windowB.bl.gridLayout.addWidget(label_10, 6,0)
    #         label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowB.bl.gridLayout.addWidget(image,6,1)
    #         label_11 = QLabel('27')
    #         windowB.bl.gridLayout.addWidget(label_11, 7,0)
    #         label_11.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowB.bl.gridLayout.addWidget(image,7,1)
    #         label_12 = QLabel('28')
    #         windowB.bl.gridLayout.addWidget(label_12, 8,0)
    #         label_12.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowB.bl.gridLayout.addWidget(image,8,1)
    #         windowB.bl.show()
    #     elif whichsection == 'G':
    #         #'29' or '30' or '31' or '32':
    #         windowB.bl.label_5.setText('29')
    #         windowB.bl.label_6.setText('30')
    #         windowB.bl.label_7.setText('31')
    #         windowB.bl.label_8.setText('32')
    #         windowB.bl.label_9.hide()
    #         windowB.bl.eicon.hide()
    #         windowB.bl.show()
    #     elif whichsection == 'H':
    #         #'33' or '34' or '35':
    #         windowB.bl.label_5.setText('33')
    #         windowB.bl.label_6.setText('34')
    #         windowB.bl.label_7.setText('35')
    #         windowB.bl.label_8.hide()
    #         windowB.bl.dicon.hide()
    #         windowB.bl.label_9.hide()
    #         windowB.bl.eicon.hide()
    #         windowB.bl.show()
    #     elif whichsection == 'I':
    #         #'36' or '37' or '38' or '39' or '40' or '41' or '42' or '43' or '44' or '45' or '46' or '47' or '48' or '49' or '50' or '44' or '45' or '46' or '47' or '48' or '49' or '50'or '51' or '52' or '53' or '54' or '55' or '56' or '57':
    #         windowB.iicon.setPixmap(QPixmap('greentrain.png'))
    #         windowB.bl.show()
    #     elif whichsection == 'J':
    #         #'58' or '59' or '60' or '61' or '62':
    #         windowB.bl.label_5.setText('58')
    #         windowB.bl.label_6.setText('59')
    #         windowB.bl.label_7.setText('60')
    #         windowB.bl.label_8.setText('61')
    #         windowB.bl.label_9.setText('61')
    #         windowB.bl.show()
    #     elif whichsection == 'K':
    #         #'63' or '64' or '65' or '67' or '68':
    #         windowB.bl.label_5.setText('62')
    #         windowB.bl.label_6.setText('63')
    #         windowB.bl.label_7.setText('64')
    #         windowB.bl.label_8.setText('64')
    #         windowB.bl.label_9.setText('66')
    #         windowB.bl.show()
    #     elif whichsection == 'L':
    #         #'69' or '70' or '71' or '72' or '73':
    #         windowB.bl.label_5.setText('69')
    #         windowB.bl.label_6.setText('70')
    #         windowB.bl.label_7.setText('71')
    #         windowB.bl.label_8.setText('72')
    #         windowB.bl.label_9.setText('73')
    #         windowB.bl.show()
    #     elif whichsection == 'M':
    #         #'74' or '75' or '76':
    #         windowB.bl.label_5.setText('74')
    #         windowB.bl.label_6.setText('75')
    #         windowB.bl.label_7.setText('76')
    #         windowB.bl.label_8.setText('77')
    #         windowB.bl.label_9.hide()
    #         windowB.bl.eicon.hide()
    #         windowB.bl.show()
    #     elif whichsection == 'N':
    #         #'77' or '78' or '79' or '80' or '81' or '83' or '84' or '85':
    #         windowB.bl.label_5.setText('77')
    #         windowB.bl.label_6.setText('78')
    #         windowB.bl.label_7.setText('79')
    #         windowB.bl.label_8.setText('80')
    #         windowB.bl.label_9.setText('81')
    #         label_10 = QLabel('82')
    #         windowB.bl.gridLayout.addWidget(label_10, 6,0)
    #         label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,6,1)
    #         label_11 = QLabel('83')
    #         windowB.bl.gridLayout.addWidget(label_11, 7,0)
    #         label_11.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,7,1)
    #         #windowB.bl.label_5.setText('82')
    #         windowB.bl.show()
    #     elif whichsection == 'O':
    #         #'86' or '87' or '88':
    #         windowA.bl.label_5.setText('86')
    #         windowA.bl.label_6.setText('87')
    #         windowA.bl.label_7.setText('88')
    #         windowA.bl.label_8.hide()
    #         windowA.bl.dicon.hide()
    #         windowA.bl.label_9.hide()
    #         windowA.bl.eicon.hide()
    #         windowA.bl.show()
    #     elif whichsection == 'P':
    #         #'89' or '90' or '91' or '92' or '93' or '94' or '95' or '96' or '97':
    #         windowA.bl.label_5.setText('89')
    #         windowA.bl.label_6.setText('90')
    #         windowA.bl.label_7.setText('91')
    #         windowA.bl.label_8.setText('92')
    #         windowA.bl.label_9.setText('93')
    #         label_10 = QLabel('94')
    #         windowA.bl.gridLayout.addWidget(label_10, 6,0)
    #         label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,6,1)
    #         label_11 = QLabel('95')
    #         windowA.bl.gridLayout.addWidget(label_11, 7,0)
    #         label_11.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,7,1)
    #         label_12 = QLabel('96')
    #         windowA.bl.gridLayout.addWidget(label_12, 8,0)
    #         label_12.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,8,1)
    #         label_13 = QLabel('97')
    #         windowA.bl.gridLayout.addWidget(label_13, 9,0)
    #         label_13.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,9,1)
    #         windowA.bl.show()
    #     elif whichsection == 'Q':
    #         #'98' or '99' or '100':
    #         windowA.bl.label_5.setText('98')
    #         windowA.bl.label_6.setText('99')
    #         windowA.bl.label_7.setText('100')
    #         windowA.bl.label_8.hide()
    #         windowA.bl.dicon.hide()
    #         windowA.bl.label_9.hide()
    #         windowA.bl.eicon.hide()
    #         windowA.bl.show()
    #     elif whichsection == 'R':
    #         #'101':
    #         windowA.bl.label_5.setText('101')
    #         windowA.bl.label_6.hide()
    #         windowA.bl.bicon.hide()
    #         windowA.bl.label_7.hide()
    #         windowA.bl.cicon.hide()
    #         windowA.bl.label_8.hide()
    #         windowA.bl.dicon.hide()
    #         windowA.bl.label_9.hide()
    #         windowA.bl.eicon.hide()
    #         windowA.bl.show()
    #     elif whichsection == 'S':
    #         #'102' or '103' or '104':
    #         windowA.bl.label_5.setText('102')
    #         windowA.bl.label_6.setText('103')
    #         windowA.bl.label_7.setText('104')
    #         windowA.bl.label_8.hide()
    #         windowA.bl.dicon.hide()
    #         windowA.bl.label_9.hide()
    #         windowA.bl.eicon.hide()
    #         windowA.bl.show()
    #     elif whichsection == 'T':
    #         #'105' or '106' or '107' or '108' or '109':
    #         windowA.bl.label_5.setText('105')
    #         windowA.bl.label_6.setText('106')
    #         windowA.bl.label_7.setText('107')
    #         windowA.bl.label_8.setText('108')
    #         windowA.bl.label_9.setText('109')
    #         windowA.bl.show()
    #     elif whichsection == 'U':
    #         #'110' or '111' or '112' or '113' or '114' or '115' or '116':
    #         windowA.bl.label_5.setText('110')
    #         windowA.bl.label_6.setText('111')
    #         windowA.bl.label_7.setText('112')
    #         windowA.bl.label_8.setText('113')
    #         windowA.bl.label_9.setText('114')
    #         label_10 = QLabel('115')
    #         windowA.bl.gridLayout.addWidget(label_10, 6,0)
    #         label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,6,1)
    #         label_11 = QLabel('116')
    #         windowA.bl.gridLayout.addWidget(label_11, 7,0)
    #         label_11.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,7,1)
    #         windowA.bl.show()
    #     elif whichsection == 'V':
    #         #'117' or '118' or '119' or '120' or '121':
    #         windowA.bl.label_5.setText('117')
    #         windowA.bl.label_6.setText('118')
    #         windowA.bl.label_7.setText('119')
    #         windowA.bl.label_8.setText('120')
    #         windowA.bl.label_9.setText('121')
    #         windowA.bl.show()
    #     elif whichsection == 'W':
    #         #'122' or '123' or '124' or '125' or '126' or '127' or '128' or '129' or '130' 
    #         # or '131' or '132' or '133' or '134' or '135' or '136' or '137' or '138' or '139' or '140' or '141' or '142' or '143':
    #         windowA.bl.label_5.setText('122')
    #         windowA.bl.label_6.setText('123')
    #         windowA.bl.label_7.setText('124')
    #         windowA.bl.label_8.setText('125')
    #         windowA.bl.label_9.setText('126')
    #         label_10 = QLabel('127')
    #         windowA.bl.gridLayout.addWidget(label_10, 6,0)
    #         label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,6,1)
    #         label_11 = QLabel('128')
    #         windowA.bl.gridLayout.addWidget(label_11, 7,0)
    #         label_11.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,7,1)
    #         label_12 = QLabel('129')
    #         windowA.bl.gridLayout.addWidget(label_12, 8,0)
    #         label_12.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,8,1)
    #         label_13 = QLabel('130')
    #         windowA.bl.gridLayout.addWidget(label_13, 9,0)
    #         label_13.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,9,1)
    #         label_14 = QLabel('131')
    #         windowA.bl.gridLayout.addWidget(label_14, 10,0)
    #         label_14.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,10,1)
    #         label_15 = QLabel('132')
    #         windowA.bl.gridLayout.addWidget(label_15, 11,0)
    #         label_15.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,11,1)
    #         label_16 = QLabel('133')
    #         windowA.bl.gridLayout.addWidget(label_16, 12,0)
    #         label_16.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,12,1)
    #         label_17 = QLabel('134')
    #         windowA.bl.gridLayout.addWidget(label_17, 13,0)
    #         label_17.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,13,1)
    #         label_18 = QLabel('135')
    #         windowA.bl.gridLayout.addWidget(label_18, 14,0)
    #         label_18.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,14,1)
    #         label_19 = QLabel('136')
    #         windowA.bl.gridLayout.addWidget(label_19, 15,0)
    #         label_19.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,15,1)
    #         label_20 = QLabel('137')
    #         windowA.bl.gridLayout.addWidget(label_20, 16,0)
    #         label_20.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,16,1)
    #         label_21 = QLabel('138')
    #         windowA.bl.gridLayout.addWidget(label_21, 17,0)
    #         label_21.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,17,1)
    #         label_22 = QLabel('139')
    #         windowA.bl.gridLayout.addWidget(label_22, 18,0)
    #         label_22.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,18,1)
    #         label_23 = QLabel('140')
    #         windowA.bl.gridLayout.addWidget(label_23, 19,0)
    #         label_23.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,19,1)
    #         label_24 = QLabel('141')
    #         windowA.bl.gridLayout.addWidget(label_24, 20,0)
    #         label_24.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,20,1)
    #         label_25 = QLabel('142')
    #         windowA.bl.gridLayout.addWidget(label_25, 21,0)
    #         label_25.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,21,1)
    #         label_26 = QLabel('143')
    #         windowA.bl.gridLayout.addWidget(label_26, 22,0)
    #         label_26.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
    #         windowA.bl.gridLayout.addWidget(image,22,1)
    #         windowA.bl.show()
    #     elif whichsection == 'X':
    #         #'144' or '145' or '146':
    #         windowA.bl.label_5.setText('144')
    #         windowA.bl.label_6.setText('145')
    #         windowA.bl.label_7.setText('146')
    #         windowA.bl.label_8.hide()
    #         windowA.bl.dicon.hide()
    #         windowA.bl.label_9.hide()
    #         windowA.bl.eicon.hide()
    #         windowA.bl.show()
    #     elif whichsection == 'Y':
    #         #'147' or '148' or '149':
    #         windowA.bl.label_5.setText('147')
    #         windowA.bl.label_6.setText('148')
    #         windowA.bl.label_7.setText('149')
    #         windowA.bl.label_8.hide()
    #         windowA.bl.dicon.hide()
    #         windowA.bl.label_9.hide()
    #         windowA.bl.eicon.hide()
    #         windowA.bl.show()
    #     elif whichsection == 'Z':
    #         #'150':
    #         windowA.bl.label_5.setText('150')
    #         windowA.bl.label_6.hide()
    #         windowA.bl.bicon.hide()
    #         windowA.bl.label_7.hide()
    #         windowA.bl.cicon.hide()
    #         windowA.bl.label_8.hide()
    #         windowA.bl.dicon.hide()
    #         windowA.bl.label_9.hide()
    #         windowA.bl.eicon.hide()
    #         windowA.bl.show()

    # #function for toggle switch colors but see if you can do labels instead of buttons??
    # def toggleColor(button1, button2):
    #     button1.setEnabled(False)
    #     button2.setEnabled(True)
    #     button1.setStyleSheet('background-color: SkyBlue; color: black')
    #     button2.setStyleSheet('background-color: white; color: gray')

    # #occupation 2 blocks ahead for now
    # #!!!!!! TO DO !!!!!!!!!
    # def changeOccupancy(block):
    #     #print("UI block", block, "is occupied")
    #     if block == '1' or '2'or '3':
    #         windowB.aicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '4'or '5'or '6':
    #         windowB.bicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '7' or '8' or '9' or '10' or '11' or '12':
    #         windowB.cicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '13' or '14' or '15' or '16':
    #         windowB.dicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '17' or '18' or '19' or '20':
    #         windowB.eicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '21' or '22' or '23' or '24' or '25' or '26' or '27' or '28':
    #         windowB.ficon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '29' or '30' or '31' or '32':
    #         windowB.gicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '33' or '34' or '35':
    #         windowB.hicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '36' or '37' or '38' or '39' or '40' or '41' or '42' or '43' or '44' or '45' or '46' or '47' or '48' or '49' or '50' or '44' or '45' or '46' or '47' or '48' or '49' or '50'or '51' or '52' or '53' or '54' or '55' or '56' or '57':
    #         windowB.iicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '58' or '59' or '60' or '61' or '62':
    #         windowB.jicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '63' or '64' or '65' or '67' or '68':
    #         windowB.kicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '69' or '70' or '71' or '72' or '73':
    #         windowB.licon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '74' or '75' or '76':
    #         windowB.micon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '77' or '78' or '79' or '80' or '81' or '83' or '84' or '85':
    #         windowA.nicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '86' or '87' or '88':
    #         windowA.oicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '89' or '90' or '91' or '92' or '93' or '94' or '95' or '96' or '97':
    #         windowA.picon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '98' or '99' or '100':
    #         windowA.qicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '101':
    #         windowA.ricon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '102' or '103' or '104':
    #         windowA.sicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '105' or '106' or '107' or '108' or '109':
    #         windowA.ticon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '110' or '111' or '112' or '113' or '114' or '115' or '116':
    #         windowA.uicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '117' or '118' or '119' or '120' or '121':
    #         windowA.vicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '122' or '123' or '124' or '125' or '126' or '127' or '128' or '129' or '130' or '131' or '132' or '133' or '134' or '135' or '136' or '137' or '138' or '139' or '140' or '141' or '142' or '143':
    #         windowA.vicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '144' or '145' or '146':
    #         windowA.xicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '147' or '148' or '149':
    #         windowA.yicon.setPixmap(QPixmap('greentrain.png'))
    #     elif block == '150':
    #         windowA.zicon.setPixmap(QPixmap('greentrain.png'))

    # def changeVacancy(block):
    #     #print("UI block", block, "is vacant")
    #     if block == '1' or '2'or '3':
    #         windowB.aicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '4'or '5'or '6':
    #         windowB.bicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '7' or '8' or '9' or '10' or '11' or '12':
    #         windowB.cicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '13' or '14' or '15' or '16':
    #         windowB.dicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '17' or '18' or '19' or '20':
    #         windowB.eicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '21' or '22' or '23' or '24' or '25' or '26' or '27' or '28':
    #         windowB.ficon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '29' or '30' or '31' or '32':
    #         windowB.gicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '33' or '34' or '35':
    #         windowB.hicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '36' or '37' or '38' or '39' or '40' or '41' or '42' or '43' or '44' or '45' or '46' or '47' or '48' or '49' or '50' or '44' or '45' or '46' or '47' or '48' or '49' or '50'or '51' or '52' or '53' or '54' or '55' or '56' or '57':
    #         windowB.iicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '58' or '59' or '60' or '61' or '62':
    #         windowB.jicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '63' or '64' or '65' or '67' or '68':
    #         windowB.kicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '69' or '70' or '71' or '72' or '73':
    #         windowB.licon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '74' or '75' or '76':
    #         windowB.micon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '77' or '78' or '79' or '80' or '81' or '83' or '84' or '85':
    #         windowA.nicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '86' or '87' or '88':
    #         windowA.oicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '89' or '90' or '91' or '92' or '93' or '94' or '95' or '96' or '97':
    #         windowA.picon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '98' or '99' or '100':
    #         windowA.qicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '101':
    #         windowA.ricon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '102' or '103' or '104':
    #         windowA.sicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '105' or '106' or '107' or '108' or '109':
    #         windowA.ticon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '110' or '111' or '112' or '113' or '114' or '115' or '116':
    #         windowA.uicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '117' or '118' or '119' or '120' or '121':
    #         windowA.vicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '122' or '123' or '124' or '125' or '126' or '127' or '128' or '129' or '130' or '131' or '132' or '133' or '134' or '135' or '136' or '137' or '138' or '139' or '140' or '141' or '142' or '143':
    #         windowA.vicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '144' or '145' or '146':
    #         windowA.xicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '147' or '148' or '149':
    #         windowA.yicon.setPixmap(QPixmap('tracks.png'))
    #     elif block == '150':
    #         windowA.zicon.setPixmap(QPixmap('tracks.png'))

    # #change train icons
    # def changeIcon(self): #laurens
    #     section = self.sectionbox.currentText()
    #     block = self.blockbox.currentText()
    #     occupation = self.occupancybox.currentText()
    #     if section == 'A':
    #         if occupation == 'Occupied':
    #             self.aicon.setPixmap(QPixmap('greentrain.png'))
    #             #counts = counts + 1
    #         else:
    #             self.aicon.setPixmap(QPixmap('tracks.png'))
    #             #counts = counts - 1
    #         # if block == '1':
    #         #     if occupation == "Occupied":
    #         #         self.aicon.setPixmap("greentrain.png")
    #         #     else:
    #         #         self.aicon.setPixmap("tracks.png")
    #         # elif block == '2':
    #         #     if occupation == "Occupied":
    #         #         self.aicon.setPixmap("greentrain.png")
    #         #     else:
    #         #         self.aicon.setPixmap("tracks.png")
    #     elif section == 'B':
    #         if occupation == 'Occupied':
    #             self.bicon.setPixmap(QPixmap('greentrain.png'))
    #             #counts = counts + 1
    #         else:
    #             self.bicon.setPixmap(QPixmap('tracks.png'))
    #             #counts = counts - 1
    #     elif section == 'C':
    #         if occupation == 'Occupied':
    #             self.cicon.setPixmap(QPixmap('greentrain.png'))
    #             #counts = counts + 1
    #         else:
    #             self.cicon.setPixmap(QPixmap('tracks.png'))
    #             #counts = counts - 1
    #     elif section == 'D':
    #         if occupation == 'Occupied':
    #             self.dicon.setPixmap(QPixmap('greentrain.png'))
    #         else:
    #             self.dicon.setPixmap(QPixmap('tracks.png'))
    #     elif section == 'E':
    #         if occupation == 'Occupied':
    #             self.eicon.setPixmap(QPixmap('greentrain.png'))
    #         else:
    #             self.eicon.setPixmap(QPixmap('tracks.png'))
    #     elif section == 'F':
    #         if occupation == 'Occupied':
    #             self.ficon.setPixmap(QPixmap('greentrain.png'))
    #         else:
    #             self.ficon.setPixmap(QPixmap('tracks.png'))
    #     elif section == 'G':
    #         if occupation == 'Occupied':
    #             self.gicon.setPixmap(QPixmap('greentrain.png'))
    #         else:
    #             self.gicon.setPixmap(QPixmap('tracks.png'))
    #     elif section == 'H':
    #         if occupation == 'Occupied':
    #             self.hicon.setPixmap(QPixmap('greentrain.png'))
    #         else:
    #             self.hicon.setPixmap(QPixmap('tracks.png'))
    #     elif section == 'I':
    #         if occupation == 'Occupied':
    #             self.iicon.setPixmap(QPixmap('greentrain.png'))
    #         else:
    #             self.iicon.setPixmap(QPixmap('tracks.png'))
    #     elif section == 'J':
    #         if occupation == 'Occupied':
    #             self.jicon.setPixmap(QPixmap('greentrain.png'))
    #         else:
    #             self.jicon.setPixmap(QPixmap('tracks.png'))

    #function for number of active trains
    #somehow counts the number of times the red train label comes up
    def activeTrains(self, counts):
        self.activetrains.display(counts)

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