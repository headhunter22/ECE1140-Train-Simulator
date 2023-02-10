from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.buttonClick)

        self.setCentralWidget(button)

    def buttonClick(self):
        print("Clicked")

# Create an application
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()

with open("styles.css","r") as file:
    app.setStyleSheet(file.read())

# Show window
window.show()

# Start the event loop.
app.exec()