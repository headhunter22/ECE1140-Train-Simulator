# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainTrackModel.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1154, 662)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.RedLineScrollArea = QScrollArea(self.centralwidget)
        self.RedLineScrollArea.setObjectName(u"RedLineScrollArea")
        self.RedLineScrollArea.setGeometry(QRect(0, 120, 411, 481))
        self.RedLineScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.RedLineScrollArea.setWidgetResizable(True)
        self.RedLineLabels = QWidget()
        self.RedLineLabels.setObjectName(u"RedLineLabels")
        self.RedLineLabels.setGeometry(QRect(0, 0, 409, 479))
        self.RedLineScrollArea.setWidget(self.RedLineLabels)
        self.RedLineLabel = QLabel(self.centralwidget)
        self.RedLineLabel.setObjectName(u"RedLineLabel")
        self.RedLineLabel.setGeometry(QRect(110, 20, 191, 51))
        self.RedLineLabel.setStyleSheet(u"font-size: 20pt")
        self.RedLineLabel.setAlignment(Qt.AlignCenter)
        self.GreenLineLabel = QLabel(self.centralwidget)
        self.GreenLineLabel.setObjectName(u"GreenLineLabel")
        self.GreenLineLabel.setGeometry(QRect(550, 20, 191, 51))
        self.GreenLineLabel.setStyleSheet(u"font-size: 20pt")
        self.GreenLineLabel.setAlignment(Qt.AlignCenter)
        self.GreenLineScrollArea = QScrollArea(self.centralwidget)
        self.GreenLineScrollArea.setObjectName(u"GreenLineScrollArea")
        self.GreenLineScrollArea.setGeometry(QRect(440, 120, 411, 481))
        self.GreenLineScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.GreenLineScrollArea.setWidgetResizable(True)
        self.RedLineLabels_2 = QWidget()
        self.RedLineLabels_2.setObjectName(u"RedLineLabels_2")
        self.RedLineLabels_2.setGeometry(QRect(0, 0, 409, 479))
        self.GreenLineScrollArea.setWidget(self.RedLineLabels_2)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 60, 401, 51))
        self.RedLineHeadersLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.RedLineHeadersLayout.setObjectName(u"RedLineHeadersLayout")
        self.RedLineHeadersLayout.setContentsMargins(0, 0, 0, 0)
        self.RedSection = QLabel(self.horizontalLayoutWidget)
        self.RedSection.setObjectName(u"RedSection")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RedSection.sizePolicy().hasHeightForWidth())
        self.RedSection.setSizePolicy(sizePolicy)
        self.RedSection.setMinimumSize(QSize(75, 0))
        self.RedSection.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout.addWidget(self.RedSection)

        self.RedTrainCount = QLabel(self.horizontalLayoutWidget)
        self.RedTrainCount.setObjectName(u"RedTrainCount")
        sizePolicy.setHeightForWidth(self.RedTrainCount.sizePolicy().hasHeightForWidth())
        self.RedTrainCount.setSizePolicy(sizePolicy)
        self.RedTrainCount.setMinimumSize(QSize(75, 0))
        self.RedTrainCount.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout.addWidget(self.RedTrainCount)

        self.RedOcc = QLabel(self.horizontalLayoutWidget)
        self.RedOcc.setObjectName(u"RedOcc")
        sizePolicy.setHeightForWidth(self.RedOcc.sizePolicy().hasHeightForWidth())
        self.RedOcc.setSizePolicy(sizePolicy)
        self.RedOcc.setMinimumSize(QSize(150, 0))
        self.RedOcc.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout.addWidget(self.RedOcc)

        self.RedInfo = QLabel(self.horizontalLayoutWidget)
        self.RedInfo.setObjectName(u"RedInfo")
        sizePolicy.setHeightForWidth(self.RedInfo.sizePolicy().hasHeightForWidth())
        self.RedInfo.setSizePolicy(sizePolicy)
        self.RedInfo.setMinimumSize(QSize(50, 0))
        self.RedInfo.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout.addWidget(self.RedInfo)

        self.Spacer1 = QFrame(self.centralwidget)
        self.Spacer1.setObjectName(u"Spacer1")
        self.Spacer1.setGeometry(QRect(420, 0, 16, 601))
        self.Spacer1.setFrameShape(QFrame.VLine)
        self.Spacer1.setFrameShadow(QFrame.Sunken)
        self.Spacer2 = QFrame(self.centralwidget)
        self.Spacer2.setObjectName(u"Spacer2")
        self.Spacer2.setGeometry(QRect(860, 0, 16, 601))
        self.Spacer2.setFrameShape(QFrame.VLine)
        self.Spacer2.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(440, 60, 411, 51))
        self.RedLineHeadersLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.RedLineHeadersLayout_2.setObjectName(u"RedLineHeadersLayout_2")
        self.RedLineHeadersLayout_2.setContentsMargins(0, 0, 0, 0)
        self.GreenSection = QLabel(self.horizontalLayoutWidget_3)
        self.GreenSection.setObjectName(u"GreenSection")
        sizePolicy.setHeightForWidth(self.GreenSection.sizePolicy().hasHeightForWidth())
        self.GreenSection.setSizePolicy(sizePolicy)
        self.GreenSection.setMinimumSize(QSize(75, 0))
        self.GreenSection.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout_2.addWidget(self.GreenSection)

        self.GreenTrainCount = QLabel(self.horizontalLayoutWidget_3)
        self.GreenTrainCount.setObjectName(u"GreenTrainCount")
        sizePolicy.setHeightForWidth(self.GreenTrainCount.sizePolicy().hasHeightForWidth())
        self.GreenTrainCount.setSizePolicy(sizePolicy)
        self.GreenTrainCount.setMinimumSize(QSize(75, 0))
        self.GreenTrainCount.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout_2.addWidget(self.GreenTrainCount)

        self.GreenOcc = QLabel(self.horizontalLayoutWidget_3)
        self.GreenOcc.setObjectName(u"GreenOcc")
        sizePolicy.setHeightForWidth(self.GreenOcc.sizePolicy().hasHeightForWidth())
        self.GreenOcc.setSizePolicy(sizePolicy)
        self.GreenOcc.setMinimumSize(QSize(150, 0))
        self.GreenOcc.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout_2.addWidget(self.GreenOcc)

        self.GreenInfo = QLabel(self.horizontalLayoutWidget_3)
        self.GreenInfo.setObjectName(u"GreenInfo")
        sizePolicy.setHeightForWidth(self.GreenInfo.sizePolicy().hasHeightForWidth())
        self.GreenInfo.setSizePolicy(sizePolicy)
        self.GreenInfo.setMinimumSize(QSize(50, 0))
        self.GreenInfo.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout_2.addWidget(self.GreenInfo)

        self.GeneralInfoLabel = QLabel(self.centralwidget)
        self.GeneralInfoLabel.setObjectName(u"GeneralInfoLabel")
        self.GeneralInfoLabel.setGeometry(QRect(920, 0, 191, 51))
        self.GeneralInfoLabel.setStyleSheet(u"font-size: 20pt")
        self.GeneralInfoLabel.setAlignment(Qt.AlignCenter)
        self.DateTimeLabel = QLabel(self.centralwidget)
        self.DateTimeLabel.setObjectName(u"DateTimeLabel")
        self.DateTimeLabel.setGeometry(QRect(880, 60, 71, 20))
        self.GreenLineGenInfo = QLabel(self.centralwidget)
        self.GreenLineGenInfo.setObjectName(u"GreenLineGenInfo")
        self.GreenLineGenInfo.setGeometry(QRect(1020, 90, 120, 50))
        self.GreenLineGenInfo.setStyleSheet(u"font-size: 20pt;\n"
"background-color: #00b321;\n"
"font-weight: bold")
        self.GreenLineGenInfo.setAlignment(Qt.AlignCenter)
        self.RedLineGenInfo = QLabel(self.centralwidget)
        self.RedLineGenInfo.setObjectName(u"RedLineGenInfo")
        self.RedLineGenInfo.setGeometry(QRect(880, 90, 120, 50))
        self.RedLineGenInfo.setStyleSheet(u"font-size: 20pt;\n"
"background-color: #FF0000;\n"
"font-weight: bold")
        self.RedLineGenInfo.setAlignment(Qt.AlignCenter)
        self.RailBreakagesLabel = QLabel(self.centralwidget)
        self.RailBreakagesLabel.setObjectName(u"RailBreakagesLabel")
        self.RailBreakagesLabel.setGeometry(QRect(920, 150, 191, 21))
        self.RailBreakagesLabel.setStyleSheet(u"font-size: 16pt;\n"
"background-color: #a8a8a8;\n"
"color: black")
        self.RailBreakagesLabel.setAlignment(Qt.AlignCenter)
        self.GeneralInfoSpacer = QFrame(self.centralwidget)
        self.GeneralInfoSpacer.setObjectName(u"GeneralInfoSpacer")
        self.GeneralInfoSpacer.setGeometry(QRect(1000, 180, 20, 331))
        self.GeneralInfoSpacer.setFrameShape(QFrame.VLine)
        self.GeneralInfoSpacer.setFrameShadow(QFrame.Sunken)
        self.RedBreakagesScroll = QScrollArea(self.centralwidget)
        self.RedBreakagesScroll.setObjectName(u"RedBreakagesScroll")
        self.RedBreakagesScroll.setGeometry(QRect(870, 180, 131, 91))
        self.RedBreakagesScroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 129, 89))
        self.RedBreakagesScroll.setWidget(self.scrollAreaWidgetContents)
        self.GreenBreakagesScroll = QScrollArea(self.centralwidget)
        self.GreenBreakagesScroll.setObjectName(u"GreenBreakagesScroll")
        self.GreenBreakagesScroll.setGeometry(QRect(1020, 180, 131, 91))
        self.GreenBreakagesScroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 129, 89))
        self.GreenBreakagesScroll.setWidget(self.scrollAreaWidgetContents_2)
        self.TotalTrainCountLabel = QLabel(self.centralwidget)
        self.TotalTrainCountLabel.setObjectName(u"TotalTrainCountLabel")
        self.TotalTrainCountLabel.setGeometry(QRect(920, 280, 191, 21))
        self.TotalTrainCountLabel.setStyleSheet(u"font-size: 16pt;\n"
"background-color: #a8a8a8;\n"
"color: black")
        self.TotalTrainCountLabel.setAlignment(Qt.AlignCenter)
        self.RedTrainCt = QLabel(self.centralwidget)
        self.RedTrainCt.setObjectName(u"RedTrainCt")
        self.RedTrainCt.setGeometry(QRect(910, 320, 58, 16))
        self.RedTrainCt.setAlignment(Qt.AlignCenter)
        self.GreenTrainCt = QLabel(self.centralwidget)
        self.GreenTrainCt.setObjectName(u"GreenTrainCt")
        self.GreenTrainCt.setGeometry(QRect(1050, 320, 58, 16))
        self.GreenTrainCt.setAlignment(Qt.AlignCenter)
        self.RRXingLabel = QLabel(self.centralwidget)
        self.RRXingLabel.setObjectName(u"RRXingLabel")
        self.RRXingLabel.setGeometry(QRect(920, 360, 191, 21))
        self.RRXingLabel.setStyleSheet(u"font-size: 16pt;\n"
"background-color: #a8a8a8;\n"
"color: black")
        self.RRXingLabel.setAlignment(Qt.AlignCenter)
        self.I47 = QLabel(self.centralwidget)
        self.I47.setObjectName(u"I47")
        self.I47.setGeometry(QRect(880, 400, 31, 16))
        self.E19 = QLabel(self.centralwidget)
        self.E19.setObjectName(u"E19")
        self.E19.setGeometry(QRect(1020, 400, 31, 16))
        self.I47Status = QLabel(self.centralwidget)
        self.I47Status.setObjectName(u"I47Status")
        self.I47Status.setGeometry(QRect(917, 400, 81, 20))
        self.I47Status.setStyleSheet(u"border: 2px solid rgb(188, 6, 0);\n"
"color: rgb(148, 0, 17);\n"
"background-color: rgb(255, 135, 119)")
        self.I47Status.setAlignment(Qt.AlignCenter)
        self.E19Status = QLabel(self.centralwidget)
        self.E19Status.setObjectName(u"E19Status")
        self.E19Status.setGeometry(QRect(1060, 400, 81, 20))
        self.E19Status.setStyleSheet(u"border: 2px solid rgb(188, 6, 0);\n"
"color: rgb(148, 0, 17);\n"
"background-color: rgb(255, 135, 119)")
        self.E19Status.setAlignment(Qt.AlignCenter)
        self.UploadTrack = QPushButton(self.centralwidget)
        self.UploadTrack.setObjectName(u"UploadTrack")
        self.UploadTrack.setGeometry(QRect(880, 590, 261, 32))
        self.TrackHeatersLabel = QLabel(self.centralwidget)
        self.TrackHeatersLabel.setObjectName(u"TrackHeatersLabel")
        self.TrackHeatersLabel.setGeometry(QRect(920, 440, 191, 21))
        self.TrackHeatersLabel.setStyleSheet(u"font-size: 16pt;\n"
"background-color: #a8a8a8;\n"
"color: black")
        self.TrackHeatersLabel.setAlignment(Qt.AlignCenter)
        self.FaultsLabel = QLabel(self.centralwidget)
        self.FaultsLabel.setObjectName(u"FaultsLabel")
        self.FaultsLabel.setGeometry(QRect(920, 510, 191, 21))
        self.FaultsLabel.setStyleSheet(u"font-size: 16pt;\n"
"background-color: #a8a8a8;\n"
"color: black")
        self.FaultsLabel.setAlignment(Qt.AlignCenter)
        self.CurrentTempLabel = QLabel(self.centralwidget)
        self.CurrentTempLabel.setObjectName(u"CurrentTempLabel")
        self.CurrentTempLabel.setGeometry(QRect(880, 480, 121, 20))
        self.HeaterStatus = QLabel(self.centralwidget)
        self.HeaterStatus.setObjectName(u"HeaterStatus")
        self.HeaterStatus.setGeometry(QRect(1040, 480, 81, 20))
        self.HeaterStatus.setStyleSheet(u"border: 2px solid rgb(188, 6, 0);\n"
"color: rgb(148, 0, 17);\n"
"background-color: rgb(255, 135, 119)")
        self.HeaterStatus.setAlignment(Qt.AlignCenter)
        self.FaultSpacer1 = QFrame(self.centralwidget)
        self.FaultSpacer1.setObjectName(u"FaultSpacer1")
        self.FaultSpacer1.setGeometry(QRect(910, 540, 20, 41))
        self.FaultSpacer1.setFrameShape(QFrame.VLine)
        self.FaultSpacer1.setFrameShadow(QFrame.Sunken)
        self.FaultSpacer2 = QFrame(self.centralwidget)
        self.FaultSpacer2.setObjectName(u"FaultSpacer2")
        self.FaultSpacer2.setGeometry(QRect(1000, 540, 20, 41))
        self.FaultSpacer2.setFrameShape(QFrame.VLine)
        self.FaultSpacer2.setFrameShadow(QFrame.Sunken)
        self.PowerFaultLabel = QLabel(self.centralwidget)
        self.PowerFaultLabel.setObjectName(u"PowerFaultLabel")
        self.PowerFaultLabel.setGeometry(QRect(870, 550, 41, 20))
        self.PowerFaultLabel.setAlignment(Qt.AlignCenter)
        self.BrokenRailLabel = QLabel(self.centralwidget)
        self.BrokenRailLabel.setObjectName(u"BrokenRailLabel")
        self.BrokenRailLabel.setGeometry(QRect(920, 550, 91, 20))
        self.BrokenRailLabel.setAlignment(Qt.AlignCenter)
        self.BrokenCircuitLabel = QLabel(self.centralwidget)
        self.BrokenCircuitLabel.setObjectName(u"BrokenCircuitLabel")
        self.BrokenCircuitLabel.setGeometry(QRect(1010, 550, 101, 20))
        self.BrokenCircuitLabel.setAlignment(Qt.AlignCenter)
        self.FaultWindowButton = QPushButton(self.centralwidget)
        self.FaultWindowButton.setObjectName(u"FaultWindowButton")
        self.FaultWindowButton.setGeometry(QRect(1110, 550, 41, 32))
        self.time = QLabel(self.centralwidget)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(957, 60, 181, 20))
        self.tempEntry = QLineEdit(self.centralwidget)
        self.tempEntry.setObjectName(u"tempEntry")
        self.tempEntry.setGeometry(QRect(10, 630, 113, 21))
        self.tempLabel = QLabel(self.centralwidget)
        self.tempLabel.setObjectName(u"tempLabel")
        self.tempLabel.setGeometry(QRect(10, 610, 131, 16))
        self.tempGo = QPushButton(self.centralwidget)
        self.tempGo.setObjectName(u"tempGo")
        self.tempGo.setGeometry(QRect(130, 620, 71, 32))
        self.Spacer3 = QFrame(self.centralwidget)
        self.Spacer3.setObjectName(u"Spacer3")
        self.Spacer3.setGeometry(QRect(210, 600, 3, 61))
        self.Spacer3.setFrameShape(QFrame.VLine)
        self.Spacer3.setFrameShadow(QFrame.Sunken)
        self.brokenRailButton = QPushButton(self.centralwidget)
        self.brokenRailButton.setObjectName(u"brokenRailButton")
        self.brokenRailButton.setGeometry(QRect(230, 620, 91, 32))
        self.powerFailure = QPushButton(self.centralwidget)
        self.powerFailure.setObjectName(u"powerFailure")
        self.powerFailure.setGeometry(QRect(520, 620, 101, 32))
        self.circuitFailure = QPushButton(self.centralwidget)
        self.circuitFailure.setObjectName(u"circuitFailure")
        self.circuitFailure.setGeometry(QRect(630, 620, 101, 32))
        self.brokenRailLineLabel = QLabel(self.centralwidget)
        self.brokenRailLineLabel.setObjectName(u"brokenRailLineLabel")
        self.brokenRailLineLabel.setGeometry(QRect(350, 610, 81, 20))
        self.brokenRailBlockLabel = QLabel(self.centralwidget)
        self.brokenRailBlockLabel.setObjectName(u"brokenRailBlockLabel")
        self.brokenRailBlockLabel.setGeometry(QRect(450, 610, 58, 16))
        self.brokenRailLineSelect = QComboBox(self.centralwidget)
        self.brokenRailLineSelect.setObjectName(u"brokenRailLineSelect")
        self.brokenRailLineSelect.setGeometry(QRect(330, 630, 91, 32))
        self.brokenRailBlockSelect = QComboBox(self.centralwidget)
        self.brokenRailBlockSelect.setObjectName(u"brokenRailBlockSelect")
        self.brokenRailBlockSelect.setGeometry(QRect(430, 630, 71, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.GeneralInfoSpacer.raise_()
        self.RedLineScrollArea.raise_()
        self.RedLineLabel.raise_()
        self.GreenLineLabel.raise_()
        self.GreenLineScrollArea.raise_()
        self.horizontalLayoutWidget.raise_()
        self.Spacer1.raise_()
        self.Spacer2.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.GeneralInfoLabel.raise_()
        self.DateTimeLabel.raise_()
        self.GreenLineGenInfo.raise_()
        self.RedLineGenInfo.raise_()
        self.RailBreakagesLabel.raise_()
        self.RedBreakagesScroll.raise_()
        self.GreenBreakagesScroll.raise_()
        self.TotalTrainCountLabel.raise_()
        self.RedTrainCt.raise_()
        self.GreenTrainCt.raise_()
        self.RRXingLabel.raise_()
        self.I47.raise_()
        self.E19.raise_()
        self.I47Status.raise_()
        self.E19Status.raise_()
        self.UploadTrack.raise_()
        self.TrackHeatersLabel.raise_()
        self.FaultsLabel.raise_()
        self.CurrentTempLabel.raise_()
        self.HeaterStatus.raise_()
        self.FaultSpacer1.raise_()
        self.FaultSpacer2.raise_()
        self.PowerFaultLabel.raise_()
        self.BrokenRailLabel.raise_()
        self.BrokenCircuitLabel.raise_()
        self.FaultWindowButton.raise_()
        self.time.raise_()
        self.tempEntry.raise_()
        self.tempLabel.raise_()
        self.tempGo.raise_()
        self.Spacer3.raise_()
        self.brokenRailButton.raise_()
        self.powerFailure.raise_()
        self.circuitFailure.raise_()
        self.brokenRailLineLabel.raise_()
        self.brokenRailBlockLabel.raise_()
        self.brokenRailLineSelect.raise_()
        self.brokenRailBlockSelect.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.RedLineLabel.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.GreenLineLabel.setText(QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.RedSection.setText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.RedTrainCount.setText(QCoreApplication.translate("MainWindow", u"# of Trains", None))
        self.RedOcc.setText(QCoreApplication.translate("MainWindow", u"Blocks Occcupied", None))
        self.RedInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.GreenSection.setText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.GreenTrainCount.setText(QCoreApplication.translate("MainWindow", u"# of Trains", None))
        self.GreenOcc.setText(QCoreApplication.translate("MainWindow", u"Blocks Occcupied", None))
        self.GreenInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.GeneralInfoLabel.setText(QCoreApplication.translate("MainWindow", u"General Info", None))
        self.DateTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Date/Time:", None))
        self.GreenLineGenInfo.setText(QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.RedLineGenInfo.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.RailBreakagesLabel.setText(QCoreApplication.translate("MainWindow", u"Rail Breakages", None))
        self.TotalTrainCountLabel.setText(QCoreApplication.translate("MainWindow", u"Total Trains Active", None))
        self.RedTrainCt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.GreenTrainCt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RRXingLabel.setText(QCoreApplication.translate("MainWindow", u"RR Crossings", None))
        self.I47.setText(QCoreApplication.translate("MainWindow", u"I-47:", None))
        self.E19.setText(QCoreApplication.translate("MainWindow", u"E-19", None))
        self.I47Status.setText(QCoreApplication.translate("MainWindow", u"Inactive", None))
        self.E19Status.setText(QCoreApplication.translate("MainWindow", u"Inactive", None))
        self.UploadTrack.setText(QCoreApplication.translate("MainWindow", u"Upload Track Layout", None))
        self.TrackHeatersLabel.setText(QCoreApplication.translate("MainWindow", u"Track Heaters", None))
        self.FaultsLabel.setText(QCoreApplication.translate("MainWindow", u"Faults", None))
        self.CurrentTempLabel.setText(QCoreApplication.translate("MainWindow", u"Current Temp:", None))
        self.HeaterStatus.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.PowerFaultLabel.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.BrokenRailLabel.setText(QCoreApplication.translate("MainWindow", u"Broken Rail", None))
        self.BrokenCircuitLabel.setText(QCoreApplication.translate("MainWindow", u"Broken Circuit", None))
        self.FaultWindowButton.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.time.setText("")
        self.tempLabel.setText(QCoreApplication.translate("MainWindow", u"Enter Temperature:", None))
        self.tempGo.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.brokenRailButton.setText(QCoreApplication.translate("MainWindow", u"Broken Rail", None))
        self.powerFailure.setText(QCoreApplication.translate("MainWindow", u"Power Failure", None))
        self.circuitFailure.setText(QCoreApplication.translate("MainWindow", u"Circuit Failure", None))
        self.brokenRailLineLabel.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.brokenRailBlockLabel.setText(QCoreApplication.translate("MainWindow", u"Block", None))
    # retranslateUi

