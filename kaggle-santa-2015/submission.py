def loadOrder(fileName):
    print("Loading order from " + fileName + "...")

    order = []
    
    # open the file
    with open(fileName) as infile:
        # read line by line
        for line in infile:                
            # remove newline character from the end
            line = line.rstrip()
            
            order.append(int(line))
                        
    print("Done... #order: " + str(len(order)))
    
    return order

def doSubmissionFromOrder(order, gifts):
    
    sleighMaxWeight = 1000.0
    currentWeight = 0.0
    currentTrip = []
    
    trips = []
    
    for giftId in order:
        gift = gifts[giftId]
        if currentWeight + gift.weight > sleighMaxWeight:
            trips.append(currentTrip)
            currentWeight = gift.weight
            currentTrip = [gift]
        else:
            currentTrip.append(gift)
            currentWeight = currentWeight + gift.weight
    trips.append(currentTrip)

#     counter = 0    
#     for trip in trips:
#         tripWeight = 0
#         for gift in trip:
#             counter = counter + 1
#             tripWeight = tripWeight + gift.weight
#         print(str(tripWeight))
#     print("order: " + str(len(order)))
#     print("counter: " + str(counter))
    
    return trips

def createSubmissionFromTrips(trips, fileName):
    tripId = 1
    
    output = open(fileName, 'w')
    output.write("GiftId,TripId\n")
    
    for trip in trips:
        for gift in trip:
            output.write(str(gift.ID) + "," + str(tripId) + "\n")
        tripId = tripId + 1
    
    output.close()
    