import random
from Train import Train
from signals import signals

class TicketSystem:
    totalPassengersMoved = {'Red': 0,
                            'Green': 0}

    def releasePassengers(self, train):
        passengersOff = train.numPassengers
        print('Passengers Off: ' + str(passengersOff))
        train.numPassengers = 0
        TicketSystem.totalPassengersMoved[train.line.lineName] += passengersOff
        signals.ctcGetPassengersPerLine.emit(passengersOff, train.line)

    def boardTrain(self, train):
        passengersWaiting = random.randint(1, 222)
        train.numPassengers += passengersWaiting
        print('Passengers On: ' + str(passengersWaiting))