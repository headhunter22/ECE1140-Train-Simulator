import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QPushButton
        self.button = QPushButton('Open File', self)
        self.button.clicked.connect(self.open_file)

    def open_file(self):
        # Open a file dialog and get the path of the selected file
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'CSV files (*.csv)')

        # Do something with the selected file
        print('Selected file:', file_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())