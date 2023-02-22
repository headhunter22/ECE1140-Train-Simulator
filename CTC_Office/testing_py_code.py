import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QStackedWidget, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create a stacked widget and add widgets to it
        self.stacked_widget = QStackedWidget()
        self.page1 = QWidget()
        self.page2 = QWidget()
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        # Add some content to the pages
        label1 = QLabel("This is page 1")
        label2 = QLabel("This is page 2")
        layout1 = QVBoxLayout(self.page1)
        layout2 = QVBoxLayout(self.page2)
        layout1.addWidget(label1)
        layout2.addWidget(label2)

        # Create buttons to switch between pages
        self.button1 = QPushButton("Page 1")
        self.button2 = QPushButton("Page 2")

        # Connect the buttons to the switch_page method
        self.button1.clicked.connect(lambda: self.switch_page(0))
        self.button2.clicked.connect(lambda: self.switch_page(1))

        # Add widgets to the layout
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

        # Set initial view
        self.switch_page(0)

    def switch_page(self, index):
        self.stacked_widget.setCurrentIndex(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())