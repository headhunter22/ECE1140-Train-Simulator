from PyQt6 import QtCore, QtGui, QtWidgets
from BlockInfo import *

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 600)
                MainWindow.setStyleSheet("background-color: rgb(255,255,255)")
                self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.RedLineContainer = QtWidgets.QWidget(parent=self.centralwidget)
                self.RedLineContainer.setObjectName("RedLineContainer")
                self.frame_3 = QtWidgets.QFrame(parent=self.RedLineContainer)
                self.frame_3.setGeometry(QtCore.QRect(0, 40, 301, 42))
                self.frame_3.setStyleSheet("background-color: rgb(255,255,255);\n"
                "padding: 0px;\n"
                "")
                self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame_3.setObjectName("frame_3")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
                self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
                self.horizontalLayout_2.setSpacing(1)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.TrainsCount = QtWidgets.QLabel(parent=self.frame_3)
                self.TrainsCount.setStyleSheet("color: rgb(0, 0, 0);\n"
                "font: 500 12pt \"Inter\";\n"
                "background-color: rgb(165, 165, 165);\n"
                "border: 2px solid;\n"
                "margin: 0px\n"
                "")
                self.TrainsCount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.TrainsCount.setObjectName("TrainsCount")
                self.horizontalLayout_2.addWidget(self.TrainsCount)
                self.Info = QtWidgets.QLabel(parent=self.frame_3)
                self.Info.setStyleSheet("background-color: rgb(165, 165, 165);\n"
                "border: 2px solid;\n"
                "\n"
                "color: rgb(0, 0, 0);\n"
                "font: 500 13pt \"Inter\";\n"
                "")
                self.Info.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.Info.setObjectName("Info")
                self.horizontalLayout_2.addWidget(self.Info)
                self.Occupancy = QtWidgets.QLabel(parent=self.frame_3)
                self.Occupancy.setStyleSheet("background-color: rgb(165, 165, 165);\n"
                "border: 2px solid;\n"
                "\n"
                "color: rgb(0, 0, 0);\n"
                "font: 500 13pt \"Inter\";\n"
                "\n"
                "")
                self.Occupancy.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.Occupancy.setObjectName("Occupancy")
                self.horizontalLayout_2.addWidget(self.Occupancy)
                self.SectionLabel = QtWidgets.QLabel(parent=self.frame_3)
                self.SectionLabel.setStyleSheet("background-color: rgb(165, 165, 165);\n"
                "border: 2px solid;\n"
                "\n"
                "color: rgb(0, 0, 0);\n"
                "font: 500 13pt \"Inter\";\n"
                "")
                self.SectionLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.SectionLabel.setObjectName("SectionLabel")
                self.horizontalLayout_2.addWidget(self.SectionLabel)
                self.frame_6 = QtWidgets.QFrame(parent=self.RedLineContainer)
                self.frame_6.setGeometry(QtCore.QRect(10, -5, 281, 41))
                self.frame_6.setStyleSheet("background-color: rgb(123, 123, 123)\n"
                "")
                self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame_6.setObjectName("frame_6")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
                self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_3.setSpacing(0)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.label_5 = QtWidgets.QLabel(parent=self.frame_6)
                font = QtGui.QFont()
                font.setFamily("Inter")
                font.setPointSize(28)
                font.setBold(True)
                font.setItalic(False)
                self.label_5.setFont(font)
                self.label_5.setStyleSheet("color: #cc0000;\n"
                "font: 700 28pt \"Inter\";\n"
                "padding-left: 20px;\n"
                "padding-right: 20px;")
                self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.label_5.setObjectName("label_5")
                self.horizontalLayout_3.addWidget(self.label_5)
                self.gridLayoutWidget = QtWidgets.QWidget(parent=self.RedLineContainer)
                self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 80, 301, 491))
                self.gridLayoutWidget.setObjectName("gridLayoutWidget")
                self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
                self.gridLayout.setContentsMargins(0, 0, 0, 0)
                self.gridLayout.setObjectName("gridLayout")
                self.verticalScrollBar = QtWidgets.QScrollBar(parent=self.gridLayoutWidget)
                self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
                self.verticalScrollBar.setObjectName("verticalScrollBar")
                self.gridLayout.addWidget(self.verticalScrollBar, 0, 4, 1, 1)
                self.verticalLayout = QtWidgets.QVBoxLayout()
                self.verticalLayout.setObjectName("verticalLayout")
                self.label_8 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
                self.label_8.setStyleSheet("color: rgb(0, 0, 0);font: 500 12pt \"Inter\";background-color: rgb(165, 165, 165);border: 2px solid;margin: 0px")
                self.label_8.setObjectName("label_8")
                self.verticalLayout.addWidget(self.label_8)
                self.label_7 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
                self.label_7.setStyleSheet("color: rgb(0, 0, 0);font: 500 12pt \"Inter\";background-color: rgb(165, 165, 165);border: 2px solid;margin: 0px")
                self.label_7.setObjectName("label_7")
                self.verticalLayout.addWidget(self.label_7)
                self.label_6 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
                self.label_6.setStyleSheet("color: rgb(0, 0, 0);font: 500 12pt \"Inter\";background-color: rgb(165, 165, 165);border: 2px solid;margin: 0px")
                self.label_6.setObjectName("label_6")
                self.verticalLayout.addWidget(self.label_6)
                self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
                self.label_4.setStyleSheet("color: rgb(0, 0, 0);font: 500 12pt \"Inter\";background-color: rgb(165, 165, 165);border: 2px solid;margin: 0px")
                self.label_4.setObjectName("label_4")
                self.verticalLayout.addWidget(self.label_4)
                self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
                self.label_3.setStyleSheet("color: rgb(0, 0, 0);font: 500 12pt \"Inter\";background-color: rgb(165, 165, 165);border: 2px solid;margin: 0px")
                self.label_3.setObjectName("label_3")
                self.verticalLayout.addWidget(self.label_3)
                self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
                self.label_2.setStyleSheet("color: rgb(0, 0, 0);font: 500 12pt \"Inter\";background-color: rgb(165, 165, 165);border: 2px solid;margin: 0px")
                self.label_2.setObjectName("label_2")
                self.verticalLayout.addWidget(self.label_2)
                self.label_9 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
                self.label_9.setStyleSheet("color: rgb(0, 0, 0);font: 500 12pt \"Inter\";background-color: rgb(165, 165, 165);border: 2px solid;margin: 0px")
                self.label_9.setObjectName("label_9")
                self.verticalLayout.addWidget(self.label_9)
                self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
                self.label.setStyleSheet("color: rgb(0, 0, 0);font: 500 12pt \"Inter\";background-color: rgb(165, 165, 165);border: 2px solid;margin: 0px")
                self.label.setObjectName("label")
                self.verticalLayout.addWidget(self.label)
                self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
                self.verticalLayout_3 = QtWidgets.QVBoxLayout()
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)
                self.verticalLayout_2 = QtWidgets.QVBoxLayout()
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
                self.verticalLayout_4 = QtWidgets.QVBoxLayout()
                self.verticalLayout_4.setObjectName("verticalLayout_4")
                self.gridLayout.addLayout(self.verticalLayout_4, 0, 3, 1, 1)
                self.horizontalLayout.addWidget(self.RedLineContainer)
                self.GreenLineContainer = QtWidgets.QWidget(parent=self.centralwidget)
                self.GreenLineContainer.setObjectName("GreenLineContainer")
                self.pushButton = QtWidgets.QPushButton(parent=self.GreenLineContainer)
                self.pushButton.setGeometry(QtCore.QRect(80, 50, 100, 32))
                self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0)")
                self.pushButton.setObjectName("pushButton")
                self.horizontalLayout.addWidget(self.GreenLineContainer)
                self.GeneralInfoContainer = QtWidgets.QWidget(parent=self.centralwidget)
                self.GeneralInfoContainer.setObjectName("GeneralInfoContainer")
                self.horizontalLayout.addWidget(self.GeneralInfoContainer)
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.TrainsCount.setText(_translate("MainWindow", "Section"))
                self.Info.setText(_translate("MainWindow", "# of Trains"))
                self.Occupancy.setText(_translate("MainWindow", "Blocks Occupied"))
                self.SectionLabel.setText(_translate("MainWindow", "Info"))
                self.label_5.setText(_translate("MainWindow", "Red Line"))
                self.label_8.setText(_translate("MainWindow", "TextLabel"))
                self.label_7.setText(_translate("MainWindow", "TextLabel"))
                self.label_6.setText(_translate("MainWindow", "TextLabel"))
                self.label_4.setText(_translate("MainWindow", "TextLabel"))
                self.label_3.setText(_translate("MainWindow", "TextLabel"))
                self.label_2.setText(_translate("MainWindow", "TextLabel"))
                self.label_9.setText(_translate("MainWindow", "TextLabel"))
                self.label.setText(_translate("MainWindow", "TextLabel"))
                self.pushButton.setText(_translate("MainWindow", "GO TO INFO"))

                self.pushButton.clicked.connect(self.getInfoPage)

        def getInfoPage(self):
                self.openBlockInfo()

        def openBlockInfo(self):
                self.window = QtWidgets.QMainWindow()
                self.ui = BlockInfo()
                self.ui.setupUi(self.window)
                self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
