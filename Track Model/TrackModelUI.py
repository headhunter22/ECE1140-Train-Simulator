from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set MainWindow
        self.setWindowTitle("My App")
        self.setBaseSize(QSize(400, 400))

        # Set VBox with buttons
        VBox = QVBoxLayout()
        CentralWidget = QWidget()
        self.setCentralWidget(CentralWidget)

        # Add Buttons to VBox
        VBox.addWidget(self.createButton())
        VBox.addWidget(self.createButton())

        CentralWidget.setLayout(VBox)

    def createButton(self):
        button = QPushButton("CLICK")
        button.setGeometry(0,0,200,200)
        button.clicked.connect(self.buttonClick)

        return button

    def buttonClick(self):
        CentralWidget.setCurrentIndex(CentralWidget.currentIndex() + 1)

class SecondScreen(QDialog):
    def __init__(self):
        super().__init__()

        loadUi("gui.ui", self)

# Run Code
if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QWidget
    #with open("styles.css","r") as file:
    #   app.setStyleSheet(file.read())

    window = MainWindow()
    screen2 = SecondScreen()

    widget.addWidget(window)
    widget.add(screen2)
    widget.setFixedSize(300, 400)
    widget.show()

    sys.exit(app.exec())