from TrainController import TrainController
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from signals import signals

class SWTrainController(QObject):
    def __init__(self):
        super().__init__()
        signals.trainControllerDispatchedSignal.connect(self.dispatchTrain)

    def dispatchTrain(self, train):
        trainController = TrainController()