import threading
import time
from signals import signals

# keeps system time
class Clock:
    def __init__(self):
        self.thread = threading.Thread(target=self.timer)

        # attributes of clock
        self.period = 0.2
        self.tickFactor = 1
        self.currSecs = 0
        self.currMins = 0
        self.currHrs = 7

        # attributes of thread
        self.lock = threading.Lock()
        self.running = True
        self.pasued = False

        # threaded timer
        self.timer = threading.Timer(self.period * self.tickFactor, self.triggered)

    # function to be called every interval
    def timer(self):
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
            self.timer.join()

    # function called when timer thread ends
    def triggered(self):
        self.timer = threading.Timer(self.period * self.tickFactor, self.triggered)

        with self.lock:
            self.timer.start()

    # start thread
    def startTimer(self):
        self.thread.start()
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