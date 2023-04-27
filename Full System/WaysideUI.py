import sys
import numpy as np
from pathlib import Path
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt, QObject
from PyQt6 import QtWidgets, uic
from signals import signals
#from Track_Configuration import Ui_TrackConfig 
from blockwidget import Ui_Section
#from Wayside_Main_B import Ui_MainWindowB
from Wayside_Main_A import Ui_MainWindowA
#from test2 import Ui_testpopup
#import PLCParser
from PLCParser import WTrack
# MainWindowA N-Z blue
# MainWindowB A-M red


class WMainWindowA(QtWidgets.QMainWindow, Ui_MainWindowA):
    def __init__(self, *args, obj=None, **kwargs):
        super(WMainWindowA, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Wayside Main UI')
        self.resize(640, 735)        
        
        self.instance =  ''
        self.first = 1
        self.sectionrange = []
        self.occupied = []
        self.sectionmatrix = []
        self.sectionrow = []
        self.sectionmatrixrow = []
        self.switchStates0 = []
        self.switchStates1 = []
        self.switchMatrix0 = []
        self.switchMatrix1 = []
        self.switchDefaults0 = []
        self.switchDefaults1 = []

        self.wayside1range = []
        self.wayside1sectionrange = []
        self.wayside2range = []
        self.wayside2sectionrange = []
        self.wayside3range = []
        self.wayside3sectionrange = []
        self.wayside4range = []
        self.wayside4sectionrange = []
        self.wayside5range = []
        self.wayside5sectionrange = []
        self.wayside6range = []
        self.wayside6sectionrange = []
        self.wayside7range = []
        self.wayside7sectionrange = []
        self.wayside8range = []
        self.wayside8sectionrange = []
        self.allthesectionsever0 = []
        self.allthesectionsever1 = []
        
        #signals
        signals.timerTicked.connect(self.ticka) #clock from ctc
        signals.waysidefirst.connect(self.firstinstance) #from selection pop up window
        signals.wtowOccupancy.connect(self.changeOccupancy) #from .py from track controller
        signals.wtowVacancy.connect(self.changeVacancy) #from .py from track controller
        signals.wtowTrainCount.connect(self.activeTrains) #from .py track controller
        signals.waysidesetup.connect(self.setuppopups)
        signals.ranges.connect(self.works)
        signals.sections.connect(self.sectionswork)
        signals.wtowSwitchesSetup.connect(self.setSwitchesSetup)
        signals.wtowSwitchChange.connect(self.newSwitchStates)
        signals.wtowSwitchDefaults.connect(self.setSwitchDefaults)
        signals.wtowCrossing.connect(self.crossingLights)
        #signals.wtowAuthority.connect(self.updateAuthority)
        
        self.plc = WTrack()
        self.setupplc()
        
        self.disableallswitchbuttons()
        self.setupgatebuttons()
        self.setupswitchbuttons()

        counts = 0
        self.activetrains.display(counts)
        self.whichwayside.currentIndexChanged.connect(self.changeinstance)
        self.whichwayside.setCurrentIndex(self.first)
        self.trackconfiguration.clicked.connect(self.newparse)

        self.pushn.clicked.connect(lambda: self.makeSectionWindow(self.sectionrange[0]))
        self.pusho.clicked.connect(lambda: self.makeSectionWindow(self.sectionrange[1]))
        self.pushp.clicked.connect(lambda: self.makeSectionWindow(self.sectionrange[2]))
        self.pushq.clicked.connect(lambda: self.makeSectionWindow(self.sectionrange[3]))
        self.pushr.clicked.connect(lambda: self.makeSectionWindow(self.sectionrange[4]))
        self.pushs.clicked.connect(lambda: self.makeSectionWindow(self.sectionrange[5]))
        self.pusht.clicked.connect(lambda: self.makeSectionWindow(self.sectionrange[6]))
        self.pushu.clicked.connect(lambda: self.makeSectionWindow(self.sectionrange[7]))
        self.pushv.clicked.connect(lambda: self.makeSectionWindow(self.sectionrange[8]))
        self.pushw.clicked.connect(lambda: self.makeSectionWindow(self.sectionrange[9]))
        self.pushx.clicked.connect(lambda: self.makeSectionWindow(self.sectionrange[10]))
        self.pushy.clicked.connect(lambda: self.makeSectionWindow(self.sectionrange[11]))
        self.pushz.clicked.connect(lambda: self.makeSectionWindow(self.sectionrange[12]))
        self.pushaa.clicked.connect(lambda: self.makeSectionWindow(self.sectionrange[13]))
        self.pushbb.clicked.connect(lambda: self.makeSectionWindow(self.sectionrange[14]))


        #lights
        #self.reda.setPixmap(QPixmap('greenlight.png'))
        #self.greenb.setPixmap(QPixmap('greenlight.png'))
    def updateAuthority(self, blocks, section):
        image = QLabel()
        pic = QPixmap('redtracks.png')
        image.setPixmap(pic.scaled(50, 50))

        matrixrow = self.sectionrange.index(section)
        #print("index matrixrow", matrixrow)
        #print("sectionmatrix", self.sectionmatrix)
        sectionBlocks = self.sectionmatrix[matrixrow]
        #print("checking these sectionBlocks", sectionBlocks)
        for i in sectionBlocks:
            for j in blocks:
                if i == j:
                    #print(j," has authority in it and =i", i)
                    index = self.sectionmatrixrow.index(i) +1
                    self.bl.gridLayout.addWidget(image, index, 1)


    def crossingLights(self, track, color): #red false green true
        red = QPixmap('redlight.png')
        green = QPixmap('greenlight.png')
        blank = QPixmap('offlight.png')

        if track == 0:
            if color == True:
                self.gatepositiona.setText("Inactive")
                self.greena.setPixmap(green)
                self.reda.setPixmap(blank)
            elif color == False:
                self.gatepositiona.setText("Active")
                self.greena.setPixmap(blank)
                self.reda.setPixmap(red)
        elif track == 1:
            if color == True:
                self.gatepositiona.setText("Inactive")
                self.greena.setPixmap(green)
                self.reda.setPixmap(blank)
            elif color == False:
                self.gatepositiona.setText("Active")
                self.greena.setPixmap(blank)
                self.reda.setPixmap(red)

    def changeinstance(self):
        num = self.whichwayside.currentIndex()+1
        #print("change instance", num)
        #print("num",num)
        self.first = num
        self.setuppopups(self.first)
        self.SwitchesSetup(self.first)
        if num == 1:
            which = 0
        elif num == 2:
            which = 0
        elif num == 3:
            which = 0
        elif num == 4:
            which = 0
        elif num == 5:
            which = 1
        elif num == 6:
            which = 1
        elif num == 7:
            which = 1
        elif num == 7:
            which = 1
        self.changeSwitchButtons(which)
        #signals.waysidefirst.emit(num)
        #signals.wtowOccupancy.emit() 
        
    def setupplc(self):
        
        self.plc.parse()#fname = "plcLogic_Red")
        #print("setupplc wayside1range 2 in ui .plc",plc.wayside1range)
        #self.wayside1range = plc.wayside1range
        #print("setupplc wayside1range 2 in ui .self",self.wayside1range)

    def newparse(self):
        #try:
        home_dir = str(Path.home())
        dialog = QFileDialog()
        fname, filetypes = dialog.getOpenFileName()#getOpenFileName(self, 'Open file', home_dir)
        #fname.selectedFiles()
        #print(" newparse ui fname", fname)
        #print("neaparse homedir", home_dir)
        self.plc.parse(fname)
        #except:
            #print("No file to parse")

    def works(self, range1, range2, range3, range4, range5, range6, range7, range8):
        #print("it works in ui from please from .py range1:", range1)
        #print("works ui range2", range2)
        #print("works ui range3", range3)
        #print("works ui range4", range4)
        self.wayside1range = range1
        self.wayside2range = range2
        self.wayside3range = range3
        self.wayside4range = range4
        self.wayside5range = range5
        self.wayside6range = range6
        self.wayside7range = range7
        self.wayside8range = range8
        #print("works ui range2", self.wayside1range)
        #print("works ui range2", self.wayside2range)
        #print("works ui range3", self.wayside3range)
        #print("works ui range4", self.wayside4range)

    def sectionswork(self, range1, range2, range3, range4, range5, range6, range7, range8):
        #print("sectionswork")
        self.wayside1sectionrange = range1
        #print("sectionswork range1 self.", self.wayside1sectionrange)
        #print("sectionswork range1 ", range1)
        self.wayside2sectionrange = range2
        #print("sectionswork range2 ", range2)
        self.wayside3sectionrange = range3
        #print("sectionswork range2 ", range3)
        self.wayside4sectionrange  = range4
        #print("sectionswork range2 ", range4)
        self.wayside5sectionrange  = range5
        self.wayside6sectionrange  = range6
        self.wayside7sectionrange  = range7
        self.wayside8sectionrange  = range8

        self.allthesectionsever0.append(range1)
        self.allthesectionsever0.append(range2)
        self.allthesectionsever0.append(range3)
        self.allthesectionsever0.append(range4)
        #print("allsectionsever0", self.allthesectionsever0)
        #print("length all", len(self))
        self.allthesectionsever1.append(range5)
        self.allthesectionsever1.append(range6)
        self.allthesectionsever1.append(range7)
        self.allthesectionsever1.append(range8)

    def setSwitchesSetup(self, allsw0, allsw1):
        #print("setSwitchesSetup ui")
        self.switchMatrix0 = allsw0
        self.switchMatrix1 = allsw1
        # self.changeSwitchButtons(allsw0, allsw1, 0)
        # self.changeSwitchButtons(allsw0, allsw1, 1)
        # print("setup sw0", allsw0)
        # print("setup sw1", allsw1)

    def newSwitchStates(self, sw0, sw1):
        if self.first == 1:
            which = 0
        elif self.first == 2:
            which = 0
        elif self.first == 3:
            which = 0
        elif self.first == 4:
            which = 0
        elif self.first == 5:
            which = 1
        elif self.first == 6:
            which = 1
        elif self.first == 7:
            which = 1
        elif self.first == 7:
            which = 1
        self.switchStates0 = sw0
        self.switchStates1 = sw1
        self.changeSwitchButtons(which)

    def setSwitchDefaults(self, allsw0, allsw1):
        #print("set defaults in ui")
        self.switchDefaults0 = allsw0
        self.switchDefaults1 = allsw1
        self.switchStates0 = allsw0
        self.switchStates1 = allsw1
        # self.changeSwitchButtons(allsw0, allsw1, 0)
        # self.changeSwitchButtons(allsw0, allsw1, 1)
        # self.disableallswitchbuttons()

    def SwitchesSetup(self, first):
        #print("switch matrix", self.switchMatrix0)
        #print("switchessetup ui")
        which = 0
        if first == 1:
            which = 0
        elif first == 2:
            which = 0
        elif first == 3:
            which = 0
        elif first == 4:
            which = 0
        elif first == 5:
            which = 1
        elif first == 6:
            which = 1
        elif first == 7:
            which = 1
        elif first == 7:
            which = 1

        self.gate10.hide()
        self.gate11.hide()
        self.gate20.hide()
        self.gate21.hide()
        self.gate30.hide()
        self.gate31.hide()
        self.gate40.hide()
        self.gate41.hide()
        self.gate50.hide()
        self.gate51.hide()
        self.gate60.hide()
        self.gate61.hide()
        self.gate70.hide()
        self.gate71.hide()
        self.switchlabel_7.hide()

        if which == 0:
            self.switchlabel.setText(str(self.switchMatrix0[0][0]))
            self.gate10.setText(str(self.switchMatrix0[0][1]))
            self.gate11.setText(str(self.switchMatrix0[0][2]))
            self.switchlabel_2.setText(str(self.switchMatrix0[1][0]))
            self.gate20.setText(str(self.switchMatrix0[1][1]))
            self.gate21.setText(str(self.switchMatrix0[1][2]))
            self.switchlabel_3.setText(str(self.switchMatrix0[2][0]))
            self.gate30.setText(str(self.switchMatrix0[2][1]))
            self.gate31.setText(str(self.switchMatrix0[2][2]))
            self.switchlabel_4.setText(str(self.switchMatrix0[3][0]))
            self.gate40.setText(str(self.switchMatrix0[3][1]))
            self.gate41.setText(str(self.switchMatrix0[3][2]))
            self.switchlabel_5.setText(str(self.switchMatrix0[4][0]))
            self.gate50.setText(str(self.switchMatrix0[4][1]))
            self.gate51.setText(str(self.switchMatrix0[4][2]))
            self.switchlabel_6.setText(str(self.switchMatrix0[5][0]))
            self.gate60.setText(str(self.switchMatrix0[5][1]))
            self.gate61.setText(str(self.switchMatrix0[5][2]))
            self.gate10.show()
            self.gate11.show()
            self.gate20.show()
            self.gate21.show()
            self.gate30.show()
            self.gate31.show()
            self.gate40.show()
            self.gate41.show()
            self.gate50.show()
            self.gate51.show()
            self.gate60.show()
            self.gate61.show()

        elif which == 1:
            self.switchlabel.setText(str(self.switchMatrix1[0][0]))
            self.gate10.setText(str(self.switchMatrix1[0][1]))
            self.gate11.setText(str(self.switchMatrix1[0][2]))
            self.switchlabel_2.setText(str(self.switchMatrix1[1][0]))
            self.gate20.setText(str(self.switchMatrix1[1][1]))
            self.gate21.setText(str(self.switchMatrix1[1][2]))
            self.switchlabel_3.setText(str(self.switchMatrix1[2][0]))
            self.gate30.setText(str(self.switchMatrix1[2][1]))
            self.gate31.setText(str(self.switchMatrix1[2][2]))
            self.switchlabel_4.setText(str(self.switchMatrix1[3][0]))
            self.gate40.setText(str(self.switchMatrix1[3][1]))
            self.gate41.setText(str(self.switchMatrix1[3][2]))
            self.switchlabel_5.setText(str(self.switchMatrix1[4][0]))
            self.gate50.setText(str(self.switchMatrix1[4][1]))
            self.gate51.setText(str(self.switchMatrix1[4][2]))
            self.switchlabel_6.setText(str(self.switchMatrix1[5][0]))
            self.gate60.setText(str(self.switchMatrix1[5][1]))
            self.gate61.setText(str(self.switchMatrix1[5][2]))
            self.switchlabel_7.setText(str(self.switchMatrix1[6][0]))
            self.gate70.setText(str(self.switchMatrix1[6][1]))
            self.gate71.setText(str(self.switchMatrix1[6][2]))
            self.switchlabel_7.show()
            self.gate10.show()
            self.gate11.show()
            self.gate20.show()
            self.gate21.show()
            self.gate30.show()
            self.gate31.show()
            self.gate40.show()
            self.gate41.show()
            self.gate50.show()
            self.gate51.show()
            self.gate60.show()
            self.gate61.show()
            self.gate70.show()
            self.gate71.show()
        #print("ehich track in switches setup", which)
        self.changeSwitchButtons(which)
        #self.changeSwitchButtons(self.switchDefaults0, self.switchDefaults1, 1)
        self.disableallswitchbuttons()

    def changeSwitchButtons(self, inst):
        #print("changing switch button function")
        

        if inst == 0:
            #print("sw0", sw0)
            if self.switchStates0[0] == 0:
                
                self.toggleColor(self.gate10, self.gate11)
                self.gate10.setStyleSheet('background-color: SkyBlue')
                self.gate11.setStyleSheet('background-color: white; color: gray')
            elif self.switchStates0[0] == 1:
                self.toggleColor(self.gate11, self.gate10)
                self.gate11.setStyleSheet('background-color: SkyBlue')
                self.gate10.setStyleSheet('background-color: white; color: gray')

            if self.switchStates0[1] == 0:
                self.toggleColor(self.gate20, self.gate21)
                self.gate20.setStyleSheet('background-color: SkyBlue')
                self.gate21.setStyleSheet('background-color: white; color: gray')
            elif self.switchStates0[1] == 1:
                self.toggleColor(self.gate21, self.gate20)
                self.gate21.setStyleSheet('background-color: SkyBlue')
                self.gate20.setStyleSheet('background-color: white; color: gray')

            if self.switchStates0[2] == 0:
                self.toggleColor(self.gate30, self.gate31)
                self.gate30.setStyleSheet('background-color: SkyBlue')
                self.gate31.setStyleSheet('background-color: white; color: gray')
            elif self.switchStates0[2] == 1:
                self.toggleColor(self.gate31, self.gate30)
                self.gate31.setStyleSheet('background-color: SkyBlue')
                self.gate30.setStyleSheet('background-color: white; color: gray')

            if self.switchStates0[3] == 0:
                self.toggleColor(self.gate40, self.gate41)
                self.gate40.setStyleSheet('background-color: SkyBlue')
                self.gate41.setStyleSheet('background-color: white; color: gray')
            elif self.switchStates0[3] == 1:
                self.toggleColor(self.gate41, self.gate40)
                self.gate41.setStyleSheet('background-color: SkyBlue')
                self.gate40.setStyleSheet('background-color: white; color: gray')

            if self.switchStates0[4] == 0:
                self.toggleColor(self.gate50, self.gate51)
                self.gate50.setStyleSheet('background-color: SkyBlue')
                self.gate51.setStyleSheet('background-color: white; color: gray')
            elif self.switchStates0[4] == 1:
                self.toggleColor(self.gate51, self.gate50)
                self.gate51.setStyleSheet('background-color: SkyBlue')
                self.gate50.setStyleSheet('background-color: white; color: gray')

            if self.switchStates0[5] == 0:
                #print("switch 6 is 0")
                self.toggleColor(self.gate60, self.gate61)
                self.gate60.setStyleSheet('background-color: SkyBlue')
                self.gate61.setStyleSheet('background-color: white; color: gray')
            elif self.switchStates0[5] == 1:
                #print("switch 6 is 1")
                self.toggleColor(self.gate61, self.gate60)
                self.gate61.setStyleSheet('background-color: SkyBlue')
                self.gate60.setStyleSheet('background-color: white; color: gray')

        elif inst == 1:
            #print("sw1", sw1)
            if self.switchStates1[0] == 0:
                self.toggleColor(self.gate10, self.gate11)
                self.gate10.setStyleSheet('background-color: SkyBlue')
                self.gate11.setStyleSheet('background-color: white; color: gray')
            elif self.switchStates1[0] == 1:
                self.toggleColor(self.gate11, self.gate10)
                self.gate11.setStyleSheet('background-color: SkyBlue')
                self.gate10.setStyleSheet('background-color: white; color: gray')

            if self.switchStates1[1] == 0:
                self.toggleColor(self.gate20, self.gate21)
                self.gate20.setStyleSheet('background-color: SkyBlue')
                self.gate21.setStyleSheet('background-color: white; color: gray')
            elif self.switchStates1[1] == 1:
                self.toggleColor(self.gate21, self.gate20)
                self.gate21.setStyleSheet('background-color: SkyBlue')
                self.gate20.setStyleSheet('background-color: white; color: gray')

            if self.switchStates1[2] == 0:
                self.toggleColor(self.gate30, self.gate31)
                self.gate31.setStyleSheet('background-color: SkyBlue')
            elif self.switchStates1[2] == 1:
                self.toggleColor(self.gate31, self.gate30)
                self.gate30.setStyleSheet('background-color: white; color: gray')

            if self.switchStates1[3] == 0:
                self.toggleColor(self.gate40, self.gate41)
                self.gate40.setStyleSheet('background-color: SkyBlue')
                self.gate41.setStyleSheet('background-color: white; color: gray')
            elif self.switchStates1[3] == 1:
                self.toggleColor(self.gate41, self.gate40)
                self.gate41.setStyleSheet('background-color: SkyBlue')
                self.gate40.setStyleSheet('background-color: white; color: gray')

            if self.switchStates1[4] == 0:
                self.toggleColor(self.gate50, self.gate51)
                self.gate50.setStyleSheet('background-color: SkyBlue')
                self.gate51.setStyleSheet('background-color: white; color: gray')
            elif self.switchStates1[4] == 1:
                self.toggleColor(self.gate51, self.gate50)
                self.gate51.setStyleSheet('background-color: SkyBlue')
                self.gate50.setStyleSheet('background-color: white; color: gray')

            if self.switchStates1[5] == 0:
                self.toggleColor(self.gate60, self.gate61)
                self.gate60.setStyleSheet('background-color: SkyBlue')
                self.gate61.setStyleSheet('background-color: white; color: gray')
            elif self.switchStates1[5] == 1:
                self.toggleColor(self.gate61, self.gate60)
                self.gate61.setStyleSheet('background-color: SkyBlue')
                self.gate60.setStyleSheet('background-color: white; color: gray')

            if self.switchStates1[6] == 0:
                self.toggleColor(self.gate70, self.gate71)
                self.gate70.setStyleSheet('background-color: SkyBlue')
                self.gate71.setStyleSheet('background-color: white; color: gray')
            elif self.switchStates1[6] == 1:
                self.toggleColor(self.gate71, self.gate70)
                self.gate71.setStyleSheet('background-color: SkyBlue')
                self.gate70.setStyleSheet('background-color: white; color: gray')
        
    def firstinstance(self, num):
        self.first = num
        self.setuppopups(self.first)
        self.SwitchesSetup(self.first)
        #print("set first", self.first, "=", num)
        #self.whichwayside.setCurrentIndex(self.first)

    def disableallswitchbuttons(self):
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
        self.gate70.setEnabled(False)
        self.gate71.setEnabled(False)

    def setupgatebuttons(self):
        #set up gate buttons
        self.maintenancemode.toggled.connect(self.maintenanceMode)
        self.automaticmode.toggled.connect(self.automaticMode)

    def setupswitchbuttons(self):
        #switch button colors
        self.automaticmode.setDown(True)
        self.gate10.clicked.connect(lambda: self.toggleColor(self.gate10, self.gate11))
        self.gate11.setStyleSheet('background-color: SkyBlue')
        self.gate11.clicked.connect(lambda: self.toggleColor(self.gate11, self.gate10))
        self.gate10.setStyleSheet('background-color: white; color: gray')
        self.gate20.clicked.connect(lambda: self.toggleColor(self.gate20, self.gate21))
        self.gate21.setStyleSheet('background-color: SkyBlue')
        self.gate21.clicked.connect(lambda: self.toggleColor(self.gate21, self.gate20))
        self.gate20.setStyleSheet('background-color: white; color: gray')
        self.gate30.clicked.connect(lambda: self.toggleColor(self.gate30, self.gate31))
        self.gate31.setStyleSheet('background-color: SkyBlue')
        self.gate31.clicked.connect(lambda: self.toggleColor(self.gate31, self.gate30))
        self.gate30.setStyleSheet('background-color: white; color: gray')
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
        self.gate70.clicked.connect(lambda: self.toggleColor(self.gate70, self.gate71))
        self.gate71.setStyleSheet('background-color: SkyBlue')
        self.gate71.clicked.connect(lambda: self.toggleColor(self.gate71, self.gate70))
        self.gate70.setStyleSheet('background-color: white; color: gray')
        self.gate10.clicked.connect(lambda: self.uichangedswitches( 0, 0))
        self.gate11.clicked.connect(lambda: self.uichangedswitches( 0, 1))
        self.gate20.clicked.connect(lambda: self.uichangedswitches( 1, 0))
        self.gate21.clicked.connect(lambda: self.uichangedswitches( 1, 1))
        self.gate30.clicked.connect(lambda: self.uichangedswitches( 2, 0))
        self.gate31.clicked.connect(lambda: self.uichangedswitches( 2, 1))
        self.gate40.clicked.connect(lambda: self.uichangedswitches( 3, 0))
        self.gate41.clicked.connect(lambda: self.uichangedswitches( 3, 1))
        self.gate50.clicked.connect(lambda: self.uichangedswitches( 4, 0))
        self.gate51.clicked.connect(lambda: self.uichangedswitches( 4, 1))
        self.gate60.clicked.connect(lambda: self.uichangedswitches( 5, 0))
        self.gate61.clicked.connect(lambda: self.uichangedswitches( 5, 1))
        self.gate70.clicked.connect(lambda: self.uichangedswitches( 6, 0))
        self.gate71.clicked.connect(lambda: self.uichangedswitches( 6, 1))


    def uichangedswitches(self, gate, state):
        #print("current", self.switchStates0, self.switchStates1)
        if self.first == 1 or self.first == 2 or self.first == 3 or self.first ==4:
            self.switchStates0[gate]=state
        elif self.first == 5 or self.first == 6 or self.first == 7 or self.first ==8:
            self.switchStates1[gate]=state
        #print("new", self.switchStates0, self.switchStates1)
        
        
        signals.wtowSwitchfromUI.emit(self.switchStates0, self.switchStates1)

    def setuppopups(self, first):
        self.sectionrange = []
        #print("first", first)
        #print("setuppopups start")
        if first == 1:
            self.linelabel.setText("Green Line")
            self.sectionrange = []
            #print("setuppopups wayside1sectionrange[0]",self.wayside1sectionrange[0])
            current = self.wayside1sectionrange[0]
            self.sectionrange.append(current)
            for i in self.wayside1sectionrange:
                if i == current:
                    continue
                else:
                    current = i
                    self.sectionrange.append(current)
                    #print(i)
        elif first == 2:
            self.linelabel.setText("Green Line")
            self.sectionrange = []
            current = self.wayside2sectionrange[0]
            #print(current)
            self.sectionrange.append(current)
            for i in self.wayside2sectionrange:
                if i == current:
                    continue
                else:
                    current = i
                    self.sectionrange.append(current)
                    #print(i)
        elif first == 3:
            self.linelabel.setText("Green Line")
            self.sectionrange = []
            current = self.wayside3sectionrange[0]
            self.sectionrange.append(current)
            for i in self.wayside3sectionrange:
                if i == current:
                    continue
                else:
                    current = i
                    self.sectionrange.append(current)
                    #print(i)
        elif first == 4:
            self.linelabel.setText("Green Line")
            self.sectionrange = []
            #print("wayside4range",self.wayside4range)
            current = self.wayside4sectionrange[0]
            self.sectionrange.append(current)
            for i in self.wayside4sectionrange:
                if i == current:
                    continue
                else:
                    current = i
                    self.sectionrange.append(current)
        elif first == 5:
            self.linelabel.setText("Red Line")
            self.sectionrange = []
            #print("wayside5range",self.wayside5range)
            current = self.wayside5sectionrange[0]
            self.sectionrange.append(current)
            for i in self.wayside5sectionrange:
                if i == current:
                    continue
                else:
                    current = i
                    self.sectionrange.append(current)
        elif first == 6:
            self.linelabel.setText("Red Line")
            self.sectionrange = []
            #print("wayside6range",self.wayside6range)
            current = self.wayside6sectionrange[0]
            self.sectionrange.append(current)
            for i in self.wayside6sectionrange:
                if i == current:
                    continue
                else:
                    current = i
                    self.sectionrange.append(current)
        elif first == 7:
            self.linelabel.setText("Red Line")
            self.sectionrange = []
            #print("wayside7range",self.wayside7range)
            current = self.wayside7sectionrange[0]
            self.sectionrange.append(current)
            for i in self.wayside7sectionrange:
                if i == current:
                    continue
                else:
                    current = i
                    self.sectionrange.append(current)
        elif first == 8:
            self.linelabel.setText("Red Line")
            self.sectionrange = []
            #print("wayside8range",self.wayside8range)
            current = self.wayside8sectionrange[0]
            self.sectionrange.append(current)
            for i in self.wayside8sectionrange:
                if i == current:
                    continue
                else:
                    current = i
                    self.sectionrange.append(current)
                    #print(i)
        #print("setuppopups sectionrange",self.sectionrange)
        #print("setuppopups first",self.first)

        positions = [(i, 0) for i in range(2,len(self.sectionrange)+2)]
        #print("length of sectionrange", self.sectionrange)
        #print(positions)
        self.namelist = {}
        nlist = []

        for row, wholerow in enumerate(self.sectionrange):
            for col, but in enumerate(wholerow):
                #self.namelist[but] = QPushButton(but)
                #self.namelist[but].clicked.connect(lambda: self.makeSectionWindow(but))
                nlist.append(but)
                #print("namlist[but]", self.namelist[but])
                #self.gridLayout_4.addWidget(self.namelist[but], row+2, col)
        l = len(self.sectionrange)
        left = 15-l
        #print("range", self.sectionrange, "len", l)
        #print("outside l",l)
        rangelabel = self.sectionrange[0] + "-" + self.sectionrange[l-1]
        self.sectionrangelabel.setText(rangelabel)
        #self.gridLayout_4.addWidget(, 16, 1)   
        img = QPixmap('tracks.png')

        self.pushn.hide()
        self.pusho.hide()
        self.pushp.hide()
        self.pushq.hide()
        self.pushr.hide()
        self.pushs.hide()
        self.pusht.hide()
        self.pushu.hide()
        self.pushv.hide()
        self.pushw.hide()
        self.pushx.hide()
        self.pushy.hide()
        self.pushz.hide()
        self.pushaa.hide()
        self.pushbb.hide()
        self.pushcc.hide()

        self.nicon.hide()
        self.oicon.hide()
        self.picon.hide()
        self.qicon.hide()
        self.ricon.hide()
        self.sicon.hide()
        self.ticon.hide()
        self.uicon.hide()
        self.vicon.hide()
        self.wicon.hide()
        self.xicon.hide()
        self.yicon.hide()
        self.zicon.hide()
        self.aaicon.hide()
        self.bbicon.hide()
        self.ccicon.hide()
        
        
        if l == 16:
            self.pushn.setText(self.sectionrange[0])
            self.pusho.setText(self.sectionrange[1])
            self.pushp.setText(self.sectionrange[2])
            self.pushq.setText(self.sectionrange[3])
            self.pushr.setText(self.sectionrange[4])
            self.pushs.setText(self.sectionrange[5])
            self.pusht.setText(self.sectionrange[6])
            self.pushu.setText(self.sectionrange[7])
            self.pushv.setText(self.sectionrange[8])
            self.pushw.setText(self.sectionrange[9])
            self.pushx.setText(self.sectionrange[10])
            self.pushy.setText(self.sectionrange[11])
            self.pushz.setText(self.sectionrange[12])
            self.pushaa.setText(self.sectionrange[13])
            self.pushbb.setText(self.sectionrange[14])
            self.pushcc.setText(self.sectionrange[15])
            self.nicon.setPixmap(img)
            self.oicon.setPixmap(img)
            self.picon.setPixmap(img)
            self.qicon.setPixmap(img)
            self.ricon.setPixmap(img)
            self.sicon.setPixmap(img)
            self.ticon.setPixmap(img)
            self.uicon.setPixmap(img)
            self.vicon.setPixmap(img)
            self.wicon.setPixmap(img)
            self.xicon.setPixmap(img)
            self.yicon.setPixmap(img)
            self.zicon.setPixmap(img)
            self.aaicon.setPixmap(img)
            self.bbicon.setPixmap(img)
            self.ccicon.setPixmap(img)
            self.pushn.show()
            self.pusho.show()
            self.pushp.show()
            self.pushq.show()
            self.pushr.show()
            self.pushs.show()
            self.pusht.show()
            self.pushu.show()
            self.pushv.show()
            self.pushw.show()
            self.pushx.show()
            self.pushy.show()
            self.pushz.show()
            self.pushaa.show()
            self.pushbb.show()
            self.pushcc.show()
            self.nicon.show()
            self.oicon.show()
            self.picon.show()
            self.qicon.show()
            self.ricon.show()
            self.sicon.show()
            self.ticon.show()
            self.uicon.show()
            self.vicon.show()
            self.wicon.show()
            self.xicon.show()
            self.yicon.show()
            self.zicon.show()
            self.aaicon.show()
            self.bbicon.show()
            self.ccicon.show()

            
        elif l == 15:
            self.pushn.setText(self.sectionrange[0])
            self.pusho.setText(self.sectionrange[1])
            self.pushp.setText(self.sectionrange[2])
            self.pushq.setText(self.sectionrange[3])
            self.pushr.setText(self.sectionrange[4])
            self.pushs.setText(self.sectionrange[5])
            self.pusht.setText(self.sectionrange[6])
            self.pushu.setText(self.sectionrange[7])
            self.pushv.setText(self.sectionrange[8])
            self.pushw.setText(self.sectionrange[9])
            self.pushx.setText(self.sectionrange[10])
            self.pushy.setText(self.sectionrange[11])
            self.pushz.setText(self.sectionrange[12])
            self.pushaa.setText(self.sectionrange[13])
            self.pushbb.setText(self.sectionrange[14])
            self.nicon.setPixmap(img)
            self.oicon.setPixmap(img)
            self.picon.setPixmap(img)
            self.qicon.setPixmap(img)
            self.ricon.setPixmap(img)
            self.sicon.setPixmap(img)
            self.ticon.setPixmap(img)
            self.uicon.setPixmap(img)
            self.vicon.setPixmap(img)
            self.wicon.setPixmap(img)
            self.xicon.setPixmap(img)
            self.yicon.setPixmap(img)
            self.zicon.setPixmap(img)
            self.aaicon.setPixmap(img)
            self.bbicon.setPixmap(img)
            self.pushn.show()
            self.pusho.show()
            self.pushp.show()
            self.pushq.show()
            self.pushr.show()
            self.pushs.show()
            self.pusht.show()
            self.pushu.show()
            self.pushv.show()
            self.pushw.show()
            self.pushx.show()
            self.pushy.show()
            self.pushz.show()
            self.pushaa.show()
            self.pushbb.show()
            self.nicon.show()
            self.oicon.show()
            self.picon.show()
            self.qicon.show()
            self.ricon.show()
            self.sicon.show()
            self.ticon.show()
            self.uicon.show()
            self.vicon.show()
            self.wicon.show()
            self.xicon.show()
            self.yicon.show()
            self.zicon.show()
            self.aaicon.show()
            self.bbicon.show()
        elif l == 14:
            self.pushn.setText(self.sectionrange[0])
            self.pusho.setText(self.sectionrange[1])
            self.pushp.setText(self.sectionrange[2])
            self.pushq.setText(self.sectionrange[3])
            self.pushr.setText(self.sectionrange[4])
            self.pushs.setText(self.sectionrange[5])
            self.pusht.setText(self.sectionrange[6])
            self.pushu.setText(self.sectionrange[7])
            self.pushv.setText(self.sectionrange[8])
            self.pushw.setText(self.sectionrange[9])
            self.pushx.setText(self.sectionrange[10])
            self.pushy.setText(self.sectionrange[11])
            self.pushz.setText(self.sectionrange[12])
            self.pushaa.setText(self.sectionrange[13])
            self.nicon.setPixmap(img)
            self.oicon.setPixmap(img)
            self.picon.setPixmap(img)
            self.qicon.setPixmap(img)
            self.ricon.setPixmap(img)
            self.sicon.setPixmap(img)
            self.ticon.setPixmap(img)
            self.uicon.setPixmap(img)
            self.vicon.setPixmap(img)
            self.wicon.setPixmap(img)
            self.xicon.setPixmap(img)
            self.yicon.setPixmap(img)
            self.zicon.setPixmap(img)
            self.aaicon.setPixmap(img)
            self.pushn.show()
            self.pusho.show()
            self.pushp.show()
            self.pushq.show()
            self.pushr.show()
            self.pushs.show()
            self.pusht.show()
            self.pushu.show()
            self.pushv.show()
            self.pushw.show()
            self.pushx.show()
            self.pushy.show()
            self.pushz.show()
            self.pushaa.show()
            self.nicon.show()
            self.oicon.show()
            self.picon.show()
            self.qicon.show()
            self.ricon.show()
            self.sicon.show()
            self.ticon.show()
            self.uicon.show()
            self.vicon.show()
            self.wicon.show()
            self.xicon.show()
            self.yicon.show()
            self.zicon.show()
            self.aaicon.show()
            
        elif l == 13:
            self.pushn.setText(self.sectionrange[0])
            self.pusho.setText(self.sectionrange[1])
            self.pushp.setText(self.sectionrange[2])
            self.pushq.setText(self.sectionrange[3])
            self.pushr.setText(self.sectionrange[4])
            self.pushs.setText(self.sectionrange[5])
            self.pusht.setText(self.sectionrange[6])
            self.pushu.setText(self.sectionrange[7])
            self.pushv.setText(self.sectionrange[8])
            self.pushw.setText(self.sectionrange[9])
            self.pushx.setText(self.sectionrange[10])
            self.pushy.setText(self.sectionrange[11])
            self.pushz.setText(self.sectionrange[12])
            self.nicon.setPixmap(img)
            self.oicon.setPixmap(img)
            self.picon.setPixmap(img)
            self.qicon.setPixmap(img)
            self.ricon.setPixmap(img)
            self.sicon.setPixmap(img)
            self.ticon.setPixmap(img)
            self.uicon.setPixmap(img)
            self.vicon.setPixmap(img)
            self.wicon.setPixmap(img)
            self.xicon.setPixmap(img)
            self.yicon.setPixmap(img)
            self.zicon.setPixmap(img)
            self.pushn.show()
            self.pusho.show()
            self.pushp.show()
            self.pushq.show()
            self.pushr.show()
            self.pushs.show()
            self.pusht.show()
            self.pushu.show()
            self.pushv.show()
            self.pushw.show()
            self.pushx.show()
            self.pushy.show()
            self.pushz.show()
            self.nicon.show()
            self.oicon.show()
            self.picon.show()
            self.qicon.show()
            self.ricon.show()
            self.sicon.show()
            self.ticon.show()
            self.uicon.show()
            self.vicon.show()
            self.wicon.show()
            self.xicon.show()
            self.yicon.show()
            self.zicon.show()
        elif l == 12:
            self.pushn.setText(self.sectionrange[0])
            self.pusho.setText(self.sectionrange[1])
            self.pushp.setText(self.sectionrange[2])
            self.pushq.setText(self.sectionrange[3])
            self.pushr.setText(self.sectionrange[4])
            self.pushs.setText(self.sectionrange[5])
            self.pusht.setText(self.sectionrange[6])
            self.pushu.setText(self.sectionrange[7])
            self.pushv.setText(self.sectionrange[8])
            self.pushw.setText(self.sectionrange[9])
            self.pushx.setText(self.sectionrange[10])
            self.pushy.setText(self.sectionrange[11])
            self.nicon.setPixmap(img)
            self.oicon.setPixmap(img)
            self.picon.setPixmap(img)
            self.qicon.setPixmap(img)
            self.ricon.setPixmap(img)
            self.sicon.setPixmap(img)
            self.ticon.setPixmap(img)
            self.uicon.setPixmap(img)
            self.vicon.setPixmap(img)
            self.wicon.setPixmap(img)
            self.xicon.setPixmap(img)
            self.yicon.setPixmap(img)
            self.pushn.show()
            self.pusho.show()
            self.pushp.show()
            self.pushq.show()
            self.pushr.show()
            self.pushs.show()
            self.pusht.show()
            self.pushu.show()
            self.pushv.show()
            self.pushw.show()
            self.pushx.show()
            self.pushy.show()
            self.nicon.show()
            self.oicon.show()
            self.picon.show()
            self.qicon.show()
            self.ricon.show()
            self.sicon.show()
            self.ticon.show()
            self.uicon.show()
            self.vicon.show()
            self.wicon.show()
            self.xicon.show()
            self.yicon.show()
        elif l == 11:
            self.pushn.setText(self.sectionrange[0])
            self.pusho.setText(self.sectionrange[1])
            self.pushp.setText(self.sectionrange[2])
            self.pushq.setText(self.sectionrange[3])
            self.pushr.setText(self.sectionrange[4])
            self.pushs.setText(self.sectionrange[5])
            self.pusht.setText(self.sectionrange[6])
            self.pushu.setText(self.sectionrange[7])
            self.pushv.setText(self.sectionrange[8])
            self.pushw.setText(self.sectionrange[9])
            self.pushx.setText(self.sectionrange[10])
            self.nicon.setPixmap(img)
            self.oicon.setPixmap(img)
            self.picon.setPixmap(img)
            self.qicon.setPixmap(img)
            self.ricon.setPixmap(img)
            self.sicon.setPixmap(img)
            self.ticon.setPixmap(img)
            self.uicon.setPixmap(img)
            self.vicon.setPixmap(img)
            self.wicon.setPixmap(img)
            self.xicon.setPixmap(img)
            self.pushn.show()
            self.pusho.show()
            self.pushp.show()
            self.pushq.show()
            self.pushr.show()
            self.pushs.show()
            self.pusht.show()
            self.pushu.show()
            self.pushv.show()
            self.pushw.show()
            self.pushx.show()
            self.nicon.show()
            self.oicon.show()
            self.picon.show()
            self.qicon.show()
            self.ricon.show()
            self.sicon.show()
            self.ticon.show()
            self.uicon.show()
            self.vicon.show()
            self.wicon.show()
            self.xicon.show()
        elif l == 10:
            self.pushn.setText(self.sectionrange[0])
            self.pusho.setText(self.sectionrange[1])
            self.pushp.setText(self.sectionrange[2])
            self.pushq.setText(self.sectionrange[3])
            self.pushr.setText(self.sectionrange[4])
            self.pushs.setText(self.sectionrange[5])
            self.pusht.setText(self.sectionrange[6])
            self.pushu.setText(self.sectionrange[7])
            self.pushv.setText(self.sectionrange[8])
            self.pushw.setText(self.sectionrange[9])
            self.nicon.setPixmap(img)
            self.oicon.setPixmap(img)
            self.picon.setPixmap(img)
            self.qicon.setPixmap(img)
            self.ricon.setPixmap(img)
            self.sicon.setPixmap(img)
            self.ticon.setPixmap(img)
            self.uicon.setPixmap(img)
            self.vicon.setPixmap(img)
            self.wicon.setPixmap(img)
            self.pushn.show()
            self.pusho.show()
            self.pushp.show()
            self.pushq.show()
            self.pushr.show()
            self.pushs.show()
            self.pusht.show()
            self.pushu.show()
            self.pushv.show()
            self.pushw.show()
            self.nicon.show()
            self.oicon.show()
            self.picon.show()
            self.qicon.show()
            self.ricon.show()
            self.sicon.show()
            self.ticon.show()
            self.uicon.show()
            self.vicon.show()
            self.wicon.show()
        elif l == 9:
            self.pushn.setText(self.sectionrange[0])
            self.pusho.setText(self.sectionrange[1])
            self.pushp.setText(self.sectionrange[2])
            self.pushq.setText(self.sectionrange[3])
            self.pushr.setText(self.sectionrange[4])
            self.pushs.setText(self.sectionrange[5])
            self.pusht.setText(self.sectionrange[6])
            self.pushu.setText(self.sectionrange[7])
            self.pushv.setText(self.sectionrange[8])
            self.nicon.setPixmap(img)
            self.oicon.setPixmap(img)
            self.picon.setPixmap(img)
            self.qicon.setPixmap(img)
            self.ricon.setPixmap(img)
            self.sicon.setPixmap(img)
            self.ticon.setPixmap(img)
            self.uicon.setPixmap(img)
            self.vicon.setPixmap(img)
            self.pushn.show()
            self.pusho.show()
            self.pushp.show()
            self.pushq.show()
            self.pushr.show()
            self.pushs.show()
            self.pusht.show()
            self.pushu.show()
            self.pushv.show()
            self.nicon.show()
            self.oicon.show()
            self.picon.show()
            self.qicon.show()
            self.ricon.show()
            self.sicon.show()
            self.ticon.show()
            self.uicon.show()
            self.vicon.show()
        elif l == 8:
            self.pushn.setText(self.sectionrange[0])
            self.pusho.setText(self.sectionrange[1])
            self.pushp.setText(self.sectionrange[2])
            self.pushq.setText(self.sectionrange[3])
            self.pushr.setText(self.sectionrange[4])
            self.pushs.setText(self.sectionrange[5])
            self.pusht.setText(self.sectionrange[6])
            self.pushu.setText(self.sectionrange[7])
            self.nicon.setPixmap(img)
            self.oicon.setPixmap(img)
            self.picon.setPixmap(img)
            self.qicon.setPixmap(img)
            self.ricon.setPixmap(img)
            self.sicon.setPixmap(img)
            self.ticon.setPixmap(img)
            self.uicon.setPixmap(img)
            self.pushn.show()
            self.pusho.show()
            self.pushp.show()
            self.pushq.show()
            self.pushr.show()
            self.pushs.show()
            self.pusht.show()
            self.pushu.show()
            self.nicon.show()
            self.oicon.show()
            self.picon.show()
            self.qicon.show()
            self.ricon.show()
            self.sicon.show()
            self.ticon.show()
            self.uicon.show()
        elif l == 7:
            self.pushn.setText(self.sectionrange[0])
            self.pusho.setText(self.sectionrange[1])
            self.pushp.setText(self.sectionrange[2])
            self.pushq.setText(self.sectionrange[3])
            self.pushr.setText(self.sectionrange[4])
            self.pushs.setText(self.sectionrange[5])
            self.pusht.setText(self.sectionrange[6])
            self.nicon.setPixmap(img)
            self.oicon.setPixmap(img)
            self.picon.setPixmap(img)
            self.qicon.setPixmap(img)
            self.ricon.setPixmap(img)
            self.sicon.setPixmap(img)
            self.ticon.setPixmap(img)
            self.pushn.show()
            self.pusho.show()
            self.pushp.show()
            self.pushq.show()
            self.pushr.show()
            self.pushs.show()
            self.pusht.show()
            self.nicon.show()
            self.oicon.show()
            self.picon.show()
            self.qicon.show()
            self.ricon.show()
            self.sicon.show()
            self.ticon.show()
        elif l == 6:
            self.pushn.setText(self.sectionrange[0])
            self.pusho.setText(self.sectionrange[1])
            self.pushp.setText(self.sectionrange[2])
            self.pushq.setText(self.sectionrange[3])
            self.pushr.setText(self.sectionrange[4])
            self.pushs.setText(self.sectionrange[5])
            self.nicon.setPixmap(img)
            self.oicon.setPixmap(img)
            self.picon.setPixmap(img)
            self.qicon.setPixmap(img)
            self.ricon.setPixmap(img)
            self.sicon.setPixmap(img)
            self.pushn.show()
            self.pusho.show()
            self.pushp.show()
            self.pushq.show()
            self.pushr.show()
            self.pushs.show()
            self.nicon.show()
            self.oicon.show()
            self.picon.show()
            self.qicon.show()
            self.ricon.show()
            self.sicon.show()
        elif l == 5:
            self.pushn.setText(self.sectionrange[0])
            self.pusho.setText(self.sectionrange[1])
            self.pushp.setText(self.sectionrange[2])
            self.pushq.setText(self.sectionrange[3])
            self.pushr.setText(self.sectionrange[4])
            self.nicon.setPixmap(img)
            self.oicon.setPixmap(img)
            self.picon.setPixmap(img)
            self.qicon.setPixmap(img)
            self.ricon.setPixmap(img)
            self.pushn.show()
            self.pusho.show()
            self.pushp.show()
            self.pushq.show()
            self.pushr.show()
            self.nicon.show()
            self.oicon.show()
            self.picon.show()
            self.qicon.show()
            self.ricon.show()

    def ticka(self, hrs, mins, secs):
        #print("wayside ticking in class a")
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
        self.gate70.setEnabled(False)
        self.gate71.setEnabled(False)

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
        self.gate70.setEnabled(False)
        self.gate71.setEnabled(False)

    def configurationWindow(self):
        self.trackconfiguration.clicked.connect(self.runParser)

    def makeSectionWindow(self, whichsection):
        #print("in makesectionwindow")
        #print("section range", self.sectionrange)
        #print("whichsection", whichsection)
        self.bl = Ui_Section()
        self.bl.sectionname.setText("Section "+ whichsection)
        self.sectionmatrix = []
        counti = 0
        countj = 0
        
        if self.first == 1:
            currentletter = []
            currentletter.append(self.wayside1range[0])
            #print("wayside1sectionrange", self.wayside1sectionrange)
            #print("wayside1range", self.wayside1range)
            #print("wayside1 sectionrange", self.sectionrange)
            for i in self.sectionrange:
                currentletter = []
                for j in self.wayside1sectionrange:
                    if j == i:
                        currentletter.append(self.wayside1range[countj])
                    else:
                        continue
                    countj = countj + 1
                counti = counti + 1
                self.sectionmatrix.append(currentletter)
        if self.first == 2:
            #print("wayside2sectionrange", self.wayside2sectionrange)
            #print("wayside2range", self.wayside2range)
            currentletter = []
            currentletter.append(self.wayside2range[0])
            for i in self.sectionrange:
                currentletter = []
                for j in self.wayside2sectionrange:
                    if j == i:
                        currentletter.append(self.wayside2range[countj])
                    else:
                        continue
                    countj = countj + 1
                counti = counti + 1
                self.sectionmatrix.append(currentletter)
        if self.first == 3:
            #print("wayside3sectionrange", self.wayside3sectionrange)
            #print("wayside3range", self.wayside3range)
            currentletter = []
            currentletter.append(self.wayside3range[0])
            for i in self.sectionrange:
                currentletter = []
                for j in self.wayside3sectionrange:
                    if j == i:
                        currentletter.append(self.wayside3range[countj])
                    else:
                        continue
                    countj = countj + 1
                counti = counti + 1
                self.sectionmatrix.append(currentletter)
        if self.first == 4:
            #print("wayside4sectionrange", self.wayside4sectionrange)
            #print("wayside4range", self.wayside4range)
            currentletter = []
            currentletter.append(self.wayside4range[0])
            for i in self.sectionrange:
                currentletter = []
                for j in self.wayside4sectionrange:
                    if j == i:
                        currentletter.append(self.wayside4range[countj])
                    else:
                        continue
                    countj = countj + 1
                counti = counti + 1
                self.sectionmatrix.append(currentletter)
        if self.first == 5:
            #print("wayside5sectionrange", self.wayside5sectionrange)
            #print("wayside5range", self.wayside5range)
            currentletter = []
            currentletter.append(self.wayside5range[0])
            for i in self.sectionrange:
                currentletter = []
                for j in self.wayside5sectionrange:
                    if j == i:
                        currentletter.append(self.wayside5range[countj])
                    else:
                        continue
                    countj = countj + 1
                counti = counti + 1
                self.sectionmatrix.append(currentletter)
        if self.first == 6:
            #print("wayside6sectionrange", self.wayside6sectionrange)
            #print("wayside6range", self.wayside6range)
            currentletter = []
            currentletter.append(self.wayside6range[0])
            for i in self.sectionrange:
                currentletter = []
                for j in self.wayside6sectionrange:
                    if j == i:
                        currentletter.append(self.wayside6range[countj])
                    else:
                        continue
                    countj = countj + 1
                counti = counti + 1
                self.sectionmatrix.append(currentletter)
        if self.first == 7:
            #print("wayside7sectionrange", self.wayside7sectionrange)
            #print("wayside7range", self.wayside7range)
            currentletter = []
            currentletter.append(self.wayside7range[0])
            for i in self.sectionrange:
                currentletter = []
                for j in self.wayside7sectionrange:
                    if j == i:
                        currentletter.append(self.wayside7range[countj])
                    else:
                        continue
                    countj = countj + 1
                counti = counti + 1
                self.sectionmatrix.append(currentletter)
        if self.first == 8:
            #print("wayside8sectionrange", self.wayside8sectionrange)
            #print("wayside8range", self.wayside8range)
            currentletter = []
            currentletter.append(self.wayside8range[0])
            for i in self.sectionrange:
                currentletter = []
                for j in self.wayside8sectionrange:
                    if j == i:
                        currentletter.append(self.wayside8range[countj])
                    else:
                        continue
                    countj = countj + 1
                counti = counti + 1
                self.sectionmatrix.append(currentletter)
                #print("current letter",currentletter)
        #print("section", self.)
        #print("section matrix",self.sectionmatrix)
        self.sectionrow = self.sectionrange.index(whichsection)
        #print("wayside1 matrix row", self.sectionmatrix[self.sectionrow])
        self.sectionmatrixrow = self.sectionmatrix[self.sectionrow]

        #for i in range(self.sectionrow):
            #self.bl.gridLayout.setText(self.sectionmatrix[self.sectionrow][i])

        l = len(self.sectionmatrix[self.sectionrow])

        if l == 16:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))
            self.bl.block2.setText(str(self.sectionmatrix[self.sectionrow][1]))
            self.bl.block3.setText(str(self.sectionmatrix[self.sectionrow][2]))
            self.bl.block3.setText(str(self.sectionmatrix[self.sectionrow][2]))
            self.bl.block4.setText(str(self.sectionmatrix[self.sectionrow][3]))
            self.bl.block5.setText(str(self.sectionmatrix[self.sectionrow][4]))
            self.bl.block8.setText(str(self.sectionmatrix[self.sectionrow][7]))
            self.bl.block9.setText(str(self.sectionmatrix[self.sectionrow][8]))
            self.bl.block10.setText(str(self.sectionmatrix[self.sectionrow][9]))
            self.bl.block11.setText(str(self.sectionmatrix[self.sectionrow][10]))
            self.bl.block13.setText(str(self.sectionmatrix[self.sectionrow][12]))
            self.bl.block14.setText(str(self.sectionmatrix[self.sectionrow][13]))
            self.bl.block15.setText(str(self.sectionmatrix[self.sectionrow][14]))
            self.bl.block16.setText(str(self.sectionmatrix[self.sectionrow][15]))
        elif l == 15:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))
            self.bl.block2.setText(str(self.sectionmatrix[self.sectionrow][1]))
            self.bl.block3.setText(str(self.sectionmatrix[self.sectionrow][2]))
            self.bl.block4.setText(str(self.sectionmatrix[self.sectionrow][3]))
            self.bl.block5.setText(str(self.sectionmatrix[self.sectionrow][4]))
            self.bl.block6.setText(str(self.sectionmatrix[self.sectionrow][5]))
            self.bl.block7.setText(str(self.sectionmatrix[self.sectionrow][6]))
            self.bl.block8.setText(str(self.sectionmatrix[self.sectionrow][7]))
            self.bl.block9.setText(str(self.sectionmatrix[self.sectionrow][8]))
            self.bl.block10.setText(str(self.sectionmatrix[self.sectionrow][9]))
            self.bl.block11.setText(str(self.sectionmatrix[self.sectionrow][10]))
            self.bl.block12.setText(str(self.sectionmatrix[self.sectionrow][11]))
            self.bl.block13.setText(str(self.sectionmatrix[self.sectionrow][12]))
            self.bl.block14.setText(str(self.sectionmatrix[self.sectionrow][13]))
            self.bl.block15.setText(str(self.sectionmatrix[self.sectionrow][14]))
        elif l == 14:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))
            self.bl.block2.setText(str(self.sectionmatrix[self.sectionrow][1]))
            self.bl.block3.setText(str(self.sectionmatrix[self.sectionrow][2]))
            self.bl.block4.setText(str(self.sectionmatrix[self.sectionrow][3]))
            self.bl.block5.setText(str(self.sectionmatrix[self.sectionrow][4]))
            self.bl.block6.setText(str(self.sectionmatrix[self.sectionrow][5]))
            self.bl.block7.setText(str(self.sectionmatrix[self.sectionrow][6]))
            self.bl.block8.setText(str(self.sectionmatrix[self.sectionrow][7]))
            self.bl.block9.setText(str(self.sectionmatrix[self.sectionrow][8]))
            self.bl.block10.setText(str(self.sectionmatrix[self.sectionrow][9]))
            self.bl.block12.setText(str(self.sectionmatrix[self.sectionrow][11]))
            self.bl.block13.setText(str(self.sectionmatrix[self.sectionrow][12]))
            self.bl.block14.setText(str(self.sectionmatrix[self.sectionrow][13]))
        elif l == 13:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))
            self.bl.block2.setText(str(self.sectionmatrix[self.sectionrow][1]))
            self.bl.block3.setText(str(self.sectionmatrix[self.sectionrow][2]))
            self.bl.block4.setText(str(self.sectionmatrix[self.sectionrow][3]))
            self.bl.block5.setText(str(self.sectionmatrix[self.sectionrow][4]))
            self.bl.block6.setText(str(self.sectionmatrix[self.sectionrow][5]))
            self.bl.block7.setText(str(self.sectionmatrix[self.sectionrow][6]))
            self.bl.block8.setText(str(self.sectionmatrix[self.sectionrow][7]))
            self.bl.block9.setText(str(self.sectionmatrix[self.sectionrow][8]))
            self.bl.block10.setText(str(self.sectionmatrix[self.sectionrow][9]))
            self.bl.block11.setText(str(self.sectionmatrix[self.sectionrow][10]))
            self.bl.block12.setText(str(self.sectionmatrix[self.sectionrow][11]))
            self.bl.block13.setText(str(self.sectionmatrix[self.sectionrow][12]))
        elif l == 12:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))
            self.bl.block2.setText(str(self.sectionmatrix[self.sectionrow][1]))
            self.bl.block3.setText(str(self.sectionmatrix[self.sectionrow][2]))
            self.bl.block4.setText(str(self.sectionmatrix[self.sectionrow][3]))
            self.bl.block5.setText(str(self.sectionmatrix[self.sectionrow][4]))
            self.bl.block6.setText(str(self.sectionmatrix[self.sectionrow][5]))
            self.bl.block8.setText(str(self.sectionmatrix[self.sectionrow][7]))
            self.bl.block9.setText(str(self.sectionmatrix[self.sectionrow][8]))
            self.bl.block10.setText(str(self.sectionmatrix[self.sectionrow][9]))
            self.bl.block11.setText(str(self.sectionmatrix[self.sectionrow][10]))
            self.bl.block12.setText(str(self.sectionmatrix[self.sectionrow][11]))
        elif l == 11:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))
            self.bl.block2.setText(str(self.sectionmatrix[self.sectionrow][1]))
            self.bl.block3.setText(str(self.sectionmatrix[self.sectionrow][2]))
            self.bl.block4.setText(str(self.sectionmatrix[self.sectionrow][3]))
            self.bl.block5.setText(str(self.sectionmatrix[self.sectionrow][4]))
            self.bl.block6.setText(str(self.sectionmatrix[self.sectionrow][5]))
            self.bl.block8.setText(str(self.sectionmatrix[self.sectionrow][7]))
            self.bl.block9.setText(str(self.sectionmatrix[self.sectionrow][8]))
            self.bl.block10.setText(str(self.sectionmatrix[self.sectionrow][9]))
            self.bl.block11.setText(str(self.sectionmatrix[self.sectionrow][10]))
        elif l == 10:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))
            self.bl.block2.setText(str(self.sectionmatrix[self.sectionrow][1]))
            self.bl.block3.setText(str(self.sectionmatrix[self.sectionrow][2]))
            self.bl.block4.setText(str(self.sectionmatrix[self.sectionrow][3]))
            self.bl.block5.setText(str(self.sectionmatrix[self.sectionrow][4]))
            self.bl.block6.setText(str(self.sectionmatrix[self.sectionrow][5]))
            self.bl.block7.setText(str(self.sectionmatrix[self.sectionrow][6]))
            self.bl.block8.setText(str(self.sectionmatrix[self.sectionrow][7]))
            self.bl.block9.setText(str(self.sectionmatrix[self.sectionrow][8]))
            self.bl.block10.setText(str(self.sectionmatrix[self.sectionrow][9]))
        elif l == 9:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))
            self.bl.block2.setText(str(self.sectionmatrix[self.sectionrow][1]))
            self.bl.block3.setText(str(self.sectionmatrix[self.sectionrow][2]))
            self.bl.block4.setText(str(self.sectionmatrix[self.sectionrow][3]))
            self.bl.block5.setText(str(self.sectionmatrix[self.sectionrow][4]))
            self.bl.block6.setText(str(self.sectionmatrix[self.sectionrow][5]))
            self.bl.block7.setText(str(self.sectionmatrix[self.sectionrow][6]))
            self.bl.block8.setText(str(self.sectionmatrix[self.sectionrow][7]))
            self.bl.block9.setText(str(self.sectionmatrix[self.sectionrow][8]))
        elif l == 8:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))
            self.bl.block2.setText(str(self.sectionmatrix[self.sectionrow][1]))
            self.bl.block3.setText(str(self.sectionmatrix[self.sectionrow][2]))
            self.bl.block4.setText(str(self.sectionmatrix[self.sectionrow][3]))
            self.bl.block5.setText(str(self.sectionmatrix[self.sectionrow][4]))
            self.bl.block6.setText(str(self.sectionmatrix[self.sectionrow][5]))
            self.bl.block7.setText(str(self.sectionmatrix[self.sectionrow][6]))
            self.bl.block8.setText(str(self.sectionmatrix[self.sectionrow][7]))
        elif l == 7:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))
            self.bl.block2.setText(str(self.sectionmatrix[self.sectionrow][1]))
            self.bl.block3.setText(str(self.sectionmatrix[self.sectionrow][2]))
            self.bl.block4.setText(str(self.sectionmatrix[self.sectionrow][3]))
            self.bl.block5.setText(str(self.sectionmatrix[self.sectionrow][4]))
            self.bl.block6.setText(str(self.sectionmatrix[self.sectionrow][5]))
            self.bl.block7.setText(str(self.sectionmatrix[self.sectionrow][6]))
        elif l == 6:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))
            self.bl.block2.setText(str(self.sectionmatrix[self.sectionrow][1]))
            self.bl.block3.setText(str(self.sectionmatrix[self.sectionrow][2]))
            self.bl.block4.setText(str(self.sectionmatrix[self.sectionrow][3]))
            self.bl.block5.setText(str(self.sectionmatrix[self.sectionrow][4]))
            self.bl.block6.setText(str(self.sectionmatrix[self.sectionrow][5]))
        elif l == 5:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))
            self.bl.block2.setText(str(self.sectionmatrix[self.sectionrow][1]))
            self.bl.block3.setText(str(self.sectionmatrix[self.sectionrow][2]))
            self.bl.block4.setText(str(self.sectionmatrix[self.sectionrow][3]))
            self.bl.block5.setText(str(self.sectionmatrix[self.sectionrow][4]))
        elif l == 4:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))
            self.bl.block2.setText(str(self.sectionmatrix[self.sectionrow][1]))
            self.bl.block3.setText(str(self.sectionmatrix[self.sectionrow][2]))
            self.bl.block4.setText(str(self.sectionmatrix[self.sectionrow][3]))
        elif l == 3:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))
            self.bl.block2.setText(str(self.sectionmatrix[self.sectionrow][1]))
            self.bl.block3.setText(str(self.sectionmatrix[self.sectionrow][2]))
        elif l == 2:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))
            self.bl.block2.setText(str(self.sectionmatrix[self.sectionrow][1]))
        elif l == 1:
            self.bl.block1.setText(str(self.sectionmatrix[self.sectionrow][0]))

        h = 30 + 46*len(self.sectionmatrix[self.sectionrow])
        self.bl.resize(250, h) 
        self.bl.show()

    #function for toggle switch colors but see if you can do labels instead of buttons??
    def toggleColor(self, button1, button2):
        button1.setEnabled(False)
        button2.setEnabled(True)
        button1.setStyleSheet('background-color: SkyBlue; color: black')
        button2.setStyleSheet('background-color: white; color: gray')

    #occupation 2 blocks ahead for now
    #!!!!!! TO DO !!!!!!!!!
    def changeOccupancy(self, line, block, sec, auth):
        #print("change occ line block sec", line, block, sec)
        img = QPixmap('greentrain.png')
        self.occupied.append(block)
        #auth = QPixmap('redtracks.png')
        #print("occupied blocks", self.occupied)
        
        if self.first == 1 and line == 'Green':
            #secbutton = self.wayside1sectionrange.index(sec)
            #print("change", secbutton, "button down in 1")
            #print("wayside1sectionrange",self.wayside1sectionrange)
            if sec == 'A':
                self.nicon.setPixmap(img)
            elif sec == 'B':
                self.oicon.setPixmap(img)
            elif sec == 'C':
                self.picon.setPixmap(img)
            elif sec == 'D':
                self.qicon.setPixmap(img)
            elif sec == 'E':
                self.ricon.setPixmap(img)
            elif sec == 'F':
                self.sicon.setPixmap(img)
            elif sec == 'G':
                self.ticon.setPixmap(img)
            elif sec == 'H':
                self.uicon.setPixmap(img)
            elif sec == 'I':
                self.vicon.setPixmap(img)
            elif sec == 'J':
                self.wicon.setPixmap(img)
            elif sec == 'K':
                self.xicon.setPixmap(img)
            elif sec == 'L':
                self.yicon.setPixmap(img)
            elif sec == 'M':
                self.zicon.setPixmap(img)
            else:
                print("occupied section not on this wayside")
        elif self.first == 2 and line == 'Green':
            #secbutton = self.wayside2sectionrange.index(sec)
            #print("change", secbutton, "button down in 2")
            if sec == 'I':
                self.nicon.setPixmap(img)
            elif sec == 'J':
                self.oicon.setPixmap(img)
            elif sec == 'K':
                self.picon.setPixmap(img)
            elif sec == 'L':
                self.qicon.setPixmap(img)
            elif sec == 'M':
                self.ricon.setPixmap(img)
            elif sec == 'N':
                self.sicon.setPixmap(img)
            elif sec == 'O':
                self.ticon.setPixmap(img)
            elif sec == 'P':
                self.uicon.setPixmap(img)
            elif sec == 'Q':
                self.vicon.setPixmap(img)
            elif sec == 'R':
                self.wicon.setPixmap(img)
            elif sec == 'S':
                self.xicon.setPixmap(img)
            elif sec == 'T':
                self.yicon.setPixmap(img)
            elif sec == 'U':
                self.zicon.setPixmap(img)
            else:
                print("occupied section not on this wayside")
            #print("wayside2sectionrange",self.wayside2sectionrange)
        elif self.first == 3 and line == 'Green':
            #secbutton = self.wayside3sectionrange.index(sec)
            #print("change", secbutton, "button down in 3")
            if sec == 'M':
                self.nicon.setPixmap(img)
            elif sec == 'N':
                self.oicon.setPixmap(img)
            elif sec == 'O':
                self.picon.setPixmap(img)
            elif sec == 'P':
                self.qicon.setPixmap(img)
            elif sec == 'Q':
                self.ricon.setPixmap(img)
            elif sec == 'R':
                self.sicon.setPixmap(img)
            elif sec == 'S':
                self.ticon.setPixmap(img)
            elif sec == 'T':
                self.uicon.setPixmap(img)
            elif sec == 'U':
                self.vicon.setPixmap(img)
            elif sec == 'V':
                self.wicon.setPixmap(img)
            elif sec == 'W':
                self.xicon.setPixmap(img)
            elif sec == 'X':
                self.yicon.setPixmap(img)
            elif sec == 'Y':
                self.zicon.setPixmap(img)
            elif sec == 'Z':
                self.yicon.setPixmap(img)
            elif sec == 'A':
                self.zicon.setPixmap(img)
            else:
                print("occupied section not on this wayside")
            #print("wayside3sectionrange",self.wayside3sectionrange)
        elif self.first == 4 and line == 'Green':
            #secbutton = self.wayside4sectionrange.index(sec)
            #print("change", secbutton, "button down in 4")
            if sec == 'U':
                self.nicon.setPixmap(img)
            elif sec == 'V':
                self.oicon.setPixmap(img)
            elif sec == 'W':
                self.picon.setPixmap(img)
            elif sec == 'X':
                self.qicon.setPixmap(img)
            elif sec == 'Y':
                self.ricon.setPixmap(img)
            elif sec == 'Z':
                self.sicon.setPixmap(img)
            elif sec == 'A':
                self.ticon.setPixmap(img)
            elif sec == 'B':
                self.uicon.setPixmap(img)
            elif sec == 'C':
                self.vicon.setPixmap(img)
            elif sec == 'D':
                self.wicon.setPixmap(img)
            elif sec == 'E':
                self.xicon.setPixmap(img)
            elif sec == 'F':
                self.yicon.setPixmap(img)
            elif sec == 'G':
                self.zicon.setPixmap(img)
            elif sec == 'H':
                self.yicon.setPixmap(img)
            elif sec == 'I':
                self.zicon.setPixmap(img)
            else:
                print("occupied section not on this wayside")
        elif self.first == 5 and line == 'Red':
            #secbutton = self.wayside5sectionrange.index(sec)
            #print("change", secbutton, "button down in 5")
            if sec == 'A':
                self.nicon.setPixmap(img)
            elif sec == 'B':
                self.oicon.setPixmap(img)
            elif sec == 'C':
                self.picon.setPixmap(img)
            elif sec == 'D':
                self.qicon.setPixmap(img)
            elif sec == 'E':
                self.ricon.setPixmap(img)
            elif sec == 'F':
                self.sicon.setPixmap(img)
            elif sec == 'G':
                self.ticon.setPixmap(img)
            elif sec == 'H':
                self.uicon.setPixmap(img)
            else:
                print("occupied section not on this wayside")
        elif self.first == 6 and line == 'Red':
            #secbutton = self.wayside6sectionrange.index(sec)
            #print("change", secbutton, "button down in 6")
            if  sec == 'F':
                self.nicon.setPixmap(img)
            elif sec == 'G':
                self.oicon.setPixmap(img)
            elif sec == 'H':
                self.picon.setPixmap(img)
            elif sec == 'I':
                self.qicon.setPixmap(img)
            elif sec == 'J':
                self.ricon.setPixmap(img)
            elif sec == 'K':
                self.sicon.setPixmap(img)
            else:
                print("occupied section not on this wayside")
        elif self.first == 7 and line == 'Red':
            #secbutton = self.wayside7sectionrange.index(sec)
            #print("change", secbutton, "button down in 7")
            
            if sec == 'H':
                self.nicon.setPixmap(img)
            elif sec == 'I':
                self.oicon.setPixmap(img)
            elif sec == 'J':
                self.picon.setPixmap(img)
            elif sec == 'K':
                self.qicon.setPixmap(img)
            elif sec == 'L':
                self.ricon.setPixmap(img)
            elif sec == 'M':
                self.sicon.setPixmap(img)
            elif sec == 'N':
                self.ticon.setPixmap(img)
            elif sec == 'O':
                self.uicon.setPixmap(img)
            elif sec == 'P':
                self.vicon.setPixmap(img)
            elif sec == 'Q':
                self.wicon.setPixmap(img)
            elif sec == 'R':
                self.xicon.setPixmap(img)
            elif sec == 'S':
                self.yicon.setPixmap(img)
            elif sec == 'T':
                self.zicon.setPixmap(img)
            elif sec == 'A':
                self.aaicon.setPixmap(img)
            else:
                print("occupied section not on this wayside")
        elif self.first == 8 and line == 'Red':
            #secbutton = self.wayside8sectionrange.index(sec)
            #print("change", secbutton, "button down in 8")
            if  sec == 'K':
                self.nicon.setPixmap(img)
            elif sec == 'L':
                self.oicon.setPixmap(img)
            elif sec == 'M':
                self.picon.setPixmap(img)
            elif sec == 'N':
                self.qicon.setPixmap(img)
            elif sec == 'O':
                self.ricon.setPixmap(img)
            elif sec == 'P':
                self.sicon.setPixmap(img)
            elif sec == 'Q':
                self.ticon.setPixmap(img)
            elif sec == 'R':
                self.uicon.setPixmap(img)
            elif sec == 'S':
                self.vicon.setPixmap(img)
            elif sec == 'T':
                self.wicon.setPixmap(img)
            elif sec == 'A':
                self.xicon.setPixmap(img)
            elif sec == 'B':
                self.yicon.setPixmap(img)
            elif sec == 'C':
                self.zicon.setPixmap(img)
            elif sec == 'D':
                self.aaicon.setPixmap(img)
            elif sec == 'E':
                self.bbicon.setPixmap(img)
            elif sec == 'F':
                self.ccicon.setPixmap(img)
            else:
                print("occupied section not on this wayside")
        # print("sectionrange", self.sectionrange)
        # try:
        #     rowindex = self.sectionrange.index(self.sectionrow)
        #     print("rowindex", rowindex)
        #     nextrow = self.ssectionrange[rowindex+1]
        #     print("nextrow", nextrow)
        #     self.sectionmatrixrow = self.sectionmatrix[self.sectionrow]
        # except:
        #     return

        image = QLabel()
        pic = QPixmap('greentrain.png')
        image.setPixmap(pic.scaled(50, 50))
        auth1 = QLabel()
        pica = QPixmap('redtracks.png')
        auth1.setPixmap(pica.scaled(50, 50))
        auth2 = QLabel()
        auth2.setPixmap(pica.scaled(50, 50))
        auth3 = QLabel()
        auth3.setPixmap(pica.scaled(50, 50))
        auth4 = QLabel()
        auth4.setPixmap(pica.scaled(50, 50))
        auth5 = QLabel()
        auth5.setPixmap(pica.scaled(50, 50))
        auth6 = QLabel()
        auth6.setPixmap(pica.scaled(50, 50))
        auth7 = QLabel()
        auth7.setPixmap(pica.scaled(50, 50))
        auth8 = QLabel()
        auth8.setPixmap(pica.scaled(50, 50))
        for i in self.sectionmatrixrow:
            #print("in forloop i", i)
            for j in self.occupied:
                #print("in forloop j", j)
                if i == j:
                    #print("i = j", i, j)
                    index = self.sectionmatrixrow.index(i) +1
                    self.bl.gridLayout.addWidget(image, index, 1)
                    if auth == 1:
                        self.bl.gridLayout.addWidget(auth1, index+1, 1)
                    elif auth == 2:
                        self.bl.gridLayout.addWidget(auth1, index+1, 1)
                        self.bl.gridLayout.addWidget(auth2, index+2, 1)
                    elif auth == 3:
                        self.bl.gridLayout.addWidget(auth1, index+1, 1)
                        self.bl.gridLayout.addWidget(auth2, index+2, 1)
                        self.bl.gridLayout.addWidget(auth3, index+3, 1)
                    elif auth == 4:
                        self.bl.gridLayout.addWidget(auth1, index+1, 1)
                        self.bl.gridLayout.addWidget(auth2, index+2, 1)
                        self.bl.gridLayout.addWidget(auth3, index+3, 1)
                        self.bl.gridLayout.addWidget(auth4, index+4, 1)
                    elif auth == 5:
                        self.bl.gridLayout.addWidget(auth1, index+1, 1)
                        self.bl.gridLayout.addWidget(auth2, index+2, 1)
                        self.bl.gridLayout.addWidget(auth3, index+3, 1)
                        self.bl.gridLayout.addWidget(auth4, index+4, 1)
                        self.bl.gridLayout.addWidget(auth5, index+5, 1)
                    elif auth == 6:
                        self.bl.gridLayout.addWidget(auth1, index+1, 1)
                        self.bl.gridLayout.addWidget(auth2, index+2, 1)
                        self.bl.gridLayout.addWidget(auth3, index+3, 1)
                        self.bl.gridLayout.addWidget(auth4, index+4, 1)
                        self.bl.gridLayout.addWidget(auth5, index+5, 1)
                        self.bl.gridLayout.addWidget(auth6, index+6, 1)
                    elif auth == 7:
                        self.bl.gridLayout.addWidget(auth1, index+1, 1)
                        self.bl.gridLayout.addWidget(auth2, index+2, 1)
                        self.bl.gridLayout.addWidget(auth3, index+3, 1)
                        self.bl.gridLayout.addWidget(auth4, index+4, 1)
                        self.bl.gridLayout.addWidget(auth5, index+5, 1)
                        self.bl.gridLayout.addWidget(auth6, index+6, 1)
                        self.bl.gridLayout.addWidget(auth7, index+7, 1)
                    elif auth == 8:
                        self.bl.gridLayout.addWidget(auth1, index+1, 1)
                        self.bl.gridLayout.addWidget(auth2, index+2, 1)
                        self.bl.gridLayout.addWidget(auth3, index+3, 1)
                        self.bl.gridLayout.addWidget(auth4, index+4, 1)
                        self.bl.gridLayout.addWidget(auth5, index+5, 1)
                        self.bl.gridLayout.addWidget(auth6, index+6, 1)
                        self.bl.gridLayout.addWidget(auth7, index+7, 1)
                        self.bl.gridLayout.addWidget(auth8, index+8, 1)


    def changeVacancy(self, line, block, sec):
        #print("wayside a UI block", block, "is vacant")
        #train is sending next block not previous so have jake look at that
        img = QPixmap('tracks.png')
        #print("vacancy line, block, sec", line, block, sec)
        try:
            find = self.occupied.index(block)
            #print("find", find)
            self.occupied.pop(find)
        except:
            pass
            #print("no blocks occupied yet")
        #print("occupied blocks from vacancy", self.occupied)
        
        if self.first == 1:
            #secbutton = self.wayside1sectionrange.index(sec)
            #print("change", secbutton, "button down in 1")
            #print("wayside1sectionrange",self.wayside1sectionrange)
            if sec == 'A':
                self.nicon.setPixmap(img)
            elif sec == 'B':
                self.oicon.setPixmap(img)
            elif sec == 'C':
                self.picon.setPixmap(img)
            elif sec == 'D':
                self.qicon.setPixmap(img)
            elif sec == 'E':
                self.ricon.setPixmap(img)
            elif sec == 'F':
                self.sicon.setPixmap(img)
            elif sec == 'G':
                self.ticon.setPixmap(img)
            elif sec == 'H':
                self.uicon.setPixmap(img)
            elif sec == 'I':
                self.vicon.setPixmap(img)
            elif sec == 'J':
                self.wicon.setPixmap(img)
            elif sec == 'K':
                self.xicon.setPixmap(img)
            elif sec == 'L':
                self.yicon.setPixmap(img)
            elif sec == 'M':
                self.zicon.setPixmap(img)
            else:
                print("vacant section not on this wayside")
        elif self.first == 2:
            #secbutton = self.wayside2sectionrange.index(sec)
            #print("change", secbutton, "button down in 2")
            if sec == 'I':
                self.nicon.setPixmap(img)
            elif sec == 'J':
                self.oicon.setPixmap(img)
            elif sec == 'K':
                self.picon.setPixmap(img)
            elif sec == 'L':
                self.qicon.setPixmap(img)
            elif sec == 'M':
                self.ricon.setPixmap(img)
            elif sec == 'N':
                self.sicon.setPixmap(img)
            elif sec == 'O':
                self.ticon.setPixmap(img)
            elif sec == 'P':
                self.uicon.setPixmap(img)
            elif sec == 'Q':
                self.vicon.setPixmap(img)
            elif sec == 'R':
                self.wicon.setPixmap(img)
            elif sec == 'S':
                self.xicon.setPixmap(img)
            elif sec == 'T':
                self.yicon.setPixmap(img)
            elif sec == 'U':
                self.zicon.setPixmap(img)
            else:
                print("vacant section not on this wayside")
            #print("wayside2sectionrange",self.wayside2sectionrange)
        elif self.first == 3:
            #secbutton = self.wayside3sectionrange.index(sec)
            #print("change", secbutton, "button down in 3")
            if sec == 'M':
                self.nicon.setPixmap(img)
            elif sec == 'N':
                self.oicon.setPixmap(img)
            elif sec == 'O':
                self.picon.setPixmap(img)
            elif sec == 'P':
                self.qicon.setPixmap(img)
            elif sec == 'Q':
                self.ricon.setPixmap(img)
            elif sec == 'R':
                self.sicon.setPixmap(img)
            elif sec == 'S':
                self.ticon.setPixmap(img)
            elif sec == 'T':
                self.uicon.setPixmap(img)
            elif sec == 'U':
                self.vicon.setPixmap(img)
            elif sec == 'V':
                self.wicon.setPixmap(img)
            elif sec == 'W':
                self.xicon.setPixmap(img)
            elif sec == 'X':
                self.yicon.setPixmap(img)
            elif sec == 'Y':
                self.zicon.setPixmap(img)
            elif sec == 'Z':
                self.yicon.setPixmap(img)
            elif sec == 'A':
                self.zicon.setPixmap(img)
            else:
                print("vacant section not on this wayside")
            #print("wayside3sectionrange",self.wayside3sectionrange)
        elif self.first == 4:
            #secbutton = self.wayside4sectionrange.index(sec)
            #print("change", secbutton, "button down in 4")
            if sec == 'U':
                self.nicon.setPixmap(img)
            elif sec == 'V':
                self.oicon.setPixmap(img)
            elif sec == 'W':
                self.picon.setPixmap(img)
            elif sec == 'X':
                self.qicon.setPixmap(img)
            elif sec == 'Y':
                self.ricon.setPixmap(img)
            elif sec == 'Z':
                self.sicon.setPixmap(img)
            elif sec == 'A':
                self.ticon.setPixmap(img)
            elif sec == 'B':
                self.uicon.setPixmap(img)
            elif sec == 'C':
                self.vicon.setPixmap(img)
            elif sec == 'D':
                self.wicon.setPixmap(img)
            elif sec == 'E':
                self.xicon.setPixmap(img)
            elif sec == 'F':
                self.yicon.setPixmap(img)
            elif sec == 'G':
                self.zicon.setPixmap(img)
            elif sec == 'H':
                self.yicon.setPixmap(img)
            elif sec == 'I':
                self.zicon.setPixmap(img)
            else:
                print("vacant section not on this wayside")
        elif self.first == 5:
            #secbutton = self.wayside5sectionrange.index(sec)
            #print("change", secbutton, "button down in 5")
            if sec == 'A':
                self.nicon.setPixmap(img)
            elif sec == 'B':
                self.oicon.setPixmap(img)
            elif sec == 'C':
                self.picon.setPixmap(img)
            elif sec == 'D':
                self.qicon.setPixmap(img)
            elif sec == 'E':
                self.ricon.setPixmap(img)
            elif sec == 'F':
                self.sicon.setPixmap(img)
            elif sec == 'G':
                self.ticon.setPixmap(img)
            elif sec == 'H':
                self.uicon.setPixmap(img)
            else:
                print("vacant section not on this wayside")
        elif self.first == 6:
            #secbutton = self.wayside6sectionrange.index(sec)
            #print("change", secbutton, "button down in 6")
            if  sec == 'F':
                self.nicon.setPixmap(img)
            elif sec == 'G':
                self.oicon.setPixmap(img)
            elif sec == 'H':
                self.picon.setPixmap(img)
            elif sec == 'I':
                self.qicon.setPixmap(img)
            elif sec == 'J':
                self.ricon.setPixmap(img)
            elif sec == 'K':
                self.sicon.setPixmap(img)
            else:
                print("vacant section not on this wayside")
        elif self.first == 7:
            #secbutton = self.wayside7sectionrange.index(sec)
            #print("change", secbutton, "button down in 7")
            
            if sec == 'H':
                self.nicon.setPixmap(img)
            elif sec == 'I':
                self.oicon.setPixmap(img)
            elif sec == 'J':
                self.picon.setPixmap(img)
            elif sec == 'K':
                self.qicon.setPixmap(img)
            elif sec == 'L':
                self.ricon.setPixmap(img)
            elif sec == 'M':
                self.sicon.setPixmap(img)
            elif sec == 'N':
                self.ticon.setPixmap(img)
            elif sec == 'O':
                self.uicon.setPixmap(img)
            elif sec == 'P':
                self.vicon.setPixmap(img)
            elif sec == 'Q':
                self.wicon.setPixmap(img)
            elif sec == 'R':
                self.xicon.setPixmap(img)
            elif sec == 'S':
                self.yicon.setPixmap(img)
            elif sec == 'T':
                self.zicon.setPixmap(img)
            elif sec == 'A':
                self.aaicon.setPixmap(img)
            else:
                print("vacant section not on this wayside")
        elif self.first == 8:
            #secbutton = self.wayside8sectionrange.index(sec)
            #print("change", secbutton, "button down in 8")
            if  sec == 'K':
                self.nicon.setPixmap(img)
            elif sec == 'L':
                self.oicon.setPixmap(img)
            elif sec == 'M':
                self.picon.setPixmap(img)
            elif sec == 'N':
                self.qicon.setPixmap(img)
            elif sec == 'O':
                self.ricon.setPixmap(img)
            elif sec == 'P':
                self.sicon.setPixmap(img)
            elif sec == 'Q':
                self.ticon.setPixmap(img)
            elif sec == 'R':
                self.uicon.setPixmap(img)
            elif sec == 'S':
                self.vicon.setPixmap(img)
            elif sec == 'T':
                self.wicon.setPixmap(img)
            elif sec == 'A':
                self.xicon.setPixmap(img)
            elif sec == 'B':
                self.yicon.setPixmap(img)
            elif sec == 'C':
                self.zicon.setPixmap(img)
            elif sec == 'D':
                self.aaicon.setPixmap(img)
            elif sec == 'E':
                self.bbicon.setPixmap(img)
            elif sec == 'F':
                self.ccicon.setPixmap(img)
            else:
                print("vacant section not on this wayside")
        
        imagev = QLabel()
        pic = QPixmap('tracks.png')
        blank = QLabel()
        bla = QPixmap('blank.png') 
        imagev.setPixmap(pic.scaled(50, 50))
        blank.setPixmap(bla.scaled(50, 50))
        for i in self.sectionmatrixrow:
            #print("in forloop i", i)
            if i == block:
                index = self.sectionmatrixrow.index(i)+1
                #self.bl.gridLayout.removeWidget(self.image)
                #self.bl.image.hide()
                self.bl.gridLayout.addWidget(blank, index, 1)
                self.bl.gridLayout.addWidget(imagev, index, 1)


     #function for number of active trains
    #somehow counts the number of times the red train label comes up
    def activeTrains(self, counts):
        self.activetrains.display(counts)
            
