# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Wayside_Test_B.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLCDNumber, QLabel, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QSplitter, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(691, 743)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_8 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(230, 311, 451, 111))
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


        self.horizontalLayout_21.addLayout(self.horizontalLayout_29)


        self.verticalLayout_9.addLayout(self.horizontalLayout_21)

        self.trackconfiguration = QPushButton(self.centralwidget)
        self.trackconfiguration.setObjectName(u"trackconfiguration")
        self.trackconfiguration.setGeometry(QRect(230, 510, 451, 31))
        self.trackconfiguration.setStyleSheet(u"font: 9pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(480, 11, 143, 51))
        self.splitter.setOrientation(Qt.Vertical)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 211, 531))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setContentsMargins(0, 0, 9, 0)
        self.pusha = QPushButton(self.gridLayoutWidget)
        self.pusha.setObjectName(u"pusha")

        self.gridLayout_2.addWidget(self.pusha, 2, 0, 1, 1)

        self.aicon = QLabel(self.gridLayoutWidget)
        self.aicon.setObjectName(u"aicon")
        self.aicon.setMaximumSize(QSize(31, 31))
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

        self.pushj = QPushButton(self.gridLayoutWidget)
        self.pushj.setObjectName(u"pushj")

        self.gridLayout_2.addWidget(self.pushj, 12, 0, 1, 1)

        self.kicon = QLabel(self.gridLayoutWidget)
        self.kicon.setObjectName(u"kicon")
        self.kicon.setMaximumSize(QSize(31, 31))
        self.kicon.setPixmap(QPixmap(u"tracks.png"))
        self.kicon.setScaledContents(True)
        self.kicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.kicon, 13, 1, 1, 1)

        self.pushh = QPushButton(self.gridLayoutWidget)
        self.pushh.setObjectName(u"pushh")

        self.gridLayout_2.addWidget(self.pushh, 10, 0, 1, 1)

        self.eicon = QLabel(self.gridLayoutWidget)
        self.eicon.setObjectName(u"eicon")
        self.eicon.setMaximumSize(QSize(31, 31))
        self.eicon.setPixmap(QPixmap(u"tracks.png"))
        self.eicon.setScaledContents(True)
        self.eicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.eicon, 7, 1, 1, 1)

        self.bicon = QLabel(self.gridLayoutWidget)
        self.bicon.setObjectName(u"bicon")
        self.bicon.setMaximumSize(QSize(31, 31))
        self.bicon.setPixmap(QPixmap(u"tracks.png"))
        self.bicon.setScaledContents(True)
        self.bicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.bicon, 4, 1, 1, 1)

        self.ficon = QLabel(self.gridLayoutWidget)
        self.ficon.setObjectName(u"ficon")
        self.ficon.setMaximumSize(QSize(31, 31))
        self.ficon.setPixmap(QPixmap(u"tracks.png"))
        self.ficon.setScaledContents(True)
        self.ficon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.ficon, 8, 1, 1, 1)

        self.iicon = QLabel(self.gridLayoutWidget)
        self.iicon.setObjectName(u"iicon")
        self.iicon.setMaximumSize(QSize(31, 31))
        self.iicon.setPixmap(QPixmap(u"tracks.png"))
        self.iicon.setScaledContents(True)
        self.iicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.iicon, 11, 1, 1, 1)

        self.dicon = QLabel(self.gridLayoutWidget)
        self.dicon.setObjectName(u"dicon")
        self.dicon.setMaximumSize(QSize(31, 31))
        self.dicon.setPixmap(QPixmap(u"tracks.png"))
        self.dicon.setScaledContents(True)
        self.dicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.dicon, 6, 1, 1, 1)

        self.pushl = QPushButton(self.gridLayoutWidget)
        self.pushl.setObjectName(u"pushl")

        self.gridLayout_2.addWidget(self.pushl, 14, 0, 1, 1)

        self.pushe = QPushButton(self.gridLayoutWidget)
        self.pushe.setObjectName(u"pushe")

        self.gridLayout_2.addWidget(self.pushe, 7, 0, 1, 1)

        self.pushf = QPushButton(self.gridLayoutWidget)
        self.pushf.setObjectName(u"pushf")

        self.gridLayout_2.addWidget(self.pushf, 8, 0, 1, 1)

        self.pushg = QPushButton(self.gridLayoutWidget)
        self.pushg.setObjectName(u"pushg")

        self.gridLayout_2.addWidget(self.pushg, 9, 0, 1, 1)

        self.pushc = QPushButton(self.gridLayoutWidget)
        self.pushc.setObjectName(u"pushc")

        self.gridLayout_2.addWidget(self.pushc, 5, 0, 1, 1)

        self.jicon = QLabel(self.gridLayoutWidget)
        self.jicon.setObjectName(u"jicon")
        self.jicon.setMaximumSize(QSize(31, 31))
        self.jicon.setPixmap(QPixmap(u"tracks.png"))
        self.jicon.setScaledContents(True)
        self.jicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.jicon, 12, 1, 1, 1)

        self.occupancylabel = QLabel(self.gridLayoutWidget)
        self.occupancylabel.setObjectName(u"occupancylabel")
        self.occupancylabel.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.occupancylabel, 1, 1, 1, 1)

        self.gicon = QLabel(self.gridLayoutWidget)
        self.gicon.setObjectName(u"gicon")
        self.gicon.setMaximumSize(QSize(31, 31))
        self.gicon.setPixmap(QPixmap(u"tracks.png"))
        self.gicon.setScaledContents(True)
        self.gicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.gicon, 9, 1, 1, 1)

        self.hicon = QLabel(self.gridLayoutWidget)
        self.hicon.setObjectName(u"hicon")
        self.hicon.setMaximumSize(QSize(31, 31))
        self.hicon.setPixmap(QPixmap(u"redtrain.png"))
        self.hicon.setScaledContents(True)
        self.hicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.hicon, 10, 1, 1, 1)

        self.pushd = QPushButton(self.gridLayoutWidget)
        self.pushd.setObjectName(u"pushd")

        self.gridLayout_2.addWidget(self.pushd, 6, 0, 1, 1)

        self.pushi = QPushButton(self.gridLayoutWidget)
        self.pushi.setObjectName(u"pushi")

        self.gridLayout_2.addWidget(self.pushi, 11, 0, 1, 1)

        self.cicon = QLabel(self.gridLayoutWidget)
        self.cicon.setObjectName(u"cicon")
        self.cicon.setMaximumSize(QSize(31, 31))
        self.cicon.setPixmap(QPixmap(u"redtrain.png"))
        self.cicon.setScaledContents(True)
        self.cicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.cicon, 5, 1, 1, 1)

        self.licon = QLabel(self.gridLayoutWidget)
        self.licon.setObjectName(u"licon")
        self.licon.setMaximumSize(QSize(31, 31))
        self.licon.setPixmap(QPixmap(u"tracks.png"))
        self.licon.setScaledContents(True)
        self.licon.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.licon, 14, 1, 1, 1)

        self.pushk = QPushButton(self.gridLayoutWidget)
        self.pushk.setObjectName(u"pushk")

        self.gridLayout_2.addWidget(self.pushk, 13, 0, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(230, 10, 331, 101))
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
        self.verticalLayoutWidget_5.setGeometry(QRect(228, 118, 451, 187))
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

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.verticalLayoutWidget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_4)

        self.ga = QPushButton(self.verticalLayoutWidget_5)
        self.ga.setObjectName(u"ga")

        self.horizontalLayout_11.addWidget(self.ga)

        self.gb = QPushButton(self.verticalLayoutWidget_5)
        self.gb.setObjectName(u"gb")

        self.horizontalLayout_11.addWidget(self.gb)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_13 = QLabel(self.verticalLayoutWidget_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_13)

        self.j1a = QPushButton(self.verticalLayoutWidget_5)
        self.j1a.setObjectName(u"j1a")

        self.horizontalLayout_12.addWidget(self.j1a)

        self.j1b = QPushButton(self.verticalLayoutWidget_5)
        self.j1b.setObjectName(u"j1b")

        self.horizontalLayout_12.addWidget(self.j1b)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.verticalLayoutWidget_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_15)

        self.j2a = QPushButton(self.verticalLayoutWidget_5)
        self.j2a.setObjectName(u"j2a")

        self.horizontalLayout_13.addWidget(self.j2a)

        self.j2b = QPushButton(self.verticalLayoutWidget_5)
        self.j2b.setObjectName(u"j2b")

        self.horizontalLayout_13.addWidget(self.j2b)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 550, 671, 141))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line_3 = QFrame(self.verticalLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_27 = QLabel(self.verticalLayoutWidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_27.setAlignment(Qt.AlignCenter)

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
        self.label_26.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_26)

        self.sspeedinput = QSpinBox(self.verticalLayoutWidget)
        self.sspeedinput.setObjectName(u"sspeedinput")
        self.sspeedinput.setMaximum(999)

        self.horizontalLayout_3.addWidget(self.sspeedinput)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_37 = QLabel(self.verticalLayoutWidget)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_37)

        self.sectionbox = QComboBox(self.verticalLayoutWidget)
        self.sectionbox.addItem("")
        self.sectionbox.addItem("")
        self.sectionbox.addItem("")
        self.sectionbox.addItem("")
        self.sectionbox.addItem("")
        self.sectionbox.addItem("")
        self.sectionbox.addItem("")
        self.sectionbox.addItem("")
        self.sectionbox.addItem("")
        self.sectionbox.addItem("")
        self.sectionbox.addItem("")
        self.sectionbox.addItem("")
        self.sectionbox.setObjectName(u"sectionbox")

        self.horizontalLayout_18.addWidget(self.sectionbox)

        self.blockbox = QComboBox(self.verticalLayoutWidget)
        self.blockbox.setObjectName(u"blockbox")

        self.horizontalLayout_18.addWidget(self.blockbox)

        self.occupancybox = QComboBox(self.verticalLayoutWidget)
        self.occupancybox.addItem("")
        self.occupancybox.addItem("")
        self.occupancybox.setObjectName(u"occupancybox")

        self.horizontalLayout_18.addWidget(self.occupancybox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_18)

        self.horizontalLayoutWidget_7 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(229, 469, 451, 31))
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
        self.horizontalLayoutWidget_5.setGeometry(QRect(230, 430, 451, 31))
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
        self.verticalLayoutWidget_4.setGeometry(QRect(570, 10, 111, 101))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.date = QLabel(self.verticalLayoutWidget_4)
        self.date.setObjectName(u"date")
        self.date.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.date.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.date)

        self.time = QLabel(self.verticalLayoutWidget_4)
        self.time.setObjectName(u"time")
        self.time.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.time)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 691, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Gates", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Active", None))
        self.label_35.setText("")
        self.label_32.setText("")
        self.label_33.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Inactive", None))
        self.label_36.setText("")
        self.label_39.setText("")
        self.label_40.setText("")
        self.trackconfiguration.setText(QCoreApplication.translate("MainWindow", u"Track Configuration", None))
        self.pusha.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.aicon.setText("")
        self.sectiontitle.setText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.pushb.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.pushj.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.kicon.setText("")
        self.pushh.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.eicon.setText("")
        self.bicon.setText("")
        self.ficon.setText("")
        self.iicon.setText("")
        self.dicon.setText("")
        self.pushl.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.pushe.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.pushf.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.pushg.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.pushc.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.jicon.setText("")
        self.occupancylabel.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.gicon.setText("")
        self.hicon.setText("")
        self.pushd.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.pushi.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.cicon.setText("")
        self.licon.setText("")
        self.pushk.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.sspeedlabel.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed              ", None))
        self.sauthlabel.setText(QCoreApplication.translate("MainWindow", u"Suggested Authority     ", None))
        self.miles2.setText(QCoreApplication.translate("MainWindow", u"miles", None))
        self.cauthlabel.setText(QCoreApplication.translate("MainWindow", u"Commanded Authority", None))
        self.miles1.setText(QCoreApplication.translate("MainWindow", u"miles", None))
        self.miles2_2.setText(QCoreApplication.translate("MainWindow", u"mph", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Switches", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" C", None))
        self.ca.setText(QCoreApplication.translate("MainWindow", u"1 -13", None))
        self.cb.setText(QCoreApplication.translate("MainWindow", u"12 - 13", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u" G", None))
        self.ga.setText(QCoreApplication.translate("MainWindow", u"29 - 150", None))
        self.gb.setText(QCoreApplication.translate("MainWindow", u"29 - 30", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u" J", None))
        self.j1a.setText(QCoreApplication.translate("MainWindow", u"57 - 58", None))
        self.j1b.setText(QCoreApplication.translate("MainWindow", u"57 - Yard", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u" J", None))
        self.j2a.setText(QCoreApplication.translate("MainWindow", u"62 - 63", None))
        self.j2b.setText(QCoreApplication.translate("MainWindow", u"Yard - 63", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Suggested Authority", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Change Occupancy", None))
        self.sectionbox.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.sectionbox.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.sectionbox.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))
        self.sectionbox.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.sectionbox.setItemText(4, QCoreApplication.translate("MainWindow", u"E", None))
        self.sectionbox.setItemText(5, QCoreApplication.translate("MainWindow", u"F", None))
        self.sectionbox.setItemText(6, QCoreApplication.translate("MainWindow", u"G", None))
        self.sectionbox.setItemText(7, QCoreApplication.translate("MainWindow", u"H", None))
        self.sectionbox.setItemText(8, QCoreApplication.translate("MainWindow", u"I", None))
        self.sectionbox.setItemText(9, QCoreApplication.translate("MainWindow", u"J", None))
        self.sectionbox.setItemText(10, QCoreApplication.translate("MainWindow", u"K", None))
        self.sectionbox.setItemText(11, QCoreApplication.translate("MainWindow", u"L", None))

        self.sectionbox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.blockbox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Block", None))
        self.occupancybox.setItemText(0, QCoreApplication.translate("MainWindow", u"Occupied", None))
        self.occupancybox.setItemText(1, QCoreApplication.translate("MainWindow", u"Unoccupied", None))

        self.occupancybox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Occupancy", None))
        self.automaticmode.setText(QCoreApplication.translate("MainWindow", u"Automatic Mode", None))
        self.maintenancemode.setText(QCoreApplication.translate("MainWindow", u"Maintenance Mode", None))
        self.activetrainlabel.setText(QCoreApplication.translate("MainWindow", u"Active Trains  ", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"2/19/2023", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"11:44 PM", None))
    # retranslateUi

