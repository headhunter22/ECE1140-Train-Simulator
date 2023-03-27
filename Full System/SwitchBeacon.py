class SwitchBeacon:

    blockNumberToTrainModel = pyqtSignal(int)

    def __init__(self, blockNumber):
        self.blockNumber = blockNumber

    def blockTraversed(self):
        blockNumberToTrainModel.emit(self.blockNumber)