# Form implementation generated from reading ui file 'Wayside_Main_A.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindowA(object):
    def setupUi(self, MainWindowA):
        MainWindowA.setObjectName("MainWindowA")
        MainWindowA.resize(642, 715)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindowA)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 624, 661))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.whichwayside = QtWidgets.QComboBox(parent=self.verticalLayoutWidget_2)
        self.whichwayside.setObjectName("whichwayside")
        self.whichwayside.addItem("")
        self.whichwayside.addItem("")
        self.whichwayside.addItem("")
        self.whichwayside.addItem("")
        self.verticalLayout_5.addWidget(self.whichwayside)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(0, -1, 9, -1)
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.qicon = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.qicon.setMaximumSize(QtCore.QSize(50, 50))
        self.qicon.setText("")
        self.qicon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.qicon.setScaledContents(True)
        self.qicon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.qicon.setObjectName("qicon")
        self.gridLayout_4.addWidget(self.qicon, 5, 1, 1, 1)
        self.nicon = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.nicon.setMaximumSize(QtCore.QSize(50, 50))
        self.nicon.setText("")
        self.nicon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.nicon.setScaledContents(True)
        self.nicon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.nicon.setObjectName("nicon")
        self.gridLayout_4.addWidget(self.nicon, 2, 1, 1, 1)
        self.pushu = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushu.setObjectName("pushu")
        self.gridLayout_4.addWidget(self.pushu, 9, 0, 1, 1)
        self.pushv = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushv.setObjectName("pushv")
        self.gridLayout_4.addWidget(self.pushv, 10, 0, 1, 1)
        self.pushx = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushx.setObjectName("pushx")
        self.gridLayout_4.addWidget(self.pushx, 12, 0, 1, 1)
        self.pushy = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushy.setObjectName("pushy")
        self.gridLayout_4.addWidget(self.pushy, 13, 0, 1, 1)
        self.yicon = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.yicon.setMaximumSize(QtCore.QSize(50, 50))
        self.yicon.setText("")
        self.yicon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.yicon.setScaledContents(True)
        self.yicon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.yicon.setObjectName("yicon")
        self.gridLayout_4.addWidget(self.yicon, 13, 1, 1, 1)
        self.pusho = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pusho.setObjectName("pusho")
        self.gridLayout_4.addWidget(self.pusho, 3, 0, 1, 1)
        self.ticon = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.ticon.setMaximumSize(QtCore.QSize(50, 50))
        self.ticon.setText("")
        self.ticon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.ticon.setScaledContents(True)
        self.ticon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ticon.setObjectName("ticon")
        self.gridLayout_4.addWidget(self.ticon, 8, 1, 1, 1)
        self.vicon = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.vicon.setMaximumSize(QtCore.QSize(50, 50))
        self.vicon.setText("")
        self.vicon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.vicon.setScaledContents(True)
        self.vicon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.vicon.setObjectName("vicon")
        self.gridLayout_4.addWidget(self.vicon, 10, 1, 1, 1)
        self.ricon = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.ricon.setMaximumSize(QtCore.QSize(50, 50))
        self.ricon.setText("")
        self.ricon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.ricon.setScaledContents(True)
        self.ricon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ricon.setObjectName("ricon")
        self.gridLayout_4.addWidget(self.ricon, 6, 1, 1, 1)
        self.sicon = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.sicon.setMaximumSize(QtCore.QSize(50, 50))
        self.sicon.setText("")
        self.sicon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.sicon.setScaledContents(True)
        self.sicon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sicon.setObjectName("sicon")
        self.gridLayout_4.addWidget(self.sicon, 7, 1, 1, 1)
        self.picon = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.picon.setMaximumSize(QtCore.QSize(50, 50))
        self.picon.setText("")
        self.picon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.picon.setScaledContents(True)
        self.picon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.picon.setObjectName("picon")
        self.gridLayout_4.addWidget(self.picon, 4, 1, 1, 1)
        self.sectiontitle_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.sectiontitle_2.setStyleSheet("font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.sectiontitle_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sectiontitle_2.setObjectName("sectiontitle_2")
        self.gridLayout_4.addWidget(self.sectiontitle_2, 1, 0, 1, 1)
        self.pushr = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushr.setObjectName("pushr")
        self.gridLayout_4.addWidget(self.pushr, 6, 0, 1, 1)
        self.xicon = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.xicon.setMaximumSize(QtCore.QSize(50, 50))
        self.xicon.setText("")
        self.xicon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.xicon.setScaledContents(True)
        self.xicon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.xicon.setObjectName("xicon")
        self.gridLayout_4.addWidget(self.xicon, 12, 1, 1, 1)
        self.occupancylabel_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.occupancylabel_2.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.occupancylabel_2.setObjectName("occupancylabel_2")
        self.gridLayout_4.addWidget(self.occupancylabel_2, 1, 1, 1, 1)
        self.pushp = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushp.setObjectName("pushp")
        self.gridLayout_4.addWidget(self.pushp, 4, 0, 1, 1)
        self.pushs = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushs.setObjectName("pushs")
        self.gridLayout_4.addWidget(self.pushs, 7, 0, 1, 1)
        self.pushn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushn.setObjectName("pushn")
        self.gridLayout_4.addWidget(self.pushn, 2, 0, 1, 1)
        self.uicon = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.uicon.setMaximumSize(QtCore.QSize(50, 50))
        self.uicon.setText("")
        self.uicon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.uicon.setScaledContents(True)
        self.uicon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.uicon.setObjectName("uicon")
        self.gridLayout_4.addWidget(self.uicon, 9, 1, 1, 1)
        self.pushq = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushq.setObjectName("pushq")
        self.gridLayout_4.addWidget(self.pushq, 5, 0, 1, 1)
        self.pusht = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pusht.setObjectName("pusht")
        self.gridLayout_4.addWidget(self.pusht, 8, 0, 1, 1)
        self.oicon = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.oicon.setMaximumSize(QtCore.QSize(50, 50))
        self.oicon.setText("")
        self.oicon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.oicon.setScaledContents(True)
        self.oicon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.oicon.setObjectName("oicon")
        self.gridLayout_4.addWidget(self.oicon, 3, 1, 1, 1)
        self.pushw = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushw.setObjectName("pushw")
        self.gridLayout_4.addWidget(self.pushw, 11, 0, 1, 1)
        self.zicon = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.zicon.setMaximumSize(QtCore.QSize(50, 50))
        self.zicon.setText("")
        self.zicon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.zicon.setScaledContents(True)
        self.zicon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.zicon.setObjectName("zicon")
        self.gridLayout_4.addWidget(self.zicon, 14, 1, 1, 1)
        self.pushz = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.pushz.setObjectName("pushz")
        self.gridLayout_4.addWidget(self.pushz, 14, 0, 1, 1)
        self.wicon = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.wicon.setMaximumSize(QtCore.QSize(50, 50))
        self.wicon.setText("")
        self.wicon.setPixmap(QtGui.QPixmap("tracks.png"))
        self.wicon.setScaledContents(True)
        self.wicon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wicon.setObjectName("wicon")
        self.gridLayout_4.addWidget(self.wicon, 11, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.line_7 = QtWidgets.QFrame(parent=self.verticalLayoutWidget_2)
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_6.addWidget(self.line_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_5.setStyleSheet("font: 700 13pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_6.setStyleSheet("font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_7.setStyleSheet("font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.line_4 = QtWidgets.QFrame(parent=self.verticalLayoutWidget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line = QtWidgets.QFrame(parent=self.verticalLayoutWidget_2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.time = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.time.setStyleSheet("font: 700 18pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.time.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.time.setObjectName("time")
        self.verticalLayout_2.addWidget(self.time)
        self.line_6 = QtWidgets.QFrame(parent=self.verticalLayoutWidget_2)
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_2.addWidget(self.line_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_18 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_18.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_7.addWidget(self.label_18)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_13 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_13.setStyleSheet("font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_11.addWidget(self.label_13)
        self.gate20 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.gate20.setCheckable(False)
        self.gate20.setObjectName("gate20")
        self.horizontalLayout_11.addWidget(self.gate20)
        self.gate21 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.gate21.setObjectName("gate21")
        self.horizontalLayout_11.addWidget(self.gate21)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_14 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_14.setStyleSheet("font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_14.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.gate50 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.gate50.setCheckable(False)
        self.gate50.setObjectName("gate50")
        self.horizontalLayout.addWidget(self.gate50)
        self.gate51 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.gate51.setObjectName("gate51")
        self.horizontalLayout.addWidget(self.gate51)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_15 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_15.setStyleSheet("font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_15.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.gate60 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.gate60.setCheckable(False)
        self.gate60.setObjectName("gate60")
        self.horizontalLayout_2.addWidget(self.gate60)
        self.gate61 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.gate61.setObjectName("gate61")
        self.horizontalLayout_2.addWidget(self.gate61)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.line_2 = QtWidgets.QFrame(parent=self.verticalLayoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_9.addWidget(self.line_2)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_50 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_50.setStyleSheet("background-color: rgb(221, 221, 221);\n"
"font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_50.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.horizontalLayout_26.addWidget(self.label_50)
        self.label_51 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_51.setStyleSheet("font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.label_51.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_26.addWidget(self.label_51)
        self.label_52 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_52.setStyleSheet("font: 700 12pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(221, 221, 221);")
        self.label_52.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.horizontalLayout_26.addWidget(self.label_52)
        self.verticalLayout_9.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_53 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_53.setStyleSheet("font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.label_53.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.horizontalLayout_20.addWidget(self.label_53)
        self.gatepositiona = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.gatepositiona.setStyleSheet("font: 9pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.gatepositiona.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.gatepositiona.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gatepositiona.setObjectName("gatepositiona")
        self.horizontalLayout_20.addWidget(self.gatepositiona)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.reda = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.reda.setMaximumSize(QtCore.QSize(21, 21))
        self.reda.setText("")
        self.reda.setPixmap(QtGui.QPixmap("greenlight.png"))
        self.reda.setScaledContents(True)
        self.reda.setObjectName("reda")
        self.horizontalLayout_27.addWidget(self.reda)
        self.yellowa = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.yellowa.setMaximumSize(QtCore.QSize(21, 21))
        self.yellowa.setText("")
        self.yellowa.setPixmap(QtGui.QPixmap("offlight.png"))
        self.yellowa.setScaledContents(True)
        self.yellowa.setObjectName("yellowa")
        self.horizontalLayout_27.addWidget(self.yellowa)
        self.greena = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.greena.setMaximumSize(QtCore.QSize(21, 21))
        self.greena.setText("")
        self.greena.setPixmap(QtGui.QPixmap("offlight.png"))
        self.greena.setScaledContents(True)
        self.greena.setObjectName("greena")
        self.horizontalLayout_27.addWidget(self.greena)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_27)
        self.verticalLayout_9.addLayout(self.horizontalLayout_20)
        self.line_5 = QtWidgets.QFrame(parent=self.verticalLayoutWidget_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_9.addWidget(self.line_5)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.activetrainlabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.activetrainlabel.setStyleSheet("font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);")
        self.activetrainlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.activetrainlabel.setObjectName("activetrainlabel")
        self.horizontalLayout_16.addWidget(self.activetrainlabel)
        self.activetrains = QtWidgets.QLCDNumber(parent=self.verticalLayoutWidget_2)
        self.activetrains.setObjectName("activetrains")
        self.horizontalLayout_16.addWidget(self.activetrains)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        self.verticalLayout_3.addLayout(self.verticalLayout_9)
        self.line_8 = QtWidgets.QFrame(parent=self.verticalLayoutWidget_2)
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_3.addWidget(self.line_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.automaticmode = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.automaticmode.setStyleSheet("font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.automaticmode.setObjectName("automaticmode")
        self.horizontalLayout_4.addWidget(self.automaticmode)
        self.maintenancemode = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.maintenancemode.setStyleSheet("font: 700 10pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.maintenancemode.setObjectName("maintenancemode")
        self.horizontalLayout_4.addWidget(self.maintenancemode)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.line_3 = QtWidgets.QFrame(parent=self.verticalLayoutWidget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.trackconfiguration = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.trackconfiguration.setStyleSheet("font: 9pt \"Georgia\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.trackconfiguration.setObjectName("trackconfiguration")
        self.verticalLayout_3.addWidget(self.trackconfiguration)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        MainWindowA.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindowA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 25))
        self.menubar.setObjectName("menubar")
        MainWindowA.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindowA)
        self.statusbar.setObjectName("statusbar")
        MainWindowA.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowA)
        QtCore.QMetaObject.connectSlotsByName(MainWindowA)

    def retranslateUi(self, MainWindowA):
        _translate = QtCore.QCoreApplication.translate
        MainWindowA.setWindowTitle(_translate("MainWindowA", "Wayside"))
        self.whichwayside.setPlaceholderText(_translate("MainWindowA", "Select Wayside"))
        self.whichwayside.setItemText(0, _translate("MainWindowA", "Wayside 1"))
        self.whichwayside.setItemText(1, _translate("MainWindowA", "Wayside 2"))
        self.whichwayside.setItemText(2, _translate("MainWindowA", "Wayside 3"))
        self.whichwayside.setItemText(3, _translate("MainWindowA", "Waysdie 4"))
        self.pushu.setText(_translate("MainWindowA", "U"))
        self.pushv.setText(_translate("MainWindowA", "V"))
        self.pushx.setText(_translate("MainWindowA", "X"))
        self.pushy.setText(_translate("MainWindowA", "Y"))
        self.pusho.setText(_translate("MainWindowA", "O"))
        self.sectiontitle_2.setText(_translate("MainWindowA", "Section"))
        self.pushr.setText(_translate("MainWindowA", "R"))
        self.occupancylabel_2.setText(_translate("MainWindowA", "Occupancy"))
        self.pushp.setText(_translate("MainWindowA", "P"))
        self.pushs.setText(_translate("MainWindowA", "S"))
        self.pushn.setText(_translate("MainWindowA", "N"))
        self.pushq.setText(_translate("MainWindowA", "Q"))
        self.pusht.setText(_translate("MainWindowA", "T"))
        self.pushw.setText(_translate("MainWindowA", "W"))
        self.pushz.setText(_translate("MainWindowA", "Z"))
        self.label_5.setText(_translate("MainWindowA", "Sections Managed:"))
        self.label_6.setText(_translate("MainWindowA", "Green Line"))
        self.label_7.setText(_translate("MainWindowA", "N - Z"))
        self.time.setText(_translate("MainWindowA", "11:44 PM"))
        self.label_18.setText(_translate("MainWindowA", "Switches"))
        self.label_13.setText(_translate("MainWindowA", "2"))
        self.gate20.setText(_translate("MainWindowA", "13 - 1"))
        self.gate21.setText(_translate("MainWindowA", "13 - 12"))
        self.label_14.setText(_translate("MainWindowA", "5"))
        self.gate50.setText(_translate("MainWindowA", "29-30"))
        self.gate51.setText(_translate("MainWindowA", "29-150"))
        self.label_15.setText(_translate("MainWindowA", "6"))
        self.gate60.setText(_translate("MainWindowA", "85 - 86"))
        self.gate61.setText(_translate("MainWindowA", "85 - 100"))
        self.label_50.setText(_translate("MainWindowA", "Crossing"))
        self.label_51.setText(_translate("MainWindowA", "Position"))
        self.label_52.setText(_translate("MainWindowA", "Lights"))
        self.label_53.setText(_translate("MainWindowA", "1"))
        self.gatepositiona.setText(_translate("MainWindowA", "Active"))
        self.activetrainlabel.setText(_translate("MainWindowA", "Active Trains  "))
        self.automaticmode.setText(_translate("MainWindowA", "Automatic Mode"))
        self.maintenancemode.setText(_translate("MainWindowA", "Maintenance Mode"))
        self.trackconfiguration.setText(_translate("MainWindowA", "Upload PLC"))
