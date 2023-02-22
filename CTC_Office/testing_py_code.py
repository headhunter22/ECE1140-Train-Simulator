import pandas as pd

track = pd.read_csv('Track Layout.csv', usecols=['Line', 'Block Number', 'Block Length (m)', 'Speed Limit (Km/Hr)', 'Infrastructure'])

print(track)

blockLength = track['Block Length (m)']