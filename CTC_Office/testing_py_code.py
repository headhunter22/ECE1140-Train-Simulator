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