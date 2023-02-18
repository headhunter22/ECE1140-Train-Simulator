import csv, sys

sys.path.append('../ECE1140-TEAM-1/')

from Track import Track
from Line import Line
from Section import Section
from Block import Block

track = Track()

with open('Track Layout.csv', newline='') as csvfile:
    trackReader = csv.reader(csvfile)

    # skip first line of headers
    next(trackReader)

    # for each real row in csv, read in data
    for row in trackReader:
        # define objects for row line, section, and block
        newLine = Line(row[0])
        newSection = Section(row[1])
        newBlock = Block(row[2:])

        # if line does not exist, add it to track lines
        if not track.lineExists(newLine.lineName):
            track.addLine(newLine)

        # if section does not exist on the line, add it to the line
        if not track.getLine(newLine.lineName).hasSection(newSection.sectionName):


        # if block does not exist in the section, add it to the block



for line in track.lines:
    print(line.lineName)