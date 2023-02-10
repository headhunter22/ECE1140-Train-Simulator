import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QPushButton, 
    QVBoxLayout,
    QWidget)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CTC Office - Test Interface")

        layout = QVBoxLayout()

        layout.addWidget(Color('red'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.buttonClicked)
        button.clicked.connect(self.buttonChecked)

        #self.setCentralWidget(button) # Set the central widget of the Window.

    def buttonClicked(self):
        print("button clicked")

    def buttonChecked(self, checked):
        print("Checked?", checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()