# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TrackModelListView.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 801, 551))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.GenInfoLabel = QLabel(self.horizontalLayoutWidget)
        self.GenInfoLabel.setObjectName(u"GenInfoLabel")
        self.GenInfoLabel.setLineWidth(1)
        self.GenInfoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.GenInfoLabel)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.GreenLineLabel = QLabel(self.horizontalLayoutWidget)
        self.GreenLineLabel.setObjectName(u"GreenLineLabel")
        self.GreenLineLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.GreenLineLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.RedLineLabel = QLabel(self.horizontalLayoutWidget)
        self.RedLineLabel.setObjectName(u"RedLineLabel")
        self.RedLineLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.RedLineLabel)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.GenInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.GreenLineLabel.setText(QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"List", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Map", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Time: 1:53 PM", None))
        self.RedLineLabel.setText(QCoreApplication.translate("MainWindow", u"General Info", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Railroad Crossing Status", None))
    # retranslateUi

