import csv

col = []

with open(r'D:/ECE_1140/ECE1140-Team-1/CTC_Office/Track_Layout.csv', newline='') as csvfile:
    trackLayout = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(trackLayout)

    for col in trackLayout:
        for row in trackLayout:
            if col[0] == 'Blue':
                print(col[0])







#import pandas as pd

#trackLayout = pd.read_csv("Track_Layout.csv", header=0)

#print(trackLayout)


#trackLayout = pandas.read_csv('Track_Layout.csv')

#print(trackLayout)