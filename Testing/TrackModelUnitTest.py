import sys, unittest
sys.path.append('../Full System')
from TrackModel import TrackModel
from Train import Train
from Line import Line

class TestTrackModel(unittest.TestCase):

    def testNumTrains(self):
        trackModel = TrackModel()
        train = Train(1, Line('Green'), '63')
        trackModel.dispatchTrain(train)

        self.assertEqual(trackModel.numTrains, 1)

unittest.main()