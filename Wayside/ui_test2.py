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
        testpopup.resize(564, 291)
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
        self.sectionbox.setGeometry(QRect(70, 200, 82, 28))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 375, 80))
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

        self.blockbox = QComboBox(self.centralwidget)
        self.blockbox.setObjectName(u"blockbox")
        self.blockbox.setGeometry(QRect(190, 200, 82, 28))
        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 100, 375, 80))
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

        self.occupancybox = QComboBox(self.centralwidget)
        self.occupancybox.addItem("")
        self.occupancybox.addItem("")
        self.occupancybox.setObjectName(u"occupancybox")
        self.occupancybox.setGeometry(QRect(301, 200, 111, 28))
        testpopup.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(testpopup)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 564, 25))
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

        self.reda.setText(QCoreApplication.translate("testpopup", u"reda", None))
        self.yellowa.setText(QCoreApplication.translate("testpopup", u"yellowa", None))
        self.greena.setText(QCoreApplication.translate("testpopup", u"greena", None))
        self.redb.setText(QCoreApplication.translate("testpopup", u"redb", None))
        self.yellowb.setText(QCoreApplication.translate("testpopup", u"yellowb", None))
        self.greenb.setText(QCoreApplication.translate("testpopup", u"greenb", None))
        self.occupancybox.setItemText(0, QCoreApplication.translate("testpopup", u"Occupied", None))
        self.occupancybox.setItemText(1, QCoreApplication.translate("testpopup", u"Unoccupied", None))

    # retranslateUi

