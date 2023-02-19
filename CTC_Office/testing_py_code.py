import csv, sys

sys.path.append('../ECE1140-TEAM-1/')



with open('Track_Layout.csv', newline='') as csvfile:
    trackReader = csv.reader(csvfile)

    # skip first line of headers
    next(trackReader)

    for row in trackReader:
        print(",",row)

