# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Wayside_Test.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLCDNumber, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QSplitter, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(562, 690)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.maintenancemode = QPushButton(self.centralwidget)
        self.maintenancemode.setObjectName(u"maintenancemode")
        self.maintenancemode.setGeometry(QRect(160, 520, 391, 31))
        self.trackconfiguration = QPushButton(self.centralwidget)
        self.trackconfiguration.setObjectName(u"trackconfiguration")
        self.trackconfiguration.setGeometry(QRect(160, 478, 391, 31))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 12):
            self.tableWidget.setRowCount(12)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(5, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(6, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(7, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(8, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(9, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(10, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(11, 0, __qtablewidgetitem24)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 20, 141, 531))
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(137)
        self.tableWidget.verticalHeader().setDefaultSectionSize(42)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(100, 90, 31, 31))
        self.label_14.setPixmap(QPixmap(u"tracks.png"))
        self.label_14.setScaledContents(True)
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(100, 510, 31, 31))
        self.label_16.setPixmap(QPixmap(u"tracks.png"))
        self.label_16.setScaledContents(True)
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(100, 430, 31, 31))
        self.label_18.setPixmap(QPixmap(u"tracks.png"))
        self.label_18.setScaledContents(True)
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(100, 350, 31, 31))
        self.label_19.setPixmap(QPixmap(u"tracks.png"))
        self.label_19.setScaledContents(True)
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(100, 300, 31, 31))
        self.label_20.setPixmap(QPixmap(u"tracks.png"))
        self.label_20.setScaledContents(True)
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(100, 260, 31, 31))
        self.label_21.setPixmap(QPixmap(u"tracks.png"))
        self.label_21.setScaledContents(True)
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(100, 220, 31, 31))
        self.label_22.setPixmap(QPixmap(u"tracks.png"))
        self.label_22.setScaledContents(True)
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(100, 180, 31, 31))
        self.label_23.setPixmap(QPixmap(u"tracks.png"))
        self.label_23.setScaledContents(True)
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(100, 130, 31, 31))
        self.label_24.setPixmap(QPixmap(u"redtrain.png"))
        self.label_24.setScaledContents(True)
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(100, 50, 31, 31))
        self.label_25.setPixmap(QPixmap(u"tracks.png"))
        self.label_25.setScaledContents(True)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 560, 541, 71))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_27 = QLabel(self.verticalLayoutWidget)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_2.addWidget(self.label_27)

        self.sauthorityinput = QSpinBox(self.verticalLayoutWidget)
        self.sauthorityinput.setObjectName(u"sauthorityinput")
        self.sauthorityinput.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.sauthorityinput)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_26 = QLabel(self.verticalLayoutWidget)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_3.addWidget(self.label_26)

        self.sspeedinput = QSpinBox(self.verticalLayoutWidget)
        self.sspeedinput.setObjectName(u"sspeedinput")
        self.sspeedinput.setMaximum(999)

        self.horizontalLayout_3.addWidget(self.sspeedinput)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(160, 19, 241, 101))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.cauthlabel = QLabel(self.verticalLayoutWidget_2)
        self.cauthlabel.setObjectName(u"cauthlabel")

        self.horizontalLayout_9.addWidget(self.cauthlabel)

        self.cauthoritydisp = QLCDNumber(self.verticalLayoutWidget_2)
        self.cauthoritydisp.setObjectName(u"cauthoritydisp")

        self.horizontalLayout_9.addWidget(self.cauthoritydisp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.sauthlabel = QLabel(self.verticalLayoutWidget_2)
        self.sauthlabel.setObjectName(u"sauthlabel")

        self.horizontalLayout_8.addWidget(self.sauthlabel)

        self.sauthoritydisp = QLCDNumber(self.verticalLayoutWidget_2)
        self.sauthoritydisp.setObjectName(u"sauthoritydisp")

        self.horizontalLayout_8.addWidget(self.sauthoritydisp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sspeedlabel = QLabel(self.verticalLayoutWidget_2)
        self.sspeedlabel.setObjectName(u"sspeedlabel")

        self.horizontalLayout_4.addWidget(self.sspeedlabel)

        self.sspeeddisp = QLCDNumber(self.verticalLayoutWidget_2)
        self.sspeeddisp.setObjectName(u"sspeeddisp")

        self.horizontalLayout_4.addWidget(self.sspeeddisp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(160, 440, 394, 31))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.activetrainlabel = QLabel(self.verticalLayoutWidget_3)
        self.activetrainlabel.setObjectName(u"activetrainlabel")

        self.horizontalLayout_7.addWidget(self.activetrainlabel)

        self.activetrains = QLCDNumber(self.verticalLayoutWidget_3)
        self.activetrains.setObjectName(u"activetrains")

        self.horizontalLayout_7.addWidget(self.activetrains)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(410, 20, 141, 101))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.date = QLabel(self.verticalLayoutWidget_4)
        self.date.setObjectName(u"date")
        self.date.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.date)

        self.time = QLabel(self.verticalLayoutWidget_4)
        self.time.setObjectName(u"time")
        self.time.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.time)

        self.label_37 = QLabel(self.centralwidget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(100, 470, 31, 31))
        self.label_37.setPixmap(QPixmap(u"redtrain.png"))
        self.label_37.setScaledContents(True)
        self.label_38 = QLabel(self.centralwidget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(100, 390, 31, 31))
        self.label_38.setPixmap(QPixmap(u"tracks.png"))
        self.label_38.setScaledContents(True)
        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(158, 128, 391, 181))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.verticalLayoutWidget_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_17)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_2 = QLabel(self.verticalLayoutWidget_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_10.addWidget(self.label_2)

        self.label_6 = QLabel(self.verticalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_10.addWidget(self.label_6)

        self.label_5 = QLabel(self.verticalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_5.setFrameShadow(QFrame.Plain)
        self.label_5.setTextFormat(Qt.AutoText)

        self.horizontalLayout_10.addWidget(self.label_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.verticalLayoutWidget_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_11.addWidget(self.label_4)

        self.label_8 = QLabel(self.verticalLayoutWidget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_11.addWidget(self.label_8)

        self.label_7 = QLabel(self.verticalLayoutWidget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_11.addWidget(self.label_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_13 = QLabel(self.verticalLayoutWidget_5)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_12.addWidget(self.label_13)

        self.label_10 = QLabel(self.verticalLayoutWidget_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_12.addWidget(self.label_10)

        self.label_9 = QLabel(self.verticalLayoutWidget_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_12.addWidget(self.label_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.verticalLayoutWidget_5)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.label_12 = QLabel(self.verticalLayoutWidget_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_13.addWidget(self.label_12)

        self.label_11 = QLabel(self.verticalLayoutWidget_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_13.addWidget(self.label_11)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.verticalLayoutWidget_8 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(160, 320, 391, 111))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_50 = QLabel(self.verticalLayoutWidget_8)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_50)

        self.label_51 = QLabel(self.verticalLayoutWidget_8)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_51)

        self.label_52 = QLabel(self.verticalLayoutWidget_8)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_52)


        self.verticalLayout_9.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_53 = QLabel(self.verticalLayoutWidget_8)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_20.addWidget(self.label_53)

        self.label_54 = QLabel(self.verticalLayoutWidget_8)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_20.addWidget(self.label_54)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_35 = QLabel(self.verticalLayoutWidget_8)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(21, 21))
        self.label_35.setPixmap(QPixmap(u"redlight.png"))
        self.label_35.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.label_35)

        self.label_32 = QLabel(self.verticalLayoutWidget_8)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(21, 21))
        self.label_32.setPixmap(QPixmap(u"yellowlight.png"))
        self.label_32.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.label_32)

        self.label_33 = QLabel(self.verticalLayoutWidget_8)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(21, 21))
        self.label_33.setPixmap(QPixmap(u"greenlight.png"))
        self.label_33.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.label_33)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_27)


        self.verticalLayout_9.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_55 = QLabel(self.verticalLayoutWidget_8)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_21.addWidget(self.label_55)

        self.label_56 = QLabel(self.verticalLayoutWidget_8)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFrameShadow(QFrame.Plain)

        self.horizontalLayout_21.addWidget(self.label_56)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_36 = QLabel(self.verticalLayoutWidget_8)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(21, 21))
        self.label_36.setPixmap(QPixmap(u"redlight.png"))
        self.label_36.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.label_36)

        self.label_39 = QLabel(self.verticalLayoutWidget_8)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(21, 21))
        self.label_39.setPixmap(QPixmap(u"yellowlight.png"))
        self.label_39.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.label_39)

        self.label_40 = QLabel(self.verticalLayoutWidget_8)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(21, 21))
        self.label_40.setPixmap(QPixmap(u"greenlight.png"))
        self.label_40.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.label_40)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_29)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_28)


        self.verticalLayout_9.addLayout(self.horizontalLayout_21)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(410, 21, 143, 51))
        self.splitter.setOrientation(Qt.Vertical)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 562, 25))
        self.menuWayside_UI = QMenu(self.menubar)
        self.menuWayside_UI.setObjectName(u"menuWayside_UI")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuWayside_UI.menuAction())

        self.retranslateUi(MainWindow)
        self.sauthorityinput.valueChanged.connect(self.sauthoritydisp.display)
        self.sspeedinput.valueChanged.connect(self.sspeeddisp.display)
        self.sauthorityinput.valueChanged.connect(self.cauthoritydisp.display)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.maintenancemode.setText(QCoreApplication.translate("MainWindow", u"Maintenance Mode", None))
        self.trackconfiguration.setText(QCoreApplication.translate("MainWindow", u"Track Configuration", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Section", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem1 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u" A", None));
        ___qtablewidgetitem2 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u" B", None));
        ___qtablewidgetitem3 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u" C", None));
        ___qtablewidgetitem4 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u" D", None));
        ___qtablewidgetitem5 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u" E", None));
        ___qtablewidgetitem6 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u" F", None));
        ___qtablewidgetitem7 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u" G", None));
        ___qtablewidgetitem8 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u" H", None));
        ___qtablewidgetitem9 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u" I", None));
        ___qtablewidgetitem10 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u" J", None));
        ___qtablewidgetitem11 = self.tableWidget.item(10, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u" K", None));
        ___qtablewidgetitem12 = self.tableWidget.item(11, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u" L", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_14.setText("")
        self.label_16.setText("")
        self.label_18.setText("")
        self.label_19.setText("")
        self.label_20.setText("")
        self.label_21.setText("")
        self.label_22.setText("")
        self.label_23.setText("")
        self.label_24.setText("")
        self.label_25.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Suggested Authority", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.cauthlabel.setText(QCoreApplication.translate("MainWindow", u"Commanded Authority", None))
        self.sauthlabel.setText(QCoreApplication.translate("MainWindow", u"Suggested Authority    ", None))
        self.sspeedlabel.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed         ", None))
        self.activetrainlabel.setText(QCoreApplication.translate("MainWindow", u"                                       Active Trains  ", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"2/19/2023 ", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"11:44 PM", None))
        self.label_37.setText("")
        self.label_38.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Switch", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" C", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"1 - 13", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"12 - 13", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u" G", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"29 - 150", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"29 - 30", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u" J", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"57 - 58", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"57 - Yard", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u" J", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"62 - 63", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Yard - 63", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Gates", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u" 1", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.label_35.setText("")
        self.label_32.setText("")
        self.label_33.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u" 2", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Inactive", None))
        self.label_36.setText("")
        self.label_39.setText("")
        self.label_40.setText("")
        self.menuWayside_UI.setTitle(QCoreApplication.translate("MainWindow", u"Wayside UI", None))
    # retranslateUi

