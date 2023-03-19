from TrackModelSend import TrackModelSend

class TrackModel:
    def __init__(self, track):
        self.Rx = TrackModelReceive()
        self.Tx = TrackModelSend() 
        self.track = track

    def receive(self):
        self.Rx.pullInfo()

    def send(self):
        self.Tx.sendInfo()