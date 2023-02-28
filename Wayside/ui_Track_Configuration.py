# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Track_Configuration.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_TrackConfig(object):
    def setupUi(self, TrackConfig):
        if not TrackConfig.objectName():
            TrackConfig.setObjectName(u"TrackConfig")
        TrackConfig.resize(658, 689)
        self.centralwidget = QWidget(TrackConfig)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 621, 577))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.ladderlogic = QPushButton(self.verticalLayoutWidget)
        self.ladderlogic.setObjectName(u"ladderlogic")
        self.ladderlogic.setStyleSheet(u"font: 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 170, 170);")

        self.horizontalLayout_10.addWidget(self.ladderlogic)

        self.functionblocklogic = QPushButton(self.verticalLayoutWidget)
        self.functionblocklogic.setObjectName(u"functionblocklogic")
        self.functionblocklogic.setStyleSheet(u"font: 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 170, 170);")

        self.horizontalLayout_10.addWidget(self.functionblocklogic)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(31, 31))
        self.label.setPixmap(QPixmap(u"pencil.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(41, 31))
        self.label_6.setStyleSheet(u"font: 700 16pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_6)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(31, 31))
        self.label_2.setPixmap(QPixmap(u"parallel.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(41, 31))
        self.label_3.setPixmap(QPixmap(u"halfcircle.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(41, 41))
        self.label_5.setPixmap(QPixmap(u"slash.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.plcdisplay = QLabel(self.verticalLayoutWidget)
        self.plcdisplay.setObjectName(u"plcdisplay")
        self.plcdisplay.setPixmap(QPixmap(u"ladderlogic.png"))

        self.verticalLayout.addWidget(self.plcdisplay)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(20, 590, 621, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.uploadplc = QPushButton(self.horizontalLayoutWidget_4)
        self.uploadplc.setObjectName(u"uploadplc")

        self.horizontalLayout_2.addWidget(self.uploadplc)

        self.label_7 = QLabel(self.horizontalLayoutWidget_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.cancel = QPushButton(self.horizontalLayoutWidget_4)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_2.addWidget(self.cancel)

        self.save = QPushButton(self.horizontalLayoutWidget_4)
        self.save.setObjectName(u"save")

        self.horizontalLayout_2.addWidget(self.save)

        TrackConfig.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(TrackConfig)
        self.statusbar.setObjectName(u"statusbar")
        TrackConfig.setStatusBar(self.statusbar)

        self.retranslateUi(TrackConfig)
        self.uploadplc.clicked.connect(TrackConfig.show)
        self.cancel.clicked.connect(TrackConfig.close)
        self.save.clicked.connect(TrackConfig.close)

        QMetaObject.connectSlotsByName(TrackConfig)
    # setupUi

    def retranslateUi(self, TrackConfig):
        TrackConfig.setWindowTitle(QCoreApplication.translate("TrackConfig", u"MainWindow", None))
        self.ladderlogic.setText(QCoreApplication.translate("TrackConfig", u"Ladder Logic", None))
        self.functionblocklogic.setText(QCoreApplication.translate("TrackConfig", u"Function Block Logic", None))
        self.label.setText("")
        self.label_6.setText(QCoreApplication.translate("TrackConfig", u"T", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_5.setText("")
        self.plcdisplay.setText("")
        self.uploadplc.setText(QCoreApplication.translate("TrackConfig", u"Upload PLC", None))
        self.label_7.setText("")
        self.cancel.setText(QCoreApplication.translate("TrackConfig", u"Cancel", None))
        self.save.setText(QCoreApplication.translate("TrackConfig", u"Save", None))
    # retranslateUi

