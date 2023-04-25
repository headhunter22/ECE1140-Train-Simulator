import sys, unittest
from PyQt6 import QtCore, QtGui, QtWidgets

sys.path.append('../Full System')
from TrackModel import TrackModel
from TrackModelUI import TrackModelUI
import TrackParser
from Train import Train
from Line import Line

class TestTrackModel(unittest.TestCase):

    def testNumTrains(self):
        trackModel = TrackModel()
        train = Train(1, Line('Green'), '63')
        trackModel.dispatchTrain(train)

        self.assertEqual(trackModel.numTrains, 1)

    # def testHeaters(self):
    #     app = QtWidgets.QApplication(sys.argv)
    #     track = TrackParser.parseTrack('TrackLayout.csv')
    #     trackModel = TrackModelUI(track)

    #     # set temperature to freezing temperature edge case
    #     trackModel.tempUpdate(32)
    #     self.assertEqual(trackModel.HeaterStatus.text(), 'On')

    #     # set temperature to freezing temperature edge case
    #     trackModel.tempUpdate(45)
    #     self.assertEqual(trackModel.HeaterStatus.text(), 'Off')

    #     # set temperature to freezing temperature edge case
    #     trackModel.tempUpdate(25)
    #     self.assertEqual(trackModel.HeaterStatus.text(), 'On')

unittest.main()