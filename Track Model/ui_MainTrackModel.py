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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QScrollArea, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1154, 621)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.RedLineScrollArea = QScrollArea(self.centralwidget)
        self.RedLineScrollArea.setObjectName(u"RedLineScrollArea")
        self.RedLineScrollArea.setGeometry(QRect(0, 120, 411, 481))
        self.RedLineScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.RedLineScrollArea.setWidgetResizable(True)
        self.RedLineLabels = QWidget()
        self.RedLineLabels.setObjectName(u"RedLineLabels")
        self.RedLineLabels.setGeometry(QRect(0, 0, 409, 479))
        self.RedLineScrollArea.setWidget(self.RedLineLabels)
        self.RedLineLabel = QLabel(self.centralwidget)
        self.RedLineLabel.setObjectName(u"RedLineLabel")
        self.RedLineLabel.setGeometry(QRect(110, 20, 191, 51))
        self.RedLineLabel.setStyleSheet(u"font-size: 20pt")
        self.RedLineLabel.setAlignment(Qt.AlignCenter)
        self.GreenLineLabel = QLabel(self.centralwidget)
        self.GreenLineLabel.setObjectName(u"GreenLineLabel")
        self.GreenLineLabel.setGeometry(QRect(550, 20, 191, 51))
        self.GreenLineLabel.setStyleSheet(u"font-size: 20pt")
        self.GreenLineLabel.setAlignment(Qt.AlignCenter)
        self.GreenLineScrollArea = QScrollArea(self.centralwidget)
        self.GreenLineScrollArea.setObjectName(u"GreenLineScrollArea")
        self.GreenLineScrollArea.setGeometry(QRect(440, 120, 411, 481))
        self.GreenLineScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.GreenLineScrollArea.setWidgetResizable(True)
        self.RedLineLabels_2 = QWidget()
        self.RedLineLabels_2.setObjectName(u"RedLineLabels_2")
        self.RedLineLabels_2.setGeometry(QRect(0, 0, 409, 479))
        self.GreenLineScrollArea.setWidget(self.RedLineLabels_2)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 60, 401, 51))
        self.RedLineHeadersLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.RedLineHeadersLayout.setObjectName(u"RedLineHeadersLayout")
        self.RedLineHeadersLayout.setContentsMargins(0, 0, 0, 0)
        self.RedSection = QLabel(self.horizontalLayoutWidget)
        self.RedSection.setObjectName(u"RedSection")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RedSection.sizePolicy().hasHeightForWidth())
        self.RedSection.setSizePolicy(sizePolicy)
        self.RedSection.setMinimumSize(QSize(75, 0))
        self.RedSection.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout.addWidget(self.RedSection)

        self.RedTrainCount = QLabel(self.horizontalLayoutWidget)
        self.RedTrainCount.setObjectName(u"RedTrainCount")
        sizePolicy.setHeightForWidth(self.RedTrainCount.sizePolicy().hasHeightForWidth())
        self.RedTrainCount.setSizePolicy(sizePolicy)
        self.RedTrainCount.setMinimumSize(QSize(75, 0))
        self.RedTrainCount.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout.addWidget(self.RedTrainCount)

        self.RedOcc = QLabel(self.horizontalLayoutWidget)
        self.RedOcc.setObjectName(u"RedOcc")
        sizePolicy.setHeightForWidth(self.RedOcc.sizePolicy().hasHeightForWidth())
        self.RedOcc.setSizePolicy(sizePolicy)
        self.RedOcc.setMinimumSize(QSize(150, 0))
        self.RedOcc.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout.addWidget(self.RedOcc)

        self.RedInfo = QLabel(self.horizontalLayoutWidget)
        self.RedInfo.setObjectName(u"RedInfo")
        sizePolicy.setHeightForWidth(self.RedInfo.sizePolicy().hasHeightForWidth())
        self.RedInfo.setSizePolicy(sizePolicy)
        self.RedInfo.setMinimumSize(QSize(50, 0))
        self.RedInfo.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout.addWidget(self.RedInfo)

        self.Spacer1 = QFrame(self.centralwidget)
        self.Spacer1.setObjectName(u"Spacer1")
        self.Spacer1.setGeometry(QRect(420, 0, 16, 621))
        self.Spacer1.setFrameShape(QFrame.VLine)
        self.Spacer1.setFrameShadow(QFrame.Sunken)
        self.Spacer2 = QFrame(self.centralwidget)
        self.Spacer2.setObjectName(u"Spacer2")
        self.Spacer2.setGeometry(QRect(860, 0, 16, 621))
        self.Spacer2.setFrameShape(QFrame.VLine)
        self.Spacer2.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(440, 60, 411, 51))
        self.RedLineHeadersLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.RedLineHeadersLayout_2.setObjectName(u"RedLineHeadersLayout_2")
        self.RedLineHeadersLayout_2.setContentsMargins(0, 0, 0, 0)
        self.GreenSection = QLabel(self.horizontalLayoutWidget_3)
        self.GreenSection.setObjectName(u"GreenSection")
        sizePolicy.setHeightForWidth(self.GreenSection.sizePolicy().hasHeightForWidth())
        self.GreenSection.setSizePolicy(sizePolicy)
        self.GreenSection.setMinimumSize(QSize(75, 0))
        self.GreenSection.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout_2.addWidget(self.GreenSection)

        self.GreenTrainCount = QLabel(self.horizontalLayoutWidget_3)
        self.GreenTrainCount.setObjectName(u"GreenTrainCount")
        sizePolicy.setHeightForWidth(self.GreenTrainCount.sizePolicy().hasHeightForWidth())
        self.GreenTrainCount.setSizePolicy(sizePolicy)
        self.GreenTrainCount.setMinimumSize(QSize(75, 0))
        self.GreenTrainCount.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout_2.addWidget(self.GreenTrainCount)

        self.GreenOcc = QLabel(self.horizontalLayoutWidget_3)
        self.GreenOcc.setObjectName(u"GreenOcc")
        sizePolicy.setHeightForWidth(self.GreenOcc.sizePolicy().hasHeightForWidth())
        self.GreenOcc.setSizePolicy(sizePolicy)
        self.GreenOcc.setMinimumSize(QSize(150, 0))
        self.GreenOcc.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout_2.addWidget(self.GreenOcc)

        self.GreenInfo = QLabel(self.horizontalLayoutWidget_3)
        self.GreenInfo.setObjectName(u"GreenInfo")
        sizePolicy.setHeightForWidth(self.GreenInfo.sizePolicy().hasHeightForWidth())
        self.GreenInfo.setSizePolicy(sizePolicy)
        self.GreenInfo.setMinimumSize(QSize(50, 0))
        self.GreenInfo.setAlignment(Qt.AlignCenter)

        self.RedLineHeadersLayout_2.addWidget(self.GreenInfo)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.RedLineLabel.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.GreenLineLabel.setText(QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.RedSection.setText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.RedTrainCount.setText(QCoreApplication.translate("MainWindow", u"# of Trains", None))
        self.RedOcc.setText(QCoreApplication.translate("MainWindow", u"Blocks Occcupied", None))
        self.RedInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.GreenSection.setText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.GreenTrainCount.setText(QCoreApplication.translate("MainWindow", u"# of Trains", None))
        self.GreenOcc.setText(QCoreApplication.translate("MainWindow", u"Blocks Occcupied", None))
        self.GreenInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
    # retranslateUi

