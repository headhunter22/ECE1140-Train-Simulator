from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6 import QtGui
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Train Controller")
        self.resize(980, 620)

        # Emergency Brake button init #
        button = QPushButton('EMERGENCY BRAKE', self)
        #txt = QLabel("Emergency Brake Disengaged", self)
        button.setGeometry(50, 50, 200, 200)
        #txt.setGeometry(75, 210, 200, 100)
        button.setCheckable(False)
        button.clicked.connect(self.EBClick)
        #button.setStyleSheet("QPushButton { background-color : rgb(255,255,255); color: rgb(0,0,0)}"



    def EBClick(self):
            self.setStyleSheet("QPushButton { background-color : rgb(255,0,0)}")
            print("Engaged")
            txt = QLabel("Emergency Brake Engaged", self)
            txt.setGeometry(75, 210, 200, 100)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
# Show window
window.show()

# Start the event loop.
app.exec()