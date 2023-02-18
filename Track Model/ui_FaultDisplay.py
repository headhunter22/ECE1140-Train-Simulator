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
        self.LineHeading.setGeometry(QRect(0, 60, 151, 51))
        self.LineHeading.setStyleSheet(u"font-size: 18pt;")
        self.LineHeading.setAlignment(Qt.AlignCenter)
        self.BlockHeading = QLabel(self.centralwidget)
        self.BlockHeading.setObjectName(u"BlockHeading")
        self.BlockHeading.setGeometry(QRect(150, 60, 181, 51))
        self.BlockHeading.setStyleSheet(u"font-size: 18pt;")
        self.BlockHeading.setAlignment(Qt.AlignCenter)
        self.TypeHeading = QLabel(self.centralwidget)
        self.TypeHeading.setObjectName(u"TypeHeading")
        self.TypeHeading.setGeometry(QRect(340, 60, 241, 51))
        self.TypeHeading.setStyleSheet(u"font-size: 18pt;")
        self.TypeHeading.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(140, 60, 20, 121))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 50, 581, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(330, 60, 20, 121))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.LineSelect = QComboBox(self.centralwidget)
        self.LineSelect.setObjectName(u"LineSelect")
        self.LineSelect.setGeometry(QRect(30, 120, 103, 32))
        self.BlockSelect = QComboBox(self.centralwidget)
        self.BlockSelect.setObjectName(u"BlockSelect")
        self.BlockSelect.setGeometry(QRect(190, 120, 103, 32))
        self.FaultLabel = QLabel(self.centralwidget)
        self.FaultLabel.setObjectName(u"FaultLabel")
        self.FaultLabel.setGeometry(QRect(340, 110, 241, 61))
        self.FaultLabel.setStyleSheet(u"font-size:15pt")
        self.FaultLabel.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.WindowHeading.setText(QCoreApplication.translate("MainWindow", u"Track Faults", None))
        self.LineHeading.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.BlockHeading.setText(QCoreApplication.translate("MainWindow", u"Block", None))
        self.TypeHeading.setText(QCoreApplication.translate("MainWindow", u"Fault Type", None))
        self.FaultLabel.setText(QCoreApplication.translate("MainWindow", u"Fault_Text", None))
    # retranslateUi

