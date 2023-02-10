
from PyQt6.QtWidgets import (QApplication, QPushButton, QDial, QProgressBar, QLabel, QWidget)
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300,200)
        self.setWindowTitle("Temperature Control")
        self.setContentsMargins(20,20,20,20)

app = QApplication(sys.argv)
window = Window()

tempDial = QDial()
ACButton = QPushButton("AC On/Off")
currTempVisual = QProgressBar()
currTempText = QLabel("Current Temp")
tempDial.show()
ACButton.show()
currTempVisual.show()
currTempText.show()

app.exec()