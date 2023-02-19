import Block

class Section:
    # constructor
    def __init__(self, sectionName):
        self.blocks = []
        self.sectionName = sectionName

    # declare methods
    def addBlock(self, block):
        self.blocks.append(block)

    def removeBlock(self, block):
        self.blocks.remove(block)

    def clearBlocks(self):
        self.blocks.clear()

    def hasBlock(self, blockID):
        for b in self.blocks:
            if b.blockName == blockID:
                return True

    def getBlock(self, blockID):
        for b in self.blocks:
            if b.blockName == blockID:
                return b