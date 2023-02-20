import csv

# import classes
from Track import Track
from Line import Line
from Section import Section
from Block import Block

def parseTrack(filename):
    # instantiate the track
    track = Track()

    with open(filename, newline='') as csvfile:
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
            if not track.hasLine(newLine.lineName):
                track.addLine(newLine)
            currLine = track.getLine(newLine.lineName)

            assert currLine is not None

            # if section does not exist on the line, add it to the line
            if not currLine.hasSection(newSection.sectionName):
                currLine.addSection(newSection)
                
            currSection = currLine.getSection(newSection.sectionName)

            # if block does not exist in the section, add it to the block
            if not currSection.hasBlock(newBlock.blockName):
                currSection.addBlock(newBlock)

            if not currLine.hasBlock(newBlock.blockName):
                currLine.addBlock(newBlock)

    return track