import datetime
from signals import signals
from PyQt6.QtCore import QThread, QTimer

# keeps system time
class Clock(QThread):
    def __init__(self):
        super().__init__()

        # attributes of clock
        self.period = 1
        self.tickFactor = 1
        self.currSecs = 0
        self.currMins = 0
        self.currHrs = 7
        self.testSecs = 25200
        self.dispHour = 0
        self.dispMin = 0
        self.dispSec = 0

        # attributes of thread
        self.running = True
        self.paused = False

        # threaded timer
        self.timer = QTimer()
        self.powerTimer = QTimer()
    
        self.timer.setInterval(self.period * self.tickFactor * 1000)
        self.timer.timeout.connect(self.triggered)

        # connect signals
        signals.CTCTimePause.connect(self.stopTimer)
        signals.CTCOneTimesSpeed.connect(self.oneTimes)
        signals.CTCTenTimesSpeed.connect(self.tenTimes)
        signals.CTCFiftyTimesSpeed.connect(self.fiftyTimes)

    # function called when timer thread ends
    def triggered(self):
        # emit triggered signal
        try:
            signals.trainControllerTimeTrigger.emit()

            timeStr = str(datetime.timedelta(seconds=self.testSecs))
            timeArr = timeStr.split(":")
            self.testSecs += 1
            self.dispHour = timeArr[0]
            
            # emit signal of timer ticking that CTC will received to keep time
            signals.timerTicked.emit(int(timeArr[0]), int(timeArr[1]), int(timeArr[2]))
        except:
            print('system ended')
            pass

    # start time
    def startTimer(self):
        self.timer.start()

    def oneTimes(self):
        self.timer.start()
        self.timer.setInterval(1000)

    def tenTimes(self):
        self.timer.start()
        self.timer.setInterval(100)

    def fiftyTimes(self):
        self.timer.start()
        self.timer.setInterval(20)

    # stop time
    def stopTimer(self):
        self.timer.stop()

    # resume thread
    def resumeTimer(self):
        if self.lock.locked():
            self.lock.release()
            self.paused = False

clock = Clock()