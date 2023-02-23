from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QApplication, QDialog, QGridLayout, QLabel, QTimeEdit, QPushButton

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a QTimeEdit widget
        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("hh:mm:ss")

        # Create a button to read the time from the QTimeEdit widget
        self.read_time_button = QPushButton("Read Time")
        self.read_time_button.clicked.connect(self.handleReadTimeClicked)

        # Create a label to display the time
        self.time_label = QLabel()

        # Create a grid layout and add the widgets to it
        layout = QGridLayout()
        layout.addWidget(QLabel("Time:"), 0, 0)
        layout.addWidget(self.time_edit, 0, 1)
        layout.addWidget(self.read_time_button, 1, 0)
        layout.addWidget(self.time_label, 1, 1)
        self.setLayout(layout)

    def handleReadTimeClicked(self):
        # Read the time from the QTimeEdit widget and display it in the label
        time = self.time_edit.time()
        self.time_label.setText(time.toString("hh:mm:ss"))

if __name__ == '__main__':
    app = QApplication([])
    dialog = MyDialog()
    dialog.show()
    app.exec()
