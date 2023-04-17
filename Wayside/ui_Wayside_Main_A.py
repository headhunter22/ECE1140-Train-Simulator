# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Wayside_Main_A.ui'
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

class Ui_MainWindowA(object):
    def setupUi(self, MainWindowA):
        if not MainWindowA.objectName():
            MainWindowA.setObjectName(u"MainWindowA")
        MainWindowA.resize(724, 737)
        self.centralwidget = QWidget(MainWindowA)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_8 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(251, 360, 451, 111))
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

        self.gatepositiona = QLabel(self.verticalLayoutWidget_8)
        self.gatepositiona.setObjectName(u"gatepositiona")
        self.gatepositiona.setStyleSheet(u"font: 9pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.gatepositiona.setFrameShadow(QFrame.Plain)
        self.gatepositiona.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.gatepositiona)

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

        self.gatepositionb = QLabel(self.verticalLayoutWidget_8)
        self.gatepositionb.setObjectName(u"gatepositionb")
        self.gatepositionb.setStyleSheet(u"font: 9pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.gatepositionb.setFrameShadow(QFrame.Plain)
        self.gatepositionb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.gatepositionb)

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
        self.trackconfiguration.setGeometry(QRect(251, 620, 451, 31))
        self.trackconfiguration.setStyleSheet(u"font: 9pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.horizontalLayoutWidget_7 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(250, 560, 451, 31))
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

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(251, 500, 451, 31))
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
        self.verticalLayoutWidget_4.setGeometry(QRect(490, 0, 211, 151))
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
        self.verticalLayoutWidget_2.setGeometry(QRect(250, 0, 231, 151))
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

        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 1, 221, 671))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setContentsMargins(0, 0, 9, 0)
        self.pushp = QPushButton(self.gridLayoutWidget_3)
        self.pushp.setObjectName(u"pushp")

        self.gridLayout_4.addWidget(self.pushp, 4, 0, 1, 1)

        self.pusht = QPushButton(self.gridLayoutWidget_3)
        self.pusht.setObjectName(u"pusht")

        self.gridLayout_4.addWidget(self.pusht, 8, 0, 1, 1)

        self.pushs = QPushButton(self.gridLayoutWidget_3)
        self.pushs.setObjectName(u"pushs")

        self.gridLayout_4.addWidget(self.pushs, 7, 0, 1, 1)

        self.pushq = QPushButton(self.gridLayoutWidget_3)
        self.pushq.setObjectName(u"pushq")

        self.gridLayout_4.addWidget(self.pushq, 5, 0, 1, 1)

        self.occupancylabel_2 = QLabel(self.gridLayoutWidget_3)
        self.occupancylabel_2.setObjectName(u"occupancylabel_2")
        self.occupancylabel_2.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_4.addWidget(self.occupancylabel_2, 1, 1, 1, 1)

        self.ticon = QLabel(self.gridLayoutWidget_3)
        self.ticon.setObjectName(u"ticon")
        self.ticon.setMaximumSize(QSize(50, 50))
        self.ticon.setPixmap(QPixmap(u"tracks.png"))
        self.ticon.setScaledContents(True)
        self.ticon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.ticon, 8, 1, 1, 1)

        self.oicon = QLabel(self.gridLayoutWidget_3)
        self.oicon.setObjectName(u"oicon")
        self.oicon.setMaximumSize(QSize(50, 50))
        self.oicon.setPixmap(QPixmap(u"tracks.png"))
        self.oicon.setScaledContents(True)
        self.oicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.oicon, 3, 1, 1, 1)

        self.qicon = QLabel(self.gridLayoutWidget_3)
        self.qicon.setObjectName(u"qicon")
        self.qicon.setMaximumSize(QSize(50, 50))
        self.qicon.setPixmap(QPixmap(u"redtrain.png"))
        self.qicon.setScaledContents(True)
        self.qicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.qicon, 5, 1, 1, 1)

        self.wicon = QLabel(self.gridLayoutWidget_3)
        self.wicon.setObjectName(u"wicon")
        self.wicon.setMaximumSize(QSize(50, 50))
        self.wicon.setPixmap(QPixmap(u"redtrain.png"))
        self.wicon.setScaledContents(True)
        self.wicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.wicon, 11, 1, 1, 1)

        self.picon = QLabel(self.gridLayoutWidget_3)
        self.picon.setObjectName(u"picon")
        self.picon.setMaximumSize(QSize(50, 50))
        self.picon.setPixmap(QPixmap(u"tracks.png"))
        self.picon.setScaledContents(True)
        self.picon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.picon, 4, 1, 1, 1)

        self.pusho = QPushButton(self.gridLayoutWidget_3)
        self.pusho.setObjectName(u"pusho")

        self.gridLayout_4.addWidget(self.pusho, 3, 0, 1, 1)

        self.pushu = QPushButton(self.gridLayoutWidget_3)
        self.pushu.setObjectName(u"pushu")

        self.gridLayout_4.addWidget(self.pushu, 9, 0, 1, 1)

        self.sectiontitle_2 = QLabel(self.gridLayoutWidget_3)
        self.sectiontitle_2.setObjectName(u"sectiontitle_2")
        self.sectiontitle_2.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.sectiontitle_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.sectiontitle_2, 1, 0, 1, 1)

        self.sicon = QLabel(self.gridLayoutWidget_3)
        self.sicon.setObjectName(u"sicon")
        self.sicon.setMaximumSize(QSize(50, 50))
        self.sicon.setPixmap(QPixmap(u"tracks.png"))
        self.sicon.setScaledContents(True)
        self.sicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.sicon, 7, 1, 1, 1)

        self.nicon = QLabel(self.gridLayoutWidget_3)
        self.nicon.setObjectName(u"nicon")
        self.nicon.setMaximumSize(QSize(50, 50))
        self.nicon.setPixmap(QPixmap(u"tracks.png"))
        self.nicon.setScaledContents(True)
        self.nicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.nicon, 2, 1, 1, 1)

        self.pushv = QPushButton(self.gridLayoutWidget_3)
        self.pushv.setObjectName(u"pushv")

        self.gridLayout_4.addWidget(self.pushv, 10, 0, 1, 1)

        self.pushn = QPushButton(self.gridLayoutWidget_3)
        self.pushn.setObjectName(u"pushn")

        self.gridLayout_4.addWidget(self.pushn, 2, 0, 1, 1)

        self.pushy = QPushButton(self.gridLayoutWidget_3)
        self.pushy.setObjectName(u"pushy")

        self.gridLayout_4.addWidget(self.pushy, 13, 0, 1, 1)

        self.pushr = QPushButton(self.gridLayoutWidget_3)
        self.pushr.setObjectName(u"pushr")

        self.gridLayout_4.addWidget(self.pushr, 6, 0, 1, 1)

        self.ricon = QLabel(self.gridLayoutWidget_3)
        self.ricon.setObjectName(u"ricon")
        self.ricon.setMaximumSize(QSize(50, 50))
        self.ricon.setPixmap(QPixmap(u"tracks.png"))
        self.ricon.setScaledContents(True)
        self.ricon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.ricon, 6, 1, 1, 1)

        self.vicon = QLabel(self.gridLayoutWidget_3)
        self.vicon.setObjectName(u"vicon")
        self.vicon.setMaximumSize(QSize(50, 50))
        self.vicon.setPixmap(QPixmap(u"tracks.png"))
        self.vicon.setScaledContents(True)
        self.vicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.vicon, 10, 1, 1, 1)

        self.pushw = QPushButton(self.gridLayoutWidget_3)
        self.pushw.setObjectName(u"pushw")

        self.gridLayout_4.addWidget(self.pushw, 11, 0, 1, 1)

        self.uicon = QLabel(self.gridLayoutWidget_3)
        self.uicon.setObjectName(u"uicon")
        self.uicon.setMaximumSize(QSize(50, 50))
        self.uicon.setPixmap(QPixmap(u"tracks.png"))
        self.uicon.setScaledContents(True)
        self.uicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.uicon, 9, 1, 1, 1)

        self.pushx = QPushButton(self.gridLayoutWidget_3)
        self.pushx.setObjectName(u"pushx")

        self.gridLayout_4.addWidget(self.pushx, 12, 0, 1, 1)

        self.pushz = QPushButton(self.gridLayoutWidget_3)
        self.pushz.setObjectName(u"pushz")

        self.gridLayout_4.addWidget(self.pushz, 14, 0, 1, 1)

        self.xicon = QLabel(self.gridLayoutWidget_3)
        self.xicon.setObjectName(u"xicon")
        self.xicon.setMaximumSize(QSize(50, 50))
        self.xicon.setPixmap(QPixmap(u"tracks.png"))
        self.xicon.setScaledContents(True)
        self.xicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.xicon, 12, 1, 1, 1)

        self.yicon = QLabel(self.gridLayoutWidget_3)
        self.yicon.setObjectName(u"yicon")
        self.yicon.setMaximumSize(QSize(50, 50))
        self.yicon.setPixmap(QPixmap(u"tracks.png"))
        self.yicon.setScaledContents(True)
        self.yicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.yicon, 13, 1, 1, 1)

        self.zicon = QLabel(self.gridLayoutWidget_3)
        self.zicon.setObjectName(u"zicon")
        self.zicon.setMaximumSize(QSize(50, 50))
        self.zicon.setPixmap(QPixmap(u"tracks.png"))
        self.zicon.setScaledContents(True)
        self.zicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.zicon, 14, 1, 1, 1)

        self.verticalLayoutWidget_6 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(250, 180, 451, 149))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.verticalLayoutWidget_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_18)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.verticalLayoutWidget_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_13)

        self.ca = QPushButton(self.verticalLayoutWidget_6)
        self.ca.setObjectName(u"ca")
        self.ca.setCheckable(False)

        self.horizontalLayout_11.addWidget(self.ca)

        self.cb = QPushButton(self.verticalLayoutWidget_6)
        self.cb.setObjectName(u"cb")

        self.horizontalLayout_11.addWidget(self.cb)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_14 = QLabel(self.verticalLayoutWidget_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_14)

        self.ga = QPushButton(self.verticalLayoutWidget_6)
        self.ga.setObjectName(u"ga")
        self.ga.setCheckable(False)

        self.horizontalLayout.addWidget(self.ga)

        self.gb = QPushButton(self.verticalLayoutWidget_6)
        self.gb.setObjectName(u"gb")

        self.horizontalLayout.addWidget(self.gb)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        MainWindowA.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindowA)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 724, 25))
        MainWindowA.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindowA)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowA.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowA)

        QMetaObject.connectSlotsByName(MainWindowA)
    # setupUi

    def retranslateUi(self, MainWindowA):
        MainWindowA.setWindowTitle(QCoreApplication.translate("MainWindowA", u"MainWindow", None))
        self.label_50.setText(QCoreApplication.translate("MainWindowA", u"Crossing", None))
        self.label_51.setText(QCoreApplication.translate("MainWindowA", u"Position", None))
        self.label_52.setText(QCoreApplication.translate("MainWindowA", u"Lights", None))
        self.label_53.setText(QCoreApplication.translate("MainWindowA", u"1", None))
        self.gatepositiona.setText(QCoreApplication.translate("MainWindowA", u"Active", None))
        self.reda.setText("")
        self.yellowa.setText("")
        self.greena.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindowA", u"2", None))
        self.gatepositionb.setText(QCoreApplication.translate("MainWindowA", u"Inactive", None))
        self.redb.setText("")
        self.yellowb.setText("")
        self.greenb.setText("")
        self.trackconfiguration.setText(QCoreApplication.translate("MainWindowA", u"Upload PLC", None))
        self.automaticmode.setText(QCoreApplication.translate("MainWindowA", u"Automatic Mode", None))
        self.maintenancemode.setText(QCoreApplication.translate("MainWindowA", u"Maintenance Mode", None))
        self.activetrainlabel.setText(QCoreApplication.translate("MainWindowA", u"Active Trains  ", None))
        self.date.setText(QCoreApplication.translate("MainWindowA", u"2/19/2023", None))
        self.time.setText(QCoreApplication.translate("MainWindowA", u"11:44 PM", None))
        self.label_5.setText(QCoreApplication.translate("MainWindowA", u"Sections Managed:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindowA", u"Green Line", None))
        self.label_7.setText(QCoreApplication.translate("MainWindowA", u"N - Z", None))
        self.pushp.setText(QCoreApplication.translate("MainWindowA", u"P", None))
        self.pusht.setText(QCoreApplication.translate("MainWindowA", u"T", None))
        self.pushs.setText(QCoreApplication.translate("MainWindowA", u"S", None))
        self.pushq.setText(QCoreApplication.translate("MainWindowA", u"Q", None))
        self.occupancylabel_2.setText(QCoreApplication.translate("MainWindowA", u"Occupancy", None))
        self.ticon.setText("")
        self.oicon.setText("")
        self.qicon.setText("")
        self.wicon.setText("")
        self.picon.setText("")
        self.pusho.setText(QCoreApplication.translate("MainWindowA", u"O", None))
        self.pushu.setText(QCoreApplication.translate("MainWindowA", u"U", None))
        self.sectiontitle_2.setText(QCoreApplication.translate("MainWindowA", u"Section", None))
        self.sicon.setText("")
        self.nicon.setText("")
        self.pushv.setText(QCoreApplication.translate("MainWindowA", u"V", None))
        self.pushn.setText(QCoreApplication.translate("MainWindowA", u"N", None))
        self.pushy.setText(QCoreApplication.translate("MainWindowA", u"Y", None))
        self.pushr.setText(QCoreApplication.translate("MainWindowA", u"R", None))
        self.ricon.setText("")
        self.vicon.setText("")
        self.pushw.setText(QCoreApplication.translate("MainWindowA", u"W", None))
        self.uicon.setText("")
        self.pushx.setText(QCoreApplication.translate("MainWindowA", u"X", None))
        self.pushz.setText(QCoreApplication.translate("MainWindowA", u"Z", None))
        self.xicon.setText("")
        self.yicon.setText("")
        self.zicon.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindowA", u"Switches", None))
        self.label_13.setText(QCoreApplication.translate("MainWindowA", u"C", None))
        self.ca.setText(QCoreApplication.translate("MainWindowA", u"12-13", None))
        self.cb.setText(QCoreApplication.translate("MainWindowA", u"1-13", None))
        self.label_14.setText(QCoreApplication.translate("MainWindowA", u"G", None))
        self.ga.setText(QCoreApplication.translate("MainWindowA", u"29-30", None))
        self.gb.setText(QCoreApplication.translate("MainWindowA", u"29-150", None))
    # retranslateUi

