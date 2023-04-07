import sys, unittest
sys.path.append('..\Full System')
print(sys.path)
import Wayside
from WaysideUI import WMainWindowA

class TestWaysideMethods(unittest.TestCase):
    def testActiveTrains(self):
        wayside = Wayside()
        waysideUI = WMainWindowA()
        self.assertEqual(waysideUI.activetrains(), 0,
                         'wrong number of active trains')
        wayside.dispatchTrain()
        self.assertEqual(waysideUI.activetrains(), 1,
                         'wrong number of active trains')
        
if __name__ == '__main__':
    
    unittest.main()









