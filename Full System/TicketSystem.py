import random
from Train import Train

class TicketSystem:

    totalPassengersMoved = 0

    def __init__(self):
        self.passengersOnboard = 0
        self.passengersWaiting = 0

    def releasePassengers(self, train):
        print('Passengers Off: ' + str(self.passengersOnboard))
        train.numPassengers -= self.passengersOnboard
        TicketSystem.totalPassengersMoved += self.passengersOnboard

    def boardTrain(self, train):
        self.passengersWaiting = random.randint(1, 222)
        train.numPassengers += self.passengersWaiting
        print('Passengers On: ' + str(self.passengersWaiting))
        self.passengersOnboard = self.passengersWaiting