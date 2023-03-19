# import Wayside Rx
# import Train Model Rx

class TrackModelSend:
    # signals sent by Track Model
    occupancyToWayside = pyqtSignal(Line, Block, int)
    trainToTrainModel = pyqtSignal(Train)
    trackToTrainModel = pyqtSignal(Track)

    def __init__(self):
        return

    '''
    def sendInfo(self):
        # send signals to wayside and train model receivers
        self.updateOccupancy()
        self.passTrain()
    '''

    def updateOccupancy(self, inLine, inBlock, occupied):
        self.occupancyToWayside.emit(inLine, inBlock, occupied)

    def passTrain(self, train):
        self.trainToTrainModel.emit(train)

    def passTrack(self, track):
        self.trackToTrainModel.emit(track)

    