import random

class TicketSystem:

    totalPassengersMoved = 0

    def __init__(self):
        self.passengersWaiting = 0
        self.passengersOnboard = 0

    def releasePassengers(self):
        print('Passengers Off: ' + str(self.passengersOnboard))
        totalPassengersMoved += self.passengersOnboard

    def boardTrain(self):
        self.passengersWaiting = random.randint(1, 222)
        print('Passengers On: ' + str(self.passengersWaiting))
        self.passengersOnboard = self.passengersWaiting
        