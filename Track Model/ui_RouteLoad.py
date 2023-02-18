# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RouteLoad.ui'
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
        MainWindow.resize(555, 176)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.UploadHeading = QLabel(self.centralwidget)
        self.UploadHeading.setObjectName(u"UploadHeading")
        self.UploadHeading.setGeometry(QRect(0, 10, 551, 51))
        self.UploadHeading.setStyleSheet(u"font-size: 25pt; background-color: grey")
        self.UploadHeading.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 80, 81, 81))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(440, 80, 100, 81))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 80, 301, 81))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.UploadHeading.setText(QCoreApplication.translate("MainWindow", u"Upload Track Layout", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
    # retranslateUi

