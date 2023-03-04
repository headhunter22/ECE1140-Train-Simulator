# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Wayside_Main_B.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(724, 505)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_8 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(251, 220, 451, 111))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.verticalLayoutWidget_8)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_2)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_50 = QLabel(self.verticalLayoutWidget_8)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_50)

        self.label_51 = QLabel(self.verticalLayoutWidget_8)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_51)

        self.label_52 = QLabel(self.verticalLayoutWidget_8)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_52)


        self.verticalLayout_9.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_53 = QLabel(self.verticalLayoutWidget_8)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_53)

        self.label_54 = QLabel(self.verticalLayoutWidget_8)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"font: 9pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_54.setFrameShadow(QFrame.Plain)
        self.label_54.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_54)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.reda = QLabel(self.verticalLayoutWidget_8)
        self.reda.setObjectName(u"reda")
        self.reda.setMaximumSize(QSize(21, 21))
        self.reda.setPixmap(QPixmap(u"offlight.png"))
        self.reda.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.reda)

        self.yellowa = QLabel(self.verticalLayoutWidget_8)
        self.yellowa.setObjectName(u"yellowa")
        self.yellowa.setMaximumSize(QSize(21, 21))
        self.yellowa.setPixmap(QPixmap(u"offlight.png"))
        self.yellowa.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.yellowa)

        self.greena = QLabel(self.verticalLayoutWidget_8)
        self.greena.setObjectName(u"greena")
        self.greena.setMaximumSize(QSize(21, 21))
        self.greena.setPixmap(QPixmap(u"offlight.png"))
        self.greena.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.greena)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_27)


        self.verticalLayout_9.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_55 = QLabel(self.verticalLayoutWidget_8)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_55)

        self.label_56 = QLabel(self.verticalLayoutWidget_8)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"font: 9pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_56.setFrameShadow(QFrame.Plain)
        self.label_56.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_56)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.redb = QLabel(self.verticalLayoutWidget_8)
        self.redb.setObjectName(u"redb")
        self.redb.setMaximumSize(QSize(21, 21))
        self.redb.setPixmap(QPixmap(u"offlight.png"))
        self.redb.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.redb)

        self.yellowb = QLabel(self.verticalLayoutWidget_8)
        self.yellowb.setObjectName(u"yellowb")
        self.yellowb.setMaximumSize(QSize(21, 21))
        self.yellowb.setPixmap(QPixmap(u"offlight.png"))
        self.yellowb.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.yellowb)

        self.greenb = QLabel(self.verticalLayoutWidget_8)
        self.greenb.setObjectName(u"greenb")
        self.greenb.setMaximumSize(QSize(21, 21))
        self.greenb.setPixmap(QPixmap(u"offlight.png"))
        self.greenb.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.greenb)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_29)


        self.verticalLayout_9.addLayout(self.horizontalLayout_21)

        self.line_5 = QFrame(self.verticalLayoutWidget_8)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_5)

        self.trackconfiguration = QPushButton(self.centralwidget)
        self.trackconfiguration.setObjectName(u"trackconfiguration")
        self.trackconfiguration.setGeometry(QRect(251, 420, 451, 31))
        self.trackconfiguration.setStyleSheet(u"font: 9pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(11, 210, 221, 241))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setContentsMargins(0, 0, 9, 0)
        self.pusha = QPushButton(self.gridLayoutWidget)
        self.pusha.setObjectName(u"pusha")

        self.gridLayout_2.addWidget(self.pusha, 2, 0, 1, 1)

        self.aicon = QLabel(self.gridLayoutWidget)
        self.aicon.setObjectName(u"aicon")
        self.aicon.setMaximumSize(QSize(50, 50))
        self.aicon.setPixmap(QPixmap(u"tracks.png"))
        self.aicon.setScaledContents(True)
        self.aicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.aicon, 2, 1, 1, 1)

        self.sectiontitle = QLabel(self.gridLayoutWidget)
        self.sectiontitle.setObjectName(u"sectiontitle")
        self.sectiontitle.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.sectiontitle.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.sectiontitle, 1, 0, 1, 1)

        self.pushb = QPushButton(self.gridLayoutWidget)
        self.pushb.setObjectName(u"pushb")

        self.gridLayout_2.addWidget(self.pushb, 4, 0, 1, 1)

        self.bicon = QLabel(self.gridLayoutWidget)
        self.bicon.setObjectName(u"bicon")
        self.bicon.setMaximumSize(QSize(50, 50))
        self.bicon.setPixmap(QPixmap(u"tracks.png"))
        self.bicon.setScaledContents(True)
        self.bicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.bicon, 4, 1, 1, 1)

        self.pushc = QPushButton(self.gridLayoutWidget)
        self.pushc.setObjectName(u"pushc")

        self.gridLayout_2.addWidget(self.pushc, 5, 0, 1, 1)

        self.occupancylabel = QLabel(self.gridLayoutWidget)
        self.occupancylabel.setObjectName(u"occupancylabel")
        self.occupancylabel.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.occupancylabel, 1, 1, 1, 1)

        self.cicon = QLabel(self.gridLayoutWidget)
        self.cicon.setObjectName(u"cicon")
        self.cicon.setMaximumSize(QSize(50, 50))
        self.cicon.setPixmap(QPixmap(u"redtrain.png"))
        self.cicon.setScaledContents(True)
        self.cicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.cicon, 5, 1, 1, 1)

        self.horizontalLayoutWidget_7 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(250, 380, 451, 31))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.automaticmode = QRadioButton(self.horizontalLayoutWidget_7)
        self.automaticmode.setObjectName(u"automaticmode")
        self.automaticmode.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.automaticmode)

        self.maintenancemode = QRadioButton(self.horizontalLayoutWidget_7)
        self.maintenancemode.setObjectName(u"maintenancemode")
        self.maintenancemode.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.maintenancemode)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(251, 0, 451, 131))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.sspeedlabel = QLabel(self.gridLayoutWidget_2)
        self.sspeedlabel.setObjectName(u"sspeedlabel")
        self.sspeedlabel.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.sspeedlabel, 2, 0, 1, 1)

        self.sspeeddisp = QLCDNumber(self.gridLayoutWidget_2)
        self.sspeeddisp.setObjectName(u"sspeeddisp")

        self.gridLayout_3.addWidget(self.sspeeddisp, 2, 1, 1, 1)

        self.sauthlabel = QLabel(self.gridLayoutWidget_2)
        self.sauthlabel.setObjectName(u"sauthlabel")
        self.sauthlabel.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.sauthlabel, 1, 0, 1, 1)

        self.miles2 = QLabel(self.gridLayoutWidget_2)
        self.miles2.setObjectName(u"miles2")
        self.miles2.setStyleSheet(u"font: 700 8pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.miles2, 1, 2, 1, 1)

        self.sauthoritydisp = QLCDNumber(self.gridLayoutWidget_2)
        self.sauthoritydisp.setObjectName(u"sauthoritydisp")

        self.gridLayout_3.addWidget(self.sauthoritydisp, 1, 1, 1, 1)

        self.cauthlabel = QLabel(self.gridLayoutWidget_2)
        self.cauthlabel.setObjectName(u"cauthlabel")
        self.cauthlabel.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.cauthlabel, 0, 0, 1, 1)

        self.miles1 = QLabel(self.gridLayoutWidget_2)
        self.miles1.setObjectName(u"miles1")
        self.miles1.setStyleSheet(u"font: 700 8pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.miles1, 0, 2, 1, 1)

        self.miles2_2 = QLabel(self.gridLayoutWidget_2)
        self.miles2_2.setObjectName(u"miles2_2")
        self.miles2_2.setStyleSheet(u"font: 700 8pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.miles2_2, 2, 2, 1, 1)

        self.cauthoritydisp = QLCDNumber(self.gridLayoutWidget_2)
        self.cauthoritydisp.setObjectName(u"cauthoritydisp")

        self.gridLayout_3.addWidget(self.cauthoritydisp, 0, 1, 1, 1)

        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(249, 140, 451, 73))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.verticalLayoutWidget_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.label_17 = QLabel(self.verticalLayoutWidget_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_17)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_2 = QLabel(self.verticalLayoutWidget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_2)

        self.ca = QPushButton(self.verticalLayoutWidget_5)
        self.ca.setObjectName(u"ca")
        self.ca.setCheckable(False)

        self.horizontalLayout_10.addWidget(self.ca)

        self.cb = QPushButton(self.verticalLayoutWidget_5)
        self.cb.setObjectName(u"cb")

        self.horizontalLayout_10.addWidget(self.cb)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(251, 340, 451, 31))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.activetrainlabel = QLabel(self.horizontalLayoutWidget_5)
        self.activetrainlabel.setObjectName(u"activetrainlabel")
        self.activetrainlabel.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.activetrainlabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.activetrainlabel)

        self.activetrains = QLCDNumber(self.horizontalLayoutWidget_5)
        self.activetrains.setObjectName(u"activetrains")

        self.horizontalLayout_16.addWidget(self.activetrains)

        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 0, 221, 71))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.date = QLabel(self.verticalLayoutWidget_4)
        self.date.setObjectName(u"date")
        self.date.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.date.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.date)

        self.time = QLabel(self.verticalLayoutWidget_4)
        self.time.setObjectName(u"time")
        self.time.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.time.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.time)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 90, 221, 107))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.line_3 = QFrame(self.verticalLayoutWidget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 700 13pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.label_7)

        self.line_4 = QFrame(self.verticalLayoutWidget_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 724, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Crossing", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.reda.setText("")
        self.yellowa.setText("")
        self.greena.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Inactive", None))
        self.redb.setText("")
        self.yellowb.setText("")
        self.greenb.setText("")
        self.trackconfiguration.setText(QCoreApplication.translate("MainWindow", u"Track Configuration", None))
        self.pusha.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.aicon.setText("")
        self.sectiontitle.setText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.pushb.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.bicon.setText("")
        self.pushc.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.occupancylabel.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.cicon.setText("")
        self.automaticmode.setText(QCoreApplication.translate("MainWindow", u"Automatic Mode", None))
        self.maintenancemode.setText(QCoreApplication.translate("MainWindow", u"Maintenance Mode", None))
        self.sspeedlabel.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed              ", None))
        self.sauthlabel.setText(QCoreApplication.translate("MainWindow", u"Suggested Authority     ", None))
        self.miles2.setText(QCoreApplication.translate("MainWindow", u"miles", None))
        self.cauthlabel.setText(QCoreApplication.translate("MainWindow", u"Commanded Authority", None))
        self.miles1.setText(QCoreApplication.translate("MainWindow", u"miles", None))
        self.miles2_2.setText(QCoreApplication.translate("MainWindow", u"mph", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Switches", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.ca.setText(QCoreApplication.translate("MainWindow", u"5 - 6", None))
        self.cb.setText(QCoreApplication.translate("MainWindow", u"5 - 11", None))
        self.activetrainlabel.setText(QCoreApplication.translate("MainWindow", u"Active Trains  ", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"2/19/2023", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"11:44 PM", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sections Managed:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Blue Line", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"A- C", None))
    # retranslateUi

