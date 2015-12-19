
def gisGift(inputFile, outputFile):
    
    output = open(outputFile, 'w')
    output.write("id,weight,wkt\n")
    
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
            
            output.write(str(splittedLine[0]))
            output.write(",")
            output.write(str(splittedLine[3]))
            output.write(",")
            output.write("POINT(" + str(splittedLine[2]) + " " + str(splittedLine[1]) + ")\n")

    output.close()

dataDirectory = "c:\\data\\kaggle-santa-2015\\"            
gisGift(dataDirectory + "gifts.csv", dataDirectory + "gifts_gis.csv")
