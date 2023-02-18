import csv
import Line, Section, Block

with open('Track Layout.csv', newline='') as csvfile:
    trackReader = csv.reader(csvfile)

    for row in trackReader:
        # if line does not exist 