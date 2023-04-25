import sys, unittest
sys.path.append('../Full System')
from TrainController import TrainController

class TestTrainController(unittest.TestCase):

    def testcurrentSpeed(self):
        trainController = TrainController()
        self.assertEqual(trainController.currentSpeed, 0)

unittest.main()