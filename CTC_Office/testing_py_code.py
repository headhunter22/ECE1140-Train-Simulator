from PyQt6.QtGui import QColor, QBrush
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

app = QApplication([])
window = QMainWindow()
table_widget = QTableWidget()

table_widget.setRowCount(3)
table_widget.setColumnCount(3)

# Add a new item to row 0, column 0 with a green background
item = QTableWidgetItem('Hello')
item.setBackground(QBrush(QColor('green')))
table_widget.setItem(0, 0, item)

window.setCentralWidget(table_widget)
window.show()
app.exec()
