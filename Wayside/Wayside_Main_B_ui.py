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
        MainWindow.resize(724, 737)
        self.centralwidget = QWidget(MainWindow)
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
        self.verticalLayoutWidget_2.setGeometry(QRect(250, 0, 451, 151))
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
        self.gridLayoutWidget_3.setGeometry(QRect(10, 80, 221, 592))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setContentsMargins(0, 0, 9, 0)
        self.sectiontitle_2 = QLabel(self.gridLayoutWidget_3)
        self.sectiontitle_2.setObjectName(u"sectiontitle_2")
        self.sectiontitle_2.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.sectiontitle_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.sectiontitle_2, 1, 0, 1, 1)

        self.pushi = QPushButton(self.gridLayoutWidget_3)
        self.pushi.setObjectName(u"pushi")

        self.gridLayout_4.addWidget(self.pushi, 10, 0, 1, 1)

        self.pushf = QPushButton(self.gridLayoutWidget_3)
        self.pushf.setObjectName(u"pushf")

        self.gridLayout_4.addWidget(self.pushf, 7, 0, 1, 1)

        self.pushd = QPushButton(self.gridLayoutWidget_3)
        self.pushd.setObjectName(u"pushd")

        self.gridLayout_4.addWidget(self.pushd, 5, 0, 1, 1)

        self.cicon = QLabel(self.gridLayoutWidget_3)
        self.cicon.setObjectName(u"cicon")
        self.cicon.setMaximumSize(QSize(50, 50))
        self.cicon.setPixmap(QPixmap(u"tracks.png"))
        self.cicon.setScaledContents(True)
        self.cicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.cicon, 4, 1, 1, 1)

        self.pushe = QPushButton(self.gridLayoutWidget_3)
        self.pushe.setObjectName(u"pushe")

        self.gridLayout_4.addWidget(self.pushe, 6, 0, 1, 1)

        self.dicon = QLabel(self.gridLayoutWidget_3)
        self.dicon.setObjectName(u"dicon")
        self.dicon.setMaximumSize(QSize(50, 50))
        self.dicon.setPixmap(QPixmap(u"redtrain.png"))
        self.dicon.setScaledContents(True)
        self.dicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.dicon, 5, 1, 1, 1)

        self.pushc = QPushButton(self.gridLayoutWidget_3)
        self.pushc.setObjectName(u"pushc")

        self.gridLayout_4.addWidget(self.pushc, 4, 0, 1, 1)

        self.pusha = QPushButton(self.gridLayoutWidget_3)
        self.pusha.setObjectName(u"pusha")

        self.gridLayout_4.addWidget(self.pusha, 2, 0, 1, 1)

        self.hicon = QLabel(self.gridLayoutWidget_3)
        self.hicon.setObjectName(u"hicon")
        self.hicon.setMaximumSize(QSize(50, 50))
        self.hicon.setPixmap(QPixmap(u"tracks.png"))
        self.hicon.setScaledContents(True)
        self.hicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.hicon, 9, 1, 1, 1)

        self.pushg = QPushButton(self.gridLayoutWidget_3)
        self.pushg.setObjectName(u"pushg")

        self.gridLayout_4.addWidget(self.pushg, 8, 0, 1, 1)

        self.occupancylabel_2 = QLabel(self.gridLayoutWidget_3)
        self.occupancylabel_2.setObjectName(u"occupancylabel_2")
        self.occupancylabel_2.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_4.addWidget(self.occupancylabel_2, 1, 1, 1, 1)

        self.eicon = QLabel(self.gridLayoutWidget_3)
        self.eicon.setObjectName(u"eicon")
        self.eicon.setMaximumSize(QSize(50, 50))
        self.eicon.setPixmap(QPixmap(u"tracks.png"))
        self.eicon.setScaledContents(True)
        self.eicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.eicon, 6, 1, 1, 1)

        self.ficon = QLabel(self.gridLayoutWidget_3)
        self.ficon.setObjectName(u"ficon")
        self.ficon.setMaximumSize(QSize(50, 50))
        self.ficon.setPixmap(QPixmap(u"tracks.png"))
        self.ficon.setScaledContents(True)
        self.ficon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.ficon, 7, 1, 1, 1)

        self.iicon = QLabel(self.gridLayoutWidget_3)
        self.iicon.setObjectName(u"iicon")
        self.iicon.setMaximumSize(QSize(50, 50))
        self.iicon.setPixmap(QPixmap(u"tracks.png"))
        self.iicon.setScaledContents(True)
        self.iicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.iicon, 10, 1, 1, 1)

        self.bicon = QLabel(self.gridLayoutWidget_3)
        self.bicon.setObjectName(u"bicon")
        self.bicon.setMaximumSize(QSize(50, 50))
        self.bicon.setPixmap(QPixmap(u"tracks.png"))
        self.bicon.setScaledContents(True)
        self.bicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.bicon, 3, 1, 1, 1)

        self.pushj = QPushButton(self.gridLayoutWidget_3)
        self.pushj.setObjectName(u"pushj")

        self.gridLayout_4.addWidget(self.pushj, 11, 0, 1, 1)

        self.pushb = QPushButton(self.gridLayoutWidget_3)
        self.pushb.setObjectName(u"pushb")

        self.gridLayout_4.addWidget(self.pushb, 3, 0, 1, 1)

        self.pushh = QPushButton(self.gridLayoutWidget_3)
        self.pushh.setObjectName(u"pushh")

        self.gridLayout_4.addWidget(self.pushh, 9, 0, 1, 1)

        self.jicon = QLabel(self.gridLayoutWidget_3)
        self.jicon.setObjectName(u"jicon")
        self.jicon.setMaximumSize(QSize(50, 50))
        self.jicon.setPixmap(QPixmap(u"redtrain.png"))
        self.jicon.setScaledContents(True)
        self.jicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.jicon, 11, 1, 1, 1)

        self.aicon = QLabel(self.gridLayoutWidget_3)
        self.aicon.setObjectName(u"aicon")
        self.aicon.setMaximumSize(QSize(50, 50))
        self.aicon.setPixmap(QPixmap(u"tracks.png"))
        self.aicon.setScaledContents(True)
        self.aicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.aicon, 2, 1, 1, 1)

        self.gicon = QLabel(self.gridLayoutWidget_3)
        self.gicon.setObjectName(u"gicon")
        self.gicon.setMaximumSize(QSize(50, 50))
        self.gicon.setPixmap(QPixmap(u"tracks.png"))
        self.gicon.setScaledContents(True)
        self.gicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.gicon, 8, 1, 1, 1)

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
        self.gatepositiona.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.reda.setText("")
        self.yellowa.setText("")
        self.greena.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.gatepositionb.setText(QCoreApplication.translate("MainWindow", u"Inactive", None))
        self.redb.setText("")
        self.yellowb.setText("")
        self.greenb.setText("")
        self.trackconfiguration.setText(QCoreApplication.translate("MainWindow", u"Track Configuration", None))
        self.automaticmode.setText(QCoreApplication.translate("MainWindow", u"Automatic Mode", None))
        self.maintenancemode.setText(QCoreApplication.translate("MainWindow", u"Maintenance Mode", None))
        self.activetrainlabel.setText(QCoreApplication.translate("MainWindow", u"Active Trains  ", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"2/19/2023", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"11:44 PM", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Sections Managed:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"A- J", None))
        self.sectiontitle_2.setText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.pushi.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.pushf.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.pushd.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.cicon.setText("")
        self.pushe.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.dicon.setText("")
        self.pushc.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pusha.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.hicon.setText("")
        self.pushg.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.occupancylabel_2.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.eicon.setText("")
        self.ficon.setText("")
        self.iicon.setText("")
        self.bicon.setText("")
        self.pushj.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.pushb.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.pushh.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.jicon.setText("")
        self.aicon.setText("")
        self.gicon.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Switches", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.ca.setText(QCoreApplication.translate("MainWindow", u"12-13", None))
        self.cb.setText(QCoreApplication.translate("MainWindow", u"1-13", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.ga.setText(QCoreApplication.translate("MainWindow", u"29-30", None))
        self.gb.setText(QCoreApplication.translate("MainWindow", u"29-150", None))
    # retranslateUi

