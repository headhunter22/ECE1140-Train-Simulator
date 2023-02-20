# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WaysideMain.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLCDNumber, QLabel,
    QMainWindow, QMenuBar, QPushButton, QScrollBar,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 430, 221, 29))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(310, 460, 221, 29))
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 11):
            self.tableWidget.setRowCount(11)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(5, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(6, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(7, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(8, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(9, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(10, 0, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 50, 261, 441))
        self.verticalScrollBar = QScrollBar(self.centralwidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(280, 50, 16, 441))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.lcdNumber = QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(20, 0, 64, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 201, 20))
        self.lcdNumber_2 = QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(160, 0, 64, 23))
        self.tableWidget_2 = QTableWidget(self.centralwidget)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        if (self.tableWidget_2.rowCount() < 4):
            self.tableWidget_2.setRowCount(4)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 0, __qtablewidgetitem33)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(310, 140, 256, 181))
        self.tableWidget_3 = QTableWidget(self.centralwidget)
        if (self.tableWidget_3.columnCount() < 3):
            self.tableWidget_3.setColumnCount(3)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem36)
        if (self.tableWidget_3.rowCount() < 2):
            self.tableWidget_3.setRowCount(2)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, __qtablewidgetitem40)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(310, 320, 381, 101))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Track Configuration", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Maintenance", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Section", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"A", None));
        ___qtablewidgetitem3 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"B", None));
        ___qtablewidgetitem4 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"C", None));
        ___qtablewidgetitem5 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"D", None));
        ___qtablewidgetitem6 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"E", None));
        ___qtablewidgetitem7 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"F", None));
        ___qtablewidgetitem8 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"G", None));
        ___qtablewidgetitem9 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"H", None));
        ___qtablewidgetitem10 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"I", None));
        ___qtablewidgetitem11 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"J", None));
        ___qtablewidgetitem12 = self.tableWidget.item(10, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"K", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"Sections Managed: A-L", None))
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Switch", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Direction", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem15 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"c", None));
        ___qtablewidgetitem16 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"G", None));
        ___qtablewidgetitem17 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"J", None));
        ___qtablewidgetitem18 = self.tableWidget_2.item(3, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"J", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        ___qtablewidgetitem19 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Gates", None));
        ___qtablewidgetitem20 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem21 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Lights", None));

        __sortingEnabled2 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        ___qtablewidgetitem22 = self.tableWidget_3.item(0, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem23 = self.tableWidget_3.item(1, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"2", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled2)

    # retranslateUi

