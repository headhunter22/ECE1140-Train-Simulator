# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainTrackModel.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1154, 621)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.RedLineScrollArea = QScrollArea(self.centralwidget)
        self.RedLineScrollArea.setObjectName(u"RedLineScrollArea")
        self.RedLineScrollArea.setGeometry(QRect(0, 80, 411, 521))
        self.RedLineScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.RedLineScrollArea.setWidgetResizable(True)
        self.RedLineLabels = QWidget()
        self.RedLineLabels.setObjectName(u"RedLineLabels")
        self.RedLineLabels.setGeometry(QRect(0, 0, 409, 519))
        self.verticalLayout_3 = QVBoxLayout(self.RedLineLabels)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.T = QLabel(self.RedLineLabels)
        self.T.setObjectName(u"T")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T.sizePolicy().hasHeightForWidth())
        self.T.setSizePolicy(sizePolicy)
        self.T.setMinimumSize(QSize(0, 50))
        self.T.setScaledContents(False)

        self.verticalLayout_3.addWidget(self.T)

        self.RedLineScrollArea.setWidget(self.RedLineLabels)
        self.RedLineLabel = QLabel(self.centralwidget)
        self.RedLineLabel.setObjectName(u"RedLineLabel")
        self.RedLineLabel.setGeometry(QRect(110, 20, 191, 51))
        self.RedLineLabel.setStyleSheet(u"font-size: 20pt")
        self.RedLineLabel.setAlignment(Qt.AlignCenter)
        self.GreenLineLabel = QLabel(self.centralwidget)
        self.GreenLineLabel.setObjectName(u"GreenLineLabel")
        self.GreenLineLabel.setGeometry(QRect(510, 20, 191, 51))
        self.GreenLineLabel.setStyleSheet(u"font-size: 20pt")
        self.GreenLineLabel.setAlignment(Qt.AlignCenter)
        self.GreenLineScrollArea = QScrollArea(self.centralwidget)
        self.GreenLineScrollArea.setObjectName(u"GreenLineScrollArea")
        self.GreenLineScrollArea.setGeometry(QRect(420, 80, 411, 521))
        self.GreenLineScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.GreenLineScrollArea.setWidgetResizable(True)
        self.RedLineLabels_2 = QWidget()
        self.RedLineLabels_2.setObjectName(u"RedLineLabels_2")
        self.RedLineLabels_2.setGeometry(QRect(0, 0, 409, 519))
        self.verticalLayout_4 = QVBoxLayout(self.RedLineLabels_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.T_3 = QLabel(self.RedLineLabels_2)
        self.T_3.setObjectName(u"T_3")
        sizePolicy.setHeightForWidth(self.T_3.sizePolicy().hasHeightForWidth())
        self.T_3.setSizePolicy(sizePolicy)
        self.T_3.setMinimumSize(QSize(0, 50))
        self.T_3.setScaledContents(False)

        self.verticalLayout_4.addWidget(self.T_3)

        self.GreenLineScrollArea.setWidget(self.RedLineLabels_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.T.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.RedLineLabel.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.GreenLineLabel.setText(QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.T_3.setText(QCoreApplication.translate("MainWindow", u"T", None))
    # retranslateUi

