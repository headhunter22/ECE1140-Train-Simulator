from TrainController import TrainController
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from signals import signals

class SWTrainController(QObject):
    def __init__(self):
        super().__init__()
        self.trainControllers = []
        signals.trainControllerDispatchedSignal.connect(self.dispatchTrain)
        signals.trainControllerTimeTrigger.connect(self.calculatePower)

    def dispatchTrain(self, train):
        print('train controlled dispatched')
        trainController = TrainController()
        self.trainControllers.append(trainController)
        signals.trainControllerUpdateCurrSpeed.emit(train, 0)

    def calculatePower(self):
        print('calculating power')
        self.trainControllers[0].sendPower()
        print('power calculated')