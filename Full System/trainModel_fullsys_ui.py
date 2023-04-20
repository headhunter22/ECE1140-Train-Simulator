# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trainModel_fullsys.ui'
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
    QSlider, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 527)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.trainBox = QComboBox(self.centralwidget)
        self.trainBox.setObjectName(u"trainBox")
        self.trainBox.setGeometry(QRect(20, 65, 191, 31))
        self.powProgressBar = QProgressBar(self.centralwidget)
        self.powProgressBar.setObjectName(u"powProgressBar")
        self.powProgressBar.setGeometry(QRect(260, 290, 251, 23))
        self.powProgressBar.setStyleSheet(u"QProgressBar {\n"
"     border: 2px solid black;\n"
"     border-radius: 5px;\n"
"     background-color: white;\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: yellow;\n"
"     width: 20px;\n"
" }")
        self.powProgressBar.setValue(24)
        self.ACprogressBar = QProgressBar(self.centralwidget)
        self.ACprogressBar.setObjectName(u"ACprogressBar")
        self.ACprogressBar.setGeometry(QRect(10, 320, 161, 21))
        self.ACprogressBar.setStyleSheet(u"QProgressBar {\n"
"     border: 2px solid black;\n"
"     border-radius: 5px;\n"
"     background-color: white;\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: blue;\n"
"     width: 20px;\n"
" }")
        self.ACprogressBar.setValue(24)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 380, 121, 21))
        self.label_12.setStyleSheet(u"font: 15pt \"Segoe UI\";")
        self.errorLabel = QLabel(self.centralwidget)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(130, 290, 31, 31))
        self.actSpeed = QLabel(self.centralwidget)
        self.actSpeed.setObjectName(u"actSpeed")
        self.actSpeed.setGeometry(QRect(260, 100, 251, 71))
        self.actSpeed.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 30, 131, 31))
        self.powLabel = QLabel(self.centralwidget)
        self.powLabel.setObjectName(u"powLabel")
        self.powLabel.setGeometry(QRect(260, 310, 251, 41))
        self.powLabel.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.lDoorLabel = QLabel(self.centralwidget)
        self.lDoorLabel.setObjectName(u"lDoorLabel")
        self.lDoorLabel.setGeometry(QRect(166, 210, 51, 20))
        self.sigFaultLabel = QPushButton(self.centralwidget)
        self.sigFaultLabel.setObjectName(u"sigFaultLabel")
        self.sigFaultLabel.setGeometry(QRect(10, 400, 71, 61))
        self.sigFaultLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.EmerButton = QPushButton(self.centralwidget)
        self.EmerButton.setObjectName(u"EmerButton")
        self.EmerButton.setGeometry(QRect(540, 220, 241, 171))
        self.EmerButton.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 100, 111, 191))
        self.tempText = QLabel(self.centralwidget)
        self.tempText.setObjectName(u"tempText")
        self.tempText.setGeometry(QRect(10, 300, 161, 20))
        self.commSpeedLabel = QLabel(self.centralwidget)
        self.commSpeedLabel.setObjectName(u"commSpeedLabel")
        self.commSpeedLabel.setGeometry(QRect(260, 170, 251, 31))
        self.commSpeedLabel.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.ACIcon = QPushButton(self.centralwidget)
        self.ACIcon.setObjectName(u"ACIcon")
        self.ACIcon.setGeometry(QRect(190, 310, 51, 51))
        self.ACIcon.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.headlightLabel = QLabel(self.centralwidget)
        self.headlightLabel.setObjectName(u"headlightLabel")
        self.headlightLabel.setGeometry(QRect(166, 170, 51, 20))
        self.brakeFaultLabel = QPushButton(self.centralwidget)
        self.brakeFaultLabel.setObjectName(u"brakeFaultLabel")
        self.brakeFaultLabel.setGeometry(QRect(150, 400, 71, 61))
        self.brakeFaultLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.rDoorLabel = QLabel(self.centralwidget)
        self.rDoorLabel.setObjectName(u"rDoorLabel")
        self.rDoorLabel.setGeometry(QRect(166, 250, 51, 20))
        self.powFaultLabel = QPushButton(self.centralwidget)
        self.powFaultLabel.setObjectName(u"powFaultLabel")
        self.powFaultLabel.setGeometry(QRect(80, 400, 71, 61))
        self.powFaultLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tempLabel_2 = QLabel(self.centralwidget)
        self.tempLabel_2.setObjectName(u"tempLabel_2")
        self.tempLabel_2.setGeometry(QRect(260, 380, 251, 41))
        self.tempLabel_2.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 11pt \"Segoe UI\";")
        self.speedLimitLabel = QLabel(self.centralwidget)
        self.speedLimitLabel.setObjectName(u"speedLimitLabel")
        self.speedLimitLabel.setGeometry(QRect(260, 200, 251, 31))
        self.speedLimitLabel.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setGeometry(QRect(580, 40, 191, 31))
        self.dateLabel.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.intLightLabel = QLabel(self.centralwidget)
        self.intLightLabel.setObjectName(u"intLightLabel")
        self.intLightLabel.setGeometry(QRect(166, 130, 51, 20))
        self.greenLineButton = QPushButton(self.centralwidget)
        self.greenLineButton.setObjectName(u"greenLineButton")
        self.greenLineButton.setGeometry(QRect(390, 40, 121, 51))
        self.greenLineButton.setStyleSheet(u"")
        self.redLineButton = QPushButton(self.centralwidget)
        self.redLineButton.setObjectName(u"redLineButton")
        self.redLineButton.setGeometry(QRect(260, 40, 121, 51))
        self.destLabel = QLabel(self.centralwidget)
        self.destLabel.setObjectName(u"destLabel")
        self.destLabel.setGeometry(QRect(540, 90, 231, 101))
        self.destLabel.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.currBlockLabel = QLabel(self.centralwidget)
        self.currBlockLabel.setObjectName(u"currBlockLabel")
        self.currBlockLabel.setGeometry(QRect(260, 420, 251, 41))
        self.currBlockLabel.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 11pt \"Segoe UI\";")
        self.popUpUI = QPushButton(self.centralwidget)
        self.popUpUI.setObjectName(u"popUpUI")
        self.popUpUI.setGeometry(QRect(540, 410, 241, 41))
        self.trainAcc = QLabel(self.centralwidget)
        self.trainAcc.setObjectName(u"trainAcc")
        self.trainAcc.setGeometry(QRect(260, 230, 251, 31))
        self.trainAcc.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.tempSlider = QSlider(self.centralwidget)
        self.tempSlider.setObjectName(u"tempSlider")
        self.tempSlider.setGeometry(QRect(10, 350, 160, 18))
        self.tempSlider.setOrientation(Qt.Horizontal)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Fault Status", None))
        self.errorLabel.setText("")
        self.actSpeed.setText(QCoreApplication.translate("MainWindow", u"Current Speed:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Current Train:</span></p></body></html>", None))
        self.powLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Power Input:</span></p></body></html>", None))
        self.lDoorLabel.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.sigFaultLabel.setText("")
        self.EmerButton.setText(QCoreApplication.translate("MainWindow", u"EMERGENCY BRAKE", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Internal Lights:</span></p><p><span style=\" font-size:12pt;\">Headlights:</span></p><p><span style=\" font-size:12pt;\">Left Doors:</span></p><p><span style=\" font-size:12pt;\">Right Doors:</span></p></body></html>", None))
        self.tempText.setText(QCoreApplication.translate("MainWindow", u"Current Temp: ", None))
        self.commSpeedLabel.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed:", None))
        self.ACIcon.setText("")
        self.headlightLabel.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.brakeFaultLabel.setText("")
        self.rDoorLabel.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.powFaultLabel.setText("")
        self.tempLabel_2.setText(QCoreApplication.translate("MainWindow", u"Current Section:", None))
        self.speedLimitLabel.setText(QCoreApplication.translate("MainWindow", u"Speed Limit:", None))
        self.dateLabel.setText("")
        self.intLightLabel.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.greenLineButton.setText(QCoreApplication.translate("MainWindow", u"GREEN LINE", None))
        self.redLineButton.setText(QCoreApplication.translate("MainWindow", u"RED LINE", None))
        self.destLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Destination:</p><p><br/></p></body></html>", None))
        self.currBlockLabel.setText(QCoreApplication.translate("MainWindow", u"Current Block:", None))
        self.popUpUI.setText(QCoreApplication.translate("MainWindow", u"Display Train Stats", None))
        self.trainAcc.setText(QCoreApplication.translate("MainWindow", u"Acceleration:", None))
    # retranslateUi

