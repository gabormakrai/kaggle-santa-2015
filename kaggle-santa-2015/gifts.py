
class Gift:
    def __init__(self, ID, longitude, latitude, weight):
        self.ID = ID
        self.longitude = longitude
        self.latitude = latitude
        self.weight = weight

    def __str__(self):
        return "Gift(id:" + str(self.id) + ")"

def loadGifts(fileName):
    print("Loading gifts from " + fileName + "...")
    
    gifts = {}
    
    firstLine = True
    # open the file
    with open(fileName) as infile:
        # read line by line
        for line in infile:                
            # remove newline character from the end
            line = line.rstrip()
            
            # parse header
            if firstLine == True:
                firstLine = False
                continue

            # split the line
            splittedLine = line.split(',')

            gift = Gift(int(splittedLine[0]), float(splittedLine[2]), float(splittedLine[1]), float(splittedLine[3]))
            gifts[gift.ID] = gift
            
    print("Done... " + str(len(gifts)) + " have been loaded...")
    
    return gifts