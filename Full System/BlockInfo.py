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
        self.ID = section.sectionName

        # fill the rest of the window with appropriate info
        self.widget = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()

        self.rows = []

        for block in section.blocks:
            self.hbox = QtWidgets.QHBoxLayout()

            # create labels and add to the hbox
            # create label for block name
            blockLabel = QtWidgets.QLabel(block.blockName, self)
            blockLabel.setFixedHeight(50)
            blockLabel.setFixedWidth(75)
            blockLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hbox.addWidget(blockLabel)

            # create label for length
            lengthLabel = QtWidgets.QLabel(str(block.length), self)
            lengthLabel.setFixedHeight(50)
            lengthLabel.setFixedWidth(100)
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
            gradeLabel.setFixedWidth(100)
            gradeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hbox.addWidget(gradeLabel)

            # create label for speed limit
            speedLabel = QtWidgets.QLabel(str(block.speedLimit), self)
            speedLabel.setFixedHeight(50)
            speedLabel.setFixedWidth(150)
            speedLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hbox.addWidget(speedLabel)

            # create label for station side
            stationLabel = QtWidgets.QLabel(block.stationSide, self)
            stationLabel.setFixedHeight(50)
            stationLabel.setFixedWidth(125)
            stationLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hbox.addWidget(stationLabel)

            # create label for underground
            undergroundLabel = QtWidgets.QLabel(str(block.underground), self)
            undergroundLabel.setFixedHeight(50)
            undergroundLabel.setFixedWidth(125)
            undergroundLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.hbox.addWidget(undergroundLabel)

            # add row to vbox and rows array
            self.vbox.addLayout(self.hbox)
            self.rows.append(self.hbox)

        self.widget.setLayout(self.vbox)
        self.MainScrollArea.setWidget(self.widget)