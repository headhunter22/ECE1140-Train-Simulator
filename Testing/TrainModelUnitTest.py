import sys, unittest
sys.path.append('..\Full System')
print(sys.path)
from TrainModel import TrainModel

class TestTrainModel(unittest.TestCase):

    def testOccupancy(self):

        trainModel = TrainModel()
        trainModel.serviceBrakeActive(True)

        #Testing if the service brake is active
        self.assertEqual(trainModel.serviceBrake, True)

unittest.main()