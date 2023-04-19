# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trainModPopUp.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(309, 272)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.trainLength = QLabel(self.centralwidget)
        self.trainLength.setObjectName(u"trainLength")
        self.trainLength.setGeometry(QRect(20, 20, 291, 31))
        self.trainLength.setStyleSheet(u"")
        self.trainWidth = QLabel(self.centralwidget)
        self.trainWidth.setObjectName(u"trainWidth")
        self.trainWidth.setGeometry(QRect(20, 60, 291, 31))
        self.passengers = QLabel(self.centralwidget)
        self.passengers.setObjectName(u"passengers")
        self.passengers.setGeometry(QRect(20, 140, 91, 31))
        self.currentMass = QLabel(self.centralwidget)
        self.currentMass.setObjectName(u"currentMass")
        self.currentMass.setGeometry(QRect(20, 180, 111, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 110, 201, 21))
        self.numPass = QLabel(self.centralwidget)
        self.numPass.setObjectName(u"numPass")
        self.numPass.setGeometry(QRect(130, 150, 63, 20))
        self.currMass = QLabel(self.centralwidget)
        self.currMass.setObjectName(u"currMass")
        self.currMass.setGeometry(QRect(130, 190, 63, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 309, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.trainLength.setText(QCoreApplication.translate("MainWindow", u"Train Length:        32.3 m", None))
        self.trainWidth.setText(QCoreApplication.translate("MainWindow", u"Train Width:         2.65 m", None))
        self.passengers.setText(QCoreApplication.translate("MainWindow", u"Passengers:", None))
        self.currentMass.setText(QCoreApplication.translate("MainWindow", u"Current Mass: ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Train Height:       3.42 m", None))
        self.numPass.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.currMass.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

