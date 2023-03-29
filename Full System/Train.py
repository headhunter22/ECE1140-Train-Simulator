from PyQt6.QtCore import QSize, QObject, QThread, pyqtSignal
from TrainController import TrainController
import threading
import time

class Worker(QObject):
    def __init__(self, train):
        super(Worker, self).__init__()
        self.train = train

    def sendSpeeds(self):
        while True:
            print('actual speed: ' + str(self.train.actSpeed) + ' commanded speed: ' + str(self.train.commandedSpeed))
            self.train.trainController.getSpeed(self.train.actSpeed, self.train.commandedSpeed)
            time.sleep(1)

class Train(QObject):
    trainCounter = 0

    def __init__(self, auth, speed, ID, line, power, actSpeed, trainController):
        super().__init__()

        self.trainController = trainController
        self.trainController.powerToTrain.connect(self.getPower)

        # id
        self.ID = ID

        # authority and speeds
        self.authority = auth
        self.currentSpeed = 0
        self.suggSpeed = speed
        self.commandedSpeed = 0
        self.commandedPower = power
        self.actSpeed = actSpeed
        self.acc = 0.5

        # location attributes
        self.line = line
        self.location = 3

        # mass info
        self.baseMass = 81950 * .453 # kgs 

        self.sendSpeeds()

    def sendSpeeds(self):
        # attach infinite while loop to worker
        self.thread = QThread()
        self.worker = Worker(self)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.sendSpeeds())
        self.thread.start()
        
    def getPower(self, power):
        self.commandedPower = power
        #print('got power: ' + str(power))

        # calculate mass

        # calculate force
        force = 0.5 * self.baseMass

        self.actualSpeed = self.commandedPower / force