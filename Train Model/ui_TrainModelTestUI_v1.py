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
    QFrame, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

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
        self.label_5.setGeometry(QRect(520, 230, 141, 21))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(520, 210, 121, 21))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(520, 270, 91, 21))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(520, 290, 101, 21))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(520, 330, 91, 21))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(520, 350, 101, 21))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(520, 310, 101, 21))
        self.inputPow = QLineEdit(self.centralwidget)
        self.inputPow.setObjectName(u"inputPow")
        self.inputPow.setGeometry(QRect(640, 230, 81, 20))
        self.inputCommSpeed = QLineEdit(self.centralwidget)
        self.inputCommSpeed.setObjectName(u"inputCommSpeed")
        self.inputCommSpeed.setGeometry(QRect(640, 80, 81, 20))
        self.outputPow = QTextEdit(self.centralwidget)
        self.outputPow.setObjectName(u"outputPow")
        self.outputPow.setGeometry(QRect(280, 300, 81, 21))
        self.inputTemp = QLineEdit(self.centralwidget)
        self.inputTemp.setObjectName(u"inputTemp")
        self.inputTemp.setGeometry(QRect(640, 210, 81, 20))
        self.outputTemp = QTextEdit(self.centralwidget)
        self.outputTemp.setObjectName(u"outputTemp")
        self.outputTemp.setGeometry(QRect(100, 300, 81, 21))
        self.tempButton = QPushButton(self.centralwidget)
        self.tempButton.setObjectName(u"tempButton")
        self.tempButton.setGeometry(QRect(740, 210, 41, 18))
        self.powButton = QPushButton(self.centralwidget)
        self.powButton.setObjectName(u"powButton")
        self.powButton.setGeometry(QRect(740, 230, 41, 18))
        self.tempLabel = QLabel(self.centralwidget)
        self.tempLabel.setObjectName(u"tempLabel")
        self.tempLabel.setGeometry(QRect(10, 300, 81, 16))
        self.powLabel = QLabel(self.centralwidget)
        self.powLabel.setObjectName(u"powLabel")
        self.powLabel.setGeometry(QRect(200, 300, 81, 20))
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
        self.intLights.setGeometry(QRect(640, 270, 111, 18))
        self.intLights.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.leftDoor = QCheckBox(self.centralwidget)
        self.leftDoor.setObjectName(u"leftDoor")
        self.leftDoor.setGeometry(QRect(640, 330, 111, 18))
        self.leftDoor.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.rightDoor = QCheckBox(self.centralwidget)
        self.rightDoor.setObjectName(u"rightDoor")
        self.rightDoor.setGeometry(QRect(640, 350, 111, 18))
        self.rightDoor.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.headlights = QCheckBox(self.centralwidget)
        self.headlights.setObjectName(u"headlights")
        self.headlights.setGeometry(QRect(640, 310, 111, 18))
        self.headlights.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(240, 80, 221, 131))
        self.checkBox.setMaximumSize(QSize(451, 131))
        self.checkBox.setStyleSheet(u"")
        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 80, 171, 101))
        self.intLightLabel = QLabel(self.centralwidget)
        self.intLightLabel.setObjectName(u"intLightLabel")
        self.intLightLabel.setGeometry(QRect(110, 80, 37, 12))
        self.extLights = QCheckBox(self.centralwidget)
        self.extLights.setObjectName(u"extLights")
        self.extLights.setGeometry(QRect(640, 290, 111, 18))
        self.extLights.setStyleSheet(u"    QCheckBox::indicator:unchecked {\n"
"		color: rgb(0, 170, 0);\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"		color: rgb(255, 0, 0);\n"
"    }")
        self.extLightLabel = QLabel(self.centralwidget)
        self.extLightLabel.setObjectName(u"extLightLabel")
        self.extLightLabel.setGeometry(QRect(110, 100, 37, 12))
        self.headlightLabel = QLabel(self.centralwidget)
        self.headlightLabel.setObjectName(u"headlightLabel")
        self.headlightLabel.setGeometry(QRect(110, 120, 37, 12))
        self.lDoorLabel = QLabel(self.centralwidget)
        self.lDoorLabel.setObjectName(u"lDoorLabel")
        self.lDoorLabel.setGeometry(QRect(110, 140, 37, 12))
        self.rDoorLabel = QLabel(self.centralwidget)
        self.rDoorLabel.setObjectName(u"rDoorLabel")
        self.rDoorLabel.setGeometry(QRect(110, 160, 37, 12))
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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Commanded Speed:</span></p></body></html>", None))
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
        self.outputTemp.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tempButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.powButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.tempLabel.setText(QCoreApplication.translate("MainWindow", u"Current Temp:", None))
        self.powLabel.setText(QCoreApplication.translate("MainWindow", u"Current Power:", None))
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
        self.intLights.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.leftDoor.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.rightDoor.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.headlights.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox.setText("")

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Internal Lights", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"External Lights", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Headlights", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Left Door", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Right Door", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.intLightLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.extLights.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.extLightLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.headlightLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.lDoorLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.rDoorLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menuTrain_Model_Test_UI.setTitle(QCoreApplication.translate("MainWindow", u"Train Model Test UI", None))
    # retranslateUi

