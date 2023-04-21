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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLCDNumber, QLabel, QLayout,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindowA(object):
    def setupUi(self, MainWindowA):
        if not MainWindowA.objectName():
            MainWindowA.setObjectName(u"MainWindowA")
        MainWindowA.resize(740, 793)
        self.centralwidget = QWidget(MainWindowA)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 0, 621, 691))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.whichwayside = QComboBox(self.verticalLayoutWidget_2)
        self.whichwayside.addItem("")
        self.whichwayside.addItem("")
        self.whichwayside.addItem("")
        self.whichwayside.addItem("")
        self.whichwayside.setObjectName(u"whichwayside")
        self.whichwayside.setMaximumSize(QSize(639, 16777215))

        self.verticalLayout_4.addWidget(self.whichwayside)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setContentsMargins(0, -1, 9, -1)
        self.qicon = QLabel(self.verticalLayoutWidget_2)
        self.qicon.setObjectName(u"qicon")
        self.qicon.setMaximumSize(QSize(50, 50))
        self.qicon.setPixmap(QPixmap(u"tracks.png"))
        self.qicon.setScaledContents(True)
        self.qicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.qicon, 5, 1, 1, 1)

        self.pushu = QPushButton(self.verticalLayoutWidget_2)
        self.pushu.setObjectName(u"pushu")

        self.gridLayout_4.addWidget(self.pushu, 9, 0, 1, 1)

        self.picon = QLabel(self.verticalLayoutWidget_2)
        self.picon.setObjectName(u"picon")
        self.picon.setMaximumSize(QSize(50, 50))
        self.picon.setPixmap(QPixmap(u"tracks.png"))
        self.picon.setScaledContents(True)
        self.picon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.picon, 4, 1, 1, 1)

        self.pushq = QPushButton(self.verticalLayoutWidget_2)
        self.pushq.setObjectName(u"pushq")

        self.gridLayout_4.addWidget(self.pushq, 5, 0, 1, 1)

        self.pushp = QPushButton(self.verticalLayoutWidget_2)
        self.pushp.setObjectName(u"pushp")

        self.gridLayout_4.addWidget(self.pushp, 4, 0, 1, 1)

        self.pushx = QPushButton(self.verticalLayoutWidget_2)
        self.pushx.setObjectName(u"pushx")

        self.gridLayout_4.addWidget(self.pushx, 12, 0, 1, 1)

        self.pusht = QPushButton(self.verticalLayoutWidget_2)
        self.pusht.setObjectName(u"pusht")

        self.gridLayout_4.addWidget(self.pusht, 8, 0, 1, 1)

        self.oicon = QLabel(self.verticalLayoutWidget_2)
        self.oicon.setObjectName(u"oicon")
        self.oicon.setMaximumSize(QSize(50, 50))
        self.oicon.setPixmap(QPixmap(u"tracks.png"))
        self.oicon.setScaledContents(True)
        self.oicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.oicon, 3, 1, 1, 1)

        self.pushaa = QPushButton(self.verticalLayoutWidget_2)
        self.pushaa.setObjectName(u"pushaa")

        self.gridLayout_4.addWidget(self.pushaa, 15, 0, 1, 1)

        self.nicon = QLabel(self.verticalLayoutWidget_2)
        self.nicon.setObjectName(u"nicon")
        self.nicon.setMaximumSize(QSize(50, 50))
        self.nicon.setPixmap(QPixmap(u"tracks.png"))
        self.nicon.setScaledContents(True)
        self.nicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.nicon, 2, 1, 1, 1)

        self.zicon = QLabel(self.verticalLayoutWidget_2)
        self.zicon.setObjectName(u"zicon")
        self.zicon.setMaximumSize(QSize(50, 50))
        self.zicon.setPixmap(QPixmap(u"tracks.png"))
        self.zicon.setScaledContents(True)
        self.zicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.zicon, 14, 1, 1, 1)

        self.pushbb = QPushButton(self.verticalLayoutWidget_2)
        self.pushbb.setObjectName(u"pushbb")

        self.gridLayout_4.addWidget(self.pushbb, 16, 0, 1, 1)

        self.pushz = QPushButton(self.verticalLayoutWidget_2)
        self.pushz.setObjectName(u"pushz")

        self.gridLayout_4.addWidget(self.pushz, 14, 0, 1, 1)

        self.ricon = QLabel(self.verticalLayoutWidget_2)
        self.ricon.setObjectName(u"ricon")
        self.ricon.setMaximumSize(QSize(50, 50))
        self.ricon.setPixmap(QPixmap(u"tracks.png"))
        self.ricon.setScaledContents(True)
        self.ricon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.ricon, 6, 1, 1, 1)

        self.pushcc = QPushButton(self.verticalLayoutWidget_2)
        self.pushcc.setObjectName(u"pushcc")

        self.gridLayout_4.addWidget(self.pushcc, 17, 0, 1, 1)

        self.pushs = QPushButton(self.verticalLayoutWidget_2)
        self.pushs.setObjectName(u"pushs")

        self.gridLayout_4.addWidget(self.pushs, 7, 0, 1, 1)

        self.pushy = QPushButton(self.verticalLayoutWidget_2)
        self.pushy.setObjectName(u"pushy")

        self.gridLayout_4.addWidget(self.pushy, 13, 0, 1, 1)

        self.uicon = QLabel(self.verticalLayoutWidget_2)
        self.uicon.setObjectName(u"uicon")
        self.uicon.setMaximumSize(QSize(50, 50))
        self.uicon.setPixmap(QPixmap(u"tracks.png"))
        self.uicon.setScaledContents(True)
        self.uicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.uicon, 9, 1, 1, 1)

        self.occupancylabel_2 = QLabel(self.verticalLayoutWidget_2)
        self.occupancylabel_2.setObjectName(u"occupancylabel_2")
        self.occupancylabel_2.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_4.addWidget(self.occupancylabel_2, 1, 1, 1, 1)

        self.pusho = QPushButton(self.verticalLayoutWidget_2)
        self.pusho.setObjectName(u"pusho")

        self.gridLayout_4.addWidget(self.pusho, 3, 0, 1, 1)

        self.wicon = QLabel(self.verticalLayoutWidget_2)
        self.wicon.setObjectName(u"wicon")
        self.wicon.setMaximumSize(QSize(50, 50))
        self.wicon.setPixmap(QPixmap(u"tracks.png"))
        self.wicon.setScaledContents(True)
        self.wicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.wicon, 11, 1, 1, 1)

        self.sectiontitle_2 = QLabel(self.verticalLayoutWidget_2)
        self.sectiontitle_2.setObjectName(u"sectiontitle_2")
        self.sectiontitle_2.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.sectiontitle_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.sectiontitle_2, 1, 0, 1, 1)

        self.pushv = QPushButton(self.verticalLayoutWidget_2)
        self.pushv.setObjectName(u"pushv")

        self.gridLayout_4.addWidget(self.pushv, 10, 0, 1, 1)

        self.pushw = QPushButton(self.verticalLayoutWidget_2)
        self.pushw.setObjectName(u"pushw")

        self.gridLayout_4.addWidget(self.pushw, 11, 0, 1, 1)

        self.sicon = QLabel(self.verticalLayoutWidget_2)
        self.sicon.setObjectName(u"sicon")
        self.sicon.setMaximumSize(QSize(50, 50))
        self.sicon.setPixmap(QPixmap(u"tracks.png"))
        self.sicon.setScaledContents(True)
        self.sicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.sicon, 7, 1, 1, 1)

        self.xicon = QLabel(self.verticalLayoutWidget_2)
        self.xicon.setObjectName(u"xicon")
        self.xicon.setMaximumSize(QSize(50, 50))
        self.xicon.setPixmap(QPixmap(u"tracks.png"))
        self.xicon.setScaledContents(True)
        self.xicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.xicon, 12, 1, 1, 1)

        self.yicon = QLabel(self.verticalLayoutWidget_2)
        self.yicon.setObjectName(u"yicon")
        self.yicon.setMaximumSize(QSize(50, 50))
        self.yicon.setPixmap(QPixmap(u"tracks.png"))
        self.yicon.setScaledContents(True)
        self.yicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.yicon, 13, 1, 1, 1)

        self.pushn = QPushButton(self.verticalLayoutWidget_2)
        self.pushn.setObjectName(u"pushn")
        self.pushn.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_4.addWidget(self.pushn, 2, 0, 1, 1)

        self.ticon = QLabel(self.verticalLayoutWidget_2)
        self.ticon.setObjectName(u"ticon")
        self.ticon.setMaximumSize(QSize(50, 50))
        self.ticon.setPixmap(QPixmap(u"tracks.png"))
        self.ticon.setScaledContents(True)
        self.ticon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.ticon, 8, 1, 1, 1)

        self.aaicon = QLabel(self.verticalLayoutWidget_2)
        self.aaicon.setObjectName(u"aaicon")
        self.aaicon.setMaximumSize(QSize(50, 50))
        self.aaicon.setPixmap(QPixmap(u"tracks.png"))
        self.aaicon.setScaledContents(True)
        self.aaicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.aaicon, 15, 1, 1, 1)

        self.pushr = QPushButton(self.verticalLayoutWidget_2)
        self.pushr.setObjectName(u"pushr")

        self.gridLayout_4.addWidget(self.pushr, 6, 0, 1, 1)

        self.vicon = QLabel(self.verticalLayoutWidget_2)
        self.vicon.setObjectName(u"vicon")
        self.vicon.setMaximumSize(QSize(50, 50))
        self.vicon.setPixmap(QPixmap(u"tracks.png"))
        self.vicon.setScaledContents(True)
        self.vicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.vicon, 10, 1, 1, 1)

        self.pushdd = QPushButton(self.verticalLayoutWidget_2)
        self.pushdd.setObjectName(u"pushdd")

        self.gridLayout_4.addWidget(self.pushdd, 18, 0, 1, 1)

        self.bbicon = QLabel(self.verticalLayoutWidget_2)
        self.bbicon.setObjectName(u"bbicon")
        self.bbicon.setMaximumSize(QSize(50, 50))
        self.bbicon.setPixmap(QPixmap(u"tracks.png"))
        self.bbicon.setScaledContents(True)
        self.bbicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.bbicon, 16, 1, 1, 1)

        self.ccicon = QLabel(self.verticalLayoutWidget_2)
        self.ccicon.setObjectName(u"ccicon")
        self.ccicon.setMaximumSize(QSize(50, 50))
        self.ccicon.setPixmap(QPixmap(u"tracks.png"))
        self.ccicon.setScaledContents(True)
        self.ccicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.ccicon, 17, 1, 1, 1)

        self.ddicon = QLabel(self.verticalLayoutWidget_2)
        self.ddicon.setObjectName(u"ddicon")
        self.ddicon.setMaximumSize(QSize(50, 50))
        self.ddicon.setPixmap(QPixmap(u"tracks.png"))
        self.ddicon.setScaledContents(True)
        self.ddicon.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.ddicon, 18, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.line_7 = QFrame(self.verticalLayoutWidget_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMaximumSize(QSize(16777215, 600))
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_6.addWidget(self.line_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 700 13pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.label_5)

        self.linelabel = QLabel(self.verticalLayoutWidget_2)
        self.linelabel.setObjectName(u"linelabel")
        self.linelabel.setStyleSheet(u"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.linelabel)

        self.sectionrangelabel = QLabel(self.verticalLayoutWidget_2)
        self.sectionrangelabel.setObjectName(u"sectionrangelabel")
        self.sectionrangelabel.setStyleSheet(u"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.sectionrangelabel)

        self.line_4 = QFrame(self.verticalLayoutWidget_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line = QFrame(self.verticalLayoutWidget_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.time = QLabel(self.verticalLayoutWidget_2)
        self.time.setObjectName(u"time")
        self.time.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.time.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.time)

        self.line_6 = QFrame(self.verticalLayoutWidget_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.line_2 = QFrame(self.verticalLayoutWidget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_19 = QLabel(self.verticalLayoutWidget_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_19)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_16 = QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_16)

        self.gate10 = QPushButton(self.verticalLayoutWidget_2)
        self.gate10.setObjectName(u"gate10")
        self.gate10.setCheckable(False)

        self.horizontalLayout_12.addWidget(self.gate10)

        self.gate11 = QPushButton(self.verticalLayoutWidget_2)
        self.gate11.setObjectName(u"gate11")

        self.horizontalLayout_12.addWidget(self.gate11)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_17 = QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_17)

        self.gate20 = QPushButton(self.verticalLayoutWidget_2)
        self.gate20.setObjectName(u"gate20")
        self.gate20.setCheckable(False)

        self.horizontalLayout_7.addWidget(self.gate20)

        self.gate21 = QPushButton(self.verticalLayoutWidget_2)
        self.gate21.setObjectName(u"gate21")

        self.horizontalLayout_7.addWidget(self.gate21)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_20 = QLabel(self.verticalLayoutWidget_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_20)

        self.gate30 = QPushButton(self.verticalLayoutWidget_2)
        self.gate30.setObjectName(u"gate30")
        self.gate30.setCheckable(False)

        self.horizontalLayout_8.addWidget(self.gate30)

        self.gate31 = QPushButton(self.verticalLayoutWidget_2)
        self.gate31.setObjectName(u"gate31")

        self.horizontalLayout_8.addWidget(self.gate31)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_21 = QLabel(self.verticalLayoutWidget_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_21)

        self.gate40 = QPushButton(self.verticalLayoutWidget_2)
        self.gate40.setObjectName(u"gate40")
        self.gate40.setCheckable(False)

        self.horizontalLayout_9.addWidget(self.gate40)

        self.gate41 = QPushButton(self.verticalLayoutWidget_2)
        self.gate41.setObjectName(u"gate41")

        self.horizontalLayout_9.addWidget(self.gate41)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_22 = QLabel(self.verticalLayoutWidget_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_22)

        self.gate50 = QPushButton(self.verticalLayoutWidget_2)
        self.gate50.setObjectName(u"gate50")
        self.gate50.setCheckable(False)

        self.horizontalLayout_10.addWidget(self.gate50)

        self.gate51 = QPushButton(self.verticalLayoutWidget_2)
        self.gate51.setObjectName(u"gate51")

        self.horizontalLayout_10.addWidget(self.gate51)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_23 = QLabel(self.verticalLayoutWidget_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_23)

        self.gate60 = QPushButton(self.verticalLayoutWidget_2)
        self.gate60.setObjectName(u"gate60")
        self.gate60.setCheckable(False)

        self.horizontalLayout_13.addWidget(self.gate60)

        self.gate61 = QPushButton(self.verticalLayoutWidget_2)
        self.gate61.setObjectName(u"gate61")

        self.horizontalLayout_13.addWidget(self.gate61)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_50 = QLabel(self.verticalLayoutWidget_2)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"background-color: rgb(221, 221, 221);\n"
"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_50)

        self.label_51 = QLabel(self.verticalLayoutWidget_2)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_51)

        self.label_52 = QLabel(self.verticalLayoutWidget_2)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(16777215, 48))
        self.label_52.setStyleSheet(u"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_52)


        self.verticalLayout_9.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_53 = QLabel(self.verticalLayoutWidget_2)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_53)

        self.gatepositiona = QLabel(self.verticalLayoutWidget_2)
        self.gatepositiona.setObjectName(u"gatepositiona")
        self.gatepositiona.setStyleSheet(u"font: 9pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.gatepositiona.setFrameShadow(QFrame.Plain)
        self.gatepositiona.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.gatepositiona)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.reda = QLabel(self.verticalLayoutWidget_2)
        self.reda.setObjectName(u"reda")
        self.reda.setMaximumSize(QSize(21, 21))
        self.reda.setPixmap(QPixmap(u"greenlight.png"))
        self.reda.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.reda)

        self.yellowa = QLabel(self.verticalLayoutWidget_2)
        self.yellowa.setObjectName(u"yellowa")
        self.yellowa.setMaximumSize(QSize(21, 21))
        self.yellowa.setPixmap(QPixmap(u"offlight.png"))
        self.yellowa.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.yellowa)

        self.greena = QLabel(self.verticalLayoutWidget_2)
        self.greena.setObjectName(u"greena")
        self.greena.setMaximumSize(QSize(21, 21))
        self.greena.setPixmap(QPixmap(u"offlight.png"))
        self.greena.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.greena)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_27)


        self.verticalLayout_9.addLayout(self.horizontalLayout_20)

        self.line_5 = QFrame(self.verticalLayoutWidget_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_5)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.activetrainlabel = QLabel(self.verticalLayoutWidget_2)
        self.activetrainlabel.setObjectName(u"activetrainlabel")
        self.activetrainlabel.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.activetrainlabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.activetrainlabel)

        self.activetrains = QLCDNumber(self.verticalLayoutWidget_2)
        self.activetrains.setObjectName(u"activetrains")

        self.horizontalLayout_16.addWidget(self.activetrains)


        self.verticalLayout_9.addLayout(self.horizontalLayout_16)


        self.verticalLayout_3.addLayout(self.verticalLayout_9)

        self.line_8 = QFrame(self.verticalLayoutWidget_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.automaticmode = QRadioButton(self.verticalLayoutWidget_2)
        self.automaticmode.setObjectName(u"automaticmode")
        self.automaticmode.setMaximumSize(QSize(16777215, 26))
        self.automaticmode.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.automaticmode)

        self.maintenancemode = QRadioButton(self.verticalLayoutWidget_2)
        self.maintenancemode.setObjectName(u"maintenancemode")
        self.maintenancemode.setStyleSheet(u"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.maintenancemode)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.line_3 = QFrame(self.verticalLayoutWidget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.trackconfiguration = QPushButton(self.verticalLayoutWidget_2)
        self.trackconfiguration.setObjectName(u"trackconfiguration")
        self.trackconfiguration.setStyleSheet(u"font: 9pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.trackconfiguration)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        MainWindowA.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindowA)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 740, 25))
        MainWindowA.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindowA)
        self.statusbar.setObjectName(u"statusbar")
        MainWindowA.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowA)

        QMetaObject.connectSlotsByName(MainWindowA)
    # setupUi

    def retranslateUi(self, MainWindowA):
        MainWindowA.setWindowTitle(QCoreApplication.translate("MainWindowA", u"Wayside", None))
        self.whichwayside.setItemText(0, QCoreApplication.translate("MainWindowA", u"Wayside 1", None))
        self.whichwayside.setItemText(1, QCoreApplication.translate("MainWindowA", u"Wayside 2", None))
        self.whichwayside.setItemText(2, QCoreApplication.translate("MainWindowA", u"Wayside 3", None))
        self.whichwayside.setItemText(3, QCoreApplication.translate("MainWindowA", u"Waysdie 4", None))

        self.whichwayside.setPlaceholderText(QCoreApplication.translate("MainWindowA", u"Select Wayside", None))
        self.qicon.setText("")
        self.pushu.setText(QCoreApplication.translate("MainWindowA", u"U", None))
        self.picon.setText("")
        self.pushq.setText(QCoreApplication.translate("MainWindowA", u"Q", None))
        self.pushp.setText(QCoreApplication.translate("MainWindowA", u"P", None))
        self.pushx.setText(QCoreApplication.translate("MainWindowA", u"X", None))
        self.pusht.setText(QCoreApplication.translate("MainWindowA", u"T", None))
        self.oicon.setText("")
        self.pushaa.setText(QCoreApplication.translate("MainWindowA", u"AA", None))
        self.nicon.setText("")
        self.zicon.setText("")
        self.pushbb.setText(QCoreApplication.translate("MainWindowA", u"BB", None))
        self.pushz.setText(QCoreApplication.translate("MainWindowA", u"Z", None))
        self.ricon.setText("")
        self.pushcc.setText(QCoreApplication.translate("MainWindowA", u"CC", None))
        self.pushs.setText(QCoreApplication.translate("MainWindowA", u"S", None))
        self.pushy.setText(QCoreApplication.translate("MainWindowA", u"Y", None))
        self.uicon.setText("")
        self.occupancylabel_2.setText(QCoreApplication.translate("MainWindowA", u"Occupancy", None))
        self.pusho.setText(QCoreApplication.translate("MainWindowA", u"O", None))
        self.wicon.setText("")
        self.sectiontitle_2.setText(QCoreApplication.translate("MainWindowA", u"Section", None))
        self.pushv.setText(QCoreApplication.translate("MainWindowA", u"V", None))
        self.pushw.setText(QCoreApplication.translate("MainWindowA", u"W", None))
        self.sicon.setText("")
        self.xicon.setText("")
        self.yicon.setText("")
        self.pushn.setText(QCoreApplication.translate("MainWindowA", u"N", None))
        self.ticon.setText("")
        self.aaicon.setText("")
        self.pushr.setText(QCoreApplication.translate("MainWindowA", u"R", None))
        self.vicon.setText("")
        self.pushdd.setText(QCoreApplication.translate("MainWindowA", u"DD", None))
        self.bbicon.setText("")
        self.ccicon.setText("")
        self.ddicon.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindowA", u"Sections Managed:", None))
        self.linelabel.setText(QCoreApplication.translate("MainWindowA", u"Green Line", None))
        self.sectionrangelabel.setText(QCoreApplication.translate("MainWindowA", u"N - Z", None))
        self.time.setText(QCoreApplication.translate("MainWindowA", u"11:44 PM", None))
        self.label_19.setText(QCoreApplication.translate("MainWindowA", u"Switches", None))
        self.label_16.setText(QCoreApplication.translate("MainWindowA", u"1", None))
        self.gate10.setText(QCoreApplication.translate("MainWindowA", u"12-13", None))
        self.gate11.setText(QCoreApplication.translate("MainWindowA", u"1-13", None))
        self.label_17.setText(QCoreApplication.translate("MainWindowA", u"2", None))
        self.gate20.setText(QCoreApplication.translate("MainWindowA", u"29-30", None))
        self.gate21.setText(QCoreApplication.translate("MainWindowA", u"29-150", None))
        self.label_20.setText(QCoreApplication.translate("MainWindowA", u"3", None))
        self.gate30.setText(QCoreApplication.translate("MainWindowA", u"57 - yard", None))
        self.gate31.setText(QCoreApplication.translate("MainWindowA", u"57 - 58", None))
        self.label_21.setText(QCoreApplication.translate("MainWindowA", u"4", None))
        self.gate40.setText(QCoreApplication.translate("MainWindowA", u"63 - yard", None))
        self.gate41.setText(QCoreApplication.translate("MainWindowA", u"63 - 62", None))
        self.label_22.setText(QCoreApplication.translate("MainWindowA", u"5", None))
        self.gate50.setText(QCoreApplication.translate("MainWindowA", u"77 - 76", None))
        self.gate51.setText(QCoreApplication.translate("MainWindowA", u"77 - 101", None))
        self.label_23.setText(QCoreApplication.translate("MainWindowA", u"6", None))
        self.gate60.setText(QCoreApplication.translate("MainWindowA", u"85 - 86", None))
        self.gate61.setText(QCoreApplication.translate("MainWindowA", u"85 - 100", None))
        self.label_50.setText(QCoreApplication.translate("MainWindowA", u"Crossing", None))
        self.label_51.setText(QCoreApplication.translate("MainWindowA", u"Position", None))
        self.label_52.setText(QCoreApplication.translate("MainWindowA", u"Lights", None))
        self.label_53.setText(QCoreApplication.translate("MainWindowA", u"1", None))
        self.gatepositiona.setText(QCoreApplication.translate("MainWindowA", u"Active", None))
        self.reda.setText("")
        self.yellowa.setText("")
        self.greena.setText("")
        self.activetrainlabel.setText(QCoreApplication.translate("MainWindowA", u"Active Trains  ", None))
        self.automaticmode.setText(QCoreApplication.translate("MainWindowA", u"Automatic Mode", None))
        self.maintenancemode.setText(QCoreApplication.translate("MainWindowA", u"Maintenance Mode", None))
        self.trackconfiguration.setText(QCoreApplication.translate("MainWindowA", u"Upload PLC", None))
    # retranslateUi

