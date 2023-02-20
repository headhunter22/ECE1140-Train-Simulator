# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TrainModelTestUI_v1.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QFrame, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(825, 488)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(480, -50, 20, 931))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(560, 0, 181, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(520, 50, 121, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(520, 80, 141, 21))
        self.clButtonR = QPushButton(self.centralwidget)
        self.clButtonR.setObjectName(u"clButtonR")
        self.clButtonR.setGeometry(QRect(640, 170, 71, 16))
        self.clButtonR.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.clButtonGreen = QPushButton(self.centralwidget)
        self.clButtonGreen.setObjectName(u"clButtonGreen")
        self.clButtonGreen.setGeometry(QRect(710, 170, 71, 16))
        self.clButtonGreen.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 255, 0);\n"
"}")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(520, 170, 141, 21))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(520, 220, 141, 21))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(520, 200, 121, 21))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(520, 250, 91, 21))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(520, 270, 101, 21))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(520, 310, 91, 21))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(520, 330, 101, 21))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(520, 290, 101, 21))
        self.inputPow = QLineEdit(self.centralwidget)
        self.inputPow.setObjectName(u"inputPow")
        self.inputPow.setGeometry(QRect(640, 220, 81, 20))
        self.inputCommSpeed = QLineEdit(self.centralwidget)
        self.inputCommSpeed.setObjectName(u"inputCommSpeed")
        self.inputCommSpeed.setGeometry(QRect(640, 80, 81, 20))
        self.inputTemp = QLineEdit(self.centralwidget)
        self.inputTemp.setObjectName(u"inputTemp")
        self.inputTemp.setGeometry(QRect(640, 200, 81, 20))
        self.tempButton = QPushButton(self.centralwidget)
        self.tempButton.setObjectName(u"tempButton")
        self.tempButton.setGeometry(QRect(740, 200, 41, 18))
        self.powButton = QPushButton(self.centralwidget)
        self.powButton.setObjectName(u"powButton")
        self.powButton.setGeometry(QRect(740, 220, 41, 18))
        self.tempLabel = QLabel(self.centralwidget)
        self.tempLabel.setObjectName(u"tempLabel")
        self.tempLabel.setGeometry(QRect(10, 310, 151, 21))
        self.tempLabel.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 11pt \"Segoe UI\";")
        self.powLabel = QLabel(self.centralwidget)
        self.powLabel.setObjectName(u"powLabel")
        self.powLabel.setGeometry(QRect(240, 370, 231, 31))
        self.powLabel.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(640, 50, 81, 22))
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(520, 120, 121, 21))
        self.commSpeedButton = QPushButton(self.centralwidget)
        self.commSpeedButton.setObjectName(u"commSpeedButton")
        self.commSpeedButton.setGeometry(QRect(740, 80, 41, 18))
        self.comboBox_Section = QComboBox(self.centralwidget)
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.addItem("")
        self.comboBox_Section.setObjectName(u"comboBox_Section")
        self.comboBox_Section.setGeometry(QRect(730, 120, 55, 22))
        self.comboBox_Block = QComboBox(self.centralwidget)
        self.comboBox_Block.addItem("")
        self.comboBox_Block.addItem("")
        self.comboBox_Block.addItem("")
        self.comboBox_Block.addItem("")
        self.comboBox_Block.addItem("")
        self.comboBox_Block.addItem("")
        self.comboBox_Block.addItem("")
        self.comboBox_Block.addItem("")
        self.comboBox_Block.addItem("")
        self.comboBox_Block.addItem("")
        self.comboBox_Block.setObjectName(u"comboBox_Block")
        self.comboBox_Block.setGeometry(QRect(730, 140, 55, 22))
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(520, 140, 121, 21))
        self.intLights = QCheckBox(self.centralwidget)
        self.intLights.setObjectName(u"intLights")
        self.intLights.setGeometry(QRect(640, 250, 111, 18))
        self.intLights.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }\n"
