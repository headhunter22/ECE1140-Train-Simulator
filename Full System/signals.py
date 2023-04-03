from PyQt6.QtCore import QObject, pyqtSignal

class Signals(QObject):
    timerTicked = pyqtSignal(int, int, int) # hrs, mins, secs to send to CTC

signals = Signals()