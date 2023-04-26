# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fullsystem.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(262, 614)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.trainModel = QPushButton(self.centralwidget)
        self.trainModel.setObjectName(u"trainModel")
        self.trainModel.setGeometry(QRect(20, 240, 111, 101))
        self.ctcOffice = QPushButton(self.centralwidget)
        self.ctcOffice.setObjectName(u"ctcOffice")
        self.ctcOffice.setGeometry(QRect(20, 20, 111, 101))
        self.waysideController = QPushButton(self.centralwidget)
        self.waysideController.setObjectName(u"waysideController")
        self.waysideController.setGeometry(QRect(20, 130, 111, 101))
        self.trainController = QPushButton(self.centralwidget)
        self.trainController.setObjectName(u"trainController")
        self.trainController.setGeometry(QRect(20, 460, 111, 101))
        self.trackModel = QPushButton(self.centralwidget)
        self.trackModel.setObjectName(u"trackModel")
        self.trackModel.setGeometry(QRect(20, 350, 111, 101))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 40, 91, 61))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 150, 101, 61))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 260, 91, 61))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 370, 81, 61))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 480, 91, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 262, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.trainModel.setText(QCoreApplication.translate("MainWindow", u"Train Model", None))
        self.ctcOffice.setText(QCoreApplication.translate("MainWindow", u"CTC Office", None))
        self.waysideController.setText(QCoreApplication.translate("MainWindow", u"Wayside Controller", None))
        self.trainController.setText(QCoreApplication.translate("MainWindow", u"Train Controller", None))
        self.trackModel.setText(QCoreApplication.translate("MainWindow", u"Track Model", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Adam Kort\n"
"ajk179@pitt.edu\n"
"814-873-1543", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mikayle Bernhard\n"
"meb291@pitt.edu\n"
"724-504-7402", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Jacob Kerstetter\n"
"jrk154@pitt.edu\n"
"484-844-5082", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Lauren Duffitt\n"
"ljd52@pitt.edu\n"
"717-742-8966", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Jason Head\n"
"jdh161@pitt.edu\n"
"734-730-8183", None))
    # retranslateUi