"\n"
"")
        self.leftDoor = QCheckBox(self.centralwidget)
        self.leftDoor.setObjectName(u"leftDoor")
        self.leftDoor.setGeometry(QRect(640, 310, 111, 18))
        self.leftDoor.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.rightDoor = QCheckBox(self.centralwidget)
        self.rightDoor.setObjectName(u"rightDoor")
        self.rightDoor.setGeometry(QRect(640, 330, 111, 18))
        self.rightDoor.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.headlights = QCheckBox(self.centralwidget)
        self.headlights.setObjectName(u"headlights")
        self.headlights.setGeometry(QRect(640, 290, 111, 18))
        self.headlights.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.intLightLabel = QLabel(self.centralwidget)
        self.intLightLabel.setObjectName(u"intLightLabel")
        self.intLightLabel.setGeometry(QRect(180, 110, 37, 12))
        self.extLights = QCheckBox(self.centralwidget)
        self.extLights.setObjectName(u"extLights")
        self.extLights.setGeometry(QRect(640, 270, 111, 18))
        self.extLights.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.extLightLabel = QLabel(self.centralwidget)
        self.extLightLabel.setObjectName(u"extLightLabel")
        self.extLightLabel.setGeometry(QRect(180, 140, 37, 12))
        self.headlightLabel = QLabel(self.centralwidget)
        self.headlightLabel.setObjectName(u"headlightLabel")
        self.headlightLabel.setGeometry(QRect(180, 170, 37, 12))
        self.lDoorLabel = QLabel(self.centralwidget)
        self.lDoorLabel.setObjectName(u"lDoorLabel")
        self.lDoorLabel.setGeometry(QRect(180, 200, 37, 12))
        self.rDoorLabel = QLabel(self.centralwidget)
        self.rDoorLabel.setObjectName(u"rDoorLabel")
        self.rDoorLabel.setGeometry(QRect(180, 230, 37, 12))
        self.brakeFault = QCheckBox(self.centralwidget)
        self.brakeFault.setObjectName(u"brakeFault")
        self.brakeFault.setGeometry(QRect(790, 290, 111, 18))
        self.brakeFault.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.sigFault_2 = QLabel(self.centralwidget)
        self.sigFault_2.setObjectName(u"sigFault_2")
        self.sigFault_2.setGeometry(QRect(670, 250, 101, 21))
        self.brakeFault_2 = QLabel(self.centralwidget)
        self.brakeFault_2.setObjectName(u"brakeFault_2")
        self.brakeFault_2.setGeometry(QRect(670, 290, 101, 21))
        self.powFault = QCheckBox(self.centralwidget)
        self.powFault.setObjectName(u"powFault")
        self.powFault.setGeometry(QRect(790, 270, 111, 18))
        self.powFault.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.sigFault = QCheckBox(self.centralwidget)
        self.sigFault.setObjectName(u"sigFault")
        self.sigFault.setGeometry(QRect(790, 250, 111, 18))
        self.sigFault.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.powFault_2 = QLabel(self.centralwidget)
        self.powFault_2.setObjectName(u"powFault_2")
        self.powFault_2.setGeometry(QRect(670, 270, 91, 21))
        self.sigFaultLabel = QPushButton(self.centralwidget)
        self.sigFaultLabel.setObjectName(u"sigFaultLabel")
        self.sigFaultLabel.setGeometry(QRect(10, 380, 71, 61))
        self.sigFaultLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.powFaultLabel = QPushButton(self.centralwidget)
        self.powFaultLabel.setObjectName(u"powFaultLabel")
        self.powFaultLabel.setGeometry(QRect(80, 380, 71, 61))
        self.powFaultLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.brakeFaultLabel = QPushButton(self.centralwidget)
        self.brakeFaultLabel.setObjectName(u"brakeFaultLabel")
        self.brakeFaultLabel.setGeometry(QRect(150, 380, 71, 61))
        self.brakeFaultLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 360, 121, 21))
        self.label_12.setStyleSheet(u"font: 15pt \"Segoe UI\";")
        self.AC = QCheckBox(self.centralwidget)
        self.AC.setObjectName(u"AC")
        self.AC.setGeometry(QRect(640, 350, 111, 18))
        self.AC.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.ACLabel = QLabel(self.centralwidget)
        self.ACLabel.setObjectName(u"ACLabel")
        self.ACLabel.setGeometry(QRect(520, 350, 101, 21))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 409, 231, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.powProgressBar = QProgressBar(self.centralwidget)
        self.powProgressBar.setObjectName(u"powProgressBar")
        self.powProgressBar.setGeometry(QRect(240, 350, 231, 23))
        self.powProgressBar.setStyleSheet(u"")
        self.powProgressBar.setValue(24)
        self.ACLabel_2 = QLabel(self.centralwidget)
        self.ACLabel_2.setObjectName(u"ACLabel_2")
        self.ACLabel_2.setGeometry(QRect(10, 330, 151, 21))
        self.ACLabel_2.setStyleSheet(u"font: 11pt \"Segoe UI\";\n"
"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.ACIcon = QPushButton(self.centralwidget)
        self.ACIcon.setObjectName(u"ACIcon")
        self.ACIcon.setGeometry(QRect(170, 300, 51, 51))
        self.ACIcon.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ACprogressBar = QProgressBar(self.centralwidget)
        self.ACprogressBar.setObjectName(u"ACprogressBar")
        self.ACprogressBar.setGeometry(QRect(10, 290, 151, 23))
        self.ACprogressBar.setValue(24)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(280, 20, 191, 31))
        self.label_14.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(240, 150, 231, 31))
        self.label_16.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(240, 70, 231, 81))
        self.label_17.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(330, 190, 141, 31))
        self.label_18.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(330, 230, 141, 31))
        self.label_19.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;")
        self.speedIcon = QPushButton(self.centralwidget)
        self.speedIcon.setObjectName(u"speedIcon")
        self.speedIcon.setGeometry(QRect(240, 190, 71, 71))
        self.speedIcon.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tempLabel_2 = QLabel(self.centralwidget)
        self.tempLabel_2.setObjectName(u"tempLabel_2")
        self.tempLabel_2.setGeometry(QRect(240, 290, 231, 21))
        self.tempLabel_2.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 11pt \"Segoe UI\";")
        self.tempLabel_3 = QLabel(self.centralwidget)
        self.tempLabel_3.setObjectName(u"tempLabel_3")
        self.tempLabel_3.setGeometry(QRect(240, 310, 231, 21))
        self.tempLabel_3.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 4px;\n"