class Ui_Section(QtWidgets.QMainWindow, Ui_Section):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ui_Section, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Block Information')

class selectionWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.select = QComboBox()
        self.resize(200, 120)
        self.select.setStyleSheet("font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
        self.select.addItem("Select Wayside")
        self.select.addItem("Green Wayside 1")
        self.select.addItem("Green Wayside 2")
        self.select.addItem("Green Wayside 3")
        self.select.addItem("Green Wayside 4")
        self.select.addItem("Red Wayside 1")
        self.select.addItem("Red Wayside 2")
        self.select.addItem("Red Wayside 3")
        self.select.addItem("Red Wayside 4")
        self.select.setCurrentIndex(0)
        layout.addWidget(self.select)
        self.setLayout(layout)
        self.select.currentTextChanged.connect(self.showmain)
        
        #signals.waysidefirst.emit(1)
              
        
    def showmain(self):
        self.main = WMainWindowA()
        self.current = self.select.currentIndex()
        #print("current from selection", self.current)
        signals.waysidefirst.emit(self.current)
        self.main.show()
        self.close()



'''#app = QtWidgets.QApplication(sys.argv)
#windowA = WMainWindowA()
#windowB = WMainWindowB()
#first = selectionWindow()

#funcA = WaysideUIFunctions(windowA)
#funcB = WaysideUIFunctions(windowB)
#windowA.show()
#windowB.show()
#first.show()
#app.exec()'''

'''# MainWindowB A-M
#class WMainWindowB(QtWidgets.QMainWindow, Ui_MainWindowB):
#     def __init__(self, *args, obj=None, **kwargs):
#         super(WMainWindowB, self).__init__(*args, **kwargs)
#         self.setupUi(self)

#         self.setWindowTitle('Wayside Main UI')

#         #signals
#         signals.wtowVacancy.connect(self.changeVacancy)
#         signals.wtowOccupancy.connect(self.changeOccupancy)
#         signals.timerTicked.connect(self.tickb)
#         signals.wtowTrainCount.connect(self.activeTrains)
        
        

#         #set all switch buttons to disabled
#         self.gate10.setEnabled(False)
#         self.gate11.setEnabled(False)
#         self.gate20.setEnabled(False)
#         self.gate21.setEnabled(False)
#         self.gate30.setEnabled(False)
#         self.gate31.setEnabled(False)
#         self.gate40.setEnabled(False)
#         self.gate41.setEnabled(False)
#         self.gate50.setEnabled(False)
#         self.gate51.setEnabled(False)
#         self.gate60.setEnabled(False)
#         self.gate61.setEnabled(False)

#         #switch button colors
#         self.automaticmode.setDown(True)
#         self.automaticmode.setDown(True)
#         self.gate10.clicked.connect(lambda: self.toggleColor(self.gate10, self.gate11))
#         self.gate10.setStyleSheet('background-color: SkyBlue')
#         self.gate11.clicked.connect(lambda: self.toggleColor(self.gate11, self.gate10))
#         self.gate11.setStyleSheet('background-color: white; color: gray')
#         self.gate20.clicked.connect(lambda: self.toggleColor(self.gate20, self.gate21))
#         self.gate21.setStyleSheet('background-color: SkyBlue')
#         self.gate21.clicked.connect(lambda: self.toggleColor(self.gate21, self.gate20))
#         self.gate20.setStyleSheet('background-color: white; color: gray')
#         self.gate30.clicked.connect(lambda: self.toggleColor(self.gate30, self.gate31))
#         self.gate30.setStyleSheet('background-color: SkyBlue')
#         self.gate31.clicked.connect(lambda: self.toggleColor(self.gate31, self.gate30))
#         self.gate31.setStyleSheet('background-color: white; color: gray')
#         self.gate40.clicked.connect(lambda: self.toggleColor(self.gate40, self.gate41))
#         self.gate41.setStyleSheet('background-color: SkyBlue')
#         self.gate41.clicked.connect(lambda: self.toggleColor(self.gate41, self.gate40))
#         self.gate40.setStyleSheet('background-color: white; color: gray')
#         self.gate50.clicked.connect(lambda: self.toggleColor(self.gate50, self.gate51))
#         self.gate51.setStyleSheet('background-color: SkyBlue')
#         self.gate51.clicked.connect(lambda: self.toggleColor(self.gate51, self.gate50))
#         self.gate50.setStyleSheet('background-color: white; color: gray')
#         self.gate60.clicked.connect(lambda: self.toggleColor(self.gate60, self.gate61))
#         self.gate61.setStyleSheet('background-color: SkyBlue')
#         self.gate61.clicked.connect(lambda: self.toggleColor(self.gate61, self.gate60))
#         self.gate60.setStyleSheet('background-color: white; color: gray')

#         #pop up windows
#         self.trackconfiguration.clicked.connect(self.configurationWindow)
#         self.pusha.clicked.connect(lambda: self.makeSectionWindow('A'))
#         self.pushb.clicked.connect(lambda: self.makeSectionWindow('B'))
#         self.pushc.clicked.connect(lambda: self.makeSectionWindow('C'))
#         self.pushd.clicked.connect(lambda: self.makeSectionWindow('D'))
#         self.pushe.clicked.connect(lambda: self.makeSectionWindow('E'))
#         self.pushf.clicked.connect(lambda: self.makeSectionWindow('F'))
#         self.pushg.clicked.connect(lambda: self.makeSectionWindow('G'))
#         self.pushh.clicked.connect(lambda: self.makeSectionWindow('H'))
#         self.pushi.clicked.connect(lambda: self.makeSectionWindow('I'))
#         self.pushj.clicked.connect(lambda: self.makeSectionWindow('J'))
#         self.pushk.clicked.connect(lambda: self.makeSectionWindow('K'))
#         self.pushl.clicked.connect(lambda: self.makeSectionWindow('L'))
#         self.pushm.clicked.connect(lambda: self.makeSectionWindow('M'))
#         #self.pushn.clicked.connect(lambda: self.makeSectionWindow('N'))

#         #set up gate buttons
#         self.maintenancemode.toggled.connect(self.maintenanceMode)
#         self.automaticmode.toggled.connect(self.automaticMode)

#         #active trains
#         self.aicon.setPixmap(QPixmap('tracks.png'))
#         self.bicon.setPixmap(QPixmap('tracks.png'))
#         self.cicon.setPixmap(QPixmap('tracks.png'))
#         self.dicon.setPixmap(QPixmap('tracks.png'))
#         #self.eicon.setPixmap(QPixmap('redtracks.png'))
#         #self.ficon.setPixmap(QPixmap('redtracks.png'))
#         self.jicon.setPixmap(QPixmap('tracks.png'))
        
#         counts = 0
#         self.activetrains.display(counts)

#         #lights
#         self.reda.setPixmap(QPixmap('greenlight.png'))
#         #self.greenb.setPixmap(QPixmap('greenlight.png'))

#     def tickb(self, hrs, mins, secs):
#         #print("wayside ticking in class b")
#         timenow = str(hrs)+":"+str(mins)+":"+str(secs)
#         #print(timenow)
#         self.time.setText(f'{int(hrs):02d}' + ':' + f'{int(mins):02d}' + ':' + f'{int(secs):02d}')

#     def maintenanceMode(self):  
#         #print("in maintenance mode") 
#         self.gate10.setEnabled(True)
#         self.gate11.setEnabled(True)
#         self.gate20.setEnabled(True)
#         self.gate21.setEnabled(True)
#         self.gate30.setEnabled(True)
#         self.gate31.setEnabled(True)
#         self.gate40.setEnabled(True)
#         self.gate41.setEnabled(True)
#         self.gate50.setEnabled(True)
#         self.gate51.setEnabled(True)
#         self.gate60.setEnabled(True)
#         self.gate61.setEnabled(True)

#     def automaticMode(self):
#         #print("in automatic mode") 
#         self.gate10.setEnabled(False)
#         self.gate11.setEnabled(False)
#         self.gate20.setEnabled(False)
#         self.gate21.setEnabled(False)
#         self.gate30.setEnabled(False)
#         self.gate31.setEnabled(False)
#         self.gate40.setEnabled(False)
#         self.gate41.setEnabled(False)
#         self.gate50.setEnabled(False)
#         self.gate51.setEnabled(False)
#         self.gate60.setEnabled(False)
#         self.gate61.setEnabled(False)

#     #function for pop up window for track configuration
#     def configurationWindow(self):
#         self.trackconfiguration.clicked.connect(self.runParser)

#     def runParser(self):
#         PLCParser.parse(self)

#     def makeSectionWindow(self, whichsection):
#         self.bl = Ui_Section()
#         self.bl.sectionname.setText("Section "+ whichsection)
        
#         image = QLabel()
#         pic = QPixmap('tracks.png')
#         image.setPixmap(pic.scaled(50, 50))
#         image1 = QLabel()
#         pic = QPixmap('tracks.png')
#         image1.setPixmap(pic.scaled(50, 50))
#         image2 = QLabel()
#         pic = QPixmap('tracks.png')
#         image2.setPixmap(pic.scaled(50, 50))
#         image3 = QLabel()
#         pic = QPixmap('tracks.png')
#         image3.setPixmap(pic.scaled(50, 50))
#         image4 = QLabel()
#         pic = QPixmap('tracks.png')
#         image4.setPixmap(pic.scaled(50, 50))
#         image5 = QLabel()
#         pic = QPixmap('tracks.png')
#         image5.setPixmap(pic.scaled(50, 50))
#         image6 = QLabel()
#         pic = QPixmap('tracks.png')
#         image6.setPixmap(pic.scaled(50, 50))
#         image7 = QLabel()
#         pic = QPixmap('tracks.png')
#         image7.setPixmap(pic.scaled(50, 50))
#         image8 = QLabel()
#         pic = QPixmap('tracks.png')
#         image8.setPixmap(pic.scaled(50, 50))
#         image9 = QLabel()
#         pic = QPixmap('tracks.png')
#         image9.setPixmap(pic.scaled(50, 50))
#         image10 = QLabel()
#         pic = QPixmap('tracks.png')
#         image10.setPixmap(pic.scaled(50, 50))
#         image11 = QLabel()
#         pic = QPixmap('tracks.png')
#         image11.setPixmap(pic.scaled(50, 50))
#         image12 = QLabel()
#         pic = QPixmap('tracks.png')
#         image12.setPixmap(pic.scaled(50, 50))
#         image13 = QLabel()
#         pic = QPixmap('tracks.png')
#         image13.setPixmap(pic.scaled(50, 50))
#         image14 = QLabel()
#         pic = QPixmap('tracks.png')
#         image14.setPixmap(pic.scaled(50, 50))
#         image15 = QLabel()
#         pic = QPixmap('tracks.png')
#         image15.setPixmap(pic.scaled(50, 50))
#         image16 = QLabel()
#         pic = QPixmap('tracks.png')
#         image16.setPixmap(pic.scaled(50, 50))
#         image17 = QLabel()
#         pic = QPixmap('tracks.png')
#         image17.setPixmap(pic.scaled(50, 50))
#         self.bl.gridLayout.addWidget(image1, 2,1)
#         self.bl.gridLayout.addWidget(image1, 2,1)
#         switch = QLabel("X")
#         switch2 = QLabel("X")

#         if whichsection == 'A':
#             #'1' or '2'or '3':
#             self.bl.label_5.setText('1')
#             self.bl.gridLayout.addWidget(switch, 1,2)
#             switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.label_6.setText('2')
#             self.bl.label_7.setText('3')
#             self.bl.label_8.hide()
#             self.bl.dicon.hide()
#             self.bl.label_9.hide()
#             self.bl.eicon.hide()
#             self.bl.show()
#         elif whichsection == 'B':
#             #'4'or '5'or '6':
#             self.bl.label_5.setText('4')
#             self.bl.label_6.setText('5')
#             self.bl.label_7.setText('6')
#             self.bl.label_8.hide()
#             self.bl.dicon.hide()
#             self.bl.label_9.hide()
#             self.bl.eicon.hide()
#             self.bl.show()
#         elif whichsection == 'C':
#             #'7' or '8' or '9' or '10' or '11' or '12':
#             self.bl.label_5.setText('7')
#             self.bl.label_6.setText('8')
#             self.bl.label_7.setText('9')
#             self.bl.label_8.setText('10')
#             self.bl.label_9.setText('11')
#             label_10 = QLabel('12')
#             label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(label_10, 6,0)
#             self.bl.gridLayout.addWidget(image2,6,1)
#             self.bl.gridLayout.addWidget(switch, 6,2)
#             switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.show()
#         elif whichsection == 'D':
#             #'13' or '14' or '15' or '16':
#             self.bl.label_5.setText('13')
#             self.bl.label_6.setText('14')
#             self.bl.label_7.setText('15')
#             self.bl.label_8.setText('16')
#             self.bl.label_9.hide()
#             self.bl.eicon.hide()
#             self.bl.show()
#         elif whichsection == 'E':
#             #'17' or '18' or '19' or '20':
#             self.bl.label_5.setText('17')
#             self.bl.label_6.setText('18')
#             self.bl.label_7.setText('19')
#             self.bl.label_8.setText('20')
#             self.bl.label_9.hide()
#             self.bl.eicon.hide()
#             self.bl.show()
#         elif whichsection == 'F':
#             #'21' or '22' or '23' or '24' or '25' or '26' or '27' or '28':
#             self.bl.label_5.setText('21')
#             self.bl.label_6.setText('22')
#             self.bl.label_7.setText('23')
#             self.bl.label_8.setText('24')
#             self.bl.label_9.setText('25')
#             label_10 = QLabel('26')
#             self.bl.gridLayout.addWidget(label_10, 6,0)
#             label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image,6,1)
#             label_11 = QLabel('27')
#             self.bl.gridLayout.addWidget(label_11, 7,0)
#             label_11.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image2,7,1)
#             label_12 = QLabel('28')
#             self.bl.gridLayout.addWidget(label_12, 8,0)
#             label_12.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image3,8,1)
#             self.bl.gridLayout.addWidget(switch, 8,2)
#             switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.show()
#         elif whichsection == 'G':
#             #'29' or '30' or '31' or '32':
#             self.bl.label_5.setText('29')
#             self.bl.gridLayout.addWidget(switch, 1,2)
#             switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.label_6.setText('30')
#             self.bl.label_7.setText('31')
#             self.bl.label_8.setText('32')
#             self.bl.label_9.hide()
#             self.bl.eicon.hide()
#             self.bl.show()
#         elif whichsection == 'H':
#             #'33' or '34' or '35':
#             self.bl.label_5.setText('33')
#             self.bl.label_6.setText('34')
#             self.bl.label_7.setText('35')
#             self.bl.label_8.hide()
#             self.bl.dicon.hide()
#             self.bl.label_9.hide()
#             self.bl.eicon.hide()
#             self.bl.show()
#         elif whichsection == 'I':
#             #'36' or '37' or '38' or '39' or '40' or '41' or '42' or '43' or '44' or '45' or '46' or '47' or '48' or '49' or '50' or '44' or '45' or '46' or '47' or '48' or '49' or '50'or '51' or '52' or '53' or '54' or '55' or '56' or '57':
#             self.bl.label_5.setText('36')
#             self.bl.label_6.setText('37')
#             self.bl.label_7.setText('38')
#             self.bl.label_8.setText('39')
#             self.bl.label_9.setText('40')
#             label_10 = QLabel('41')
#             self.bl.gridLayout.addWidget(label_10, 6,0)
#             label_10.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image,6,1)
#             label_11 = QLabel('42')
#             self.bl.gridLayout.addWidget(label_11, 7,0)
#             label_11.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image2,7,1)
#             label_12 = QLabel('43')
#             self.bl.gridLayout.addWidget(label_12, 8,0)
#             label_12.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image3,8,1)
#             self.bl.gridLayout.addWidget(switch, 1,2)
#             switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             label_13 = QLabel('44')
#             self.bl.gridLayout.addWidget(label_13, 9,0)
#             label_13.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image4,9,1)
#             label_14 = QLabel('45')
#             self.bl.gridLayout.addWidget(label_14, 10,0)
#             label_14.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image5,10,1)
#             label_15 = QLabel('46')
#             self.bl.gridLayout.addWidget(label_15, 11,0)
#             label_15.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image6,11,1)
#             label_16 = QLabel('47')
#             self.bl.gridLayout.addWidget(label_16, 12,0)
#             label_16.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image7,12,1)
#             label_17 = QLabel('48')
#             self.bl.gridLayout.addWidget(label_17, 13,0)
#             label_17.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image8,13,1)
#             label_18 = QLabel('49')
#             self.bl.gridLayout.addWidget(label_18, 14,0)
#             label_18.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image9,14,1)
#             label_19 = QLabel('50')
#             self.bl.gridLayout.addWidget(label_19, 15,0)
#             label_19.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image10,15,1)
#             label_20 = QLabel('51')
#             self.bl.gridLayout.addWidget(label_20, 16,0)
#             label_20.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image11,16,1)
#             label_21 = QLabel('52')
#             self.bl.gridLayout.addWidget(label_21, 17,0)
#             label_21.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image12,17,1)
#             label_22 = QLabel('53')
#             self.bl.gridLayout.addWidget(label_22, 18,0)
#             label_22.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image13,18,1)
#             label_23 = QLabel('54')
#             self.bl.gridLayout.addWidget(label_23, 19,0)
#             label_23.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image14,19,1)
#             label_24 = QLabel('55')
#             self.bl.gridLayout.addWidget(label_24, 20,0)
#             label_24.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image15,20,1)
#             label_25 = QLabel('56')
#             self.bl.gridLayout.addWidget(label_25, 21,0)
#             label_25.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image16,21,1)
#             label_26 = QLabel('57')
#             self.bl.gridLayout.addWidget(label_26, 22,0)
#             label_26.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.gridLayout.addWidget(image17,22,1)
#             self.bl.gridLayout.addWidget(switch, 22,2)
#             switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.show()
#         elif whichsection == 'J':
#             #'58' or '59' or '60' or '61' or '62':
#             self.bl.label_5.setText('58')
#             self.bl.gridLayout.addWidget(switch, 2,2)
#             switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.label_6.setText('59')
#             self.bl.label_7.setText('60')
#             self.bl.label_8.setText('61')
#             self.bl.label_9.setText('61')
#             self.bl.gridLayout.addWidget(switch2, 5,2)
#             switch2.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.show()
#         elif whichsection == 'K':
#             #'63' or '64' or '65' or '67' or '68':
#             self.bl.label_5.setText('62')
#             self.bl.gridLayout.addWidget(switch, 1,2)
#             switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.label_6.setText('63')
#             self.bl.label_7.setText('64')
#             self.bl.label_8.setText('64')
#             self.bl.label_9.setText('66')
#             self.bl.show()
#         elif whichsection == 'L':
#             #'69' or '70' or '71' or '72' or '73':
#             self.bl.label_5.setText('69')
#             self.bl.label_6.setText('70')
#             self.bl.label_7.setText('71')
#             self.bl.label_8.setText('72')
#             self.bl.label_9.setText('73')
#             self.bl.show()
#         elif whichsection == 'M':
#             #'74' or '75' or '76':
#             self.bl.label_5.setText('74')
#             self.bl.label_6.setText('75')
#             self.bl.label_7.setText('76')
#             self.bl.label_8.setText('77')
#             self.bl.gridLayout.addWidget(switch, 4,2)
#             switch.setStyleSheet("background-color: rgb(221, 221, 221);\n""font: 700 12pt \"Georgia\";\n""color: rgb(0, 0, 0);")
#             self.bl.label_9.hide()
#             self.bl.eicon.hide()
#             self.bl.show()
        

#     #function for toggle switch colors but see if you can do labels instead of buttons??
#     def toggleColor(self,button1, button2):
#         button1.setEnabled(False)
#         button2.setEnabled(True)
#         button1.setStyleSheet('background-color: SkyBlue; color: black')
#         button2.setStyleSheet('background-color: white; color: gray')

#     #occupation 2 blocks ahead for now
#     #!!!!!! TO DO !!!!!!!!!
#     def changeOccupancy(self, block):
#         print("wayside b UI block", block, "is occupied")
#         if block > 0 and block < 4:
#             self.aicon.setPixmap(QPixmap('greentrain.png'))
#         if block > 3 and block < 7: #== '4'or '5'or '6':
#             self.bicon.setPixmap(QPixmap('greentrain.png'))
#         if block > 6 and block < 13: #== '7' or '8' or '9' or '10' or '11' or '12':
#             self.cicon.setPixmap(QPixmap('greentrain.png'))
#         if block > 12 and block < 16: #== '13' or '14' or '15' or '16':
#             self.dicon.setPixmap(QPixmap('greentrain.png'))
#         if block > 16 and block < 21: #== '17' or '18' or '19' or '20':
#             self.eicon.setPixmap(QPixmap('greentrain.png'))
#         if block > 20 and block < 29: #== '21' or '22' or '23' or '24' or '25' or '26' or '27' or '28':
#             self.ficon.setPixmap(QPixmap('greentrain.png'))
#         if block > 28 and block < 33: #== '29' or '30' or '31' or '32':
#             self.gicon.setPixmap(QPixmap('greentrain.png'))
#         if block > 32 and block < 36: #== '33' or '34' or '35':
#             self.hicon.setPixmap(QPixmap('greentrain.png'))
#         if block > 35 and block < 58: #== '36' or '37' or '38' or '39' or '40' or '41' or '42' or '43' or '44' or '45' or '46' or '47' or '48' or '49' or '50' or '44' or '45' or '46' or '47' or '48' or '49' or '50'or '51' or '52' or '53' or '54' or '55' or '56' or '57':
#             self.iicon.setPixmap(QPixmap('greentrain.png'))
#         if block > 57 and block < 63: #== '58' or '59' or '60' or '61' or '62':
#             self.jicon.setPixmap(QPixmap('greentrain.png'))
#         if block > 62 and block < 69: #== '63' or '64' or '65' or '67' or '68':
#             self.kicon.setPixmap(QPixmap('greentrain.png'))
#         if block > 68 and block < 74: #== '69' or '70' or '71' or '72' or '73':
#             self.licon.setPixmap(QPixmap('greentrain.png'))
#         if block > 73 and block < 77: #== '74' or '75' or '76':
#             self.micon.setPixmap(QPixmap('greentrain.png'))
#         if block == 74:
#             self.gate50.setStyleSheet('background-color: SkyBlue')
#             self.gate51.setStyleSheet('background-color: white; color: gray')
#         if block == 83:
#             self.gate60.setStyleSheet('background-color: SkyBlue')
#             self.gate61.setStyleSheet('background-color: white; color: gray')
#         if block == 98:
#             self.gate61.setStyleSheet('background-color: SkyBlue')
#             self.gate60.setStyleSheet('background-color: white; color: gray')
#         if block == 79:
#             self.gate51.setStyleSheet('background-color: SkyBlue')
#             self.gate50.setStyleSheet('background-color: white; color: gray')
#         if block == 148:
#             self.gate20.setStyleSheet('background-color: SkyBlue')
#             self.gate21.setStyleSheet('background-color: white; color: gray')
#         if block == 11:
#             self.gate11.setStyleSheet('background-color: SkyBlue')
#             self.gate10.setStyleSheet('background-color: white; color: gray')
#         if block == 2:
#             self.gate10.setStyleSheet('background-color: SkyBlue')
#             self.gate11.setStyleSheet('background-color: white; color: gray')
#         if block == 27:
#             self.gate21.setStyleSheet('background-color: SkyBlue')
#             self.gate20.setStyleSheet('background-color: white; color: gray')
#         if block == 55:
#             self.gate31.setStyleSheet('background-color: SkyBlue')
#             self.gate30.setStyleSheet('background-color: white; color: gray')

#     def changeVacancy(self, block):
#         print("wayside b UI block", block, "is vacant")
#         if block > 0 and block < 4:
#             self.aicon.setPixmap(QPixmap('tracks.png'))
#         if block > 3 and block < 7: #== '4'or '5'or '6':
#             self.bicon.setPixmap(QPixmap('tracks.png'))
#         if block > 6 and block < 13: #== '7' or '8' or '9' or '10' or '11' or '12':
#             self.cicon.setPixmap(QPixmap('tracks.png'))
#         if block > 12 and block < 16: #== '13' or '14' or '15' or '16':
#             self.dicon.setPixmap(QPixmap('tracks.png'))
#         if block > 16 and block < 21: #== '17' or '18' or '19' or '20':
#             self.eicon.setPixmap(QPixmap('tracks.png'))
#         if block > 20 and block < 29: #== '21' or '22' or '23' or '24' or '25' or '26' or '27' or '28':
#             self.ficon.setPixmap(QPixmap('tracks.png'))
#         if block > 28 and block < 33: #== '29' or '30' or '31' or '32':
#             self.gicon.setPixmap(QPixmap('tracks.png'))
#         if block > 32 and block < 36: #== '33' or '34' or '35':
#             self.hicon.setPixmap(QPixmap('tracks.png'))
#         if block > 35 and block < 58: #== '36' or '37' or '38' or '39' or '40' or '41' or '42' or '43' or '44' or '45' or '46' or '47' or '48' or '49' or '50' or '44' or '45' or '46' or '47' or '48' or '49' or '50'or '51' or '52' or '53' or '54' or '55' or '56' or '57':
#             self.iicon.setPixmap(QPixmap('tracks.png'))
#         if block > 57 and block < 63: #== '58' or '59' or '60' or '61' or '62':
#             self.jicon.setPixmap(QPixmap('tracks.png'))
#         if block > 62 and block < 69: #== '63' or '64' or '65' or '67' or '68':
#             self.kicon.setPixmap(QPixmap('tracks.png'))
#         if block > 68 and block < 74: #== '69' or '70' or '71' or '72' or '73':
#             self.licon.setPixmap(QPixmap('tracks.png'))
#         if block > 73 and block < 77: #== '74' or '75' or '76':
#             self.micon.setPixmap(QPixmap('tracks.png'))

#      #function for number of active trains
#     #somehow counts the number of times the red train label comes up
#     def activeTrains(self, counts):
#         self.activetrains.display(counts)'''

'''#class WaysideUIFunctions(QObject):
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
    # def activeTrains(self, counts):
    #     self.activetrains.display(counts)'''

'''#test = Ui_testpopup()
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
#                 window.jicon.setPixmap(QPixmap('tracks.png'))'''
    
'''#track configuration pop up so hold a funeral

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
#                 self.plcdisplay.setText(data)'''

'''#class Communications():
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
    #send switches'''