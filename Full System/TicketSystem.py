import random
from Train import Train
from signals import signals

class TicketSystem:

    totalPassengersMoved = {'Red: ': 0,
                            'Green: ': 0}

    def releasePassengers(self, train):
        passengersOff = random.randint(1, train.numPassengers)
        print('Passengers Off: ' + str(passengersOff))
        train.numPassengers -= passengersOff
        TicketSystem.totalPassengersMoved[train.line.lineName] += passengersOff
        signals.ctcGetPassengersPerLine.emit(passengersOff, train.line.lineName)

    def boardTrain(self, train):
        passengersWaiting = random.randint(1, 222)
        train.numPassengers += passengersWaiting
        print('Passengers On: ' + str(passengersWaiting))