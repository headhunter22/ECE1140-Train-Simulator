# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testthis.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QPushButton,
    QSizePolicy, QWidget)

class Ui_test(object):
    def setupUi(self, test):
        if not test.objectName():
            test.setObjectName(u"test")
        test.resize(400, 300)
        self.horizontalLayoutWidget = QWidget(test)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(120, 20, 265, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.reda = QPushButton(self.horizontalLayoutWidget)
        self.reda.setObjectName(u"reda")

        self.horizontalLayout.addWidget(self.reda)

        self.yellowa = QPushButton(self.horizontalLayoutWidget)
        self.yellowa.setObjectName(u"yellowa")

        self.horizontalLayout.addWidget(self.yellowa)

        self.greena = QPushButton(self.horizontalLayoutWidget)
        self.greena.setObjectName(u"greena")

        self.horizontalLayout.addWidget(self.greena)

        self.horizontalLayoutWidget_2 = QWidget(test)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(120, 110, 265, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.redb = QPushButton(self.horizontalLayoutWidget_2)
        self.redb.setObjectName(u"redb")

        self.horizontalLayout_2.addWidget(self.redb)

        self.yellowb = QPushButton(self.horizontalLayoutWidget_2)
        self.yellowb.setObjectName(u"yellowb")

        self.horizontalLayout_2.addWidget(self.yellowb)

        self.greenb = QPushButton(self.horizontalLayoutWidget_2)
        self.greenb.setObjectName(u"greenb")

        self.horizontalLayout_2.addWidget(self.greenb)

        self.section = QComboBox(test)
        self.section.setObjectName(u"section")
        self.section.setGeometry(QRect(180, 210, 82, 28))
        self.block = QComboBox(test)
        self.block.setObjectName(u"block")
        self.block.setGeometry(QRect(300, 210, 82, 28))

        self.retranslateUi(test)

        QMetaObject.connectSlotsByName(test)
    # setupUi

    def retranslateUi(self, test):
        test.setWindowTitle(QCoreApplication.translate("test", u"Form", None))
        self.reda.setText(QCoreApplication.translate("test", u"reda", None))
        self.yellowa.setText(QCoreApplication.translate("test", u"yellowa", None))
        self.greena.setText(QCoreApplication.translate("test", u"greena", None))
        self.redb.setText(QCoreApplication.translate("test", u"redb", None))
        self.yellowb.setText(QCoreApplication.translate("test", u"yellowb", None))
        self.greenb.setText(QCoreApplication.translate("test", u"greenb", None))
    # retranslateUi

