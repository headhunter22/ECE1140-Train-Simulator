# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test2.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QMainWindow,
    QMenuBar, QRadioButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_testpopup(object):
    def setupUi(self, testpopup):
        if not testpopup.objectName():
            testpopup.setObjectName(u"testpopup")
        testpopup.resize(402, 316)
        self.centralwidget = QWidget(testpopup)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sectionbox = QComboBox(self.centralwidget)
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
        self.sectionbox.setGeometry(QRect(19, 220, 82, 28))
        self.blockbox = QComboBox(self.centralwidget)
        self.blockbox.setObjectName(u"blockbox")
        self.blockbox.setGeometry(QRect(139, 220, 82, 28))
        self.occupancybox = QComboBox(self.centralwidget)
        self.occupancybox.addItem("")
        self.occupancybox.addItem("")
        self.occupancybox.setObjectName(u"occupancybox")
        self.occupancybox.setGeometry(QRect(250, 220, 111, 28))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 10, 359, 46))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.reda = QRadioButton(self.horizontalLayoutWidget)
        self.reda.setObjectName(u"reda")

        self.horizontalLayout.addWidget(self.reda)

        self.yellowa = QRadioButton(self.horizontalLayoutWidget)
        self.yellowa.setObjectName(u"yellowa")

        self.horizontalLayout.addWidget(self.yellowa)

        self.greena = QRadioButton(self.horizontalLayoutWidget)
        self.greena.setObjectName(u"greena")

        self.horizontalLayout.addWidget(self.greena)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(20, 60, 361, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.redb = QRadioButton(self.horizontalLayoutWidget_3)
        self.redb.setObjectName(u"redb")

        self.horizontalLayout_3.addWidget(self.redb)

        self.yellowb = QRadioButton(self.horizontalLayoutWidget_3)
        self.yellowb.setObjectName(u"yellowb")

        self.horizontalLayout_3.addWidget(self.yellowb)

        self.greenb = QRadioButton(self.horizontalLayoutWidget_3)
        self.greenb.setObjectName(u"greenb")

        self.horizontalLayout_3.addWidget(self.greenb)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 110, 361, 36))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.autoC0 = QRadioButton(self.horizontalLayoutWidget_2)
        self.autoC0.setObjectName(u"autoC0")

        self.horizontalLayout_2.addWidget(self.autoC0)

        self.autoC1 = QRadioButton(self.horizontalLayoutWidget_2)
        self.autoC1.setObjectName(u"autoC1")

        self.horizontalLayout_2.addWidget(self.autoC1)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(20, 160, 361, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.autoG0 = QRadioButton(self.horizontalLayoutWidget_4)
        self.autoG0.setObjectName(u"autoG0")

        self.horizontalLayout_4.addWidget(self.autoG0)

        self.autoG1 = QRadioButton(self.horizontalLayoutWidget_4)
        self.autoG1.setObjectName(u"autoG1")

        self.horizontalLayout_4.addWidget(self.autoG1)

        testpopup.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(testpopup)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 402, 25))
        testpopup.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(testpopup)
        self.statusbar.setObjectName(u"statusbar")
        testpopup.setStatusBar(self.statusbar)

        self.retranslateUi(testpopup)

        QMetaObject.connectSlotsByName(testpopup)
    # setupUi

    def retranslateUi(self, testpopup):
        testpopup.setWindowTitle(QCoreApplication.translate("testpopup", u"MainWindow", None))
        self.sectionbox.setItemText(0, QCoreApplication.translate("testpopup", u"A", None))
        self.sectionbox.setItemText(1, QCoreApplication.translate("testpopup", u"B", None))
        self.sectionbox.setItemText(2, QCoreApplication.translate("testpopup", u"C", None))
        self.sectionbox.setItemText(3, QCoreApplication.translate("testpopup", u"D", None))
        self.sectionbox.setItemText(4, QCoreApplication.translate("testpopup", u"E", None))
        self.sectionbox.setItemText(5, QCoreApplication.translate("testpopup", u"F", None))
        self.sectionbox.setItemText(6, QCoreApplication.translate("testpopup", u"G", None))
        self.sectionbox.setItemText(7, QCoreApplication.translate("testpopup", u"H", None))
        self.sectionbox.setItemText(8, QCoreApplication.translate("testpopup", u"I", None))
        self.sectionbox.setItemText(9, QCoreApplication.translate("testpopup", u"J", None))

        self.sectionbox.setPlaceholderText(QCoreApplication.translate("testpopup", u"Section", None))
        self.blockbox.setPlaceholderText(QCoreApplication.translate("testpopup", u"Block", None))
        self.occupancybox.setItemText(0, QCoreApplication.translate("testpopup", u"Occupied", None))
        self.occupancybox.setItemText(1, QCoreApplication.translate("testpopup", u"Unoccupied", None))

        self.occupancybox.setPlaceholderText(QCoreApplication.translate("testpopup", u"Occupation", None))
        self.reda.setText(QCoreApplication.translate("testpopup", u"reda", None))
        self.yellowa.setText(QCoreApplication.translate("testpopup", u"yellowa", None))
        self.greena.setText(QCoreApplication.translate("testpopup", u"greena", None))
        self.redb.setText(QCoreApplication.translate("testpopup", u"redb", None))
        self.yellowb.setText(QCoreApplication.translate("testpopup", u"yellowb", None))
        self.greenb.setText(QCoreApplication.translate("testpopup", u"greenb", None))
        self.autoC0.setText(QCoreApplication.translate("testpopup", u"c0", None))
        self.autoC1.setText(QCoreApplication.translate("testpopup", u"c1", None))
        self.autoG0.setText(QCoreApplication.translate("testpopup", u"g0", None))
        self.autoG1.setText(QCoreApplication.translate("testpopup", u"g1", None))
    # retranslateUi

