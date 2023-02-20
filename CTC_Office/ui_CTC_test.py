# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CTC_test.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(657, 788)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.locationText = QLabel(self.centralwidget)
        self.locationText.setObjectName(u"locationText")
        self.locationText.setGeometry(QRect(130, 110, 161, 31))
        font = QFont()
        font.setPointSize(11)
        self.locationText.setFont(font)
        self.enterLocation = QLineEdit(self.centralwidget)
        self.enterLocation.setObjectName(u"enterLocation")
        self.enterLocation.setGeometry(QRect(400, 110, 91, 28))
        self.enterSpeed = QLineEdit(self.centralwidget)
        self.enterSpeed.setObjectName(u"enterSpeed")
        self.enterSpeed.setGeometry(QRect(340, 160, 91, 28))
        self.speedText = QLabel(self.centralwidget)
        self.speedText.setObjectName(u"speedText")
        self.speedText.setGeometry(QRect(130, 160, 201, 31))
        self.speedText.setFont(font)
        self.mph = QLabel(self.centralwidget)
        self.mph.setObjectName(u"mph")
        self.mph.setGeometry(QRect(440, 160, 51, 31))
        self.mph.setFont(font)
        self.InputsBox = QFrame(self.centralwidget)
        self.InputsBox.setObjectName(u"InputsBox")
        self.InputsBox.setGeometry(QRect(100, 20, 411, 51))
        self.InputsBox.setAutoFillBackground(False)
        self.InputsBox.setStyleSheet(u"background-color: #B8B8B8\n"
"")
        self.InputsBox.setFrameShape(QFrame.StyledPanel)
        self.InputsBox.setFrameShadow(QFrame.Raised)
        self.Inputs = QLabel(self.InputsBox)
        self.Inputs.setObjectName(u"Inputs")
        self.Inputs.setGeometry(QRect(170, 0, 61, 41))
        font1 = QFont()
        font1.setPointSize(16)
        self.Inputs.setFont(font1)
        self.Inputs.setStyleSheet(u"color: black")
        self.OutputsBox_18 = QFrame(self.centralwidget)
        self.OutputsBox_18.setObjectName(u"OutputsBox_18")
        self.OutputsBox_18.setGeometry(QRect(100, 240, 411, 51))
        self.OutputsBox_18.setAutoFillBackground(False)
        self.OutputsBox_18.setStyleSheet(u"background-color: #B8B8B8")
        self.OutputsBox_18.setFrameShape(QFrame.StyledPanel)
        self.OutputsBox_18.setFrameShadow(QFrame.Raised)
        self.Outputs_2 = QLabel(self.OutputsBox_18)
        self.Outputs_2.setObjectName(u"Outputs_2")
        self.Outputs_2.setGeometry(QRect(170, 0, 81, 41))
        self.Outputs_2.setFont(font1)
        self.Outputs_2.setStyleSheet(u"color: black")
        self.authority = QLabel(self.centralwidget)
        self.authority.setObjectName(u"authority")
        self.authority.setGeometry(QRect(160, 320, 121, 31))
        self.authority.setFont(font)
        self.suggSpeedOutput = QLabel(self.centralwidget)
        self.suggSpeedOutput.setObjectName(u"suggSpeedOutput")
        self.suggSpeedOutput.setGeometry(QRect(330, 320, 221, 31))
        self.suggSpeedOutput.setFont(font)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(70, 360, 471, 21))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.greenLine_2 = QLabel(self.centralwidget)
        self.greenLine_2.setObjectName(u"greenLine_2")
        self.greenLine_2.setGeometry(QRect(110, 380, 91, 31))
        self.greenLine_2.setFont(font)
        self.redLineText = QLabel(self.centralwidget)
        self.redLineText.setObjectName(u"redLineText")
        self.redLineText.setGeometry(QRect(390, 380, 81, 31))
        self.redLineText.setFont(font)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 440, 251, 221))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 1, 1, 1, 1)

        self.red_E_sw2_5 = QLabel(self.gridLayoutWidget)
        self.red_E_sw2_5.setObjectName(u"red_E_sw2_5")

        self.gridLayout.addWidget(self.red_E_sw2_5, 3, 2, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 3, 1, 1, 1)

        self.red_E_sw2_2 = QLabel(self.gridLayoutWidget)
        self.red_E_sw2_2.setObjectName(u"red_E_sw2_2")

        self.gridLayout.addWidget(self.red_E_sw2_2, 0, 2, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 5, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 4, 1, 1, 1)

        self.red_E_sw2_3 = QLabel(self.gridLayoutWidget)
        self.red_E_sw2_3.setObjectName(u"red_E_sw2_3")

        self.gridLayout.addWidget(self.red_E_sw2_3, 1, 2, 1, 1)

        self.red_E_sw2_4 = QLabel(self.gridLayoutWidget)
        self.red_E_sw2_4.setObjectName(u"red_E_sw2_4")

        self.gridLayout.addWidget(self.red_E_sw2_4, 2, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.red_E_sw2_7 = QLabel(self.gridLayoutWidget)
        self.red_E_sw2_7.setObjectName(u"red_E_sw2_7")

        self.gridLayout.addWidget(self.red_E_sw2_7, 5, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 0, 1, 1, 1)

        self.red_E_sw2_6 = QLabel(self.gridLayoutWidget)
        self.red_E_sw2_6.setObjectName(u"red_E_sw2_6")

        self.gridLayout.addWidget(self.red_E_sw2_6, 4, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(320, 440, 251, 261))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget_2)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_2.addWidget(self.label_30, 5, 1, 1, 1)

        self.red_H_sw1_1 = QLabel(self.gridLayoutWidget_2)
        self.red_H_sw1_1.setObjectName(u"red_H_sw1_1")

        self.gridLayout_2.addWidget(self.red_H_sw1_1, 1, 1, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_2.addWidget(self.label_28, 3, 1, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_2)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 4, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 5, 0, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget_2)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_2.addWidget(self.label_31, 6, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 6, 0, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 2, 1, 1, 1)

        self.red_E_sw1 = QLabel(self.gridLayoutWidget_2)
        self.red_E_sw1.setObjectName(u"red_E_sw1")

        self.gridLayout_2.addWidget(self.red_E_sw1, 0, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 1)

        self.red_E_sw2 = QLabel(self.gridLayoutWidget_2)
        self.red_E_sw2.setObjectName(u"red_E_sw2")

        self.gridLayout_2.addWidget(self.red_E_sw2, 0, 2, 1, 1)

        self.label_33 = QLabel(self.gridLayoutWidget_2)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_2.addWidget(self.label_33, 1, 2, 1, 1)

        self.label_34 = QLabel(self.gridLayoutWidget_2)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_2.addWidget(self.label_34, 2, 2, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget_2)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_2.addWidget(self.label_35, 3, 2, 1, 1)

        self.label_36 = QLabel(self.gridLayoutWidget_2)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_2.addWidget(self.label_36, 4, 2, 1, 1)

        self.label_37 = QLabel(self.gridLayoutWidget_2)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_2.addWidget(self.label_37, 5, 2, 1, 1)

        self.label_38 = QLabel(self.gridLayoutWidget_2)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_2.addWidget(self.label_38, 6, 2, 1, 1)

        self.lineSelect = QComboBox(self.centralwidget)
        self.lineSelect.addItem("")
        self.lineSelect.addItem("")
        self.lineSelect.setObjectName(u"lineSelect")
        self.lineSelect.setGeometry(QRect(300, 110, 82, 28))
        self.lineText = QLabel(self.centralwidget)
        self.lineText.setObjectName(u"lineText")
        self.lineText.setGeometry(QRect(320, 80, 41, 31))
        self.lineText.setFont(font)
        self.blockText = QLabel(self.centralwidget)
        self.blockText.setObjectName(u"blockText")
        self.blockText.setGeometry(QRect(420, 80, 51, 31))
        self.blockText.setFont(font)
        self.enterButton = QPushButton(self.centralwidget)
        self.enterButton.setObjectName(u"enterButton")
        self.enterButton.setGeometry(QRect(430, 200, 83, 29))
        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setGeometry(QRect(330, 200, 83, 29))
        self.autoSelect = QCheckBox(self.centralwidget)
        self.autoSelect.setObjectName(u"autoSelect")
        self.autoSelect.setGeometry(QRect(410, 720, 78, 22))
        self.manualSelect = QCheckBox(self.centralwidget)
        self.manualSelect.setObjectName(u"manualSelect")
        self.manualSelect.setGeometry(QRect(490, 720, 61, 22))
        self.maintenanceSelect = QCheckBox(self.centralwidget)
        self.maintenanceSelect.setObjectName(u"maintenanceSelect")
        self.maintenanceSelect.setGeometry(QRect(560, 720, 91, 22))
        self.modesText = QLabel(self.centralwidget)
        self.modesText.setObjectName(u"modesText")
        self.modesText.setGeometry(QRect(360, 720, 41, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 657, 21))
        self.menuCTC_Dispatcher_Test_UI = QMenu(self.menubar)
        self.menuCTC_Dispatcher_Test_UI.setObjectName(u"menuCTC_Dispatcher_Test_UI")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCTC_Dispatcher_Test_UI.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.locationText.setText(QCoreApplication.translate("MainWindow", u"Enter Train Location:", None))
        self.enterSpeed.setText("")
        self.speedText.setText(QCoreApplication.translate("MainWindow", u"Enter Suggested Speed:", None))
        self.mph.setText(QCoreApplication.translate("MainWindow", u"mph", None))
        self.Inputs.setText(QCoreApplication.translate("MainWindow", u"Inputs", None))
        self.Outputs_2.setText(QCoreApplication.translate("MainWindow", u"Outputs", None))
        self.authority.setText(QCoreApplication.translate("MainWindow", u"Authority: 1.52mi", None))
        self.suggSpeedOutput.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed: --mph", None))
        self.greenLine_2.setText(QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.redLineText.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"           G", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"           M", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.red_E_sw2_5.setText(QCoreApplication.translate("MainWindow", u"9-Yard", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.red_E_sw2_2.setText(QCoreApplication.translate("MainWindow", u"9-Yard", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"           N", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.red_E_sw2_3.setText(QCoreApplication.translate("MainWindow", u"9-Yard", None))
        self.red_E_sw2_4.setText(QCoreApplication.translate("MainWindow", u"9-Yard", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"           J", None))
        self.red_E_sw2_7.setText(QCoreApplication.translate("MainWindow", u"9-Yard", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"           J", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.red_E_sw2_6.setText(QCoreApplication.translate("MainWindow", u"9-Yard", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"           C", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"           H", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"43-44", None))
        self.red_H_sw1_1.setText(QCoreApplication.translate("MainWindow", u"       15-16", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"32-33", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"38-39", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"           H", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"           N", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"52-53", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"           H", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"           E", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"           J", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"27-28", None))
        self.red_E_sw1.setText(QCoreApplication.translate("MainWindow", u"         9-10", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"           H", None))
        self.red_E_sw2.setText(QCoreApplication.translate("MainWindow", u"        9-Yard", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"        1-16", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"27-76", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"32-72", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"38-71", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"43-67", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"52-66", None))
        self.lineSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"Green", None))
        self.lineSelect.setItemText(1, QCoreApplication.translate("MainWindow", u"Red", None))

        self.lineText.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.blockText.setText(QCoreApplication.translate("MainWindow", u"Block", None))
        self.enterButton.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.autoSelect.setText(QCoreApplication.translate("MainWindow", u"Automatic", None))
        self.manualSelect.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.maintenanceSelect.setText(QCoreApplication.translate("MainWindow", u"Maintenance", None))
        self.modesText.setText(QCoreApplication.translate("MainWindow", u"Modes:", None))
        self.menuCTC_Dispatcher_Test_UI.setTitle(QCoreApplication.translate("MainWindow", u"CTC Dispatcher - Test UI", None))
    # retranslateUi

