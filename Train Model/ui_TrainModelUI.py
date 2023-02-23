# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TrainModelUI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(817, 507)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.speedIcon = QPushButton(self.centralwidget)
        self.speedIcon.setObjectName(u"speedIcon")
        self.speedIcon.setGeometry(QRect(600, 190, 111, 91))
        self.speedIcon.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(590, 20, 191, 31))
        self.label_14.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.EmerButton = QPushButton(self.centralwidget)
        self.EmerButton.setObjectName(u"EmerButton")
        self.EmerButton.setGeometry(QRect(280, 409, 231, 31))
        self.EmerButton.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.tempLabel_3 = QLabel(self.centralwidget)
        self.tempLabel_3.setObjectName(u"tempLabel_3")
        self.tempLabel_3.setGeometry(QRect(280, 380, 231, 21))
        self.tempLabel_3.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 11pt \"Segoe UI\";")
        self.headlightLabel = QLabel(self.centralwidget)
        self.headlightLabel.setObjectName(u"headlightLabel")
        self.headlightLabel.setGeometry(QRect(190, 170, 37, 12))
        self.ACIcon = QPushButton(self.centralwidget)
        self.ACIcon.setObjectName(u"ACIcon")
        self.ACIcon.setGeometry(QRect(170, 290, 61, 61))
        self.ACIcon.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(550, 330, 221, 31))
        self.label_18.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(30, 10, 131, 31))
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(550, 70, 231, 81))
        self.label_17.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 80, 111, 191))
        self.tempLabel_2 = QLabel(self.centralwidget)
        self.tempLabel_2.setObjectName(u"tempLabel_2")
        self.tempLabel_2.setGeometry(QRect(280, 360, 231, 21))
        self.tempLabel_2.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 11pt \"Segoe UI\";")
        self.powLabel = QLabel(self.centralwidget)
        self.powLabel.setObjectName(u"powLabel")
        self.powLabel.setGeometry(QRect(550, 410, 231, 31))
        self.powLabel.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.sigFaultLabel = QPushButton(self.centralwidget)
        self.sigFaultLabel.setObjectName(u"sigFaultLabel")
        self.sigFaultLabel.setGeometry(QRect(20, 380, 71, 61))
        self.sigFaultLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.trainBox = QComboBox(self.centralwidget)
        self.trainBox.setObjectName(u"trainBox")
        self.trainBox.setGeometry(QRect(30, 45, 191, 31))
        self.powProgressBar = QProgressBar(self.centralwidget)
        self.powProgressBar.setObjectName(u"powProgressBar")
        self.powProgressBar.setGeometry(QRect(550, 390, 231, 23))
        self.powProgressBar.setStyleSheet(u"")
        self.powProgressBar.setValue(24)
        self.actSpeed = QLabel(self.centralwidget)
        self.actSpeed.setObjectName(u"actSpeed")
        self.actSpeed.setGeometry(QRect(550, 300, 221, 31))
        self.actSpeed.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.lDoorLabel = QLabel(self.centralwidget)
        self.lDoorLabel.setObjectName(u"lDoorLabel")
        self.lDoorLabel.setGeometry(QRect(190, 200, 37, 12))
        self.ACprogressBar = QProgressBar(self.centralwidget)
        self.ACprogressBar.setObjectName(u"ACprogressBar")
        self.ACprogressBar.setGeometry(QRect(20, 300, 151, 23))
        self.ACprogressBar.setValue(24)
        self.brakeFaultLabel = QPushButton(self.centralwidget)
        self.brakeFaultLabel.setObjectName(u"brakeFaultLabel")
        self.brakeFaultLabel.setGeometry(QRect(160, 380, 71, 61))
        self.brakeFaultLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.powFaultLabel = QPushButton(self.centralwidget)
        self.powFaultLabel.setObjectName(u"powFaultLabel")
        self.powFaultLabel.setGeometry(QRect(90, 380, 71, 61))
        self.powFaultLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tempLabel = QLabel(self.centralwidget)
        self.tempLabel.setObjectName(u"tempLabel")
        self.tempLabel.setGeometry(QRect(20, 320, 141, 21))
        self.tempLabel.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 11pt \"Segoe UI\";")
        self.intLightLabel = QLabel(self.centralwidget)
        self.intLightLabel.setObjectName(u"intLightLabel")
        self.intLightLabel.setGeometry(QRect(190, 110, 37, 12))
        self.extLightLabel = QLabel(self.centralwidget)
        self.extLightLabel.setObjectName(u"extLightLabel")
        self.extLightLabel.setGeometry(QRect(190, 140, 37, 12))
        self.commSpeedLabel = QLabel(self.centralwidget)
        self.commSpeedLabel.setObjectName(u"commSpeedLabel")
        self.commSpeedLabel.setGeometry(QRect(550, 150, 231, 31))
        self.commSpeedLabel.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.rDoorLabel = QLabel(self.centralwidget)
        self.rDoorLabel.setObjectName(u"rDoorLabel")
        self.rDoorLabel.setGeometry(QRect(190, 230, 37, 12))
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 360, 121, 21))
        self.label_12.setStyleSheet(u"font: 15pt \"Segoe UI\";")
        self.trainMapLabel = QPushButton(self.centralwidget)
        self.trainMapLabel.setObjectName(u"trainMapLabel")
        self.trainMapLabel.setGeometry(QRect(260, 50, 271, 301))
        self.trainMapLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.redLineButton = QPushButton(self.centralwidget)
        self.redLineButton.setObjectName(u"redLineButton")
        self.redLineButton.setGeometry(QRect(270, 10, 121, 29))
        self.greenLineButton = QPushButton(self.centralwidget)
        self.greenLineButton.setObjectName(u"greenLineButton")
        self.greenLineButton.setGeometry(QRect(400, 10, 121, 29))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 817, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.speedIcon.setText("")
        self.label_14.setText("")
        self.EmerButton.setText(QCoreApplication.translate("MainWindow", u"EMERGENCY BRAKE", None))
        self.tempLabel_3.setText(QCoreApplication.translate("MainWindow", u"Current Block:", None))
        self.headlightLabel.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.ACIcon.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Speed Limit:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Current Train:</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Next Station:</p><p>Scheduled Arrival:</p><p>Estimated Arrival:</p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Internal Lights:</span></p><p><span style=\" font-size:12pt;\">External Lights:</span></p><p><span style=\" font-size:12pt;\">Headlights:</span></p><p><span style=\" font-size:12pt;\">Left Doors:</span></p><p><span style=\" font-size:12pt;\">Right Doors:</span></p></body></html>", None))
        self.tempLabel_2.setText(QCoreApplication.translate("MainWindow", u"Current Section:", None))
        self.powLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Power Input:</span></p></body></html>", None))
        self.sigFaultLabel.setText("")
        self.actSpeed.setText(QCoreApplication.translate("MainWindow", u"Actual Speed:", None))
        self.lDoorLabel.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.brakeFaultLabel.setText("")
        self.powFaultLabel.setText("")
        self.tempLabel.setText(QCoreApplication.translate("MainWindow", u"Internal Temp:", None))
        self.intLightLabel.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.extLightLabel.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.commSpeedLabel.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed:", None))
        self.rDoorLabel.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Fault Status", None))
        self.trainMapLabel.setText("")
        self.redLineButton.setText(QCoreApplication.translate("MainWindow", u"RED LINE", None))
        self.greenLineButton.setText(QCoreApplication.translate("MainWindow", u"GREEN LINE", None))
    # retranslateUi

