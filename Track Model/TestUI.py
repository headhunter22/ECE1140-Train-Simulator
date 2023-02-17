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
        # create main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 530)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # switch setting section
        # heading
        self.SwitchLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.SwitchLabel.setGeometry(QtCore.QRect(180, 10, 58, 16))
        self.SwitchLabel.setObjectName("SwitchLabel")

        # line & dropdown
        self.SwitchLineLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.SwitchLineLabel.setGeometry(QtCore.QRect(20, 60, 81, 20))
        self.SwitchLineLabel.setObjectName("SwitchLineLabel")

        self.SwitchLine = QtWidgets.QComboBox(parent=self.centralwidget)
        self.SwitchLine.setGeometry(QtCore.QRect(0, 90, 91, 32))
        self.SwitchLine.setObjectName("SwitchLineDropdown")

        # block & dropdown
        self.SwitchBlock = QtWidgets.QLabel(parent=self.centralwidget)
        self.SwitchBlock.setGeometry(QtCore.QRect(110, 60, 58, 16))
        self.SwitchBlock.setObjectName("SwitchBlock")

        self.SwitchBlockDropDown = QtWidgets.QComboBox(parent=self.centralwidget)
        self.SwitchBlockDropDown.setGeometry(QtCore.QRect(90, 90, 71, 32))
        self.SwitchBlockDropDown.setObjectName("SwitchBlockDropdown")

        # connection
        self.SwitchConn = QtWidgets.QLabel(parent=self.centralwidget)
        self.SwitchConn.setGeometry(QtCore.QRect(230, 60, 80, 20))
        self.SwitchConn.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SwitchConn.setObjectName("SwitchConn")

        self.Connection = QtWidgets.QLabel(parent=self.centralwidget)
        self.Connection.setGeometry(QtCore.QRect(230, 90, 150, 20))
        self.Connection.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Connection.setObjectName("Connection")

        # railroad crossings
        # headings
        self.RRXing = QtWidgets.QLabel(parent=self.centralwidget)
        self.RRXing.setGeometry(QtCore.QRect(150, 150, 121, 16))
        self.RRXing.setObjectName("RRXing")
        self.RRRedLine = QtWidgets.QLabel(parent=self.centralwidget)
        self.RRRedLine.setGeometry(QtCore.QRect(60, 180, 121, 16))
        self.RRRedLine.setObjectName("RRRedLine")
        self.RRGreenLine = QtWidgets.QLabel(parent=self.centralwidget)
        self.RRGreenLine.setGeometry(QtCore.QRect(300, 180, 121, 16))
        self.RRGreenLine.setObjectName("RRGreenLine")

        # checkboxes
        self.RedXing = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.RedXing.setGeometry(QtCore.QRect(50, 210, 85, 20))
        self.RedXing.setObjectName("checkBox")
        self.GreenXing = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.GreenXing.setGeometry(QtCore.QRect(300, 210, 85, 20))
        self.GreenXing.setObjectName("checkBox_2")

        # block occupancy
        # header
        self.OccHeader = QtWidgets.QLabel(parent=self.centralwidget)
        self.OccHeader.setGeometry(QtCore.QRect(160, 270, 121, 16))
        self.OccHeader.setObjectName("OccHeader")

        # line label and dropdown
        self.OccLine = QtWidgets.QLabel(parent=self.centralwidget)
        self.OccLine.setGeometry(QtCore.QRect(20, 300, 81, 20))
        self.OccLine.setObjectName("OccLine")

        self.OccLineSel = QtWidgets.QComboBox(parent=self.centralwidget)
        self.OccLineSel.setGeometry(QtCore.QRect(0, 320, 91, 32))
        self.OccLineSel.setObjectName("OccLineSel")

        # block label & dropdown
        self.OccBlock = QtWidgets.QLabel(parent=self.centralwidget)
        self.OccBlock.setGeometry(QtCore.QRect(110, 300, 58, 16))
        self.OccBlock.setObjectName("OccBlock")

        self.OccBlockSel = QtWidgets.QComboBox(parent=self.centralwidget)
        self.OccBlockSel.setGeometry(QtCore.QRect(90, 320, 71, 32))
        self.OccBlockSel.setObjectName("OccBlockSel")

        # set to occupied/vacant label
        self.SetTo = QtWidgets.QLabel(parent=self.centralwidget)
        self.SetTo.setGeometry(QtCore.QRect(300, 300, 81, 20))
        self.SetTo.setObjectName("SetTo")

        # set occupied/vacant buttons
        self.setOccupied = QtWidgets.QPushButton(parent=self.centralwidget)
        self.setOccupied.setGeometry(QtCore.QRect(250, 330, 71, 32))
        self.setOccupied.setObjectName("setOccupied")
        self.setVacant = QtWidgets.QPushButton(parent=self.centralwidget)
        self.setVacant.setGeometry(QtCore.QRect(330, 330, 71, 32))
        self.setVacant.setObjectName("setVacant")

        # track heaters
        # header
        self.TrackHeaters = QtWidgets.QLabel(parent=self.centralwidget)
        self.TrackHeaters.setGeometry(QtCore.QRect(40, 390, 121, 16))
        self.TrackHeaters.setObjectName("TrackHeaters")

        # enter temp button
        self.EnterTemp = QtWidgets.QPushButton(parent=self.centralwidget)
        self.EnterTemp.setGeometry(QtCore.QRect(20, 410, 100, 31))
        self.EnterTemp.setObjectName("EnterTemp")

        # enter temp text field
        self.tempEntry = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.tempEntry.setGeometry(QtCore.QRect(10, 440, 125, 21))
        self.tempEntry.setObjectName("tempEntry")

        # heater status
        self.HeaterStatus = QtWidgets.QLabel(parent=self.centralwidget)
        self.HeaterStatus.setGeometry(QtCore.QRect(10, 470, 141, 16))
        self.HeaterStatus.setObjectName("HeaterStatus")

        # date/time label
        self.tempEntry = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.tempEntry.setGeometry(QtCore.QRect(10, 440, 125, 21))
        self.tempEntry.setObjectName("tempEntry")

        # fault inducing/check
        self.InduceFault = QtWidgets.QLabel(parent=self.centralwidget)
        self.InduceFault.setGeometry(QtCore.QRect(260, 390, 121, 16))
        self.InduceFault.setObjectName("InduceFault")
    
        # dividers
        self.divider1 = QtWidgets.QFrame(parent=self.centralwidget)
        self.divider1.setGeometry(QtCore.QRect(0, 130, 411, 16))
        self.divider1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.divider1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.divider1.setObjectName("divider1")
        self.divider2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.divider2.setGeometry(QtCore.QRect(0, 250, 411, 16))
        self.divider2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.divider2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.divider2.setObjectName("divider2")
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
        
        # set up main window
        MainWindow.setCentralWidget(self.centralwidget)

        # retranslate
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # set up main window
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        # switch labels
        self.SwitchLabel.setText(_translate("MainWindow", "Switches"))
        self.SwitchBlock.setText(_translate("MainWindow", "Block"))
        self.SwitchConn.setText(_translate("MainWindow", "Connection"))

        # railroad crossing labels
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
        self.OccBlock.setText(_translate("MainWindow", "Block"))
        self.SetTo.setText(_translate("MainWindow", "Set To:"))
        self.OccLine.setText(_translate("MainWindow", "Line"))
        self.InduceFault.setText(_translate("MainWindow", "Induce Fault"))
        self.DateTime.setText(_translate("MainWindow", "Date/Time"))
        self.SwitchLineLabel.setText(_translate("MainWindow", "Line"))

        # switch section dropdowns
        # switch select lines, sections, and blocks (default red)
        self.SwitchLine.addItems(['Red', 'Green', 'Blue'])
        self.SwitchBlockDropDown.addItems(map(str, range(1, 77)))
        self.Connection.setText("Connection")
        
        # detect change in line to change section and block options 
        self.SwitchLine.currentTextChanged.connect(self.switchLineChanged)

        # connect section and block changing to the same function to update connection labels
        self.SwitchBlockDropDown.currentTextChanged.connect(self.switchBlockChange)

        # block occupancy set/unset
        self.OccLineSel.addItems(['Red', 'Green', 'Blue'])
        self.SwitchBlockDropDown.currentTextChanged.connect(self.switchBlockChange)

        # block occupancy set/unset
        self.OccLineSel.addItems(['Red', 'Green', 'Blue'])
        self.OccBlockSel.addItems(map(str, range(1, 77)))

        # detect switch in line to change section and block options
        self.OccLineSel.currentTextChanged.connect(self.occLineChanged)

        # define occupied/vacant buttons
        self.setOccupied.setText(_translate("MainWindow", "Occupied"))
        self.setVacant.setText(_translate("MainWindow", "Vacant"))

        # connect buttons to the function
        self.setOccupied.clicked.connect(self.setOcc)
        self.setVacant.clicked.connect(self.setVac)

        # track heaters
        # read temp entry when entered
        self.HeaterStatus.setText(_translate("MainWindow", "Heater Status: ON"))
        self.TrackHeaters.setText(_translate("MainWindow", "Track Heaters"))
        self.EnterTemp.setText(_translate("MainWindow", "Enter Temp"))
        self.EnterTemp.clicked.connect(self.tempChanged)

    # function to change the track heater status based on temp input
    def tempChanged(self):
        if not self.tempEntry.text().isnumeric(): 
            return
        if int(self.tempEntry.text()) >= 39:
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

        # for each line, add correct blocks
        if selection == 'Red':
            self.SwitchBlockDropDown.addItems(map(str, range(1, 77)))
        if selection == 'Blue':
            self.SwitchBlockDropDown.addItems(map(str, range(1, 16)))
        if selection == 'Green':
            self.SwitchBlockDropDown.addItems(map(str, range(1, 151)))

    def switchBlockChange(self):
        # update the label for the connection
        rawtext = SwitchQuery.selectSwitches(self.SwitchLine.currentText(), self.SwitchBlockDropDown.currentText())
        
        self.SwitchSectionDropDown.clear()

        # for each line, add correct sections and blocks
        if selection == 'Red':
            self.SwitchBlockDropDown.addItems(map(str, range(1, 77)))
        if selection == 'Blue':
            self.SwitchBlockDropDown.addItems(map(str, range(1, 16)))
        if selection == 'Green':
            self.SwitchBlockDropDown.addItems(map(str, range(1, 151)))

    def switchBlockChange(self):
        # update the label for the connection
        rawtext = SwitchQuery.selectSwitches(self.SwitchLine.currentText(), self.SwitchBlockDropDown.currentText())
        charRemove = ['[', ']', ',', '\'', '(', ')']

        # remove unnecessary characters from query
        for char in charRemove:
            rawtext = rawtext.replace(char, '')

        # set the label text
        self.Connection.setText(rawtext)    

    def occLineChanged(self, selection):
        # clear current options in the dropdowns 
        self.OccBlockSel.clear()

        # for each line, add correct sections and blocks
        if selection == 'Red':
            self.OccBlockSel.addItems(map(str, range(1, 77)))
        if selection == 'Blue':
            self.OccBlockSel.addItems(map(str, range(1, 16)))
        if selection == 'Green':
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