"padding: 2px;\n"
"font: 11pt \"Segoe UI\";")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(140, 40, 71, 16))
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(150, 60, 61, 20))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 45, 111, 31))
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 10, 131, 31))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(570, 400, 211, 20))
        self.pushButton_2.setStyleSheet(u"font: italic 9pt \"Segoe UI\";")
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 80, 111, 191))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 825, 17))
        self.menuTrain_Model_Test_UI = QMenu(self.menubar)
        self.menuTrain_Model_Test_UI.setObjectName(u"menuTrain_Model_Test_UI")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTrain_Model_Test_UI.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; text-decoration: underline; color:#000000;\">Test Data</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Current Time:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Comm. Speed:</span></p></body></html>", None))
        self.clButtonR.setText(QCoreApplication.translate("MainWindow", u"RED", None))
        self.clButtonGreen.setText(QCoreApplication.translate("MainWindow", u"GREEN", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Current Line: </span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Power Input:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Current Temp:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Internal Lights:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">External Lights:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Left Doors:</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Right Doors:</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Headlights:</span></p></body></html>", None))
        self.tempButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.powButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.tempLabel.setText(QCoreApplication.translate("MainWindow", u"Internal Temp:", None))
        self.powLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Power Input:</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Current Section</span></p></body></html>", None))
        self.commSpeedButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.comboBox_Section.setItemText(0, QCoreApplication.translate("MainWindow", u"A", None))
        self.comboBox_Section.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.comboBox_Section.setItemText(2, QCoreApplication.translate("MainWindow", u"C", None))
        self.comboBox_Section.setItemText(3, QCoreApplication.translate("MainWindow", u"D", None))
        self.comboBox_Section.setItemText(4, QCoreApplication.translate("MainWindow", u"E", None))
        self.comboBox_Section.setItemText(5, QCoreApplication.translate("MainWindow", u"F", None))
        self.comboBox_Section.setItemText(6, QCoreApplication.translate("MainWindow", u"G", None))
        self.comboBox_Section.setItemText(7, QCoreApplication.translate("MainWindow", u"H", None))
        self.comboBox_Section.setItemText(8, QCoreApplication.translate("MainWindow", u"I", None))
        self.comboBox_Section.setItemText(9, QCoreApplication.translate("MainWindow", u"J", None))
        self.comboBox_Section.setItemText(10, QCoreApplication.translate("MainWindow", u"K", None))
        self.comboBox_Section.setItemText(11, QCoreApplication.translate("MainWindow", u"L", None))
        self.comboBox_Section.setItemText(12, QCoreApplication.translate("MainWindow", u"M", None))
        self.comboBox_Section.setItemText(13, QCoreApplication.translate("MainWindow", u"N", None))
        self.comboBox_Section.setItemText(14, QCoreApplication.translate("MainWindow", u"O", None))
        self.comboBox_Section.setItemText(15, QCoreApplication.translate("MainWindow", u"P", None))
        self.comboBox_Section.setItemText(16, QCoreApplication.translate("MainWindow", u"Q", None))
        self.comboBox_Section.setItemText(17, QCoreApplication.translate("MainWindow", u"R", None))

        self.comboBox_Block.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_Block.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_Block.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_Block.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_Block.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_Block.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_Block.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_Block.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_Block.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_Block.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Current Block</span></p></body></html>", None))
        self.intLights.setText("")
        self.leftDoor.setText("")
        self.rightDoor.setText("")
        self.headlights.setText("")
        self.intLightLabel.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.extLights.setText("")
        self.extLightLabel.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.headlightLabel.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.lDoorLabel.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.rDoorLabel.setText(QCoreApplication.translate("MainWindow", u"Null", None))
        self.brakeFault.setText("")
        self.sigFault_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Signal Fault:</span></p></body></html>", None))
        self.brakeFault_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Brake Fault:</span></p></body></html>", None))
        self.powFault.setText("")
        self.sigFault.setText("")
        self.powFault_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Power Fault:</span></p></body></html>", None))
        self.sigFaultLabel.setText("")
        self.powFaultLabel.setText("")
        self.brakeFaultLabel.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Fault Status", None))
        self.AC.setText("")
        self.ACLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">AC:</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"EMERGENCY BRAKE", None))
        self.ACLabel_2.setText(QCoreApplication.translate("MainWindow", u"AC Status:", None))
        self.ACIcon.setText("")
        self.label_14.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Next Station:</p><p>Scheduled Arrival:</p><p>Estimated Arrival:</p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Speed Limit:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Actual Limit:", None))
        self.speedIcon.setText("")
        self.tempLabel_2.setText(QCoreApplication.translate("MainWindow", u"Current Section:", None))
        self.tempLabel_3.setText(QCoreApplication.translate("MainWindow", u"Current Block:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Red Line</p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Green Line</p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Current Train:</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Load Train Schedule", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Internal Lights:</span></p><p><span style=\" font-size:12pt;\">External Lights:</span></p><p><span style=\" font-size:12pt;\">Headlights:</span></p><p><span style=\" font-size:12pt;\">Left Doors:</span></p><p><span style=\" font-size:12pt;\">Right Doors:</span></p></body></html>", None))
        self.menuTrain_Model_Test_UI.setTitle(QCoreApplication.translate("MainWindow", u"Train Model Test UI", None))
    # retranslateUi

