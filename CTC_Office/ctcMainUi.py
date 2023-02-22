from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QIntValidator
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from ctcMainUiImport import Ui_MainWindow
import TrackParser

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()

if __name__ == '__main__':
    track = TrackParser.parseTrack('Track Layout.csv')
    app = QApplication([])
    window = MainWindow()
    app.exec()