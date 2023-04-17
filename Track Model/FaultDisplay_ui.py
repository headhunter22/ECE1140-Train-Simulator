# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FaultDisplay.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(583, 186)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.WindowHeading = QLabel(self.centralwidget)
        self.WindowHeading.setObjectName(u"WindowHeading")
        self.WindowHeading.setGeometry(QRect(0, 0, 581, 51))
        self.WindowHeading.setStyleSheet(u"font-size: 25pt")
        self.WindowHeading.setAlignment(Qt.AlignCenter)
        self.LineHeading = QLabel(self.centralwidget)
        self.LineHeading.setObjectName(u"LineHeading")
        self.LineHeading.setGeometry(QRect(90, 50, 151, 51))
        self.LineHeading.setStyleSheet(u"font-size: 18pt;")
        self.LineHeading.setAlignment(Qt.AlignCenter)
        self.TypeHeading = QLabel(self.centralwidget)
        self.TypeHeading.setObjectName(u"TypeHeading")
        self.TypeHeading.setGeometry(QRect(340, 50, 241, 51))
        self.TypeHeading.setStyleSheet(u"font-size: 18pt;")
        self.TypeHeading.setAlignment(Qt.AlignCenter)
        self.HLine = QFrame(self.centralwidget)
        self.HLine.setObjectName(u"HLine")
        self.HLine.setGeometry(QRect(0, 50, 581, 16))
        self.HLine.setFrameShape(QFrame.HLine)
        self.HLine.setFrameShadow(QFrame.Sunken)
        self.RightVLine = QFrame(self.centralwidget)
        self.RightVLine.setObjectName(u"RightVLine")
        self.RightVLine.setGeometry(QRect(330, 60, 20, 121))
        self.RightVLine.setFrameShape(QFrame.VLine)
        self.RightVLine.setFrameShadow(QFrame.Sunken)
        self.FaultLabel = QLabel(self.centralwidget)
        self.FaultLabel.setObjectName(u"FaultLabel")
        self.FaultLabel.setGeometry(QRect(340, 110, 241, 61))
        self.FaultLabel.setStyleSheet(u"font-size:15pt")
        self.FaultLabel.setAlignment(Qt.AlignCenter)
        self.FaultSelect = QComboBox(self.centralwidget)
        self.FaultSelect.addItem("")
        self.FaultSelect.addItem("")
        self.FaultSelect.addItem("")
        self.FaultSelect.setObjectName(u"FaultSelect")
        self.FaultSelect.setGeometry(QRect(352, 120, 221, 32))
        self.LocationLabel = QLabel(self.centralwidget)
        self.LocationLabel.setObjectName(u"LocationLabel")
        self.LocationLabel.setGeometry(QRect(10, 120, 311, 21))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.WindowHeading.setText(QCoreApplication.translate("MainWindow", u"Track Faults", None))
        self.LineHeading.setText(QCoreApplication.translate("MainWindow", u"Locations", None))
        self.TypeHeading.setText(QCoreApplication.translate("MainWindow", u"Fault Type", None))
        self.FaultLabel.setText("")
        self.FaultSelect.setItemText(0, QCoreApplication.translate("MainWindow", u"Power", None))
        self.FaultSelect.setItemText(1, QCoreApplication.translate("MainWindow", u"Broken Rail", None))
        self.FaultSelect.setItemText(2, QCoreApplication.translate("MainWindow", u"Broken Circuit", None))

        self.LocationLabel.setText("")
    # retranslateUi

