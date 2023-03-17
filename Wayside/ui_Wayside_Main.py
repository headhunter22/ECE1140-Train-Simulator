# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Wayside_Main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(718, 610)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.maintenancemode = QPushButton(self.centralwidget)
        self.maintenancemode.setObjectName(u"maintenancemode")
        self.maintenancemode.setGeometry(QRect(250, 520, 451, 29))
        self.trackconfiguration = QPushButton(self.centralwidget)
        self.trackconfiguration.setObjectName(u"trackconfiguration")
        self.trackconfiguration.setGeometry(QRect(250, 470, 451, 29))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 0, 141, 20))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 221, 521))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setContentsMargins(0, 0, 9, 0)
        self.sectiontitle = QLabel(self.gridLayoutWidget)
        self.sectiontitle.setObjectName(u"sectiontitle")
        self.sectiontitle.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.sectiontitle.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.sectiontitle, 1, 0, 1, 1)

        self.pushc_7 = QPushButton(self.gridLayoutWidget)
        self.pushc_7.setObjectName(u"pushc_7")

        self.gridLayout_2.addWidget(self.pushc_7, 10, 0, 1, 1)

        self.pushc_4 = QPushButton(self.gridLayoutWidget)
        self.pushc_4.setObjectName(u"pushc_4")

        self.gridLayout_2.addWidget(self.pushc_4, 7, 0, 1, 1)

        self.pushc_2 = QPushButton(self.gridLayoutWidget)
        self.pushc_2.setObjectName(u"pushc_2")

        self.gridLayout_2.addWidget(self.pushc_2, 5, 0, 1, 1)

        self.bicon = QLabel(self.gridLayoutWidget)
        self.bicon.setObjectName(u"bicon")
        self.bicon.setMaximumSize(QSize(50, 50))
        self.bicon.setPixmap(QPixmap(u"tracks.png"))
        self.bicon.setScaledContents(True)
        self.bicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.bicon, 4, 1, 1, 1)

        self.pushc_3 = QPushButton(self.gridLayoutWidget)
        self.pushc_3.setObjectName(u"pushc_3")

        self.gridLayout_2.addWidget(self.pushc_3, 6, 0, 1, 1)

        self.cicon = QLabel(self.gridLayoutWidget)
        self.cicon.setObjectName(u"cicon")
        self.cicon.setMaximumSize(QSize(50, 50))
        self.cicon.setPixmap(QPixmap(u"redtrain.png"))
        self.cicon.setScaledContents(True)
        self.cicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.cicon, 5, 1, 1, 1)

        self.pushc = QPushButton(self.gridLayoutWidget)
        self.pushc.setObjectName(u"pushc")

        self.gridLayout_2.addWidget(self.pushc, 4, 0, 1, 1)

        self.pusha = QPushButton(self.gridLayoutWidget)
        self.pusha.setObjectName(u"pusha")

        self.gridLayout_2.addWidget(self.pusha, 2, 0, 1, 1)

        self.bicon_3 = QLabel(self.gridLayoutWidget)
        self.bicon_3.setObjectName(u"bicon_3")
        self.bicon_3.setMaximumSize(QSize(50, 50))
        self.bicon_3.setPixmap(QPixmap(u"tracks.png"))
        self.bicon_3.setScaledContents(True)
        self.bicon_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.bicon_3, 9, 1, 1, 1)

        self.pushc_5 = QPushButton(self.gridLayoutWidget)
        self.pushc_5.setObjectName(u"pushc_5")

        self.gridLayout_2.addWidget(self.pushc_5, 8, 0, 1, 1)

        self.occupancylabel = QLabel(self.gridLayoutWidget)
        self.occupancylabel.setObjectName(u"occupancylabel")
        self.occupancylabel.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.occupancylabel, 1, 1, 1, 1)

        self.bicon_2 = QLabel(self.gridLayoutWidget)
        self.bicon_2.setObjectName(u"bicon_2")
        self.bicon_2.setMaximumSize(QSize(50, 50))
        self.bicon_2.setPixmap(QPixmap(u"tracks.png"))
        self.bicon_2.setScaledContents(True)
        self.bicon_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.bicon_2, 6, 1, 1, 1)

        self.bicon_4 = QLabel(self.gridLayoutWidget)
        self.bicon_4.setObjectName(u"bicon_4")
        self.bicon_4.setMaximumSize(QSize(50, 50))
        self.bicon_4.setPixmap(QPixmap(u"tracks.png"))
        self.bicon_4.setScaledContents(True)
        self.bicon_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.bicon_4, 7, 1, 1, 1)

        self.bicon_6 = QLabel(self.gridLayoutWidget)
        self.bicon_6.setObjectName(u"bicon_6")
        self.bicon_6.setMaximumSize(QSize(50, 50))
        self.bicon_6.setPixmap(QPixmap(u"tracks.png"))
        self.bicon_6.setScaledContents(True)
        self.bicon_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.bicon_6, 10, 1, 1, 1)

        self.aicon_2 = QLabel(self.gridLayoutWidget)
        self.aicon_2.setObjectName(u"aicon_2")
        self.aicon_2.setMaximumSize(QSize(50, 50))
        self.aicon_2.setPixmap(QPixmap(u"tracks.png"))
        self.aicon_2.setScaledContents(True)
        self.aicon_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.aicon_2, 3, 1, 1, 1)

        self.pushc_8 = QPushButton(self.gridLayoutWidget)
        self.pushc_8.setObjectName(u"pushc_8")

        self.gridLayout_2.addWidget(self.pushc_8, 11, 0, 1, 1)

        self.pushb = QPushButton(self.gridLayoutWidget)
        self.pushb.setObjectName(u"pushb")

        self.gridLayout_2.addWidget(self.pushb, 3, 0, 1, 1)

        self.pushc_6 = QPushButton(self.gridLayoutWidget)
        self.pushc_6.setObjectName(u"pushc_6")

        self.gridLayout_2.addWidget(self.pushc_6, 9, 0, 1, 1)

        self.cicon_2 = QLabel(self.gridLayoutWidget)
        self.cicon_2.setObjectName(u"cicon_2")
        self.cicon_2.setMaximumSize(QSize(50, 50))
        self.cicon_2.setPixmap(QPixmap(u"redtrain.png"))
        self.cicon_2.setScaledContents(True)
        self.cicon_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.cicon_2, 11, 1, 1, 1)

        self.aicon = QLabel(self.gridLayoutWidget)
        self.aicon.setObjectName(u"aicon")
        self.aicon.setMaximumSize(QSize(50, 50))
        self.aicon.setPixmap(QPixmap(u"tracks.png"))
        self.aicon.setScaledContents(True)
        self.aicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.aicon, 2, 1, 1, 1)

        self.bicon_5 = QLabel(self.gridLayoutWidget)
        self.bicon_5.setObjectName(u"bicon_5")
        self.bicon_5.setMaximumSize(QSize(50, 50))
        self.bicon_5.setPixmap(QPixmap(u"tracks.png"))
        self.bicon_5.setScaledContents(True)
        self.bicon_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.bicon_5, 8, 1, 1, 1)

        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(250, 150, 451, 149))
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
        self.label_13 = QLabel(self.verticalLayoutWidget_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_13)

        self.ca = QPushButton(self.verticalLayoutWidget_5)
        self.ca.setObjectName(u"ca")
        self.ca.setCheckable(False)

        self.horizontalLayout_10.addWidget(self.ca)

        self.cb = QPushButton(self.verticalLayoutWidget_5)
        self.cb.setObjectName(u"cb")

        self.horizontalLayout_10.addWidget(self.cb)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_14 = QLabel(self.verticalLayoutWidget_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_14)

        self.ca_2 = QPushButton(self.verticalLayoutWidget_5)
        self.ca_2.setObjectName(u"ca_2")
        self.ca_2.setCheckable(False)

        self.horizontalLayout.addWidget(self.ca_2)

        self.cb_2 = QPushButton(self.verticalLayoutWidget_5)
        self.cb_2.setObjectName(u"cb_2")

        self.horizontalLayout.addWidget(self.cb_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.verticalLayoutWidget_8 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(250, 320, 451, 131))
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

        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(250, 30, 151, 101))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.time = QLabel(self.verticalLayoutWidget_4)
        self.time.setObjectName(u"time")
        self.time.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.time.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.time)

        self.date = QLabel(self.verticalLayoutWidget_4)
        self.date.setObjectName(u"date")
        self.date.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.date.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.date)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 718, 25))
        self.menuWayside_UI = QMenu(self.menubar)
        self.menuWayside_UI.setObjectName(u"menuWayside_UI")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuWayside_UI.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.maintenancemode.setText(QCoreApplication.translate("MainWindow", u"Maintenance Mode", None))
        self.trackconfiguration.setText(QCoreApplication.translate("MainWindow", u"Track Configuration", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"2/19/2023 11:44 PM", None))
        self.sectiontitle.setText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.pushc_7.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.pushc_4.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.pushc_2.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.bicon.setText("")
        self.pushc_3.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.cicon.setText("")
        self.pushc.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pusha.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.bicon_3.setText("")
        self.pushc_5.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.occupancylabel.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.bicon_2.setText("")
        self.bicon_4.setText("")
        self.bicon_6.setText("")
        self.aicon_2.setText("")
        self.pushc_8.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.pushb.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.pushc_6.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.cicon_2.setText("")
        self.aicon.setText("")
        self.bicon_5.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Switches", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.ca.setText(QCoreApplication.translate("MainWindow", u"12-13", None))
        self.cb.setText(QCoreApplication.translate("MainWindow", u"1-13", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.ca_2.setText(QCoreApplication.translate("MainWindow", u"29-30", None))
        self.cb_2.setText(QCoreApplication.translate("MainWindow", u"29-150", None))
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
        self.time.setText(QCoreApplication.translate("MainWindow", u"11:44 PM", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"2/19/2023", None))
        self.menuWayside_UI.setTitle(QCoreApplication.translate("MainWindow", u"Wayside UI", None))
    # retranslateUi

