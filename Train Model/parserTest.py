import TrackParser

track = TrackParser.parseTrack('Track Layout.csv')
speedVar = track.getLine('Red').getBlock('17').speedLimit
print(speedVar)      
        