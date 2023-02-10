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

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()

with open("styles.css","r") as file:
    app.setStyleSheet(file.read())

# Show window
window.show()

# Start the event loop.
app.exec()