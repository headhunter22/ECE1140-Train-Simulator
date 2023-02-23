# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TrainModelTestUI_v2.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(337, 526)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 100, 141, 21))
        self.sigFault_2 = QLabel(self.centralwidget)
        self.sigFault_2.setObjectName(u"sigFault_2")
        self.sigFault_2.setGeometry(QRect(170, 270, 101, 21))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 270, 91, 21))
        self.powFault = QCheckBox(self.centralwidget)
        self.powFault.setObjectName(u"powFault")
        self.powFault.setGeometry(QRect(290, 290, 111, 18))
        self.powFault.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(140, 70, 81, 22))
        self.inputTemp = QLineEdit(self.centralwidget)
        self.inputTemp.setObjectName(u"inputTemp")
        self.inputTemp.setGeometry(QRect(140, 200, 81, 20))
        self.inputPow = QLineEdit(self.centralwidget)
        self.inputPow.setObjectName(u"inputPow")
        self.inputPow.setGeometry(QRect(140, 220, 81, 20))
        self.addTrain = QPushButton(self.centralwidget)
        self.addTrain.setObjectName(u"addTrain")
        self.addTrain.setGeometry(QRect(70, 410, 211, 20))
        self.addTrain.setStyleSheet(u"font: italic 9pt \"Segoe UI\";")
        self.headlights = QCheckBox(self.centralwidget)
        self.headlights.setObjectName(u"headlights")
        self.headlights.setGeometry(QRect(140, 310, 111, 18))
        self.headlights.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.rightDoor = QCheckBox(self.centralwidget)
        self.rightDoor.setObjectName(u"rightDoor")
        self.rightDoor.setGeometry(QRect(140, 350, 111, 18))
        self.rightDoor.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.AC = QCheckBox(self.centralwidget)
        self.AC.setObjectName(u"AC")
        self.AC.setGeometry(QRect(140, 370, 111, 18))
        self.AC.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.commSpeedButton = QPushButton(self.centralwidget)
        self.commSpeedButton.setObjectName(u"commSpeedButton")
        self.commSpeedButton.setGeometry(QRect(240, 100, 41, 18))
        self.sigFault = QCheckBox(self.centralwidget)
        self.sigFault.setObjectName(u"sigFault")
        self.sigFault.setGeometry(QRect(290, 270, 111, 18))
        self.sigFault.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(70, 440, 211, 20))
        self.pushButton_3.setStyleSheet(u"font: italic 9pt \"Segoe UI\";")
        self.brakeFault_2 = QLabel(self.centralwidget)
        self.brakeFault_2.setObjectName(u"brakeFault_2")
        self.brakeFault_2.setGeometry(QRect(170, 310, 101, 21))
        self.currentBlockLabel = QLabel(self.centralwidget)
        self.currentBlockLabel.setObjectName(u"currentBlockLabel")
        self.currentBlockLabel.setGeometry(QRect(20, 150, 121, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 181, 41))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 330, 91, 21))
        self.powFault_2 = QLabel(self.centralwidget)
        self.powFault_2.setObjectName(u"powFault_2")
        self.powFault_2.setGeometry(QRect(170, 290, 91, 21))
        self.currentBlock = QComboBox(self.centralwidget)
        self.currentBlock.addItem("")
        self.currentBlock.addItem("")
        self.currentBlock.addItem("")
        self.currentBlock.addItem("")
        self.currentBlock.addItem("")
        self.currentBlock.addItem("")
        self.currentBlock.addItem("")
        self.currentBlock.addItem("")
        self.currentBlock.addItem("")
        self.currentBlock.addItem("")
        self.currentBlock.setObjectName(u"currentBlock")
        self.currentBlock.setGeometry(QRect(230, 150, 55, 22))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 350, 101, 21))
        self.commSpeed = QLineEdit(self.centralwidget)
        self.commSpeed.setObjectName(u"commSpeed")
        self.commSpeed.setGeometry(QRect(140, 100, 81, 20))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 200, 121, 21))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 290, 101, 21))
        self.leftDoor = QCheckBox(self.centralwidget)
        self.leftDoor.setObjectName(u"leftDoor")
        self.leftDoor.setGeometry(QRect(140, 330, 111, 18))
        self.leftDoor.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 310, 101, 21))
        self.ACLabel = QLabel(self.centralwidget)
        self.ACLabel.setObjectName(u"ACLabel")
        self.ACLabel.setGeometry(QRect(20, 370, 101, 21))
        self.extLights = QCheckBox(self.centralwidget)
        self.extLights.setObjectName(u"extLights")
        self.extLights.setGeometry(QRect(140, 290, 111, 18))
        self.extLights.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.powButton = QPushButton(self.centralwidget)
        self.powButton.setObjectName(u"powButton")
        self.powButton.setGeometry(QRect(240, 220, 41, 18))
        self.intLights = QCheckBox(self.centralwidget)
        self.intLights.setObjectName(u"intLights")
        self.intLights.setGeometry(QRect(140, 270, 111, 18))
        self.intLights.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }\n"
"\n"
"")
        self.brakeFault = QCheckBox(self.centralwidget)
        self.brakeFault.setObjectName(u"brakeFault")
        self.brakeFault.setGeometry(QRect(290, 310, 111, 18))
        self.brakeFault.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 220, 141, 21))
        self.tempButton = QPushButton(self.centralwidget)
        self.tempButton.setObjectName(u"tempButton")
        self.tempButton.setGeometry(QRect(240, 200, 41, 18))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 121, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 337, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Comm. Speed:</span></p></body></html>", None))
        self.sigFault_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Signal Fault:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Internal Lights:</span></p></body></html>", None))
        self.powFault.setText("")
        self.addTrain.setText(QCoreApplication.translate("MainWindow", u"Add Train", None))
        self.headlights.setText("")
        self.rightDoor.setText("")
        self.AC.setText("")
        self.commSpeedButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.sigFault.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Load Train Schedule", None))
        self.brakeFault_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Brake Fault:</span></p></body></html>", None))
        self.currentBlockLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Current Block</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; text-decoration: underline; color:#000000;\">Test Data</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Left Doors:</span></p></body></html>", None))
        self.powFault_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Power Fault:</span></p></body></html>", None))
        self.currentBlock.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.currentBlock.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.currentBlock.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.currentBlock.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.currentBlock.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.currentBlock.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.currentBlock.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.currentBlock.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.currentBlock.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.currentBlock.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Right Doors:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Current Temp:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">External Lights:</span></p></body></html>", None))
        self.leftDoor.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Headlights:</span></p></body></html>", None))
        self.ACLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">AC:</span></p></body></html>", None))
        self.extLights.setText("")
        self.powButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.intLights.setText("")
        self.brakeFault.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Power Input:</span></p></body></html>", None))
        self.tempButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Current Time:</span></p></body></html>", None))
    # retranslateUi

