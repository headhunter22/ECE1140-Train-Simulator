import sys, os
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtCore import QSize

# Block Info Class
class BlockInfo(QtWidgets.QMainWindow):
    def __init__(self, section, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("BlockInfo.ui", self)
        self.setWindowTitle('Block Info')

        # set the header
        self.Header.setText("Section " + section.sectionName + " Info")

        # fill the rest of the window with appropriate info
        self.widget = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()

        for block in section.blocks:
            self.hbox = QtWidgets.QHBoxLayout()

            # create labels and add to the hbox
            # create label for block name
            blockLabel = QtWidgets.QLabel(block.blockName, self)
            blockLabel.setFixedHeight(50)
            blockLabel.setFixedWidth(75)
            blockLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hbox.addWidget(blockLabel)

            # create label for occupancy
            occupiedLabel = QtWidgets.QLabel(str(block.occupied), self)
            occupiedLabel.setFixedHeight(50)
            occupiedLabel.setFixedWidth(75)
            occupiedLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hbox.addWidget(occupiedLabel)

            # create label for length
            lengthLabel = QtWidgets.QLabel(str(block.length), self)
            lengthLabel.setFixedHeight(50)
            lengthLabel.setFixedWidth(50)
            lengthLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hbox.addWidget(lengthLabel)

            # create label for elevation
            elevationLabel = QtWidgets.QLabel(str(block.elevation), self)
            elevationLabel.setFixedHeight(50)
            elevationLabel.setFixedWidth(100)
            elevationLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hbox.addWidget(elevationLabel)

            # create label for grade
            gradeLabel = QtWidgets.QLabel(block.grade, self)
            gradeLabel.setFixedHeight(50)
            gradeLabel.setFixedWidth(75)
            gradeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hbox.addWidget(gradeLabel)

            # create label for speed limit
            speedLabel = QtWidgets.QLabel(str(block.speedLimit), self)
            speedLabel.setFixedHeight(50)
            speedLabel.setFixedWidth(125)
            speedLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hbox.addWidget(speedLabel)

            # create label for station side
            stationLabel = QtWidgets.QLabel(block.stationSide, self)
            stationLabel.setFixedHeight(50)
            stationLabel.setFixedWidth(100)
            stationLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hbox.addWidget(stationLabel)

            # create label for underground
            undergroundLabel = QtWidgets.QLabel(str(block.underground), self)
            undergroundLabel.setFixedHeight(50)
            undergroundLabel.setFixedWidth(100)
            undergroundLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hbox.addWidget(undergroundLabel)

            # create label for switchConnection
            switchLabel = QtWidgets.QLabel(str(block.switchConnection), self)
            switchLabel.setFixedHeight(50)
            switchLabel.setFixedWidth(125)
            switchLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hbox.addWidget(switchLabel)

            # create label for passengers
            passengersLabel = QtWidgets.QLabel(str(block.passengers), self)
            passengersLabel.setFixedHeight(50)
            passengersLabel.setFixedWidth(75)
            passengersLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hbox.addWidget(passengersLabel)

            # add row to vbox
            self.vbox.addLayout(self.hbox)

        self.widget.setLayout(self.vbox)
        self.MainScrollArea.setWidget(self.widget)