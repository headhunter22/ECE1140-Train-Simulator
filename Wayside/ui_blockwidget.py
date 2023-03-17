# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'blockwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Section(object):
    def setupUi(self, Section):
        if not Section.objectName():
            Section.setObjectName(u"Section")
        Section.resize(476, 415)
        self.gridLayoutWidget = QWidget(Section)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 455, 371))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.aicon = QLabel(self.gridLayoutWidget)
        self.aicon.setObjectName(u"aicon")
        self.aicon.setMaximumSize(QSize(50, 50))
        self.aicon.setPixmap(QPixmap(u"tracks.png"))
        self.aicon.setScaledContents(True)
        self.aicon.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.aicon, 1, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")

        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)

        self.bicon = QLabel(self.gridLayoutWidget)
        self.bicon.setObjectName(u"bicon")
        self.bicon.setMaximumSize(QSize(50, 50))
        self.bicon.setPixmap(QPixmap(u"redtrain.png"))
        self.bicon.setScaledContents(True)
        self.bicon.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.bicon, 2, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.cicon = QLabel(self.gridLayoutWidget)
        self.cicon.setObjectName(u"cicon")
        self.cicon.setMaximumSize(QSize(50, 50))
        self.cicon.setPixmap(QPixmap(u"tracks.png"))
        self.cicon.setScaledContents(True)
        self.cicon.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.cicon, 3, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 700 14pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.sectionname = QLabel(self.gridLayoutWidget)
        self.sectionname.setObjectName(u"sectionname")
        self.sectionname.setStyleSheet(u"font: 700 14pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.sectionname.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.sectionname, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 700 14pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 700 14pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);\n"
"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")

        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)

        self.dicon = QLabel(self.gridLayoutWidget)
        self.dicon.setObjectName(u"dicon")
        self.dicon.setMaximumSize(QSize(50, 50))
        self.dicon.setPixmap(QPixmap(u"tracks.png"))
        self.dicon.setScaledContents(True)
        self.dicon.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.dicon, 4, 1, 1, 1)

        self.eicon = QLabel(self.gridLayoutWidget)
        self.eicon.setObjectName(u"eicon")
        self.eicon.setMaximumSize(QSize(50, 50))
        self.eicon.setPixmap(QPixmap(u"tracks.png"))
        self.eicon.setScaledContents(True)
        self.eicon.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.eicon, 5, 1, 1, 1)


        self.retranslateUi(Section)

        QMetaObject.connectSlotsByName(Section)
    # setupUi

    def retranslateUi(self, Section):
        Section.setWindowTitle(QCoreApplication.translate("Section", u"Form", None))
        self.aicon.setText("")
        self.label_8.setText(QCoreApplication.translate("Section", u"4", None))
        self.bicon.setText("")
        self.label_6.setText(QCoreApplication.translate("Section", u"2", None))
        self.cicon.setText("")
        self.label_2.setText(QCoreApplication.translate("Section", u"Occupation", None))
        self.sectionname.setText(QCoreApplication.translate("Section", u"Section A", None))
        self.label_3.setText(QCoreApplication.translate("Section", u"Switch", None))
        self.label_4.setText(QCoreApplication.translate("Section", u"Crossing", None))
        self.label_7.setText(QCoreApplication.translate("Section", u"3", None))
        self.label_5.setText(QCoreApplication.translate("Section", u"1", None))
        self.label_9.setText(QCoreApplication.translate("Section", u"5", None))
        self.dicon.setText("")
        self.eicon.setText("")
    # retranslateUi

