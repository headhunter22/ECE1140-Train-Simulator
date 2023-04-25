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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(583, 277)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.WindowHeading = QLabel(self.centralwidget)
        self.WindowHeading.setObjectName(u"WindowHeading")
        self.WindowHeading.setGeometry(QRect(0, 0, 581, 51))
        self.WindowHeading.setStyleSheet(u"font-size: 25pt")
        self.WindowHeading.setAlignment(Qt.AlignCenter)
        self.LineHeading = QLabel(self.centralwidget)
        self.LineHeading.setObjectName(u"LineHeading")
        self.LineHeading.setGeometry(QRect(210, 50, 151, 51))
        self.LineHeading.setStyleSheet(u"font-size: 18pt;")
        self.LineHeading.setAlignment(Qt.AlignCenter)
        self.HLine = QFrame(self.centralwidget)
        self.HLine.setObjectName(u"HLine")
        self.HLine.setGeometry(QRect(0, 50, 581, 16))
        self.HLine.setFrameShape(QFrame.HLine)
        self.HLine.setFrameShadow(QFrame.Sunken)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 90, 561, 181))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.WindowHeading.setText(QCoreApplication.translate("MainWindow", u"Broken Rails", None))
        self.LineHeading.setText(QCoreApplication.translate("MainWindow", u"Locations", None))
    # retranslateUi

