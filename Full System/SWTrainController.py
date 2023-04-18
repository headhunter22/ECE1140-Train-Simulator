from TrainController import TrainController
from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from signals import signals

class SWTrainController(QObject):
    def __init__(self):
        super().__init__()
        self.trainControllers = []
        signals.trainControllerDispatchedSignal.connect(self.dispatchTrain)
        signals.trainControllerTimeTrigger.connect(self.calculatePower)
        signals.trainWaiting.connect(self.disconnectSignal)
        signals.trainGo.connect(self.connectSignal)

    def dispatchTrain(self, train):
        print('train controlled dispatched')
        trainController = TrainController()
        self.trainControllers.append(trainController)
        signals.trainControllerUpdateCurrSpeed.emit(train, 0)

    def calculatePower(self):
        if len(self.trainControllers) == 0:
            return
        else:
            self.trainControllers[0].sendPower()

    def disconnectSignal(self):
        signals.trainControllerTimeTrigger.disconnect(self.calculatePower)

    def connectSignal(self):
        signals.trainControllerTimeTrigger.connect(self.calculatePower)