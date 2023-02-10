import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        self.setFixedSize(QSize(400, 300))
        button.clicked.connect(self.buttonClicked)
        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def buttonClicked(self):
        print("button clicked")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()