# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollBar,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(255,255,255)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.RedLineContainer = QWidget(self.centralwidget)
        self.RedLineContainer.setObjectName(u"RedLineContainer")
        self.frame_3 = QFrame(self.RedLineContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 40, 301, 42))
        self.frame_3.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"padding: 0px;\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.TrainsCount = QLabel(self.frame_3)
        self.TrainsCount.setObjectName(u"TrainsCount")
        self.TrainsCount.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 500 12pt \"Inter\";\n"
"background-color: rgb(165, 165, 165);\n"
"border: 2px solid;\n"
"margin: 0px\n"
"")
        self.TrainsCount.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.TrainsCount)

        self.Info = QLabel(self.frame_3)
        self.Info.setObjectName(u"Info")
        self.Info.setStyleSheet(u"background-color: rgb(165, 165, 165);\n"
"border: 2px solid;\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 500 13pt \"Inter\";\n"
"")
        self.Info.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Info)

        self.Occupancy = QLabel(self.frame_3)
        self.Occupancy.setObjectName(u"Occupancy")
        self.Occupancy.setStyleSheet(u"background-color: rgb(165, 165, 165);\n"
"border: 2px solid;\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 500 13pt \"Inter\";\n"
"\n"
"")
        self.Occupancy.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Occupancy)

        self.SectionLabel = QLabel(self.frame_3)
        self.SectionLabel.setObjectName(u"SectionLabel")
        self.SectionLabel.setStyleSheet(u"background-color: rgb(165, 165, 165);\n"
"border: 2px solid;\n"
"\n"
"color: rgb(0, 0, 0);\n"
"font: 500 13pt \"Inter\";\n"
"")
        self.SectionLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.SectionLabel)

        self.frame_6 = QFrame(self.RedLineContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, -5, 281, 41))
        self.frame_6.setStyleSheet(u"background-color: rgb(123, 123, 123)\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: #cc0000;\n"
"font: 700 28pt \"Inter\";\n"
"padding-left: 20px;\n"
"padding-right: 20px;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.gridLayoutWidget = QWidget(self.RedLineContainer)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 80, 301, 491))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalScrollBar = QScrollBar(self.gridLayoutWidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.verticalScrollBar, 0, 4, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0);\u2029font: 500 12pt \"Inter\";\u2029background-color: rgb(165, 165, 165);\u2029border: 2px solid;\u2029margin: 0px\u2029")

        self.verticalLayout.addWidget(self.label_8)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);\u2029font: 500 12pt \"Inter\";\u2029background-color: rgb(165, 165, 165);\u2029border: 2px solid;\u2029margin: 0px\u2029")

        self.verticalLayout.addWidget(self.label_7)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);\u2029font: 500 12pt \"Inter\";\u2029background-color: rgb(165, 165, 165);\u2029border: 2px solid;\u2029margin: 0px\u2029")

        self.verticalLayout.addWidget(self.label_6)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);\u2029font: 500 12pt \"Inter\";\u2029background-color: rgb(165, 165, 165);\u2029border: 2px solid;\u2029margin: 0px\u2029")

        self.verticalLayout.addWidget(self.label_4)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);\u2029font: 500 12pt \"Inter\";\u2029background-color: rgb(165, 165, 165);\u2029border: 2px solid;\u2029margin: 0px\u2029")

        self.verticalLayout.addWidget(self.label_3)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);\u2029font: 500 12pt \"Inter\";\u2029background-color: rgb(165, 165, 165);\u2029border: 2px solid;\u2029margin: 0px\u2029")

        self.verticalLayout.addWidget(self.label_2)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0);\u2029font: 500 12pt \"Inter\";\u2029background-color: rgb(165, 165, 165);\u2029border: 2px solid;\u2029margin: 0px\u2029")

        self.verticalLayout.addWidget(self.label_9)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\u2029font: 500 12pt \"Inter\";\u2029background-color: rgb(165, 165, 165);\u2029border: 2px solid;\u2029margin: 0px\u2029")

        self.verticalLayout.addWidget(self.label)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.gridLayout.addLayout(self.verticalLayout_4, 0, 3, 1, 1)


        self.horizontalLayout.addWidget(self.RedLineContainer)

        self.GreenLineContainer = QWidget(self.centralwidget)
        self.GreenLineContainer.setObjectName(u"GreenLineContainer")
        self.pushButton = QPushButton(self.GreenLineContainer)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 50, 100, 32))
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 0, 0)")

        self.horizontalLayout.addWidget(self.GreenLineContainer)

        self.GeneralInfoContainer = QWidget(self.centralwidget)
        self.GeneralInfoContainer.setObjectName(u"GeneralInfoContainer")

        self.horizontalLayout.addWidget(self.GeneralInfoContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.TrainsCount.setText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.Info.setText(QCoreApplication.translate("MainWindow", u"# of Trains", None))
        self.Occupancy.setText(QCoreApplication.translate("MainWindow", u"Blocks Occupied", None))
        self.SectionLabel.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"GO TO INFO", None))
    # retranslateUi

