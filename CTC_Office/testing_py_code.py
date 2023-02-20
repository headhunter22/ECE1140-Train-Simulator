import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QButtonGroup, QToolButton
from PyQt6.QtGui import QPalette, QGuiApplication

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

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

# Create a QApplication instance
app = QApplication(sys.argv)

# Create a MyWidget instance and show it
widget = MyWidget()
widget.show()

# Run the event loop
sys.exit(app.exec())




"""
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button1 = QPushButton('Button 1', self)
        self.button1.setGeometry(50, 50, 100, 50)
        self.button1.clicked.connect(self.button_clicked)

        self.button2 = QPushButton('Button 2', self)
        self.button2.setGeometry(200, 50, 100, 50)
        self.button2.clicked.connect(self.button_clicked)

        self.current_button = None  # keep track of the current pressed button

    def button_clicked(self):
        button = self.sender()
        if button == self.current_button:  # if the same button is clicked again, toggle the color
            color = 'white' if self.get_button_color(button) == 'blue' else 'blue'
            self.set_button_color(button, color)
        else:  # if a different button is clicked, toggle the colors of both buttons
            color1, color2 = 'blue', 'white'
            if self.current_button:
                color1, color2 = color2, color1  # swap colors if there is a current button
                self.set_button_color(self.current_button, color2)
            self.current_button = button
            self.set_button_color(button, color1)

    def set_button_color(self, button, color):
        button.setStyleSheet(f"background-color: {color};")

    def get_button_color(self, button):
        return button.palette().button().color().name()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    """