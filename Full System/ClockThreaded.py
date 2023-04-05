import time
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

        # attributes of thread
        self.running = True
        self.pasued = False

        # threaded timer
        self.timer = QTimer()
        self.timer.setInterval(self.period * self.tickFactor * 1000)
        self.timer.timeout.connect(self.triggered)
        print('timer created')
    # function to be called every interval
    def timerFunc(self):
        print('timer starting')
        while self.running:
            time.sleep(self.tickFactor)

            # lock the thread for important code
            with self.lock:
                # increment seconds
                self.currSecs += 1
                if self.currSecs == 60: # reset secs after 60
                    self.currMins += 1
                    self.currSecs = 0
                if self.currMins == 60: # reset mins after 60
                    self.currHrs += 1
                    self.curMins = 0
                if self.currHrs == 24: # reset hrs after 24
                    self.currHrs = 0

                # emit signal of timer ticking that CTC will received to keep time
                signals.timerTicked.emit(self.currHrs, self.currMins, self.currSecs)

        # cancel the timer
        try:
            self.timer.join()
        except:
            print('app closing')

        self.timer.cancel()

    # function called when timer thread ends
    def triggered(self):
        # emit triggered signal
        try:
            signals.trainControllerTimeTrigger.emit()
        except:
            print('system ended')
            pass

    # start thread
    def startTimer(self):
        self.timer.start()

    # stop thread
    def stopTimer(self):
        self.running = False
        self.resumeTimer()
        self.timer.join()

    # pause thread
    def pauseTimer(self):
        if not self.lock.locked():
            self.lock.acquire()
            self.paused = True

    # resume thread
    def resumeTimer(self):
        if self.lock.locked():
            self.lock.release()
            self.paused = False

clock = Clock()