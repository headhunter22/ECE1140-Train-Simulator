# necessary imports
from PyQt6 import QtCore, QtGui, QtWidgets
import SwitchQuery

redOcc, greenOcc, blueOcc = {}, {}, {}

for i in range(1, 77):
    redOcc[i] = 0
for i in range(1, 151):
    greenOcc[i] = 0
for i in range(1, 16):
    blueOcc[i] = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 530)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.switchLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.switchLabel.setGeometry(QtCore.QRect(180, 10, 58, 16))
        self.switchLabel.setObjectName("switchLabel")
        self.SwitchSec = QtWidgets.QLabel(parent=self.centralwidget)
        self.SwitchSec.setGeometry(QtCore.QRect(110, 60, 58, 16))
        self.SwitchSec.setObjectName("SwitchSec")
        self.SwitchBlock = QtWidgets.QLabel(parent=self.centralwidget)
        self.SwitchBlock.setGeometry(QtCore.QRect(210, 60, 58, 16))
        self.SwitchBlock.setObjectName("SwitchBlock")
        self.SwitchConn = QtWidgets.QLabel(parent=self.centralwidget)
        self.SwitchConn.setGeometry(QtCore.QRect(300, 60, 81, 20))
        self.SwitchConn.setObjectName("SwitchConn")
        self.Connection = QtWidgets.QLabel(parent=self.centralwidget)
        self.Connection.setGeometry(QtCore.QRect(270, 90, 121, 20))
        self.Connection.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Connection.setObjectName("Connection")
        self.divider1 = QtWidgets.QFrame(parent=self.centralwidget)
        self.divider1.setGeometry(QtCore.QRect(0, 130, 411, 16))
        self.divider1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.divider1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.divider1.setObjectName("divider1")
        self.RRXing = QtWidgets.QLabel(parent=self.centralwidget)
        self.RRXing.setGeometry(QtCore.QRect(150, 150, 121, 16))
        self.RRXing.setObjectName("RRXing")
        self.RRRedLine = QtWidgets.QLabel(parent=self.centralwidget)
        self.RRRedLine.setGeometry(QtCore.QRect(60, 180, 121, 16))
        self.RRRedLine.setObjectName("RRRedLine")
        self.RRGreenLine = QtWidgets.QLabel(parent=self.centralwidget)
        self.RRGreenLine.setGeometry(QtCore.QRect(300, 180, 121, 16))
        self.RRGreenLine.setObjectName("RRGreenLine")
        self.RedXing = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.RedXing.setGeometry(QtCore.QRect(50, 210, 85, 20))
        self.RedXing.setObjectName("checkBox")
        self.GreenXing = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.GreenXing.setGeometry(QtCore.QRect(300, 210, 85, 20))
        self.GreenXing.setObjectName("checkBox_2")
        self.divider2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.divider2.setGeometry(QtCore.QRect(0, 250, 411, 16))
        self.divider2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.divider2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.divider2.setObjectName("divider2")
        self.OccHeader = QtWidgets.QLabel(parent=self.centralwidget)
        self.OccHeader.setGeometry(QtCore.QRect(160, 270, 121, 16))
        self.OccHeader.setObjectName("OccHeader")
        self.OccSec = QtWidgets.QLabel(parent=self.centralwidget)
        self.OccSec.setGeometry(QtCore.QRect(110, 300, 58, 16))
        self.OccSec.setObjectName("OccSec")
        self.OccBlock = QtWidgets.QLabel(parent=self.centralwidget)
        self.OccBlock.setGeometry(QtCore.QRect(190, 300, 58, 16))
        self.OccBlock.setObjectName("OccBlock")
        self.SetTo = QtWidgets.QLabel(parent=self.centralwidget)
        self.SetTo.setGeometry(QtCore.QRect(300, 300, 81, 20))
        self.SetTo.setObjectName("SetTo")
        self.OccLine = QtWidgets.QLabel(parent=self.centralwidget)
        self.OccLine.setGeometry(QtCore.QRect(40, 300, 58, 16))
        self.OccLine.setObjectName("OccLine")
        self.divider3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.divider3.setGeometry(QtCore.QRect(0, 370, 411, 16))
        self.divider3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.divider3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.divider3.setObjectName("divider3")
        self.divider4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.divider4.setGeometry(QtCore.QRect(163, 380, 20, 141))
        self.divider4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.divider4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.divider4.setObjectName("divider4")
        self.TrackHeaters = QtWidgets.QLabel(parent=self.centralwidget)
        self.TrackHeaters.setGeometry(QtCore.QRect(40, 390, 121, 16))
        self.TrackHeaters.setObjectName("TrackHeaters")
        self.InduceFault = QtWidgets.QLabel(parent=self.centralwidget)
        self.InduceFault.setGeometry(QtCore.QRect(260, 390, 121, 16))
        self.InduceFault.setObjectName("InduceFault")
        self.HeaterStatus = QtWidgets.QLabel(parent=self.centralwidget)
        self.HeaterStatus.setGeometry(QtCore.QRect(10, 470, 141, 16))
        self.HeaterStatus.setObjectName("HeaterStatus")
        self.DateTime = QtWidgets.QLabel(parent=self.centralwidget)
        self.DateTime.setGeometry(QtCore.QRect(10, 500, 141, 16))
        self.DateTime.setObjectName("DateTime")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 440, 125, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.setOccupied = QtWidgets.QPushButton(parent=self.centralwidget)
        self.setOccupied.setGeometry(QtCore.QRect(250, 330, 71, 32))
        self.setOccupied.setObjectName("setOccupied")
        self.setVacant = QtWidgets.QPushButton(parent=self.centralwidget)
        self.setVacant.setGeometry(QtCore.QRect(330, 330, 71, 32))
        self.setVacant.setObjectName("setVacant")
        self.SwitchSectionDropDown = QtWidgets.QComboBox(parent=self.centralwidget)
        self.SwitchSectionDropDown.setGeometry(QtCore.QRect(90, 90, 91, 32))
        self.SwitchSectionDropDown.setObjectName("comboBox")
        self.SwitchBlockDropDown = QtWidgets.QComboBox(parent=self.centralwidget)
        self.SwitchBlockDropDown.setGeometry(QtCore.QRect(200, 90, 71, 32))
        self.SwitchBlockDropDown.setObjectName("comboBox_2")
        self.SwitchSec_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.SwitchSec_2.setGeometry(QtCore.QRect(20, 60, 81, 20))
        self.SwitchSec_2.setObjectName("SwitchSec_2")
        self.SwitchLine = QtWidgets.QComboBox(parent=self.centralwidget)
        self.SwitchLine.setGeometry(QtCore.QRect(0, 90, 91, 32))
        self.SwitchLine.setObjectName("comboBox_3")
        self.EnterTemp = QtWidgets.QPushButton(parent=self.centralwidget)
        self.EnterTemp.setGeometry(QtCore.QRect(20, 410, 100, 31))
        self.EnterTemp.setObjectName("EnterTemp")
        self.OccLineSel = QtWidgets.QComboBox(parent=self.centralwidget)
        self.OccLineSel.setGeometry(QtCore.QRect(0, 320, 91, 32))
        self.OccLineSel.setObjectName("OccLineSel")
        self.OccSecSel = QtWidgets.QComboBox(parent=self.centralwidget)
        self.OccSecSel.setGeometry(QtCore.QRect(90, 320, 91, 32))
        self.OccSecSel.setObjectName("OccSecSel")
        self.OccBlockSel = QtWidgets.QComboBox(parent=self.centralwidget)
        self.OccBlockSel.setGeometry(QtCore.QRect(180, 320, 71, 32))
        self.OccBlockSel.setObjectName("OccBlockSel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.switchLabel.setText(_translate("MainWindow", "Switches"))
        self.SwitchSec.setText(_translate("MainWindow", "Section"))
        self.SwitchBlock.setText(_translate("MainWindow", "Block"))
        self.SwitchConn.setText(_translate("MainWindow", "Connection"))
        self.RRXing.setText(_translate("MainWindow", "Railroad Crossings"))
        self.RRRedLine.setText(_translate("MainWindow", "Red Line"))
        self.RRGreenLine.setText(_translate("MainWindow", "Green Line"))

        # crossing check boxes
        # red x-ing connect to function
        self.RedXing.setText(_translate("MainWindow", "E-19"))
        self.RedXing.toggled.connect(self.getCrossingStatuses)

        # green x-ing connect to function
        self.GreenXing.setText(_translate("MainWindow", "I-47"))
        self.GreenXing.toggled.connect(self.getCrossingStatuses)

        self.OccHeader.setText(_translate("MainWindow", "Occupancy"))
        self.OccSec.setText(_translate("MainWindow", "Section"))
        self.OccBlock.setText(_translate("MainWindow", "Block"))
        self.SetTo.setText(_translate("MainWindow", "Set To:"))
        self.OccLine.setText(_translate("MainWindow", "Line"))
        self.InduceFault.setText(_translate("MainWindow", "Induce Fault"))
        self.DateTime.setText(_translate("MainWindow", "Date/Time"))
        self.SwitchSec_2.setText(_translate("MainWindow", "Line"))

        # switch section dropdowns
        # switch select lines, sections, and blocks (default red)
        self.SwitchLine.addItems(['Red', 'Green', 'Blue'])
        self.SwitchSectionDropDown.addItems(list(map(chr, range(65,85))))
        self.SwitchBlockDropDown.addItems(map(str, range(1, 77)))
        self.Connection.setText("Connection")
        
        # detect change in line to change section and block options 
        self.SwitchLine.currentTextChanged.connect(self.switchLineChanged)

        # connect section and block changing to the same function to update connection labels
        self.SwitchSectionDropDown.currentTextChanged.connect(self.switchSectionOrBlockChange)
        self.SwitchBlockDropDown.currentTextChanged.connect(self.switchSectionOrBlockChange)

        # block occupancy set/unset
        self.OccLineSel.addItems(['Red', 'Green', 'Blue'])
        self.OccSecSel.addItems(list(map(chr, range(65,85))))
        self.OccBlockSel.addItems(map(str, range(1, 77)))

        # detect switch in line to change section and block options
        self.OccLineSel.currentTextChanged.connect(self.occLineChanged)

        # define occupied/vacant buttons
        self.setOccupied.setText(_translate("MainWindow", "Occupied"))
        self.setVacant.setText(_translate("MainWindow", "Vacant"))

        # connect buttons to the function
        # self.setOccupied.clicked.connect(self.setOcc)
        # self.setVacant.clicked.connect(self.setVac)

        # track heaters
        # read temp entry when entered
        self.HeaterStatus.setText(_translate("MainWindow", "Heater Status: ON"))
        self.TrackHeaters.setText(_translate("MainWindow", "Track Heaters"))
        self.EnterTemp.setText(_translate("MainWindow", "Enter Temp"))
        self.EnterTemp.clicked.connect(self.tempChanged)

    # function to change the track heater status based on temp input
    def tempChanged(self):
        if not self.lineEdit.text().isnumeric(): 
            return
        if int(self.lineEdit.text()) >= 39:
            self.HeaterStatus.setText("Heater Status: OFF")
        else:
            self.HeaterStatus.setText("Heater Status: ON")

    # function to get crossing statuses when they change
    def getCrossingStatuses(self):
        print([self.RedXing.isChecked(), self.GreenXing.isChecked()])

    # function to change dropdowns for switch selection
    def switchLineChanged(self, selection):
        # clear current options in the dropdowns 
        self.SwitchBlockDropDown.clear()
        self.SwitchSectionDropDown.clear()

        # for each line, add correct sections and blocks
        if selection == 'Red':
            self.SwitchSectionDropDown.addItems(list(map(chr, range(65,85))))
            self.SwitchBlockDropDown.addItems(map(str, range(1, 77)))
        if selection == 'Blue':
            self.SwitchSectionDropDown.addItems(list(map(chr, range(65,68))))
            self.SwitchBlockDropDown.addItems(map(str, range(1, 16)))
        if selection == 'Green':
            self.SwitchSectionDropDown.addItems(list(map(chr, range(65,91))))
            self.SwitchBlockDropDown.addItems(map(str, range(1, 151)))

    def switchSectionOrBlockChange(self):
        # update the label for the connection
        rawtext = SwitchQuery.selectSwitches(self.SwitchLine.currentText(), self.SwitchSectionDropDown.currentText(), self.SwitchBlockDropDown.currentText())
        charRemove = ['[', ']', ',', '\'', '(', ')']

        # remove unnecessary characters from query
        for char in charRemove:
            rawtext = rawtext.replace(char, '')

        # set the label text
        self.Connection.setText(rawtext)    

    def occLineChanged(self, selection):
        # clear current options in the dropdowns 
        self.OccBlockSel.clear()
        self.OccSecSel.clear()

        # for each line, add correct sections and blocks
        if selection == 'Red':
            self.OccSecSel.addItems(list(map(chr, range(65,85))))
            self.OccBlockSel.addItems(map(str, range(1, 77)))
        if selection == 'Blue':
            self.OccSecSel.addItems(list(map(chr, range(65,68))))
            self.OccBlockSel.addItems(map(str, range(1, 16)))
        if selection == 'Green':
            self.OccSecSel.addItems(list(map(chr, range(65,91))))
            self.OccBlockSel.addItems(map(str, range(1, 151)))

    def setOcc(self):
        if self.OccLineSel.currentText() == 'Red':
            redOcc[int(self.OccBlockSel.currentText())] = 1
        elif self.OccLineSel.currentText() == 'Green':
            greenOcc[int(self.OccBlockSel.currentText())] = 1
        else:
            blueOcc[int(self.OccBlockSel.currentText())] = 1

    def setVac(self):
        if self.OccLineSel.currentText() == 'Red':
            redOcc[int(self.OccBlockSel.currentText())] = 0
        elif self.OccLineSel.currentText() == 'Green':
            greenOcc[int(self.OccBlockSel.currentText())] = 0
        else:
            blueOcc[int(self.OccBlockSel.currentText())] = 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
