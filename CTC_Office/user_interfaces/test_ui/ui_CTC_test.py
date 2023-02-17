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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2039, 1020)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.InputLocation = QLabel(self.centralwidget)
        self.InputLocation.setObjectName(u"InputLocation")
        self.InputLocation.setGeometry(QRect(90, 100, 161, 31))
        font = QFont()
        font.setPointSize(11)
        self.InputLocation.setFont(font)
        self.EnterLocation = QLineEdit(self.centralwidget)
        self.EnterLocation.setObjectName(u"EnterLocation")
        self.EnterLocation.setGeometry(QRect(360, 100, 91, 28))
        self.EnterSpeed = QLineEdit(self.centralwidget)
        self.EnterSpeed.setObjectName(u"EnterSpeed")
        self.EnterSpeed.setGeometry(QRect(300, 150, 91, 28))
        self.InputSpeed = QLabel(self.centralwidget)
        self.InputSpeed.setObjectName(u"InputSpeed")
        self.InputSpeed.setGeometry(QRect(90, 150, 201, 31))
        self.InputSpeed.setFont(font)
        self.mph = QLabel(self.centralwidget)
        self.mph.setObjectName(u"mph")
        self.mph.setGeometry(QRect(400, 150, 51, 31))
        self.mph.setFont(font)
        self.InputsBox = QFrame(self.centralwidget)
        self.InputsBox.setObjectName(u"InputsBox")
        self.InputsBox.setGeometry(QRect(60, 10, 411, 51))
        self.InputsBox.setAutoFillBackground(True)
        self.InputsBox.setFrameShape(QFrame.StyledPanel)
        self.InputsBox.setFrameShadow(QFrame.Raised)
        self.Inputs = QLabel(self.InputsBox)
        self.Inputs.setObjectName(u"Inputs")
        self.Inputs.setGeometry(QRect(160, 0, 81, 41))
        font1 = QFont()
        font1.setPointSize(16)
        self.Inputs.setFont(font1)
        self.OutputsBox_18 = QFrame(self.centralwidget)
        self.OutputsBox_18.setObjectName(u"OutputsBox_18")
        self.OutputsBox_18.setGeometry(QRect(60, 230, 411, 51))
        self.OutputsBox_18.setAutoFillBackground(True)
        self.OutputsBox_18.setFrameShape(QFrame.StyledPanel)
        self.OutputsBox_18.setFrameShadow(QFrame.Raised)
        self.Outputs_2 = QLabel(self.OutputsBox_18)
        self.Outputs_2.setObjectName(u"Outputs_2")
        self.Outputs_2.setGeometry(QRect(150, 0, 101, 41))
        self.Outputs_2.setFont(font1)
        self.SuggAuth_2 = QLabel(self.centralwidget)
        self.SuggAuth_2.setObjectName(u"SuggAuth_2")
        self.SuggAuth_2.setGeometry(QRect(30, 310, 241, 31))
        self.SuggAuth_2.setFont(font)
        self.SuggSpeed_2 = QLabel(self.centralwidget)
        self.SuggSpeed_2.setObjectName(u"SuggSpeed_2")
        self.SuggSpeed_2.setGeometry(QRect(290, 310, 221, 31))
        self.SuggSpeed_2.setFont(font)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(30, 350, 471, 21))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.GreenLine_2 = QLabel(self.centralwidget)
        self.GreenLine_2.setObjectName(u"GreenLine_2")
        self.GreenLine_2.setGeometry(QRect(100, 370, 91, 31))
        self.GreenLine_2.setFont(font)
        self.RedLine_2 = QLabel(self.centralwidget)
        self.RedLine_2.setObjectName(u"RedLine_2")
        self.RedLine_2.setGeometry(QRect(320, 370, 81, 31))
        self.RedLine_2.setFont(font)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 430, 231, 241))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 0, 1, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 1, 1, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 3, 1, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 4, 1, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 5, 1, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(290, 430, 321, 241))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_2)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_2.addWidget(self.label_29, 4, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_2)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_2.addWidget(self.label_27, 1, 1, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_2)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 0, 1, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_2.addWidget(self.label_28, 3, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 5, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget_2)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_2.addWidget(self.label_30, 5, 1, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 2, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 6, 0, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget_2)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_2.addWidget(self.label_31, 6, 1, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(260, 100, 82, 28))
        self.InputLocation_2 = QLabel(self.centralwidget)
        self.InputLocation_2.setObjectName(u"InputLocation_2")
        self.InputLocation_2.setGeometry(QRect(280, 70, 41, 31))
        self.InputLocation_2.setFont(font)
        self.InputLocation_3 = QLabel(self.centralwidget)
        self.InputLocation_3.setObjectName(u"InputLocation_3")
        self.InputLocation_3.setGeometry(QRect(380, 70, 51, 31))
        self.InputLocation_3.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(390, 190, 83, 29))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(290, 190, 83, 29))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2039, 25))
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
        self.InputLocation.setText(QCoreApplication.translate("MainWindow", u"Enter Train Location:", None))
        self.EnterSpeed.setText("")
        self.InputSpeed.setText(QCoreApplication.translate("MainWindow", u"Enter Suggested Speed:", None))
        self.mph.setText(QCoreApplication.translate("MainWindow", u"mph", None))
        self.Inputs.setText(QCoreApplication.translate("MainWindow", u"Inputs", None))
        self.Outputs_2.setText(QCoreApplication.translate("MainWindow", u"Outputs", None))
        self.SuggAuth_2.setText(QCoreApplication.translate("MainWindow", u"Suggested Authority: 1.52mi", None))
        self.SuggSpeed_2.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed: 42mph", None))
        self.GreenLine_2.setText(QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.RedLine_2.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"sw", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Green", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Red", None))

        self.InputLocation_2.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.InputLocation_3.setText(QCoreApplication.translate("MainWindow", u"Block", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.menuCTC_Dispatcher_Test_UI.setTitle(QCoreApplication.translate("MainWindow", u"CTC Dispatcher - Test UI", None))
    # retranslateUi

