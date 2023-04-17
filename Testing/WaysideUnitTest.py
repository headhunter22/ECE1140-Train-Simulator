import sys, unittest
sys.path.append('../Full System')
print(sys.path)
from Wayside import Wayside
from WaysideUI import WMainWindowA
from Train import Train
from Track import Track
from Line import Line
from CTC import CTC
import TrackParser

class TestWaysideMethods(unittest.TestCase):   
    def testOccupancyReceived(self):
        train = Train(1, Line('Green'), '63')
        wayside.blockOccupancyReceived(train.block)
        self.assertEqual(waysideUI.oblock, 63)

    
if __name__ == '__main__':
    track = TrackParser.parseTrack("TrackLayout.csv")
    ctcOffice = CTC(track)
    wayside = Wayside(ctcOffice)
    waysideUI = WMainWindowA()
    unittest.main()









