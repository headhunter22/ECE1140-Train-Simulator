from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                              QLabel, QVBoxLayout, QWidget, QListWidget, QButtonGroup,
                              QToolButton)
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPalette, QGuiApplication

from Wayside_Test import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        layout = QVBoxLayout()

        self.button_group = QButtonGroup()

        # Create the first tool button, initially checked and blue background
        self.button1 = QToolButton()
        self.button1.setText("Button 1")
        self.button1.setCheckable(True)
        self.button1.setChecked(True)
        self.button1.setStyleSheet("background-color: blue;")
        self.button_group.addButton(self.button1)

        # Create the second tool button, unchecked and white background
        self.button2 = QToolButton()
        self.button2.setText("Button 2")
        self.button2.setCheckable(True)
        self.button2.setChecked(False)
        self.button2.setStyleSheet("background-color: white;")
        self.button_group.addButton(self.button2)

        # Add the buttons to the layout
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        # Connect the clicked signal of the buttons to the slot method
        self.button1.clicked.connect(self.on_button_clicked)
        self.button2.clicked.connect(self.on_button_clicked)

        self.setLayout(layout)

    def on_button_clicked(self):
    # Check which button was clicked
        clicked_button = self.sender()

        if clicked_button == self.button2:
            # Swap the checked state of the buttons
            self.button1.setChecked(not self.button1.isChecked())
            self.button2.setChecked(not self.button2.isChecked())

            # Swap the background colors of the buttons
            bg_color1 = self.button1.palette().color(QPalette.ColorRole.Button)
            bg_color2 = self.button2.palette().color(QPalette.ColorRole.Button)

            self.button1.setStyleSheet(f"background-color: {bg_color2.name()};")
            self.button2.setStyleSheet(f"background-color: {bg_color1.name()};")


# app = QtWidgets.QApplication(sys.argv)

# window = MainWindow()
# window.show()
# app.exec()

# Create a QApplication instance
app = QApplication(sys.argv)

# Create a MyWidget instance and show it
widget = MainWindow()
widget.show()

# Run the event loop
sys.exit(app.exec())