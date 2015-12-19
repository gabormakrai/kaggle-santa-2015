from gifts import loadGifts

def gisSubmission(inputFile, outputFile, gifts):
    
    trips = {}
    
    output = open(outputFile, 'w')
    output.write("tripID;wkt\n")
    
    firstLine = True
    # open the file
    with open(inputFile) as infile:
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
            
            tripId = int(splittedLine[1])
            giftId = int(splittedLine[0])
            
            if tripId not in trips:
                trips[tripId] = []
            
            trips[tripId].append(gifts[giftId])
            
    for tripId in trips:
        trip = trips[tripId]
        output.write(str(tripId) + ";")
        output.write("LINESTRING(0 90,")
        for gift in trip:
            output.write("," + str(gift.longitude) + " " + str(gift.latitude))
        output.write(",0 90")
        output.write(")\n")
    
    output.close()
    
dataDirectory = "c:\\data\\kaggle-santa-2015\\"
gifts = loadGifts(dataDirectory + "gifts.csv")

gisSubmission(dataDirectory + "sample_submission.csv", dataDirectory + "sub_gis.csv", gifts)

