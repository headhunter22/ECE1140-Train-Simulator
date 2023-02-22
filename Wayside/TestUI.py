import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QListWidget, QButtonGroup, QToolButton)
from PyQt6.QtGui import QPalette, QGuiApplication
from PyQt6 import QtWidgets, uic
from Wayside_Test import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self = Ui_MainWindow()
        self.setupUi(self)

        layout = QVBoxLayout()

# app = QtWidgets.QApplication(sys.argv)
if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MainWindow()
    widget.show()

    app.exec()