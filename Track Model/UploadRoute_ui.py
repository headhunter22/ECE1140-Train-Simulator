# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UploadRoute.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(667, 102)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Heading = QLabel(self.centralwidget)
        self.Heading.setObjectName(u"Heading")
        self.Heading.setGeometry(QRect(0, 10, 661, 31))
        self.Heading.setStyleSheet(u"font-size: 20px")
        self.Heading.setAlignment(Qt.AlignCenter)
        self.GoButton = QPushButton(self.centralwidget)
        self.GoButton.setObjectName(u"GoButton")
        self.GoButton.setGeometry(QRect(410, 60, 100, 32))
        self.CancelButton = QPushButton(self.centralwidget)
        self.CancelButton.setObjectName(u"CancelButton")
        self.CancelButton.setGeometry(QRect(530, 60, 100, 32))
        self.SelectFileButton = QPushButton(self.centralwidget)
        self.SelectFileButton.setObjectName(u"SelectFileButton")
        self.SelectFileButton.setGeometry(QRect(10, 60, 351, 32))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Heading.setText(QCoreApplication.translate("MainWindow", u"Upload Track Layout", None))
        self.GoButton.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.CancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.SelectFileButton.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
    # retranslateUi

